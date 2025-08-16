# Vireon Virtual Lab Documentation

This folder contains structured documentation for the **Vireon Virtual Lab**, a simulation suite exploring alternative models of gravity based on charge–frequency–mass interactions.

## Documentation Sections

- [`CODE_LAYOUT.md`](CODE_LAYOUT.md)  
  Overview of the repository structure, core modules, experiment folders, output conventions, and configuration systems.

- [`layout_parts/`](layout_parts/)  
  Modular breakdown of the codebase, including details about:
  - Core simulation logic
  - Experiment structure
  - Output handling
  - GUI interface components (future)

## How to Contribute

If you're contributing to the Vireon project:

1. Run `python generate_layout.py` whenever the folder structure changes.
2. Update `config.default.yaml` and experiment `config.yaml` files with clear, minimal parameters.
3. Document new modules or experiments in `docs/layout_parts/`.

## Future Additions

- Full GUI documentation (planned for v0.2)
- Scientific background on charge-frequency gravity theory
- Experiment validation reports
- Graphical output samples

---

For questions or contributions, open an issue on [GitHub](https://github.com/DNIN-LIL/vireon-virtual-lab).
