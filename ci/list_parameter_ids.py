"""Emit parameter_db.csv's ID column as a JSON array for the CI matrix.

Integer coercion rejects non-integer IDs so they cannot be interpolated
as untrusted text into shell steps.
"""
import csv
import json
import sys


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "src/data/parameter_db.csv"
    ids = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        if "ID" not in (reader.fieldnames or []):
            sys.exit(f"{path}: missing 'ID' column")
        for row in reader:
            raw = row["ID"]
            try:
                ids.append(int(raw))
            except (TypeError, ValueError):
                sys.exit(
                    f"ID {raw!r} in {path} is not an integer; "
                    "refusing to expand matrix."
                )
    if len(set(ids)) != len(ids):
        dupes = sorted({x for x in ids if ids.count(x) > 1})
        sys.exit(f"{path}: duplicate IDs {dupes}; matrix shards would collide.")
    print(json.dumps(ids))


if __name__ == "__main__":
    main()
