import os
import sys
import requests
import pandas as pd

def main():
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        print("Error: FRED_API_KEY environment variable not set.")
        sys.exit(1)

    releases = {
        "NFP": 50,
        "CPI": 10
    }

    os.makedirs("../../data/economic-calendar", exist_ok=True)

    for name, rid in releases.items():
        print(f"Fetching release dates for {name} (Release ID: {rid})...")
        url = f"https://api.stlouisfed.org/fred/release/dates?release_id={rid}&api_key={api_key}&file_type=json"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if "release_dates" in data:
                # Extract dates
                dates = [item["date"] for item in data["release_dates"]]
                df = pd.DataFrame({"date": dates})
                # Drop duplicates and sort
                df = df.drop_duplicates().sort_values(by="date")
                
                out_path = f"../../data/economic-calendar/{name.lower()}_dates.csv"
                df.to_csv(out_path, index=False)
                print(f"Saved {len(df)} dates to {out_path}")
            else:
                print(f"Unexpected JSON structure for {name}: {data.keys()}")
                
        except Exception as e:
            print(f"Failed to fetch {name}: {e}")

if __name__ == "__main__":
    main()
