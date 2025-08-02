import os
from pathlib import Path

root = Path(__file__).resolve().parent
docs_dir = root / "docs" / "layout_parts"
docs_dir.mkdir(parents=True, exist_ok=True)

index_file = root / "CODE_LAYOUT.md"

sections = {
    "overview": docs_dir / "code_layout_overview.md",
    "core": docs_dir / "code_layout_core_modules.md",
    "experiments": docs_dir / "code_layout_experiments.md",
    "interface": docs_dir / "code_layout_interface.md",
    "output": docs_dir / "code_layout_output_handling.md",
    "entry": docs_dir / "code_layout_entry_and_config.md",
}

tree_lines = []
def build_tree(p: Path, prefix=""):
    if "__pycache__" in p.parts or p.name.startswith('.') or p.suffix == ".pyc":
        return
    tree_lines.append(prefix + p.name + ("/" if p.is_dir() else ""))
    if p.is_dir():
        children = sorted([
            c for c in p.iterdir()
            if "__pycache__" not in c.parts and not c.name.startswith('.') and c.suffix != ".pyc"
        ])
        for i, child in enumerate(children):
            branch = "└── " if i == len(children) - 1 else "├── "
            build_tree(child, prefix + branch)

build_tree(root)

# Write each modular section
sections["overview"].write_text(
    "# Project Overview\n\n"
    "The Vireon Virtual Lab is a modular simulation environment for physics research. This file explains the general structure.\n\n"
    "- `core/`: reusable physics logic and utilities\n"
    "- `experiments/`: simulation modules with config + logic\n"
    "- `interface/`: GUI (Tkinter-based)\n"
    "- `output/`: logs, plots, and generated frames\n"
    "- `venv/`: virtual environment (local only)\n\n"
    "### Project Tree\n\n"
    "```\n" + "\n".join(tree_lines) + "\n```\n",
    encoding="utf-8"
)

sections["core"].write_text(
    "# Core Modules (`core/`)\n\n"
    "- `config_loader.py`: loads YAML config files\n"
    "- `physics.py`: force and interaction logic\n"
    "- `particle_engine.py`: updates position and velocity\n"
    "- `visualizer.py`: generates plots from data\n"
    "- `logger.py`: exports logs to CSV\n"
    "- `waveform_generator.py`: produces oscillation waveforms\n"
    "- `lab_runner.py`: runs selected experiment logic\n",
    encoding="utf-8"
)

sections["experiments"].write_text(
    "# Experiments Folder\n\n"
    "Each experiment has its own folder inside `experiments/`, containing:\n\n"
    "- `config.yaml`: parameters for the run\n"
    "- `logic.py`: defines a `run()` method for simulation\n\n"
    "Run an experiment using:\n"
    "```bash\npython main.py --exp experiment_name\n```\n",
    encoding="utf-8"
)

sections["interface"].write_text(
    "# Interface (GUI)\n\n"
    "Located in the `interface/` folder. Uses `tkinter` for a native GUI.\n\n"
    "- `ui.py`: basic interface and input controls\n"
    "- `settings_form.py`: optional parameter selectors\n\n"
    "Launch with:\n"
    "```bash\npython main.py\n```\n",
    encoding="utf-8"
)

sections["output"].write_text(
    "# Output Folder\n\n"
    "Simulation results are saved to `output/`:\n\n"
    "- `logs/`: CSV files with results\n"
    "- `plots/`: static images\n"
    "- `frames/`: time-lapse data\n\n"
    "All subfolders are ignored by `.gitignore`.\n",
    encoding="utf-8"
)

sections["entry"].write_text(
    "# Entrypoint and Config\n\n"
    "## `main.py`\n"
    "Launches experiments or the GUI:\n\n"
    "- `python main.py --exp experiment_folder`\n"
    "- `python main.py` (to launch GUI)\n\n"
    "## Config Files\n"
    "- `config.default.yaml`: shared default parameters\n"
    "- `config.local.yaml`: machine-specific overrides\n",
    encoding="utf-8"
)

# Write the index file
with index_file.open("w", encoding="utf-8") as f:
    f.write("# Vireon Code Layout (Index)\n\n")
    f.write("This documentation describes the structure and logic of the Vireon Virtual Lab repository, split across modular sections for clarity.\n\n")
    f.write("## Sections\n\n")
    for label, path in sections.items():
        title = path.name.replace("_", " ").replace(".md", "").title()
        f.write(f"- [{title}](docs/layout_parts/{path.name})\n")
    f.write("\n---\n\n")
    f.write("## Folder Tree (Top-Level Layout)\n\n")
    f.write("```\n")
    for line in tree_lines:
        f.write(line + "\n")
    f.write("```\n")

print("✅ Wrote CODE_LAYOUT.md and all modular docs in docs/layout_parts/")
