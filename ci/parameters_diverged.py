"""Print 'true' if parameter_db.csv has changed since the commit that
last updated the cached estimates CSV, else 'false'.

Compares via git so any change to parameter_db.csv (parameter values,
Origin URLs, whitespace) is caught. Requires fetch-depth: 0 on the
caller's checkout. Fail-closed: any unexpected error prints 'true'
so a corrupt repo state forces a refresh rather than silently skipping.
"""
import subprocess
import sys

DB = "src/data/parameter_db.csv"
EST = "src/data/lattice_estimator_estimates.csv"


def _run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, check=True)


def main():
    try:
        last = _run(["git", "log", "-1", "--format=%H", "--", EST]).stdout.strip()
        if not last:
            print("true")
            return
        diff = subprocess.run(
            ["git", "diff", "--quiet", last, "--", DB], capture_output=True
        )
        print("true" if diff.returncode != 0 else "false")
    except Exception as e:
        print(f"parameters_diverged: {e}", file=sys.stderr)
        print("true")


if __name__ == "__main__":
    main()
