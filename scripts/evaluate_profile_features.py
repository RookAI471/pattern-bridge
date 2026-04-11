#!/home/lordtedders/.openclaw/workspace/pattern-bridge/.venv/bin/python
import argparse
from pathlib import Path
import pandas as pd


def tail_run(df_desc: pd.DataFrame, max_tpos: int = 2) -> int:
    run = 0
    for v in df_desc['tpo_count']:
        if v <= max_tpos:
            run += 1
        else:
            break
    return run


def evaluate_profile(profile: pd.DataFrame) -> dict:
    desc = profile.sort_values('price_level', ascending=False).reset_index(drop=True)
    asc = profile.sort_values('price_level', ascending=True).reset_index(drop=True)

    top_tail_run = tail_run(desc, max_tpos=2)
    bottom_tail_run = tail_run(asc, max_tpos=2)

    poc_row = profile.sort_values(['tpo_count', 'price_level'], ascending=[False, False]).iloc[0]
    poc_price = float(poc_row['price_level'])
    max_tpo = int(poc_row['tpo_count'])

    # crude center band around POC +/- 4 points
    center = profile[(profile['price_level'] >= poc_price - 4.0) & (profile['price_level'] <= poc_price + 4.0)]
    center_mean = center['tpo_count'].mean() if len(center) else 0

    # tail bands, top 10 rows and bottom 10 rows
    top_band = desc.head(10)
    bot_band = asc.head(10)
    top_mean = top_band['tpo_count'].mean() if len(top_band) else 0
    bot_mean = bot_band['tpo_count'].mean() if len(bot_band) else 0

    # poor lower tail proxy: first 3 price levels at low all have >1 TPO
    low3 = asc.head(3)
    poor_tpol = len(low3) == 3 and all(low3['tpo_count'] >= 2)

    # bikini proxy: both tails present but center much fatter than both ends
    bikini_candidate = (
        top_tail_run >= 2 and bottom_tail_run >= 2 and
        center_mean > top_mean * 2 and center_mean > bot_mean * 2
    )

    return {
        'profile_high': float(profile['price_level'].max()),
        'profile_low': float(profile['price_level'].min()),
        'poc_price': poc_price,
        'poc_tpo': max_tpo,
        'top_tail_low_tpo_run': int(top_tail_run),
        'bottom_tail_low_tpo_run': int(bottom_tail_run),
        'center_mean_tpo': float(center_mean),
        'top_band_mean_tpo': float(top_mean),
        'bottom_band_mean_tpo': float(bot_mean),
        'poor_tpol_candidate': bool(poor_tpol),
        'bikini_candidate': bool(bikini_candidate),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('profiles', nargs='+')
    args = ap.parse_args()

    rows = []
    for p in args.profiles:
        path = Path(p)
        df = pd.read_csv(path)
        metrics = evaluate_profile(df)
        metrics['profile_file'] = path.name
        rows.append(metrics)

    out = pd.DataFrame(rows)
    cols = ['profile_file','profile_high','profile_low','poc_price','poc_tpo','top_tail_low_tpo_run','bottom_tail_low_tpo_run','center_mean_tpo','top_band_mean_tpo','bottom_band_mean_tpo','poor_tpol_candidate','bikini_candidate']
    print(out[cols].to_string(index=False))


if __name__ == '__main__':
    main()
