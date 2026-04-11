#!/home/lordtedders/.openclaw/workspace/pattern-bridge/.venv/bin/python
import argparse
import math
from pathlib import Path
import pandas as pd


def frange_quarters(low: float, high: float, tick: float):
    start = math.floor(low / tick) * tick
    end = math.ceil(high / tick) * tick
    steps = int(round((end - start) / tick))
    for i in range(steps + 1):
        yield round(start + i * tick, 10)


def build_profile(df: pd.DataFrame, tick: float = 0.25) -> pd.DataFrame:
    rows = []
    period_labels = [chr(ord('A') + i) if i < 26 else f'P{i}' for i in range(len(df))]
    for idx, row in enumerate(df.itertuples(index=False)):
        label = period_labels[idx]
        for price in frange_quarters(row.low, row.high, tick):
            rows.append({
                'price_level': price,
                'period_index': idx,
                'period_label': label,
                'datetime': row.datetime,
            })
    prof = pd.DataFrame(rows)
    if prof.empty:
        return prof
    out = prof.groupby('price_level').agg(
        tpo_count=('period_index', 'count'),
        first_seen_period=('period_label', 'first'),
        last_seen_period=('period_label', 'last'),
        periods=('period_label', lambda s: ''.join(s)),
    ).reset_index().sort_values('price_level', ascending=False)
    out['is_single_print'] = out['tpo_count'] == 1
    max_count = out['tpo_count'].max()
    out['relative_density'] = out['tpo_count'] / max_count if max_count else 0
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--date', required=True, help='YYYY-MM-DD session date to inspect')
    ap.add_argument('--tick', type=float, default=0.25)
    ap.add_argument('--outdir', required=True)
    args = ap.parse_args()

    df = pd.read_csv(args.input, parse_dates=['datetime'])
    df['session_date'] = df['datetime'].dt.strftime('%Y-%m-%d')
    day = df[df['session_date'] == args.date][['datetime', 'open', 'high', 'low', 'close', 'volume']].copy()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    profile = build_profile(day, tick=args.tick)
    profile_path = outdir / f'es_profile_{args.date}.csv'
    bars_path = outdir / f'es_profile_{args.date}_bars.csv'
    profile.to_csv(profile_path, index=False)
    day.to_csv(bars_path, index=False)

    print(f'bars={len(day)} profile_rows={len(profile)}')
    print(f'profile_path={profile_path}')
    if not profile.empty:
        poc = profile.sort_values(['tpo_count', 'price_level'], ascending=[False, False]).iloc[0]
        print(f"poc_price={poc['price_level']} poc_tpos={poc['tpo_count']}")
        print('top_profile_levels:')
        print(profile.head(25).to_string(index=False))


if __name__ == '__main__':
    main()
