import importlib.util
import sys
from pathlib import Path

def run_lab(exp_name):
    exp_path = Path("experiments") / exp_name / "logic.py"

    if not exp_path.exists():
        print(f"❌ Experiment not found: {exp_path}")
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("logic", str(exp_path))
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"❌ Failed to execute {exp_path}:\n{e}")
        sys.exit(1)

    if hasattr(module, "run"):
        try:
            module.run()
        except Exception as e:
            print(f"❌ Error during simulation:\n{e}")
            sys.exit(1)
    else:
        print(f"❌ No run() function in {exp_path}")
        sys.exit(1)
