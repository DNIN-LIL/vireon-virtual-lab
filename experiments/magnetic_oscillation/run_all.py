# experiments/magnetic_oscillation/run_all.py
import sys
import subprocess
from pathlib import Path
import pandas as pd

SUBEXPS = [
    "vacuum_sine",
    "vacuum_square",
    "vacuum_triangle",
    "plasma_sine",
    "plasma_square",
    "plasma_triangle",
]

ROOT = Path(__file__).resolve().parents[2]  # repo root (../../)
MAIN = ROOT / "main.py"

def run_all():
    for name in SUBEXPS:
        cmd = [sys.executable, str(MAIN), "--exp", f"magnetic_oscillation/{name}"]
        print("Running:", " ".join(cmd))
        subprocess.run(cmd, check=True)
        print("Completed:", name)

def collect():
    rows = []
    for name in SUBEXPS:
        out_dir = ROOT / "output" / "magnetic_oscillation" / name
        csv_path = out_dir / "summary.csv"
        if csv_path.exists():
            df = pd.read_csv(csv_path)
            # expect one row per subexp
            if not df.empty:
                r = df.iloc[0].to_dict()
                r["experiment"] = name
                rows.append(r)
    if rows:
        df = pd.DataFrame(rows)
        out_dir = ROOT / "output" / "magnetic_oscillation"
        out_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(out_dir / "summary.csv", index=False)
        print("Summary saved to", out_dir / "summary.csv")
    else:
        print("No summaries found.")

if __name__ == "__main__":
    run_all()
    collect()
