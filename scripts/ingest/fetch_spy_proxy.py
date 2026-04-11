import yfinance as yf
import pandas as pd
import os

def main():
    # We use SPY as a proxy for ES to bypass the historical intraday futures paywall for v0.
    # Note: yfinance 60m data is restricted to the last 730 days.
    # For full 2021/2022 archetype validation, we will fallback to daily SPY or require a paid dataset.
    
    ticker = "SPY"
    print(f"Fetching daily proxy data for {ticker} (Max history to capture 2021-2022 seeds)...")
    
    spy = yf.Ticker(ticker)
    # Daily data goes back decades, perfectly fine for weekly HTF sweeps
    df_daily = spy.history(period="10y", interval="1d")
    
    os.makedirs("../../data/market-data", exist_ok=True)
    df_daily.to_csv(f"../../data/market-data/{ticker.lower()}_daily.csv")
    print(f"Saved daily data to data/market-data/{ticker.lower()}_daily.csv")
    
    print(f"Fetching 60m proxy data for {ticker} (Last 730 days max workaround)...")
    try:
        df_60m = spy.history(period="730d", interval="60m")
        df_60m.to_csv(f"../../data/market-data/{ticker.lower()}_60m.csv")
        print(f"Saved 60m data to data/market-data/{ticker.lower()}_60m.csv")
    except Exception as e:
        print(f"Failed to fetch 60m data: {e}")

if __name__ == "__main__":
    main()
