"""Merge per-parameter partial estimate CSVs into the canonical
estimates CSV. If --parameter-db is given, cross-check the merged ID
set against it to catch a shard that uploaded a malformed CSV.
"""
import argparse
import glob
import sys

import pandas as pd


def _check_ids_match(merged: pd.DataFrame, parameter_db_path: str) -> None:
    expected = pd.read_csv(parameter_db_path)
    expected_ids = sorted(int(x) for x in expected["ID"].tolist())
    got_ids = sorted(int(x) for x in merged["ID"].tolist())
    if got_ids != expected_ids:
        sys.exit(
            f"merged ID set {got_ids} does not match parameter_db {expected_ids}"
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pattern",
        help="Glob matching all partial CSVs to merge "
        "(e.g. 'partials/estimates-*/partial-*.csv').",
    )
    parser.add_argument(
        "--output",
        default="src/data/lattice_estimator_estimates.csv",
        help="Output CSV path.",
    )
    parser.add_argument(
        "--parameter-db",
        default=None,
        help="If given, check the merged ID set against this parameter database.",
    )
    args = parser.parse_args()

    paths = sorted(glob.glob(args.pattern))
    if not paths:
        sys.exit(f"no partial CSVs matched pattern: {args.pattern}")

    merged = (
        pd.concat([pd.read_csv(p) for p in paths], ignore_index=True)
        .sort_values("ID")
        .reset_index(drop=True)
    )

    if args.parameter_db is not None:
        _check_ids_match(merged, args.parameter_db)

    merged.to_csv(args.output, index=False)
    print(merged.to_string(index=False))


if __name__ == "__main__":
    main()
