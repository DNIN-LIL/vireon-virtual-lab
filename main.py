import os
from core.engine.lab_runner import run_lab

def list_experiments(base_path="experiments"):
    return [
        d for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d)) and os.path.exists(os.path.join(base_path, d, "logic.py"))
    ]

def main():
    print("🧪 Welcome to Vireon Virtual Lab")

    experiments = list_experiments()
    if not experiments:
        print("⚠️ No experiments found.")
        return

    print("\nAvailable Experiments:")
    for i, exp in enumerate(experiments, 1):
        print(f"  {i}. {exp.replace('_', ' ').title()}")

    choice = input("\nEnter experiment number or name: ").strip()

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(experiments):
            run_lab(experiments[idx])
        else:
            print("❌ Invalid number.")
    elif choice in experiments:
        run_lab(choice)
    else:
        print("❌ Invalid selection.")

if __name__ == "__main__":
    main()
