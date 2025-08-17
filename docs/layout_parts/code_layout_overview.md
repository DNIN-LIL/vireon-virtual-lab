# Project Overview

The Vireon Virtual Lab is a modular simulation environment for physics research. This file explains the general structure.

- `core/`: reusable physics logic and utilities
- `experiments/`: simulation modules with config + logic
- `interface/`: GUI (Tkinter-based)
- `output/`: logs, plots, and generated frames
- `venv/`: virtual environment (local only)

### Project Tree

```
Vireon/
├── __init__.py
├── ai/
├── ├── __init__.py
├── └── analysis.py
├── config.default.yaml
├── config.local.yaml
├── core/
├── ├── __init__.py
├── ├── config_loader.py
├── ├── engine/
├── ├── ├── __init__.py
├── ├── └── lab_runner.py
├── ├── logger.py
├── ├── medium.py
├── ├── particle_engine.py
├── ├── physics.py
├── ├── visualizer.py
├── └── waveform_generator.py
├── docs/
├── ├── code_layout.html
├── ├── CODE_LAYOUT.md
├── ├── layout_parts/
├── ├── ├── code_layout_core_modules.md
├── ├── ├── code_layout_entry_and_config.md
├── ├── ├── code_layout_experiments.md
├── ├── ├── code_layout_interface.md
├── ├── ├── code_layout_output_handling.md
├── ├── └── code_layout_overview.md
├── └── readme.md
├── experiments/
├── ├── __init__.py
├── ├── charge_frequency_sweep/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── charge_frequency_sweep_in_plasma/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── field_orientation_variance/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── field_orientation_variance_in_plasma/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── interference_field_superposition/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── interference_field_superposition_in_plasma/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── mass_scaling_at_constant_qf/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── mass_scaling_at_constant_qf_in_plasma/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── plasma_resonance_collapse/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── resonant_particle_field/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── resonant_particle_field_in_plasma/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── toroidal_field_rotation/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── toroidal_field_rotation_in_plasma/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── vacuum_permittivity_modulation/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── vacuum_permittivity_modulation_in_plasma/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── waveform_shape_response/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── waveform_shape_response_in_plasma/
├── ├── ├── __init__.py
├── ├── ├── config.yaml
├── ├── └── logic.py
├── ├── z_electric_oscillation/
├── ├── ├── __init__.py
├── ├── ├── logic.py
├── ├── ├── plasma_sine/
├── ├── ├── ├── __init__.py
├── ├── ├── ├── config.yaml
├── ├── ├── └── logic.py
├── ├── ├── plasma_square/
├── ├── ├── ├── __init__.py
├── ├── ├── ├── config.yaml
├── ├── ├── └── logic.py
├── ├── ├── plasma_triangle/
├── ├── ├── ├── __init__.py
├── ├── ├── ├── config.yaml
├── ├── ├── └── logic.py
├── ├── ├── shared_logic.py
├── ├── ├── vacuum_sine/
├── ├── ├── ├── __init__.py
├── ├── ├── ├── config.yaml
├── ├── ├── └── logic.py
├── ├── ├── vacuum_square/
├── ├── ├── ├── __init__.py
├── ├── ├── ├── config.yaml
├── ├── ├── └── logic.py
├── ├── └── vacuum_triangle/
├── ├── └── ├── __init__.py
├── ├── └── ├── config.yaml
├── ├── └── └── logic.py
├── └── z_magnetic_oscillation/
├── └── ├── __init__.py
├── └── ├── logic.py
├── └── ├── plasma_sine/
├── └── ├── ├── __init__.py
├── └── ├── ├── config.yaml
├── └── ├── └── logic.py
├── └── ├── plasma_square/
├── └── ├── ├── __init__.py
├── └── ├── ├── config.yaml
├── └── ├── └── logic.py
├── └── ├── plasma_triangle/
├── └── ├── ├── __init__.py
├── └── ├── ├── config.yaml
├── └── ├── └── logic.py
├── └── ├── shared_logic.py
├── └── ├── vacuum_sine/
├── └── ├── ├── __init__.py
├── └── ├── ├── config.yaml
├── └── ├── └── logic.py
├── └── ├── vacuum_square/
├── └── ├── ├── __init__.py
├── └── ├── ├── config.yaml
├── └── ├── └── logic.py
├── └── └── vacuum_triangle/
├── └── └── ├── __init__.py
├── └── └── ├── config.yaml
├── └── └── └── logic.py
├── generate_layout.py
├── interface/
├── main.py
├── output/
├── ├── charge_frequency_sweep/
├── ├── ├── force_matrix.csv
├── ├── └── force_matrix.png
├── ├── charge_frequency_sweep_in_plasma/
├── ├── ├── force_matrix.csv
├── ├── └── force_matrix.png
├── ├── electric_oscillation/
├── ├── ├── vacuum_sine/
├── ├── ├── ├── force_trace.csv
├── ├── ├── ├── force_trace.png
├── ├── ├── ├── orbit.png
├── ├── ├── ├── signal.png
├── ├── ├── ├── summary.csv
├── ├── ├── ├── time_series.csv
├── ├── ├── └── vector_time_series.csv
├── ├── ├── vacuum_square/
├── ├── ├── ├── force_trace.csv
├── ├── ├── ├── force_trace.png
├── ├── ├── ├── orbit.png
├── ├── ├── ├── signal.png
├── ├── ├── ├── summary.csv
├── ├── ├── ├── time_series.csv
├── ├── ├── └── vector_time_series.csv
├── ├── └── vacuum_triangle/
├── ├── └── ├── force_trace.csv
├── ├── └── ├── force_trace.png
├── ├── └── ├── orbit.png
├── ├── └── ├── signal.png
├── ├── └── ├── summary.csv
├── ├── └── ├── time_series.csv
├── ├── └── └── vector_time_series.csv
├── ├── field_orientation_variance/
├── ├── ├── force_matrix_angle_0deg.csv
├── ├── ├── force_matrix_angle_0deg.png
├── ├── ├── force_matrix_angle_15deg.csv
├── ├── ├── force_matrix_angle_15deg.png
├── ├── ├── force_matrix_angle_30deg.csv
├── ├── ├── force_matrix_angle_30deg.png
├── ├── ├── force_matrix_angle_45deg.csv
├── ├── ├── force_matrix_angle_45deg.png
├── ├── ├── force_matrix_angle_60deg.csv
├── ├── ├── force_matrix_angle_60deg.png
├── ├── ├── force_matrix_angle_75deg.csv
├── ├── ├── force_matrix_angle_75deg.png
├── ├── ├── force_matrix_angle_90deg.csv
├── ├── ├── force_matrix_angle_90deg.png
├── ├── └── forces_3d.npz
├── ├── field_orientation_variance_in_plasma/
├── ├── ├── force_matrix_angle_0deg.csv
├── ├── ├── force_matrix_angle_0deg.png
├── ├── ├── force_matrix_angle_15deg.csv
├── ├── ├── force_matrix_angle_15deg.png
├── ├── ├── force_matrix_angle_30deg.csv
├── ├── ├── force_matrix_angle_30deg.png
├── ├── ├── force_matrix_angle_45deg.csv
├── ├── ├── force_matrix_angle_45deg.png
├── ├── ├── force_matrix_angle_60deg.csv
├── ├── ├── force_matrix_angle_60deg.png
├── ├── ├── force_matrix_angle_75deg.csv
├── ├── ├── force_matrix_angle_75deg.png
├── ├── ├── force_matrix_angle_90deg.csv
├── ├── ├── force_matrix_angle_90deg.png
├── ├── └── forces_3d.npz
├── ├── interference_field_superposition/
├── ├── ├── force_map.csv
├── ├── ├── force_map.png
├── ├── ├── force_vector_quiver.png
├── ├── ├── force_vector_x.csv
├── ├── ├── force_vector_y.csv
├── ├── ├── gravimeter_signal.csv
├── ├── ├── phasor_summary.csv
├── ├── ├── potential_map.csv
├── ├── └── potential_map.png
├── ├── interference_field_superposition_in_plasma/
├── ├── ├── force_map.csv
├── ├── ├── force_map.png
├── ├── ├── force_vector_quiver.png
├── ├── ├── force_vector_x.csv
├── ├── ├── force_vector_y.csv
├── ├── ├── phasor_summary.csv
├── ├── ├── potential_map.csv
├── ├── ├── potential_map.png
├── ├── └── vorticity.csv
├── ├── magnetic_oscillation/
├── ├── ├── vacuum_sine/
├── ├── ├── ├── force_trace.csv
├── ├── ├── ├── force_trace.png
├── ├── ├── └── summary.csv
├── ├── ├── vacuum_square/
├── ├── ├── ├── force_trace.csv
├── ├── ├── ├── force_trace.png
├── ├── ├── └── summary.csv
├── ├── └── vacuum_triangle/
├── ├── └── ├── force_trace.csv
├── ├── └── ├── force_trace.png
├── ├── └── └── summary.csv
├── ├── mass_scaling/
├── ├── mass_scaling_at_constant_qf/
├── ├── ├── accel_vs_mass.png
├── ├── ├── force_vs_mass.png
├── ├── ├── mass_force_accel.csv
├── ├── └── results.npz
├── ├── mass_scaling_at_constant_qf_in_plasma/
├── ├── ├── accel_vs_mass.png
├── ├── ├── force_vs_mass.png
├── ├── ├── mass_force_accel.csv
├── ├── └── results.npz
├── ├── plasma_resonance_collapse/
├── ├── ├── collapse_trace.csv
├── ├── ├── collapse_trace.png
├── ├── ├── final_polar_sawtooth.png
├── ├── ├── final_polar_sine.png
├── ├── ├── final_polar_square.png
├── ├── ├── final_polar_triangle.png
├── ├── ├── modulated/
├── ├── ├── ├── collapse_trace.csv
├── ├── ├── ├── energy.png
├── ├── ├── ├── frame_0000.png
├── ├── ├── ├── frame_0100.png
├── ├── ├── ├── frame_0200.png
├── ├── ├── ├── frame_0300.png
├── ├── ├── ├── frame_0400.png
├── ├── ├── ├── frame_0500.png
├── ├── ├── ├── frame_0600.png
├── ├── ├── ├── frame_0700.png
├── ├── ├── ├── frame_0800.png
├── ├── ├── ├── frame_0900.png
├── ├── ├── ├── frame_0999.png
├── ├── ├── ├── positions_t0000.csv
├── ├── ├── ├── positions_t0100.csv
├── ├── ├── ├── positions_t0200.csv
├── ├── ├── ├── positions_t0300.csv
├── ├── ├── ├── positions_t0400.csv
├── ├── ├── ├── positions_t0500.csv
├── ├── ├── ├── positions_t0600.csv
├── ├── ├── ├── positions_t0700.csv
├── ├── ├── ├── positions_t0800.csv
├── ├── ├── ├── positions_t0900.csv
├── ├── ├── ├── positions_t0999.csv
├── ├── ├── ├── radius.png
├── ├── ├── └── radius_trace.csv
├── ├── ├── radius_timeseries_sawtooth.png
├── ├── ├── radius_timeseries_sine.png
├── ├── ├── radius_timeseries_square.png
├── ├── ├── radius_timeseries_triangle.png
├── ├── ├── results_sawtooth.npz
├── ├── ├── results_sine.npz
├── ├── ├── results_square.npz
├── ├── ├── results_triangle.npz
├── ├── ├── sine/
├── ├── ├── ├── collapse_trace.csv
├── ├── ├── ├── energy.png
├── ├── ├── ├── frame_0000.png
├── ├── ├── ├── frame_0100.png
├── ├── ├── ├── frame_0200.png
├── ├── ├── ├── frame_0300.png
├── ├── ├── ├── frame_0400.png
├── ├── ├── ├── frame_0500.png
├── ├── ├── ├── frame_0600.png
├── ├── ├── ├── frame_0700.png
├── ├── ├── ├── frame_0800.png
├── ├── ├── ├── frame_0900.png
├── ├── ├── ├── frame_0999.png
├── ├── ├── ├── positions_t0000.csv
├── ├── ├── ├── positions_t0100.csv
├── ├── ├── ├── positions_t0200.csv
├── ├── ├── ├── positions_t0300.csv
├── ├── ├── ├── positions_t0400.csv
├── ├── ├── ├── positions_t0500.csv
├── ├── ├── ├── positions_t0600.csv
├── ├── ├── ├── positions_t0700.csv
├── ├── ├── ├── positions_t0800.csv
├── ├── ├── ├── positions_t0900.csv
├── ├── ├── ├── positions_t0999.csv
├── ├── ├── ├── radius.png
├── ├── ├── └── radius_trace.csv
├── ├── ├── square/
├── ├── ├── ├── collapse_trace.csv
├── ├── ├── ├── energy.png
├── ├── ├── ├── frame_0000.png
├── ├── ├── ├── frame_0100.png
├── ├── ├── ├── frame_0200.png
├── ├── ├── ├── frame_0300.png
├── ├── ├── ├── frame_0400.png
├── ├── ├── ├── frame_0500.png
├── ├── ├── ├── frame_0600.png
├── ├── ├── ├── frame_0700.png
├── ├── ├── ├── frame_0800.png
├── ├── ├── ├── frame_0900.png
├── ├── ├── ├── frame_0999.png
├── ├── ├── ├── positions_t0000.csv
├── ├── ├── ├── positions_t0100.csv
├── ├── ├── ├── positions_t0200.csv
├── ├── ├── ├── positions_t0300.csv
├── ├── ├── ├── positions_t0400.csv
├── ├── ├── ├── positions_t0500.csv
├── ├── ├── ├── positions_t0600.csv
├── ├── ├── ├── positions_t0700.csv
├── ├── ├── ├── positions_t0800.csv
├── ├── ├── ├── positions_t0900.csv
├── ├── ├── ├── positions_t0999.csv
├── ├── ├── ├── radius.png
├── ├── ├── └── radius_trace.csv
├── ├── ├── time_series_sawtooth.csv
├── ├── ├── time_series_sine.csv
├── ├── ├── time_series_square.csv
├── ├── ├── time_series_triangle.csv
├── ├── └── triangle/
├── ├── └── ├── collapse_trace.csv
├── ├── └── ├── energy.png
├── ├── └── ├── frame_0000.png
├── ├── └── ├── frame_0100.png
├── ├── └── ├── frame_0200.png
├── ├── └── ├── frame_0300.png
├── ├── └── ├── frame_0400.png
├── ├── └── ├── frame_0500.png
├── ├── └── ├── frame_0600.png
├── ├── └── ├── frame_0700.png
├── ├── └── ├── frame_0800.png
├── ├── └── ├── frame_0900.png
├── ├── └── ├── frame_0999.png
├── ├── └── ├── positions_t0000.csv
├── ├── └── ├── positions_t0100.csv
├── ├── └── ├── positions_t0200.csv
├── ├── └── ├── positions_t0300.csv
├── ├── └── ├── positions_t0400.csv
├── ├── └── ├── positions_t0500.csv
├── ├── └── ├── positions_t0600.csv
├── ├── └── ├── positions_t0700.csv
├── ├── └── ├── positions_t0800.csv
├── ├── └── ├── positions_t0900.csv
├── ├── └── ├── positions_t0999.csv
├── ├── └── ├── radius.png
├── ├── └── └── radius_trace.csv
├── ├── resonant_particle_field/
├── ├── ├── field_grad_sawtooth.png
├── ├── ├── field_grad_sine.png
├── ├── ├── field_grad_square.png
├── ├── ├── field_grad_triangle.png
├── ├── ├── field_sawtooth.csv
├── ├── ├── field_sawtooth.png
├── ├── ├── field_sine.csv
├── ├── ├── field_sine.png
├── ├── ├── field_square.csv
├── ├── ├── field_square.png
├── ├── ├── field_triangle.csv
├── ├── ├── field_triangle.png
├── ├── ├── potential_sawtooth.csv
├── ├── ├── potential_sine.csv
├── ├── ├── potential_square.csv
├── ├── ├── potential_triangle.csv
├── ├── ├── resonance_force_plot.png
├── ├── ├── resonance_force_trace.csv
├── ├── └── summary.npz
├── ├── resonant_particle_field_in_plasma/
├── ├── ├── field_grad_sawtooth.png
├── ├── ├── field_grad_sine.png
├── ├── ├── field_grad_square.png
├── ├── ├── field_grad_triangle.png
├── ├── ├── field_sawtooth.csv
├── ├── ├── field_sawtooth.png
├── ├── ├── field_sine.csv
├── ├── ├── field_sine.png
├── ├── ├── field_square.csv
├── ├── ├── field_square.png
├── ├── ├── field_triangle.csv
├── ├── ├── field_triangle.png
├── ├── ├── potential_sawtooth.csv
├── ├── ├── potential_sine.csv
├── ├── ├── potential_square.csv
├── ├── ├── potential_triangle.csv
├── ├── └── summary.npz
├── ├── toroidal_field_rotation/
├── ├── ├── field_grad_sawtooth.png
├── ├── ├── field_grad_sine.png
├── ├── ├── field_grad_square.png
├── ├── ├── field_grad_triangle.png
├── ├── ├── field_sawtooth.csv
├── ├── ├── field_sawtooth.png
├── ├── ├── field_sine.csv
├── ├── ├── field_sine.png
├── ├── ├── field_square.csv
├── ├── ├── field_square.png
├── ├── ├── field_triangle.csv
├── ├── ├── field_triangle.png
├── ├── ├── modulated/
├── ├── ├── ├── toroidal_force_plot.png
├── ├── ├── └── toroidal_force_trace.csv
├── ├── ├── potential_sawtooth.csv
├── ├── ├── potential_sine.csv
├── ├── ├── potential_square.csv
├── ├── ├── potential_triangle.csv
├── ├── ├── sine/
├── ├── ├── ├── toroidal_force_plot.png
├── ├── ├── └── toroidal_force_trace.csv
├── ├── ├── square/
├── ├── ├── ├── toroidal_force_plot.png
├── ├── ├── └── toroidal_force_trace.csv
├── ├── ├── summary.npz
├── ├── └── triangle/
├── ├── └── ├── toroidal_force_plot.png
├── ├── └── └── toroidal_force_trace.csv
├── ├── toroidal_field_rotation_in_plasma/
├── ├── ├── field_grad_sawtooth.png
├── ├── ├── field_grad_sine.png
├── ├── ├── field_grad_square.png
├── ├── ├── field_grad_triangle.png
├── ├── ├── field_sawtooth.csv
├── ├── ├── field_sawtooth.png
├── ├── ├── field_sine.csv
├── ├── ├── field_sine.png
├── ├── ├── field_square.csv
├── ├── ├── field_square.png
├── ├── ├── field_triangle.csv
├── ├── ├── field_triangle.png
├── ├── ├── potential_sawtooth.csv
├── ├── ├── potential_sine.csv
├── ├── ├── potential_square.csv
├── ├── ├── potential_triangle.csv
├── ├── └── summary.npz
├── ├── vacuum_permittivity_modulation/
├── ├── ├── accel_vs_epsilon.png
├── ├── ├── epsilon_sweep.csv
├── ├── ├── force_vs_epsilon.png
├── ├── ├── modulated/
├── ├── ├── results.npz
├── ├── ├── sine/
├── ├── ├── ├── permittivity_force_plot.png
├── ├── ├── └── permittivity_force_response.csv
├── ├── ├── square/
├── ├── ├── ├── permittivity_force_plot.png
├── ├── ├── └── permittivity_force_response.csv
├── ├── └── triangle/
├── ├── └── ├── permittivity_force_plot.png
├── ├── └── └── permittivity_force_response.csv
├── ├── vacuum_permittivity_modulation_in_plasma/
├── ├── ├── accel_vs_epsilon_plasma.png
├── ├── ├── epsilon_sweep_plasma.csv
├── ├── ├── force_vs_epsilon_plasma.png
├── ├── ├── results_plasma.npz
├── ├── └── sine/
├── ├── └── ├── plasma_permittivity_force_plot.png
├── ├── └── └── plasma_permittivity_force_response.csv
├── ├── waveform_shape_response/
├── ├── ├── results.npz
├── ├── ├── sine_waveform_plot.png
├── ├── ├── square_waveform_plot.png
├── ├── ├── summary_metrics.csv
├── ├── ├── time_series_sine.csv
├── ├── ├── time_series_square.csv
├── ├── ├── time_series_triangle.csv
├── ├── ├── triangle_waveform_plot.png
├── ├── ├── waveform_force_results.csv
├── ├── └── waveform_overlay.png
├── ├── waveform_shape_response_in_plasma/
├── ├── ├── results_plasma.npz
├── ├── ├── summary_metrics.csv
├── ├── ├── time_series_sine.csv
├── ├── ├── time_series_square.csv
├── ├── ├── time_series_triangle.csv
├── ├── └── waveform_overlay_plasma.png
├── ├── z_electric_oscillation/
├── ├── ├── vacuum_sine/
├── ├── ├── ├── orbit.png
├── ├── ├── ├── signal.png
├── ├── ├── ├── time_series.csv
├── ├── ├── └── vector_time_series.csv
├── ├── ├── vacuum_square/
├── ├── ├── ├── orbit.png
├── ├── ├── ├── signal.png
├── ├── ├── ├── time_series.csv
├── ├── ├── └── vector_time_series.csv
├── ├── └── vacuum_triangle/
├── ├── └── ├── orbit.png
├── ├── └── ├── signal.png
├── ├── └── ├── time_series.csv
├── ├── └── └── vector_time_series.csv
├── └── z_magnetic_oscillation/
├── └── ├── plasma_triangle/
├── └── ├── ├── orbit.png
├── └── ├── ├── signal.png
├── └── ├── ├── time_series.csv
├── └── ├── └── vector_time_series.csv
├── └── ├── vacuum_sine/
├── └── ├── ├── orbit.png
├── └── ├── ├── signal.png
├── └── ├── ├── time_series.csv
├── └── ├── └── vector_time_series.csv
├── └── └── vacuum_square/
├── └── └── ├── orbit.png
├── └── └── ├── signal.png
├── └── └── ├── time_series.csv
├── └── └── └── vector_time_series.csv
├── venv/
├── ├── Include/
├── ├── Lib/
├── ├── └── site-packages/
├── ├── └── ├── _distutils_hack/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── └── override.py
├── ├── └── ├── _yaml/
├── ├── └── ├── └── __init__.py
├── ├── └── ├── contourpy/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── _contourpy.cp312-win_amd64.lib
├── ├── └── ├── ├── _contourpy.cp312-win_amd64.pyd
├── ├── └── ├── ├── _contourpy.pyi
├── ├── └── ├── ├── _version.py
├── ├── └── ├── ├── array.py
├── ├── └── ├── ├── chunk.py
├── ├── └── ├── ├── convert.py
├── ├── └── ├── ├── dechunk.py
├── ├── └── ├── ├── enum_util.py
├── ├── └── ├── ├── py.typed
├── ├── └── ├── ├── typecheck.py
├── ├── └── ├── ├── types.py
├── ├── └── ├── └── util/
├── ├── └── ├── └── ├── __init__.py
├── ├── └── ├── └── ├── _build_config.py
├── ├── └── ├── └── ├── bokeh_renderer.py
├── ├── └── ├── └── ├── bokeh_util.py
├── ├── └── ├── └── ├── data.py
├── ├── └── ├── └── ├── mpl_renderer.py
├── ├── └── ├── └── ├── mpl_util.py
├── ├── └── ├── └── └── renderer.py
├── ├── └── ├── contourpy-1.3.3.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── └── WHEEL
├── ├── └── ├── cycler/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── └── py.typed
├── ├── └── ├── cycler-0.12.1.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── └── WHEEL
├── ├── └── ├── dateutil/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── _common.py
├── ├── └── ├── ├── _version.py
├── ├── └── ├── ├── easter.py
├── ├── └── ├── ├── parser/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _parser.py
├── ├── └── ├── ├── └── isoparser.py
├── ├── └── ├── ├── relativedelta.py
├── ├── └── ├── ├── rrule.py
├── ├── └── ├── ├── tz/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _common.py
├── ├── └── ├── ├── ├── _factories.py
├── ├── └── ├── ├── ├── tz.py
├── ├── └── ├── ├── └── win.py
├── ├── └── ├── ├── tzwin.py
├── ├── └── ├── ├── utils.py
├── ├── └── ├── └── zoneinfo/
├── ├── └── ├── └── ├── __init__.py
├── ├── └── ├── └── ├── dateutil-zoneinfo.tar.gz
├── ├── └── ├── └── └── rebuild.py
├── ├── └── ├── distutils-precedence.pth
├── ├── └── ├── fontTools/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── __main__.py
├── ├── └── ├── ├── afmLib.py
├── ├── └── ├── ├── agl.py
├── ├── └── ├── ├── cffLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── CFF2ToCFF.py
├── ├── └── ├── ├── ├── CFFToCFF2.py
├── ├── └── ├── ├── ├── specializer.py
├── ├── └── ├── ├── ├── transforms.py
├── ├── └── ├── ├── └── width.py
├── ├── └── ├── ├── colorLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── builder.py
├── ├── └── ├── ├── ├── errors.py
├── ├── └── ├── ├── ├── geometry.py
├── ├── └── ├── ├── ├── table_builder.py
├── ├── └── ├── ├── └── unbuilder.py
├── ├── └── ├── ├── config/
├── ├── └── ├── ├── └── __init__.py
├── ├── └── ├── ├── cu2qu/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── benchmark.py
├── ├── └── ├── ├── ├── cli.py
├── ├── └── ├── ├── ├── cu2qu.c
├── ├── └── ├── ├── ├── cu2qu.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── cu2qu.py
├── ├── └── ├── ├── ├── errors.py
├── ├── └── ├── ├── └── ufo.py
├── ├── └── ├── ├── designspaceLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── split.py
├── ├── └── ├── ├── ├── statNames.py
├── ├── └── ├── ├── └── types.py
├── ├── └── ├── ├── encodings/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── codecs.py
├── ├── └── ├── ├── ├── MacRoman.py
├── ├── └── ├── ├── └── StandardEncoding.py
├── ├── └── ├── ├── feaLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ast.py
├── ├── └── ├── ├── ├── builder.py
├── ├── └── ├── ├── ├── error.py
├── ├── └── ├── ├── ├── lexer.c
├── ├── └── ├── ├── ├── lexer.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── lexer.py
├── ├── └── ├── ├── ├── location.py
├── ├── └── ├── ├── ├── lookupDebugInfo.py
├── ├── └── ├── ├── ├── parser.py
├── ├── └── ├── ├── └── variableScalar.py
├── ├── └── ├── ├── fontBuilder.py
├── ├── └── ├── ├── help.py
├── ├── └── ├── ├── merge/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── cmap.py
├── ├── └── ├── ├── ├── layout.py
├── ├── └── ├── ├── ├── options.py
├── ├── └── ├── ├── ├── tables.py
├── ├── └── ├── ├── ├── unicode.py
├── ├── └── ├── ├── └── util.py
├── ├── └── ├── ├── misc/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── arrayTools.py
├── ├── └── ├── ├── ├── bezierTools.c
├── ├── └── ├── ├── ├── bezierTools.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── bezierTools.py
├── ├── └── ├── ├── ├── classifyTools.py
├── ├── └── ├── ├── ├── cliTools.py
├── ├── └── ├── ├── ├── configTools.py
├── ├── └── ├── ├── ├── cython.py
├── ├── └── ├── ├── ├── dictTools.py
├── ├── └── ├── ├── ├── eexec.py
├── ├── └── ├── ├── ├── encodingTools.py
├── ├── └── ├── ├── ├── etree.py
├── ├── └── ├── ├── ├── filenames.py
├── ├── └── ├── ├── ├── filesystem/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _base.py
├── ├── └── ├── ├── ├── ├── _copy.py
├── ├── └── ├── ├── ├── ├── _errors.py
├── ├── └── ├── ├── ├── ├── _info.py
├── ├── └── ├── ├── ├── ├── _osfs.py
├── ├── └── ├── ├── ├── ├── _path.py
├── ├── └── ├── ├── ├── ├── _subfs.py
├── ├── └── ├── ├── ├── ├── _tempfs.py
├── ├── └── ├── ├── ├── ├── _tools.py
├── ├── └── ├── ├── ├── ├── _walk.py
├── ├── └── ├── ├── ├── └── _zipfs.py
├── ├── └── ├── ├── ├── fixedTools.py
├── ├── └── ├── ├── ├── intTools.py
├── ├── └── ├── ├── ├── iterTools.py
├── ├── └── ├── ├── ├── lazyTools.py
├── ├── └── ├── ├── ├── loggingTools.py
├── ├── └── ├── ├── ├── macCreatorType.py
├── ├── └── ├── ├── ├── macRes.py
├── ├── └── ├── ├── ├── plistlib/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── psCharStrings.py
├── ├── └── ├── ├── ├── psLib.py
├── ├── └── ├── ├── ├── psOperators.py
├── ├── └── ├── ├── ├── py23.py
├── ├── └── ├── ├── ├── roundTools.py
├── ├── └── ├── ├── ├── sstruct.py
├── ├── └── ├── ├── ├── symfont.py
├── ├── └── ├── ├── ├── testTools.py
├── ├── └── ├── ├── ├── textTools.py
├── ├── └── ├── ├── ├── timeTools.py
├── ├── └── ├── ├── ├── transform.py
├── ├── └── ├── ├── ├── treeTools.py
├── ├── └── ├── ├── ├── vector.py
├── ├── └── ├── ├── ├── visitor.py
├── ├── └── ├── ├── ├── xmlReader.py
├── ├── └── ├── ├── └── xmlWriter.py
├── ├── └── ├── ├── mtiLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── └── __main__.py
├── ├── └── ├── ├── otlLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── builder.py
├── ├── └── ├── ├── ├── error.py
├── ├── └── ├── ├── ├── maxContextCalc.py
├── ├── └── ├── ├── └── optimize/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── __main__.py
├── ├── └── ├── ├── └── └── gpos.py
├── ├── └── ├── ├── pens/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── areaPen.py
├── ├── └── ├── ├── ├── basePen.py
├── ├── └── ├── ├── ├── boundsPen.py
├── ├── └── ├── ├── ├── cairoPen.py
├── ├── └── ├── ├── ├── cocoaPen.py
├── ├── └── ├── ├── ├── cu2quPen.py
├── ├── └── ├── ├── ├── explicitClosingLinePen.py
├── ├── └── ├── ├── ├── filterPen.py
├── ├── └── ├── ├── ├── freetypePen.py
├── ├── └── ├── ├── ├── hashPointPen.py
├── ├── └── ├── ├── ├── momentsPen.c
├── ├── └── ├── ├── ├── momentsPen.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── momentsPen.py
├── ├── └── ├── ├── ├── perimeterPen.py
├── ├── └── ├── ├── ├── pointInsidePen.py
├── ├── └── ├── ├── ├── pointPen.py
├── ├── └── ├── ├── ├── qtPen.py
├── ├── └── ├── ├── ├── qu2cuPen.py
├── ├── └── ├── ├── ├── quartzPen.py
├── ├── └── ├── ├── ├── recordingPen.py
├── ├── └── ├── ├── ├── reportLabPen.py
├── ├── └── ├── ├── ├── reverseContourPen.py
├── ├── └── ├── ├── ├── roundingPen.py
├── ├── └── ├── ├── ├── statisticsPen.py
├── ├── └── ├── ├── ├── svgPathPen.py
├── ├── └── ├── ├── ├── t2CharStringPen.py
├── ├── └── ├── ├── ├── teePen.py
├── ├── └── ├── ├── ├── transformPen.py
├── ├── └── ├── ├── ├── ttGlyphPen.py
├── ├── └── ├── ├── └── wxPen.py
├── ├── └── ├── ├── qu2cu/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── benchmark.py
├── ├── └── ├── ├── ├── cli.py
├── ├── └── ├── ├── ├── qu2cu.c
├── ├── └── ├── ├── ├── qu2cu.cp312-win_amd64.pyd
├── ├── └── ├── ├── └── qu2cu.py
├── ├── └── ├── ├── subset/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── cff.py
├── ├── └── ├── ├── ├── svg.py
├── ├── └── ├── ├── └── util.py
├── ├── └── ├── ├── svgLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── └── path/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── arc.py
├── ├── └── ├── ├── └── ├── parser.py
├── ├── └── ├── ├── └── └── shapes.py
├── ├── └── ├── ├── t1Lib/
├── ├── └── ├── ├── └── __init__.py
├── ├── └── ├── ├── tfmLib.py
├── ├── └── ├── ├── ttLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── macUtils.py
├── ├── └── ├── ├── ├── removeOverlaps.py
├── ├── └── ├── ├── ├── reorderGlyphs.py
├── ├── └── ├── ├── ├── scaleUpem.py
├── ├── └── ├── ├── ├── sfnt.py
├── ├── └── ├── ├── ├── standardGlyphOrder.py
├── ├── └── ├── ├── ├── tables/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _a_n_k_r.py
├── ├── └── ├── ├── ├── ├── _a_v_a_r.py
├── ├── └── ├── ├── ├── ├── _b_s_l_n.py
├── ├── └── ├── ├── ├── ├── _c_i_d_g.py
├── ├── └── ├── ├── ├── ├── _c_m_a_p.py
├── ├── └── ├── ├── ├── ├── _c_v_a_r.py
├── ├── └── ├── ├── ├── ├── _c_v_t.py
├── ├── └── ├── ├── ├── ├── _f_e_a_t.py
├── ├── └── ├── ├── ├── ├── _f_p_g_m.py
├── ├── └── ├── ├── ├── ├── _f_v_a_r.py
├── ├── └── ├── ├── ├── ├── _g_a_s_p.py
├── ├── └── ├── ├── ├── ├── _g_c_i_d.py
├── ├── └── ├── ├── ├── ├── _g_l_y_f.py
├── ├── └── ├── ├── ├── ├── _g_v_a_r.py
├── ├── └── ├── ├── ├── ├── _h_d_m_x.py
├── ├── └── ├── ├── ├── ├── _h_e_a_d.py
├── ├── └── ├── ├── ├── ├── _h_h_e_a.py
├── ├── └── ├── ├── ├── ├── _h_m_t_x.py
├── ├── └── ├── ├── ├── ├── _k_e_r_n.py
├── ├── └── ├── ├── ├── ├── _l_c_a_r.py
├── ├── └── ├── ├── ├── ├── _l_o_c_a.py
├── ├── └── ├── ├── ├── ├── _l_t_a_g.py
├── ├── └── ├── ├── ├── ├── _m_a_x_p.py
├── ├── └── ├── ├── ├── ├── _m_e_t_a.py
├── ├── └── ├── ├── ├── ├── _m_o_r_t.py
├── ├── └── ├── ├── ├── ├── _m_o_r_x.py
├── ├── └── ├── ├── ├── ├── _n_a_m_e.py
├── ├── └── ├── ├── ├── ├── _o_p_b_d.py
├── ├── └── ├── ├── ├── ├── _p_o_s_t.py
├── ├── └── ├── ├── ├── ├── _p_r_e_p.py
├── ├── └── ├── ├── ├── ├── _p_r_o_p.py
├── ├── └── ├── ├── ├── ├── _s_b_i_x.py
├── ├── └── ├── ├── ├── ├── _t_r_a_k.py
├── ├── └── ├── ├── ├── ├── _v_h_e_a.py
├── ├── └── ├── ├── ├── ├── _v_m_t_x.py
├── ├── └── ├── ├── ├── ├── asciiTable.py
├── ├── └── ├── ├── ├── ├── B_A_S_E_.py
├── ├── └── ├── ├── ├── ├── BitmapGlyphMetrics.py
├── ├── └── ├── ├── ├── ├── C_B_D_T_.py
├── ├── └── ├── ├── ├── ├── C_B_L_C_.py
├── ├── └── ├── ├── ├── ├── C_F_F_.py
├── ├── └── ├── ├── ├── ├── C_F_F__2.py
├── ├── └── ├── ├── ├── ├── C_O_L_R_.py
├── ├── └── ├── ├── ├── ├── C_P_A_L_.py
├── ├── └── ├── ├── ├── ├── D__e_b_g.py
├── ├── └── ├── ├── ├── ├── D_S_I_G_.py
├── ├── └── ├── ├── ├── ├── DefaultTable.py
├── ├── └── ├── ├── ├── ├── E_B_D_T_.py
├── ├── └── ├── ├── ├── ├── E_B_L_C_.py
├── ├── └── ├── ├── ├── ├── F__e_a_t.py
├── ├── └── ├── ├── ├── ├── F_F_T_M_.py
├── ├── └── ├── ├── ├── ├── G__l_a_t.py
├── ├── └── ├── ├── ├── ├── G__l_o_c.py
├── ├── └── ├── ├── ├── ├── G_D_E_F_.py
├── ├── └── ├── ├── ├── ├── G_M_A_P_.py
├── ├── └── ├── ├── ├── ├── G_P_K_G_.py
├── ├── └── ├── ├── ├── ├── G_P_O_S_.py
├── ├── └── ├── ├── ├── ├── G_S_U_B_.py
├── ├── └── ├── ├── ├── ├── G_V_A_R_.py
├── ├── └── ├── ├── ├── ├── grUtils.py
├── ├── └── ├── ├── ├── ├── H_V_A_R_.py
├── ├── └── ├── ├── ├── ├── J_S_T_F_.py
├── ├── └── ├── ├── ├── ├── L_T_S_H_.py
├── ├── └── ├── ├── ├── ├── M_A_T_H_.py
├── ├── └── ├── ├── ├── ├── M_E_T_A_.py
├── ├── └── ├── ├── ├── ├── M_V_A_R_.py
├── ├── └── ├── ├── ├── ├── O_S_2f_2.py
├── ├── └── ├── ├── ├── ├── otBase.py
├── ├── └── ├── ├── ├── ├── otConverters.py
├── ├── └── ├── ├── ├── ├── otData.py
├── ├── └── ├── ├── ├── ├── otTables.py
├── ├── └── ├── ├── ├── ├── otTraverse.py
├── ├── └── ├── ├── ├── ├── S__i_l_f.py
├── ├── └── ├── ├── ├── ├── S__i_l_l.py
├── ├── └── ├── ├── ├── ├── S_I_N_G_.py
├── ├── └── ├── ├── ├── ├── S_T_A_T_.py
├── ├── └── ├── ├── ├── ├── S_V_G_.py
├── ├── └── ├── ├── ├── ├── sbixGlyph.py
├── ├── └── ├── ├── ├── ├── sbixStrike.py
├── ├── └── ├── ├── ├── ├── T_S_I__0.py
├── ├── └── ├── ├── ├── ├── T_S_I__1.py
├── ├── └── ├── ├── ├── ├── T_S_I__2.py
├── ├── └── ├── ├── ├── ├── T_S_I__3.py
├── ├── └── ├── ├── ├── ├── T_S_I__5.py
├── ├── └── ├── ├── ├── ├── T_S_I_B_.py
├── ├── └── ├── ├── ├── ├── T_S_I_C_.py
├── ├── └── ├── ├── ├── ├── T_S_I_D_.py
├── ├── └── ├── ├── ├── ├── T_S_I_J_.py
├── ├── └── ├── ├── ├── ├── T_S_I_P_.py
├── ├── └── ├── ├── ├── ├── T_S_I_S_.py
├── ├── └── ├── ├── ├── ├── T_S_I_V_.py
├── ├── └── ├── ├── ├── ├── T_T_F_A_.py
├── ├── └── ├── ├── ├── ├── table_API_readme.txt
├── ├── └── ├── ├── ├── ├── ttProgram.py
├── ├── └── ├── ├── ├── ├── TupleVariation.py
├── ├── └── ├── ├── ├── ├── V_A_R_C_.py
├── ├── └── ├── ├── ├── ├── V_D_M_X_.py
├── ├── └── ├── ├── ├── ├── V_O_R_G_.py
├── ├── └── ├── ├── ├── └── V_V_A_R_.py
├── ├── └── ├── ├── ├── ttCollection.py
├── ├── └── ├── ├── ├── ttFont.py
├── ├── └── ├── ├── ├── ttGlyphSet.py
├── ├── └── ├── ├── ├── ttVisitor.py
├── ├── └── ├── ├── └── woff2.py
├── ├── └── ├── ├── ttx.py
├── ├── └── ├── ├── ufoLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── converters.py
├── ├── └── ├── ├── ├── errors.py
├── ├── └── ├── ├── ├── etree.py
├── ├── └── ├── ├── ├── filenames.py
├── ├── └── ├── ├── ├── glifLib.py
├── ├── └── ├── ├── ├── kerning.py
├── ├── └── ├── ├── ├── plistlib.py
├── ├── └── ├── ├── ├── pointPen.py
├── ├── └── ├── ├── ├── utils.py
├── ├── └── ├── ├── └── validators.py
├── ├── └── ├── ├── unicode.py
├── ├── └── ├── ├── unicodedata/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── Blocks.py
├── ├── └── ├── ├── ├── Mirrored.py
├── ├── └── ├── ├── ├── OTTags.py
├── ├── └── ├── ├── ├── ScriptExtensions.py
├── ├── └── ├── ├── └── Scripts.py
├── ├── └── ├── ├── varLib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── avar.py
├── ├── └── ├── ├── ├── avarPlanner.py
├── ├── └── ├── ├── ├── builder.py
├── ├── └── ├── ├── ├── cff.py
├── ├── └── ├── ├── ├── errors.py
├── ├── └── ├── ├── ├── featureVars.py
├── ├── └── ├── ├── ├── hvar.py
├── ├── └── ├── ├── ├── instancer/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── featureVars.py
├── ├── └── ├── ├── ├── ├── names.py
├── ├── └── ├── ├── ├── └── solver.py
├── ├── └── ├── ├── ├── interpolatable.py
├── ├── └── ├── ├── ├── interpolatableHelpers.py
├── ├── └── ├── ├── ├── interpolatablePlot.py
├── ├── └── ├── ├── ├── interpolatableTestContourOrder.py
├── ├── └── ├── ├── ├── interpolatableTestStartingPoint.py
├── ├── └── ├── ├── ├── interpolate_layout.py
├── ├── └── ├── ├── ├── iup.c
├── ├── └── ├── ├── ├── iup.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── iup.py
├── ├── └── ├── ├── ├── merger.py
├── ├── └── ├── ├── ├── models.py
├── ├── └── ├── ├── ├── multiVarStore.py
├── ├── └── ├── ├── ├── mutator.py
├── ├── └── ├── ├── ├── mvar.py
├── ├── └── ├── ├── ├── plot.py
├── ├── └── ├── ├── ├── stat.py
├── ├── └── ├── ├── └── varStore.py
├── ├── └── ├── └── voltLib/
├── ├── └── ├── └── ├── __init__.py
├── ├── └── ├── └── ├── __main__.py
├── ├── └── ├── └── ├── ast.py
├── ├── └── ├── └── ├── error.py
├── ├── └── ├── └── ├── lexer.py
├── ├── └── ├── └── ├── parser.py
├── ├── └── ├── └── └── voltToFea.py
├── ├── └── ├── fonttools-4.59.0.dist-info/
├── ├── └── ├── ├── entry_points.txt
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── licenses/
├── ├── └── ├── ├── ├── LICENSE
├── ├── └── ├── ├── └── LICENSE.external
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── └── WHEEL
├── ├── └── ├── kiwisolver/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── _cext.cp312-win_amd64.pyd
├── ├── └── ├── ├── _cext.pyi
├── ├── └── ├── ├── exceptions.py
├── ├── └── ├── └── py.typed
├── ├── └── ├── kiwisolver-1.4.8.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── └── WHEEL
├── ├── └── ├── matplotlib/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── __init__.pyi
├── ├── └── ├── ├── _afm.py
├── ├── └── ├── ├── _animation_data.py
├── ├── └── ├── ├── _api/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── deprecation.py
├── ├── └── ├── ├── └── deprecation.pyi
├── ├── └── ├── ├── _blocking_input.py
├── ├── └── ├── ├── _c_internal_utils.cp312-win_amd64.pyd
├── ├── └── ├── ├── _c_internal_utils.pyi
├── ├── └── ├── ├── _cm.py
├── ├── └── ├── ├── _cm_bivar.py
├── ├── └── ├── ├── _cm_listed.py
├── ├── └── ├── ├── _cm_multivar.py
├── ├── └── ├── ├── _color_data.py
├── ├── └── ├── ├── _color_data.pyi
├── ├── └── ├── ├── _constrained_layout.py
├── ├── └── ├── ├── _docstring.py
├── ├── └── ├── ├── _docstring.pyi
├── ├── └── ├── ├── _enums.py
├── ├── └── ├── ├── _enums.pyi
├── ├── └── ├── ├── _fontconfig_pattern.py
├── ├── └── ├── ├── _image.cp312-win_amd64.pyd
├── ├── └── ├── ├── _image.pyi
├── ├── └── ├── ├── _internal_utils.py
├── ├── └── ├── ├── _layoutgrid.py
├── ├── └── ├── ├── _mathtext.py
├── ├── └── ├── ├── _mathtext_data.py
├── ├── └── ├── ├── _path.cp312-win_amd64.pyd
├── ├── └── ├── ├── _path.pyi
├── ├── └── ├── ├── _pylab_helpers.py
├── ├── └── ├── ├── _pylab_helpers.pyi
├── ├── └── ├── ├── _qhull.cp312-win_amd64.pyd
├── ├── └── ├── ├── _qhull.pyi
├── ├── └── ├── ├── _text_helpers.py
├── ├── └── ├── ├── _tight_bbox.py
├── ├── └── ├── ├── _tight_layout.py
├── ├── └── ├── ├── _tri.cp312-win_amd64.pyd
├── ├── └── ├── ├── _tri.pyi
├── ├── └── ├── ├── _type1font.py
├── ├── └── ├── ├── _version.py
├── ├── └── ├── ├── animation.py
├── ├── └── ├── ├── animation.pyi
├── ├── └── ├── ├── artist.py
├── ├── └── ├── ├── artist.pyi
├── ├── └── ├── ├── axes/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _axes.py
├── ├── └── ├── ├── ├── _axes.pyi
├── ├── └── ├── ├── ├── _base.py
├── ├── └── ├── ├── ├── _base.pyi
├── ├── └── ├── ├── ├── _secondary_axes.py
├── ├── └── ├── ├── └── _secondary_axes.pyi
├── ├── └── ├── ├── axis.py
├── ├── └── ├── ├── axis.pyi
├── ├── └── ├── ├── backend_bases.py
├── ├── └── ├── ├── backend_bases.pyi
├── ├── └── ├── ├── backend_managers.py
├── ├── └── ├── ├── backend_managers.pyi
├── ├── └── ├── ├── backend_tools.py
├── ├── └── ├── ├── backend_tools.pyi
├── ├── └── ├── ├── backends/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _backend_agg.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _backend_agg.pyi
├── ├── └── ├── ├── ├── _backend_gtk.py
├── ├── └── ├── ├── ├── _backend_pdf_ps.py
├── ├── └── ├── ├── ├── _backend_tk.py
├── ├── └── ├── ├── ├── _macosx.pyi
├── ├── └── ├── ├── ├── _tkagg.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _tkagg.pyi
├── ├── └── ├── ├── ├── backend_agg.py
├── ├── └── ├── ├── ├── backend_cairo.py
├── ├── └── ├── ├── ├── backend_gtk3.py
├── ├── └── ├── ├── ├── backend_gtk3agg.py
├── ├── └── ├── ├── ├── backend_gtk3cairo.py
├── ├── └── ├── ├── ├── backend_gtk4.py
├── ├── └── ├── ├── ├── backend_gtk4agg.py
├── ├── └── ├── ├── ├── backend_gtk4cairo.py
├── ├── └── ├── ├── ├── backend_macosx.py
├── ├── └── ├── ├── ├── backend_mixed.py
├── ├── └── ├── ├── ├── backend_nbagg.py
├── ├── └── ├── ├── ├── backend_pdf.py
├── ├── └── ├── ├── ├── backend_pgf.py
├── ├── └── ├── ├── ├── backend_ps.py
├── ├── └── ├── ├── ├── backend_qt.py
├── ├── └── ├── ├── ├── backend_qt5.py
├── ├── └── ├── ├── ├── backend_qt5agg.py
├── ├── └── ├── ├── ├── backend_qt5cairo.py
├── ├── └── ├── ├── ├── backend_qtagg.py
├── ├── └── ├── ├── ├── backend_qtcairo.py
├── ├── └── ├── ├── ├── backend_svg.py
├── ├── └── ├── ├── ├── backend_template.py
├── ├── └── ├── ├── ├── backend_tkagg.py
├── ├── └── ├── ├── ├── backend_tkcairo.py
├── ├── └── ├── ├── ├── backend_webagg.py
├── ├── └── ├── ├── ├── backend_webagg_core.py
├── ├── └── ├── ├── ├── backend_wx.py
├── ├── └── ├── ├── ├── backend_wxagg.py
├── ├── └── ├── ├── ├── backend_wxcairo.py
├── ├── └── ├── ├── ├── qt_compat.py
├── ├── └── ├── ├── ├── qt_editor/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _formlayout.py
├── ├── └── ├── ├── ├── └── figureoptions.py
├── ├── └── ├── ├── ├── registry.py
├── ├── └── ├── ├── └── web_backend/
├── ├── └── ├── ├── └── ├── all_figures.html
├── ├── └── ├── ├── └── ├── css/
├── ├── └── ├── ├── └── ├── ├── boilerplate.css
├── ├── └── ├── ├── └── ├── ├── fbm.css
├── ├── └── ├── ├── └── ├── ├── mpl.css
├── ├── └── ├── ├── └── ├── └── page.css
├── ├── └── ├── ├── └── ├── ipython_inline_figure.html
├── ├── └── ├── ├── └── ├── js/
├── ├── └── ├── ├── └── ├── ├── mpl.js
├── ├── └── ├── ├── └── ├── ├── mpl_tornado.js
├── ├── └── ├── ├── └── ├── └── nbagg_mpl.js
├── ├── └── ├── ├── └── └── single_figure.html
├── ├── └── ├── ├── bezier.py
├── ├── └── ├── ├── bezier.pyi
├── ├── └── ├── ├── category.py
├── ├── └── ├── ├── cbook.py
├── ├── └── ├── ├── cbook.pyi
├── ├── └── ├── ├── cm.py
├── ├── └── ├── ├── cm.pyi
├── ├── └── ├── ├── collections.py
├── ├── └── ├── ├── collections.pyi
├── ├── └── ├── ├── colorbar.py
├── ├── └── ├── ├── colorbar.pyi
├── ├── └── ├── ├── colorizer.py
├── ├── └── ├── ├── colorizer.pyi
├── ├── └── ├── ├── colors.py
├── ├── └── ├── ├── colors.pyi
├── ├── └── ├── ├── container.py
├── ├── └── ├── ├── container.pyi
├── ├── └── ├── ├── contour.py
├── ├── └── ├── ├── contour.pyi
├── ├── └── ├── ├── dates.py
├── ├── └── ├── ├── dviread.py
├── ├── └── ├── ├── dviread.pyi
├── ├── └── ├── ├── figure.py
├── ├── └── ├── ├── figure.pyi
├── ├── └── ├── ├── font_manager.py
├── ├── └── ├── ├── font_manager.pyi
├── ├── └── ├── ├── ft2font.cp312-win_amd64.pyd
├── ├── └── ├── ├── ft2font.pyi
├── ├── └── ├── ├── gridspec.py
├── ├── └── ├── ├── gridspec.pyi
├── ├── └── ├── ├── hatch.py
├── ├── └── ├── ├── hatch.pyi
├── ├── └── ├── ├── image.py
├── ├── └── ├── ├── image.pyi
├── ├── └── ├── ├── inset.py
├── ├── └── ├── ├── inset.pyi
├── ├── └── ├── ├── layout_engine.py
├── ├── └── ├── ├── layout_engine.pyi
├── ├── └── ├── ├── legend.py
├── ├── └── ├── ├── legend.pyi
├── ├── └── ├── ├── legend_handler.py
├── ├── └── ├── ├── legend_handler.pyi
├── ├── └── ├── ├── lines.py
├── ├── └── ├── ├── lines.pyi
├── ├── └── ├── ├── markers.py
├── ├── └── ├── ├── markers.pyi
├── ├── └── ├── ├── mathtext.py
├── ├── └── ├── ├── mathtext.pyi
├── ├── └── ├── ├── mlab.py
├── ├── └── ├── ├── mlab.pyi
├── ├── └── ├── ├── mpl-data/
├── ├── └── ├── ├── ├── fonts/
├── ├── └── ├── ├── ├── ├── afm/
├── ├── └── ├── ├── ├── ├── ├── cmex10.afm
├── ├── └── ├── ├── ├── ├── ├── cmmi10.afm
├── ├── └── ├── ├── ├── ├── ├── cmr10.afm
├── ├── └── ├── ├── ├── ├── ├── cmsy10.afm
├── ├── └── ├── ├── ├── ├── ├── cmtt10.afm
├── ├── └── ├── ├── ├── ├── ├── pagd8a.afm
├── ├── └── ├── ├── ├── ├── ├── pagdo8a.afm
├── ├── └── ├── ├── ├── ├── ├── pagk8a.afm
├── ├── └── ├── ├── ├── ├── ├── pagko8a.afm
├── ├── └── ├── ├── ├── ├── ├── pbkd8a.afm
├── ├── └── ├── ├── ├── ├── ├── pbkdi8a.afm
├── ├── └── ├── ├── ├── ├── ├── pbkl8a.afm
├── ├── └── ├── ├── ├── ├── ├── pbkli8a.afm
├── ├── └── ├── ├── ├── ├── ├── pcrb8a.afm
├── ├── └── ├── ├── ├── ├── ├── pcrbo8a.afm
├── ├── └── ├── ├── ├── ├── ├── pcrr8a.afm
├── ├── └── ├── ├── ├── ├── ├── pcrro8a.afm
├── ├── └── ├── ├── ├── ├── ├── phvb8a.afm
├── ├── └── ├── ├── ├── ├── ├── phvb8an.afm
├── ├── └── ├── ├── ├── ├── ├── phvbo8a.afm
├── ├── └── ├── ├── ├── ├── ├── phvbo8an.afm
├── ├── └── ├── ├── ├── ├── ├── phvl8a.afm
├── ├── └── ├── ├── ├── ├── ├── phvlo8a.afm
├── ├── └── ├── ├── ├── ├── ├── phvr8a.afm
├── ├── └── ├── ├── ├── ├── ├── phvr8an.afm
├── ├── └── ├── ├── ├── ├── ├── phvro8a.afm
├── ├── └── ├── ├── ├── ├── ├── phvro8an.afm
├── ├── └── ├── ├── ├── ├── ├── pncb8a.afm
├── ├── └── ├── ├── ├── ├── ├── pncbi8a.afm
├── ├── └── ├── ├── ├── ├── ├── pncr8a.afm
├── ├── └── ├── ├── ├── ├── ├── pncri8a.afm
├── ├── └── ├── ├── ├── ├── ├── pplb8a.afm
├── ├── └── ├── ├── ├── ├── ├── pplbi8a.afm
├── ├── └── ├── ├── ├── ├── ├── pplr8a.afm
├── ├── └── ├── ├── ├── ├── ├── pplri8a.afm
├── ├── └── ├── ├── ├── ├── ├── psyr.afm
├── ├── └── ├── ├── ├── ├── ├── ptmb8a.afm
├── ├── └── ├── ├── ├── ├── ├── ptmbi8a.afm
├── ├── └── ├── ├── ├── ├── ├── ptmr8a.afm
├── ├── └── ├── ├── ├── ├── ├── ptmri8a.afm
├── ├── └── ├── ├── ├── ├── ├── putb8a.afm
├── ├── └── ├── ├── ├── ├── ├── putbi8a.afm
├── ├── └── ├── ├── ├── ├── ├── putr8a.afm
├── ├── └── ├── ├── ├── ├── ├── putri8a.afm
├── ├── └── ├── ├── ├── ├── ├── pzcmi8a.afm
├── ├── └── ├── ├── ├── ├── └── pzdr.afm
├── ├── └── ├── ├── ├── ├── pdfcorefonts/
├── ├── └── ├── ├── ├── ├── ├── Courier-Bold.afm
├── ├── └── ├── ├── ├── ├── ├── Courier-BoldOblique.afm
├── ├── └── ├── ├── ├── ├── ├── Courier-Oblique.afm
├── ├── └── ├── ├── ├── ├── ├── Courier.afm
├── ├── └── ├── ├── ├── ├── ├── Helvetica-Bold.afm
├── ├── └── ├── ├── ├── ├── ├── Helvetica-BoldOblique.afm
├── ├── └── ├── ├── ├── ├── ├── Helvetica-Oblique.afm
├── ├── └── ├── ├── ├── ├── ├── Helvetica.afm
├── ├── └── ├── ├── ├── ├── ├── readme.txt
├── ├── └── ├── ├── ├── ├── ├── Symbol.afm
├── ├── └── ├── ├── ├── ├── ├── Times-Bold.afm
├── ├── └── ├── ├── ├── ├── ├── Times-BoldItalic.afm
├── ├── └── ├── ├── ├── ├── ├── Times-Italic.afm
├── ├── └── ├── ├── ├── ├── ├── Times-Roman.afm
├── ├── └── ├── ├── ├── ├── └── ZapfDingbats.afm
├── ├── └── ├── ├── ├── └── ttf/
├── ├── └── ├── ├── ├── └── ├── cmb10.ttf
├── ├── └── ├── ├── ├── └── ├── cmex10.ttf
├── ├── └── ├── ├── ├── └── ├── cmmi10.ttf
├── ├── └── ├── ├── ├── └── ├── cmr10.ttf
├── ├── └── ├── ├── ├── └── ├── cmss10.ttf
├── ├── └── ├── ├── ├── └── ├── cmsy10.ttf
├── ├── └── ├── ├── ├── └── ├── cmtt10.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSans-Bold.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSans-BoldOblique.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSans-Oblique.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSans.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSansDisplay.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSansMono-Bold.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSansMono-BoldOblique.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSansMono-Oblique.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSansMono.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSerif-Bold.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSerif-BoldItalic.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSerif-Italic.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSerif.ttf
├── ├── └── ├── ├── ├── └── ├── DejaVuSerifDisplay.ttf
├── ├── └── ├── ├── ├── └── ├── LICENSE_DEJAVU
├── ├── └── ├── ├── ├── └── ├── LICENSE_STIX
├── ├── └── ├── ├── ├── └── ├── STIXGeneral.ttf
├── ├── └── ├── ├── ├── └── ├── STIXGeneralBol.ttf
├── ├── └── ├── ├── ├── └── ├── STIXGeneralBolIta.ttf
├── ├── └── ├── ├── ├── └── ├── STIXGeneralItalic.ttf
├── ├── └── ├── ├── ├── └── ├── STIXNonUni.ttf
├── ├── └── ├── ├── ├── └── ├── STIXNonUniBol.ttf
├── ├── └── ├── ├── ├── └── ├── STIXNonUniBolIta.ttf
├── ├── └── ├── ├── ├── └── ├── STIXNonUniIta.ttf
├── ├── └── ├── ├── ├── └── ├── STIXSizFiveSymReg.ttf
├── ├── └── ├── ├── ├── └── ├── STIXSizFourSymBol.ttf
├── ├── └── ├── ├── ├── └── ├── STIXSizFourSymReg.ttf
├── ├── └── ├── ├── ├── └── ├── STIXSizOneSymBol.ttf
├── ├── └── ├── ├── ├── └── ├── STIXSizOneSymReg.ttf
├── ├── └── ├── ├── ├── └── ├── STIXSizThreeSymBol.ttf
├── ├── └── ├── ├── ├── └── ├── STIXSizThreeSymReg.ttf
├── ├── └── ├── ├── ├── └── ├── STIXSizTwoSymBol.ttf
├── ├── └── ├── ├── ├── └── └── STIXSizTwoSymReg.ttf
├── ├── └── ├── ├── ├── images/
├── ├── └── ├── ├── ├── ├── back-symbolic.svg
├── ├── └── ├── ├── ├── ├── back.pdf
├── ├── └── ├── ├── ├── ├── back.png
├── ├── └── ├── ├── ├── ├── back.svg
├── ├── └── ├── ├── ├── ├── back_large.png
├── ├── └── ├── ├── ├── ├── filesave-symbolic.svg
├── ├── └── ├── ├── ├── ├── filesave.pdf
├── ├── └── ├── ├── ├── ├── filesave.png
├── ├── └── ├── ├── ├── ├── filesave.svg
├── ├── └── ├── ├── ├── ├── filesave_large.png
├── ├── └── ├── ├── ├── ├── forward-symbolic.svg
├── ├── └── ├── ├── ├── ├── forward.pdf
├── ├── └── ├── ├── ├── ├── forward.png
├── ├── └── ├── ├── ├── ├── forward.svg
├── ├── └── ├── ├── ├── ├── forward_large.png
├── ├── └── ├── ├── ├── ├── hand.pdf
├── ├── └── ├── ├── ├── ├── hand.png
├── ├── └── ├── ├── ├── ├── hand.svg
├── ├── └── ├── ├── ├── ├── help-symbolic.svg
├── ├── └── ├── ├── ├── ├── help.pdf
├── ├── └── ├── ├── ├── ├── help.png
├── ├── └── ├── ├── ├── ├── help.svg
├── ├── └── ├── ├── ├── ├── help_large.png
├── ├── └── ├── ├── ├── ├── home-symbolic.svg
├── ├── └── ├── ├── ├── ├── home.pdf
├── ├── └── ├── ├── ├── ├── home.png
├── ├── └── ├── ├── ├── ├── home.svg
├── ├── └── ├── ├── ├── ├── home_large.png
├── ├── └── ├── ├── ├── ├── matplotlib.pdf
├── ├── └── ├── ├── ├── ├── matplotlib.png
├── ├── └── ├── ├── ├── ├── matplotlib.svg
├── ├── └── ├── ├── ├── ├── matplotlib_large.png
├── ├── └── ├── ├── ├── ├── move-symbolic.svg
├── ├── └── ├── ├── ├── ├── move.pdf
├── ├── └── ├── ├── ├── ├── move.png
├── ├── └── ├── ├── ├── ├── move.svg
├── ├── └── ├── ├── ├── ├── move_large.png
├── ├── └── ├── ├── ├── ├── qt4_editor_options.pdf
├── ├── └── ├── ├── ├── ├── qt4_editor_options.png
├── ├── └── ├── ├── ├── ├── qt4_editor_options.svg
├── ├── └── ├── ├── ├── ├── qt4_editor_options_large.png
├── ├── └── ├── ├── ├── ├── subplots-symbolic.svg
├── ├── └── ├── ├── ├── ├── subplots.pdf
├── ├── └── ├── ├── ├── ├── subplots.png
├── ├── └── ├── ├── ├── ├── subplots.svg
├── ├── └── ├── ├── ├── ├── subplots_large.png
├── ├── └── ├── ├── ├── ├── zoom_to_rect-symbolic.svg
├── ├── └── ├── ├── ├── ├── zoom_to_rect.pdf
├── ├── └── ├── ├── ├── ├── zoom_to_rect.png
├── ├── └── ├── ├── ├── ├── zoom_to_rect.svg
├── ├── └── ├── ├── ├── └── zoom_to_rect_large.png
├── ├── └── ├── ├── ├── kpsewhich.lua
├── ├── └── ├── ├── ├── matplotlibrc
├── ├── └── ├── ├── ├── plot_directive/
├── ├── └── ├── ├── ├── └── plot_directive.css
├── ├── └── ├── ├── ├── sample_data/
├── ├── └── ├── ├── ├── ├── axes_grid/
├── ├── └── ├── ├── ├── ├── └── bivariate_normal.npy
├── ├── └── ├── ├── ├── ├── data_x_x2_x3.csv
├── ├── └── ├── ├── ├── ├── eeg.dat
├── ├── └── ├── ├── ├── ├── embedding_in_wx3.xrc
├── ├── └── ├── ├── ├── ├── goog.npz
├── ├── └── ├── ├── ├── ├── grace_hopper.jpg
├── ├── └── ├── ├── ├── ├── jacksboro_fault_dem.npz
├── ├── └── ├── ├── ├── ├── logo2.png
├── ├── └── ├── ├── ├── ├── membrane.dat
├── ├── └── ├── ├── ├── ├── Minduka_Present_Blue_Pack.png
├── ├── └── ├── ├── ├── ├── msft.csv
├── ├── └── ├── ├── ├── ├── README.txt
├── ├── └── ├── ├── ├── ├── s1045.ima.gz
├── ├── └── ├── ├── ├── ├── Stocks.csv
├── ├── └── ├── ├── ├── └── topobathy.npz
├── ├── └── ├── ├── └── stylelib/
├── ├── └── ├── ├── └── ├── _classic_test_patch.mplstyle
├── ├── └── ├── ├── └── ├── _mpl-gallery-nogrid.mplstyle
├── ├── └── ├── ├── └── ├── _mpl-gallery.mplstyle
├── ├── └── ├── ├── └── ├── bmh.mplstyle
├── ├── └── ├── ├── └── ├── classic.mplstyle
├── ├── └── ├── ├── └── ├── dark_background.mplstyle
├── ├── └── ├── ├── └── ├── fast.mplstyle
├── ├── └── ├── ├── └── ├── fivethirtyeight.mplstyle
├── ├── └── ├── ├── └── ├── ggplot.mplstyle
├── ├── └── ├── ├── └── ├── grayscale.mplstyle
├── ├── └── ├── ├── └── ├── petroff10.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-bright.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-colorblind.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-dark-palette.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-dark.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-darkgrid.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-deep.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-muted.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-notebook.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-paper.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-pastel.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-poster.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-talk.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-ticks.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-white.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8-whitegrid.mplstyle
├── ├── └── ├── ├── └── ├── seaborn-v0_8.mplstyle
├── ├── └── ├── ├── └── ├── Solarize_Light2.mplstyle
├── ├── └── ├── ├── └── └── tableau-colorblind10.mplstyle
├── ├── └── ├── ├── offsetbox.py
├── ├── └── ├── ├── offsetbox.pyi
├── ├── └── ├── ├── patches.py
├── ├── └── ├── ├── patches.pyi
├── ├── └── ├── ├── path.py
├── ├── └── ├── ├── path.pyi
├── ├── └── ├── ├── patheffects.py
├── ├── └── ├── ├── patheffects.pyi
├── ├── └── ├── ├── projections/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── geo.py
├── ├── └── ├── ├── ├── geo.pyi
├── ├── └── ├── ├── ├── polar.py
├── ├── └── ├── ├── └── polar.pyi
├── ├── └── ├── ├── py.typed
├── ├── └── ├── ├── pylab.py
├── ├── └── ├── ├── pyplot.py
├── ├── └── ├── ├── quiver.py
├── ├── └── ├── ├── quiver.pyi
├── ├── └── ├── ├── rcsetup.py
├── ├── └── ├── ├── rcsetup.pyi
├── ├── └── ├── ├── sankey.py
├── ├── └── ├── ├── sankey.pyi
├── ├── └── ├── ├── scale.py
├── ├── └── ├── ├── scale.pyi
├── ├── └── ├── ├── sphinxext/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── figmpl_directive.py
├── ├── └── ├── ├── ├── mathmpl.py
├── ├── └── ├── ├── ├── plot_directive.py
├── ├── └── ├── ├── └── roles.py
├── ├── └── ├── ├── spines.py
├── ├── └── ├── ├── spines.pyi
├── ├── └── ├── ├── stackplot.py
├── ├── └── ├── ├── stackplot.pyi
├── ├── └── ├── ├── streamplot.py
├── ├── └── ├── ├── streamplot.pyi
├── ├── └── ├── ├── style/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── core.py
├── ├── └── ├── ├── └── core.pyi
├── ├── └── ├── ├── table.py
├── ├── └── ├── ├── table.pyi
├── ├── └── ├── ├── testing/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _markers.py
├── ├── └── ├── ├── ├── compare.py
├── ├── └── ├── ├── ├── compare.pyi
├── ├── └── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── conftest.pyi
├── ├── └── ├── ├── ├── decorators.py
├── ├── └── ├── ├── ├── decorators.pyi
├── ├── └── ├── ├── ├── exceptions.py
├── ├── └── ├── ├── ├── jpl_units/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Duration.py
├── ├── └── ├── ├── ├── ├── Epoch.py
├── ├── └── ├── ├── ├── ├── EpochConverter.py
├── ├── └── ├── ├── ├── ├── StrConverter.py
├── ├── └── ├── ├── ├── ├── UnitDbl.py
├── ├── └── ├── ├── ├── ├── UnitDblConverter.py
├── ├── └── ├── ├── ├── └── UnitDblFormatter.py
├── ├── └── ├── ├── ├── widgets.py
├── ├── └── ├── ├── └── widgets.pyi
├── ├── └── ├── ├── tests/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── test_afm.py
├── ├── └── ├── ├── ├── test_agg.py
├── ├── └── ├── ├── ├── test_agg_filter.py
├── ├── └── ├── ├── ├── test_animation.py
├── ├── └── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── test_arrow_patches.py
├── ├── └── ├── ├── ├── test_artist.py
├── ├── └── ├── ├── ├── test_axes.py
├── ├── └── ├── ├── ├── test_axis.py
├── ├── └── ├── ├── ├── test_backend_bases.py
├── ├── └── ├── ├── ├── test_backend_cairo.py
├── ├── └── ├── ├── ├── test_backend_gtk3.py
├── ├── └── ├── ├── ├── test_backend_inline.py
├── ├── └── ├── ├── ├── test_backend_macosx.py
├── ├── └── ├── ├── ├── test_backend_nbagg.py
├── ├── └── ├── ├── ├── test_backend_pdf.py
├── ├── └── ├── ├── ├── test_backend_pgf.py
├── ├── └── ├── ├── ├── test_backend_ps.py
├── ├── └── ├── ├── ├── test_backend_qt.py
├── ├── └── ├── ├── ├── test_backend_registry.py
├── ├── └── ├── ├── ├── test_backend_svg.py
├── ├── └── ├── ├── ├── test_backend_template.py
├── ├── └── ├── ├── ├── test_backend_tk.py
├── ├── └── ├── ├── ├── test_backend_tools.py
├── ├── └── ├── ├── ├── test_backend_webagg.py
├── ├── └── ├── ├── ├── test_backends_interactive.py
├── ├── └── ├── ├── ├── test_basic.py
├── ├── └── ├── ├── ├── test_bbox_tight.py
├── ├── └── ├── ├── ├── test_bezier.py
├── ├── └── ├── ├── ├── test_category.py
├── ├── └── ├── ├── ├── test_cbook.py
├── ├── └── ├── ├── ├── test_collections.py
├── ├── └── ├── ├── ├── test_colorbar.py
├── ├── └── ├── ├── ├── test_colors.py
├── ├── └── ├── ├── ├── test_compare_images.py
├── ├── └── ├── ├── ├── test_constrainedlayout.py
├── ├── └── ├── ├── ├── test_container.py
├── ├── └── ├── ├── ├── test_contour.py
├── ├── └── ├── ├── ├── test_cycles.py
├── ├── └── ├── ├── ├── test_dates.py
├── ├── └── ├── ├── ├── test_datetime.py
├── ├── └── ├── ├── ├── test_determinism.py
├── ├── └── ├── ├── ├── test_doc.py
├── ├── └── ├── ├── ├── test_dviread.py
├── ├── └── ├── ├── ├── test_figure.py
├── ├── └── ├── ├── ├── test_font_manager.py
├── ├── └── ├── ├── ├── test_fontconfig_pattern.py
├── ├── └── ├── ├── ├── test_ft2font.py
├── ├── └── ├── ├── ├── test_getattr.py
├── ├── └── ├── ├── ├── test_gridspec.py
├── ├── └── ├── ├── ├── test_image.py
├── ├── └── ├── ├── ├── test_legend.py
├── ├── └── ├── ├── ├── test_lines.py
├── ├── └── ├── ├── ├── test_marker.py
├── ├── └── ├── ├── ├── test_mathtext.py
├── ├── └── ├── ├── ├── test_matplotlib.py
├── ├── └── ├── ├── ├── test_mlab.py
├── ├── └── ├── ├── ├── test_multivariate_colormaps.py
├── ├── └── ├── ├── ├── test_offsetbox.py
├── ├── └── ├── ├── ├── test_patches.py
├── ├── └── ├── ├── ├── test_path.py
├── ├── └── ├── ├── ├── test_patheffects.py
├── ├── └── ├── ├── ├── test_pickle.py
├── ├── └── ├── ├── ├── test_png.py
├── ├── └── ├── ├── ├── test_polar.py
├── ├── └── ├── ├── ├── test_preprocess_data.py
├── ├── └── ├── ├── ├── test_pyplot.py
├── ├── └── ├── ├── ├── test_quiver.py
├── ├── └── ├── ├── ├── test_rcparams.py
├── ├── └── ├── ├── ├── test_sankey.py
├── ├── └── ├── ├── ├── test_scale.py
├── ├── └── ├── ├── ├── test_simplification.py
├── ├── └── ├── ├── ├── test_skew.py
├── ├── └── ├── ├── ├── test_sphinxext.py
├── ├── └── ├── ├── ├── test_spines.py
├── ├── └── ├── ├── ├── test_streamplot.py
├── ├── └── ├── ├── ├── test_style.py
├── ├── └── ├── ├── ├── test_subplots.py
├── ├── └── ├── ├── ├── test_table.py
├── ├── └── ├── ├── ├── test_testing.py
├── ├── └── ├── ├── ├── test_texmanager.py
├── ├── └── ├── ├── ├── test_text.py
├── ├── └── ├── ├── ├── test_textpath.py
├── ├── └── ├── ├── ├── test_ticker.py
├── ├── └── ├── ├── ├── test_tightlayout.py
├── ├── └── ├── ├── ├── test_transforms.py
├── ├── └── ├── ├── ├── test_triangulation.py
├── ├── └── ├── ├── ├── test_type1font.py
├── ├── └── ├── ├── ├── test_units.py
├── ├── └── ├── ├── ├── test_usetex.py
├── ├── └── ├── ├── └── test_widgets.py
├── ├── └── ├── ├── texmanager.py
├── ├── └── ├── ├── texmanager.pyi
├── ├── └── ├── ├── text.py
├── ├── └── ├── ├── text.pyi
├── ├── └── ├── ├── textpath.py
├── ├── └── ├── ├── textpath.pyi
├── ├── └── ├── ├── ticker.py
├── ├── └── ├── ├── ticker.pyi
├── ├── └── ├── ├── transforms.py
├── ├── └── ├── ├── transforms.pyi
├── ├── └── ├── ├── tri/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _triangulation.py
├── ├── └── ├── ├── ├── _triangulation.pyi
├── ├── └── ├── ├── ├── _tricontour.py
├── ├── └── ├── ├── ├── _tricontour.pyi
├── ├── └── ├── ├── ├── _trifinder.py
├── ├── └── ├── ├── ├── _trifinder.pyi
├── ├── └── ├── ├── ├── _triinterpolate.py
├── ├── └── ├── ├── ├── _triinterpolate.pyi
├── ├── └── ├── ├── ├── _tripcolor.py
├── ├── └── ├── ├── ├── _tripcolor.pyi
├── ├── └── ├── ├── ├── _triplot.py
├── ├── └── ├── ├── ├── _triplot.pyi
├── ├── └── ├── ├── ├── _trirefine.py
├── ├── └── ├── ├── ├── _trirefine.pyi
├── ├── └── ├── ├── ├── _tritools.py
├── ├── └── ├── ├── └── _tritools.pyi
├── ├── └── ├── ├── typing.py
├── ├── └── ├── ├── units.py
├── ├── └── ├── ├── widgets.py
├── ├── └── ├── └── widgets.pyi
├── ├── └── ├── matplotlib-3.10.5.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── REQUESTED
├── ├── └── ├── └── WHEEL
├── ├── └── ├── mpl_toolkits/
├── ├── └── ├── ├── axes_grid1/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── anchored_artists.py
├── ├── └── ├── ├── ├── axes_divider.py
├── ├── └── ├── ├── ├── axes_grid.py
├── ├── └── ├── ├── ├── axes_rgb.py
├── ├── └── ├── ├── ├── axes_size.py
├── ├── └── ├── ├── ├── inset_locator.py
├── ├── └── ├── ├── ├── mpl_axes.py
├── ├── └── ├── ├── ├── parasite_axes.py
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── conftest.py
├── ├── └── ├── ├── └── └── test_axes_grid1.py
├── ├── └── ├── ├── axisartist/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── angle_helper.py
├── ├── └── ├── ├── ├── axes_divider.py
├── ├── └── ├── ├── ├── axis_artist.py
├── ├── └── ├── ├── ├── axisline_style.py
├── ├── └── ├── ├── ├── axislines.py
├── ├── └── ├── ├── ├── floating_axes.py
├── ├── └── ├── ├── ├── grid_finder.py
├── ├── └── ├── ├── ├── grid_helper_curvelinear.py
├── ├── └── ├── ├── ├── parasite_axes.py
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── conftest.py
├── ├── └── ├── ├── └── ├── test_angle_helper.py
├── ├── └── ├── ├── └── ├── test_axis_artist.py
├── ├── └── ├── ├── └── ├── test_axislines.py
├── ├── └── ├── ├── └── ├── test_floating_axes.py
├── ├── └── ├── ├── └── ├── test_grid_finder.py
├── ├── └── ├── ├── └── └── test_grid_helper_curvelinear.py
├── ├── └── ├── └── mplot3d/
├── ├── └── ├── └── ├── __init__.py
├── ├── └── ├── └── ├── art3d.py
├── ├── └── ├── └── ├── axes3d.py
├── ├── └── ├── └── ├── axis3d.py
├── ├── └── ├── └── ├── proj3d.py
├── ├── └── ├── └── └── tests/
├── ├── └── ├── └── └── ├── __init__.py
├── ├── └── ├── └── └── ├── conftest.py
├── ├── └── ├── └── └── ├── test_art3d.py
├── ├── └── ├── └── └── ├── test_axes3d.py
├── ├── └── ├── └── └── └── test_legend3d.py
├── ├── └── ├── numpy/
├── ├── └── ├── ├── __config__.py
├── ├── └── ├── ├── __config__.pyi
├── ├── └── ├── ├── __init__.cython-30.pxd
├── ├── └── ├── ├── __init__.pxd
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── __init__.pyi
├── ├── └── ├── ├── _array_api_info.py
├── ├── └── ├── ├── _array_api_info.pyi
├── ├── └── ├── ├── _configtool.py
├── ├── └── ├── ├── _configtool.pyi
├── ├── └── ├── ├── _core/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _add_newdocs.py
├── ├── └── ├── ├── ├── _add_newdocs.pyi
├── ├── └── ├── ├── ├── _add_newdocs_scalars.py
├── ├── └── ├── ├── ├── _add_newdocs_scalars.pyi
├── ├── └── ├── ├── ├── _asarray.py
├── ├── └── ├── ├── ├── _asarray.pyi
├── ├── └── ├── ├── ├── _dtype.py
├── ├── └── ├── ├── ├── _dtype.pyi
├── ├── └── ├── ├── ├── _dtype_ctypes.py
├── ├── └── ├── ├── ├── _dtype_ctypes.pyi
├── ├── └── ├── ├── ├── _exceptions.py
├── ├── └── ├── ├── ├── _exceptions.pyi
├── ├── └── ├── ├── ├── _internal.py
├── ├── └── ├── ├── ├── _internal.pyi
├── ├── └── ├── ├── ├── _machar.py
├── ├── └── ├── ├── ├── _machar.pyi
├── ├── └── ├── ├── ├── _methods.py
├── ├── └── ├── ├── ├── _methods.pyi
├── ├── └── ├── ├── ├── _multiarray_tests.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _multiarray_tests.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _multiarray_umath.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _multiarray_umath.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _operand_flag_tests.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _operand_flag_tests.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _rational_tests.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _rational_tests.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _simd.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _simd.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _simd.pyi
├── ├── └── ├── ├── ├── _string_helpers.py
├── ├── └── ├── ├── ├── _string_helpers.pyi
├── ├── └── ├── ├── ├── _struct_ufunc_tests.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _struct_ufunc_tests.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _type_aliases.py
├── ├── └── ├── ├── ├── _type_aliases.pyi
├── ├── └── ├── ├── ├── _ufunc_config.py
├── ├── └── ├── ├── ├── _ufunc_config.pyi
├── ├── └── ├── ├── ├── _umath_tests.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _umath_tests.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── arrayprint.py
├── ├── └── ├── ├── ├── arrayprint.pyi
├── ├── └── ├── ├── ├── cversions.py
├── ├── └── ├── ├── ├── defchararray.py
├── ├── └── ├── ├── ├── defchararray.pyi
├── ├── └── ├── ├── ├── einsumfunc.py
├── ├── └── ├── ├── ├── einsumfunc.pyi
├── ├── └── ├── ├── ├── fromnumeric.py
├── ├── └── ├── ├── ├── fromnumeric.pyi
├── ├── └── ├── ├── ├── function_base.py
├── ├── └── ├── ├── ├── function_base.pyi
├── ├── └── ├── ├── ├── getlimits.py
├── ├── └── ├── ├── ├── getlimits.pyi
├── ├── └── ├── ├── ├── include/
├── ├── └── ├── ├── ├── └── numpy/
├── ├── └── ├── ├── ├── └── ├── __multiarray_api.c
├── ├── └── ├── ├── ├── └── ├── __multiarray_api.h
├── ├── └── ├── ├── ├── └── ├── __ufunc_api.c
├── ├── └── ├── ├── ├── └── ├── __ufunc_api.h
├── ├── └── ├── ├── ├── └── ├── _neighborhood_iterator_imp.h
├── ├── └── ├── ├── ├── └── ├── _numpyconfig.h
├── ├── └── ├── ├── ├── └── ├── _public_dtype_api_table.h
├── ├── └── ├── ├── ├── └── ├── arrayobject.h
├── ├── └── ├── ├── ├── └── ├── arrayscalars.h
├── ├── └── ├── ├── ├── └── ├── dtype_api.h
├── ├── └── ├── ├── ├── └── ├── halffloat.h
├── ├── └── ├── ├── ├── └── ├── ndarrayobject.h
├── ├── └── ├── ├── ├── └── ├── ndarraytypes.h
├── ├── └── ├── ├── ├── └── ├── npy_2_compat.h
├── ├── └── ├── ├── ├── └── ├── npy_2_complexcompat.h
├── ├── └── ├── ├── ├── └── ├── npy_3kcompat.h
├── ├── └── ├── ├── ├── └── ├── npy_common.h
├── ├── └── ├── ├── ├── └── ├── npy_cpu.h
├── ├── └── ├── ├── ├── └── ├── npy_endian.h
├── ├── └── ├── ├── ├── └── ├── npy_math.h
├── ├── └── ├── ├── ├── └── ├── npy_no_deprecated_api.h
├── ├── └── ├── ├── ├── └── ├── npy_os.h
├── ├── └── ├── ├── ├── └── ├── numpyconfig.h
├── ├── └── ├── ├── ├── └── ├── random/
├── ├── └── ├── ├── ├── └── ├── ├── bitgen.h
├── ├── └── ├── ├── ├── └── ├── ├── distributions.h
├── ├── └── ├── ├── ├── └── ├── ├── libdivide.h
├── ├── └── ├── ├── ├── └── ├── └── LICENSE.txt
├── ├── └── ├── ├── ├── └── ├── ufuncobject.h
├── ├── └── ├── ├── ├── └── └── utils.h
├── ├── └── ├── ├── ├── lib/
├── ├── └── ├── ├── ├── ├── npy-pkg-config/
├── ├── └── ├── ├── ├── ├── ├── mlib.ini
├── ├── └── ├── ├── ├── ├── └── npymath.ini
├── ├── └── ├── ├── ├── ├── npymath.lib
├── ├── └── ├── ├── ├── └── pkgconfig/
├── ├── └── ├── ├── ├── └── └── numpy.pc
├── ├── └── ├── ├── ├── memmap.py
├── ├── └── ├── ├── ├── memmap.pyi
├── ├── └── ├── ├── ├── multiarray.py
├── ├── └── ├── ├── ├── multiarray.pyi
├── ├── └── ├── ├── ├── numeric.py
├── ├── └── ├── ├── ├── numeric.pyi
├── ├── └── ├── ├── ├── numerictypes.py
├── ├── └── ├── ├── ├── numerictypes.pyi
├── ├── └── ├── ├── ├── overrides.py
├── ├── └── ├── ├── ├── overrides.pyi
├── ├── └── ├── ├── ├── printoptions.py
├── ├── └── ├── ├── ├── printoptions.pyi
├── ├── └── ├── ├── ├── records.py
├── ├── └── ├── ├── ├── records.pyi
├── ├── └── ├── ├── ├── shape_base.py
├── ├── └── ├── ├── ├── shape_base.pyi
├── ├── └── ├── ├── ├── strings.py
├── ├── └── ├── ├── ├── strings.pyi
├── ├── └── ├── ├── ├── tests/
├── ├── └── ├── ├── ├── ├── _locales.py
├── ├── └── ├── ├── ├── ├── _natype.py
├── ├── └── ├── ├── ├── ├── data/
├── ├── └── ├── ├── ├── ├── ├── astype_copy.pkl
├── ├── └── ├── ├── ├── ├── ├── generate_umath_validation_data.cpp
├── ├── └── ├── ├── ├── ├── ├── recarray_from_file.fits
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-arccos.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-arccosh.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-arcsin.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-arcsinh.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-arctan.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-arctanh.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-cbrt.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-cos.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-cosh.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-exp.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-exp2.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-expm1.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-log.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-log10.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-log1p.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-log2.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-README.txt
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-sin.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-sinh.csv
├── ├── └── ├── ├── ├── ├── ├── umath-validation-set-tan.csv
├── ├── └── ├── ├── ├── ├── └── umath-validation-set-tanh.csv
├── ├── └── ├── ├── ├── ├── examples/
├── ├── └── ├── ├── ├── ├── ├── cython/
├── ├── └── ├── ├── ├── ├── ├── ├── checks.pyx
├── ├── └── ├── ├── ├── ├── ├── ├── meson.build
├── ├── └── ├── ├── ├── ├── ├── └── setup.py
├── ├── └── ├── ├── ├── ├── └── limited_api/
├── ├── └── ├── ├── ├── ├── └── ├── limited_api1.c
├── ├── └── ├── ├── ├── ├── └── ├── limited_api2.pyx
├── ├── └── ├── ├── ├── ├── └── ├── limited_api_latest.c
├── ├── └── ├── ├── ├── ├── └── ├── meson.build
├── ├── └── ├── ├── ├── ├── └── └── setup.py
├── ├── └── ├── ├── ├── ├── test__exceptions.py
├── ├── └── ├── ├── ├── ├── test_abc.py
├── ├── └── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── ├── test_argparse.py
├── ├── └── ├── ├── ├── ├── test_array_api_info.py
├── ├── └── ├── ├── ├── ├── test_array_coercion.py
├── ├── └── ├── ├── ├── ├── test_array_interface.py
├── ├── └── ├── ├── ├── ├── test_arraymethod.py
├── ├── └── ├── ├── ├── ├── test_arrayobject.py
├── ├── └── ├── ├── ├── ├── test_arrayprint.py
├── ├── └── ├── ├── ├── ├── test_casting_floatingpoint_errors.py
├── ├── └── ├── ├── ├── ├── test_casting_unittests.py
├── ├── └── ├── ├── ├── ├── test_conversion_utils.py
├── ├── └── ├── ├── ├── ├── test_cpu_dispatcher.py
├── ├── └── ├── ├── ├── ├── test_cpu_features.py
├── ├── └── ├── ├── ├── ├── test_custom_dtypes.py
├── ├── └── ├── ├── ├── ├── test_cython.py
├── ├── └── ├── ├── ├── ├── test_datetime.py
├── ├── └── ├── ├── ├── ├── test_defchararray.py
├── ├── └── ├── ├── ├── ├── test_deprecations.py
├── ├── └── ├── ├── ├── ├── test_dlpack.py
├── ├── └── ├── ├── ├── ├── test_dtype.py
├── ├── └── ├── ├── ├── ├── test_einsum.py
├── ├── └── ├── ├── ├── ├── test_errstate.py
├── ├── └── ├── ├── ├── ├── test_extint128.py
├── ├── └── ├── ├── ├── ├── test_function_base.py
├── ├── └── ├── ├── ├── ├── test_getlimits.py
├── ├── └── ├── ├── ├── ├── test_half.py
├── ├── └── ├── ├── ├── ├── test_hashtable.py
├── ├── └── ├── ├── ├── ├── test_indexerrors.py
├── ├── └── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── test_item_selection.py
├── ├── └── ├── ├── ├── ├── test_limited_api.py
├── ├── └── ├── ├── ├── ├── test_longdouble.py
├── ├── └── ├── ├── ├── ├── test_machar.py
├── ├── └── ├── ├── ├── ├── test_mem_overlap.py
├── ├── └── ├── ├── ├── ├── test_mem_policy.py
├── ├── └── ├── ├── ├── ├── test_memmap.py
├── ├── └── ├── ├── ├── ├── test_multiarray.py
├── ├── └── ├── ├── ├── ├── test_multithreading.py
├── ├── └── ├── ├── ├── ├── test_nditer.py
├── ├── └── ├── ├── ├── ├── test_nep50_promotions.py
├── ├── └── ├── ├── ├── ├── test_numeric.py
├── ├── └── ├── ├── ├── ├── test_numerictypes.py
├── ├── └── ├── ├── ├── ├── test_overrides.py
├── ├── └── ├── ├── ├── ├── test_print.py
├── ├── └── ├── ├── ├── ├── test_protocols.py
├── ├── └── ├── ├── ├── ├── test_records.py
├── ├── └── ├── ├── ├── ├── test_regression.py
├── ├── └── ├── ├── ├── ├── test_scalar_ctors.py
├── ├── └── ├── ├── ├── ├── test_scalar_methods.py
├── ├── └── ├── ├── ├── ├── test_scalarbuffer.py
├── ├── └── ├── ├── ├── ├── test_scalarinherit.py
├── ├── └── ├── ├── ├── ├── test_scalarmath.py
├── ├── └── ├── ├── ├── ├── test_scalarprint.py
├── ├── └── ├── ├── ├── ├── test_shape_base.py
├── ├── └── ├── ├── ├── ├── test_simd.py
├── ├── └── ├── ├── ├── ├── test_simd_module.py
├── ├── └── ├── ├── ├── ├── test_stringdtype.py
├── ├── └── ├── ├── ├── ├── test_strings.py
├── ├── └── ├── ├── ├── ├── test_ufunc.py
├── ├── └── ├── ├── ├── ├── test_umath.py
├── ├── └── ├── ├── ├── ├── test_umath_accuracy.py
├── ├── └── ├── ├── ├── ├── test_umath_complex.py
├── ├── └── ├── ├── ├── └── test_unicode.py
├── ├── └── ├── ├── ├── umath.py
├── ├── └── ├── ├── └── umath.pyi
├── ├── └── ├── ├── _distributor_init.py
├── ├── └── ├── ├── _distributor_init.pyi
├── ├── └── ├── ├── _expired_attrs_2_0.py
├── ├── └── ├── ├── _expired_attrs_2_0.pyi
├── ├── └── ├── ├── _globals.py
├── ├── └── ├── ├── _globals.pyi
├── ├── └── ├── ├── _pyinstaller/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── hook-numpy.py
├── ├── └── ├── ├── ├── hook-numpy.pyi
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── pyinstaller-smoke.py
├── ├── └── ├── ├── └── └── test_pyinstaller.py
├── ├── └── ├── ├── _pytesttester.py
├── ├── └── ├── ├── _pytesttester.pyi
├── ├── └── ├── ├── _typing/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _add_docstring.py
├── ├── └── ├── ├── ├── _array_like.py
├── ├── └── ├── ├── ├── _callable.pyi
├── ├── └── ├── ├── ├── _char_codes.py
├── ├── └── ├── ├── ├── _dtype_like.py
├── ├── └── ├── ├── ├── _extended_precision.py
├── ├── └── ├── ├── ├── _nbit.py
├── ├── └── ├── ├── ├── _nbit_base.py
├── ├── └── ├── ├── ├── _nbit_base.pyi
├── ├── └── ├── ├── ├── _nested_sequence.py
├── ├── └── ├── ├── ├── _scalars.py
├── ├── └── ├── ├── ├── _shape.py
├── ├── └── ├── ├── ├── _ufunc.py
├── ├── └── ├── ├── └── _ufunc.pyi
├── ├── └── ├── ├── _utils/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _convertions.py
├── ├── └── ├── ├── ├── _convertions.pyi
├── ├── └── ├── ├── ├── _inspect.py
├── ├── └── ├── ├── ├── _inspect.pyi
├── ├── └── ├── ├── ├── _pep440.py
├── ├── └── ├── ├── └── _pep440.pyi
├── ├── └── ├── ├── char/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── └── __init__.pyi
├── ├── └── ├── ├── conftest.py
├── ├── └── ├── ├── core/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _dtype.py
├── ├── └── ├── ├── ├── _dtype.pyi
├── ├── └── ├── ├── ├── _dtype_ctypes.py
├── ├── └── ├── ├── ├── _dtype_ctypes.pyi
├── ├── └── ├── ├── ├── _internal.py
├── ├── └── ├── ├── ├── _multiarray_umath.py
├── ├── └── ├── ├── ├── _utils.py
├── ├── └── ├── ├── ├── arrayprint.py
├── ├── └── ├── ├── ├── defchararray.py
├── ├── └── ├── ├── ├── einsumfunc.py
├── ├── └── ├── ├── ├── fromnumeric.py
├── ├── └── ├── ├── ├── function_base.py
├── ├── └── ├── ├── ├── getlimits.py
├── ├── └── ├── ├── ├── multiarray.py
├── ├── └── ├── ├── ├── numeric.py
├── ├── └── ├── ├── ├── numerictypes.py
├── ├── └── ├── ├── ├── overrides.py
├── ├── └── ├── ├── ├── overrides.pyi
├── ├── └── ├── ├── ├── records.py
├── ├── └── ├── ├── ├── shape_base.py
├── ├── └── ├── ├── └── umath.py
├── ├── └── ├── ├── ctypeslib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _ctypeslib.py
├── ├── └── ├── ├── └── _ctypeslib.pyi
├── ├── └── ├── ├── doc/
├── ├── └── ├── ├── └── ufuncs.py
├── ├── └── ├── ├── dtypes.py
├── ├── └── ├── ├── dtypes.pyi
├── ├── └── ├── ├── exceptions.py
├── ├── └── ├── ├── exceptions.pyi
├── ├── └── ├── ├── f2py/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── __version__.py
├── ├── └── ├── ├── ├── __version__.pyi
├── ├── └── ├── ├── ├── _backends/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── ├── _backend.py
├── ├── └── ├── ├── ├── ├── _backend.pyi
├── ├── └── ├── ├── ├── ├── _distutils.py
├── ├── └── ├── ├── ├── ├── _distutils.pyi
├── ├── └── ├── ├── ├── ├── _meson.py
├── ├── └── ├── ├── ├── ├── _meson.pyi
├── ├── └── ├── ├── ├── └── meson.build.template
├── ├── └── ├── ├── ├── _isocbind.py
├── ├── └── ├── ├── ├── _isocbind.pyi
├── ├── └── ├── ├── ├── _src_pyf.py
├── ├── └── ├── ├── ├── _src_pyf.pyi
├── ├── └── ├── ├── ├── auxfuncs.py
├── ├── └── ├── ├── ├── auxfuncs.pyi
├── ├── └── ├── ├── ├── capi_maps.py
├── ├── └── ├── ├── ├── capi_maps.pyi
├── ├── └── ├── ├── ├── cb_rules.py
├── ├── └── ├── ├── ├── cb_rules.pyi
├── ├── └── ├── ├── ├── cfuncs.py
├── ├── └── ├── ├── ├── cfuncs.pyi
├── ├── └── ├── ├── ├── common_rules.py
├── ├── └── ├── ├── ├── common_rules.pyi
├── ├── └── ├── ├── ├── crackfortran.py
├── ├── └── ├── ├── ├── crackfortran.pyi
├── ├── └── ├── ├── ├── diagnose.py
├── ├── └── ├── ├── ├── diagnose.pyi
├── ├── └── ├── ├── ├── f2py2e.py
├── ├── └── ├── ├── ├── f2py2e.pyi
├── ├── └── ├── ├── ├── f90mod_rules.py
├── ├── └── ├── ├── ├── f90mod_rules.pyi
├── ├── └── ├── ├── ├── func2subr.py
├── ├── └── ├── ├── ├── func2subr.pyi
├── ├── └── ├── ├── ├── rules.py
├── ├── └── ├── ├── ├── rules.pyi
├── ├── └── ├── ├── ├── setup.cfg
├── ├── └── ├── ├── ├── src/
├── ├── └── ├── ├── ├── ├── fortranobject.c
├── ├── └── ├── ├── ├── └── fortranobject.h
├── ├── └── ├── ├── ├── symbolic.py
├── ├── └── ├── ├── ├── symbolic.pyi
├── ├── └── ├── ├── ├── tests/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── src/
├── ├── └── ├── ├── ├── ├── ├── abstract_interface/
├── ├── └── ├── ├── ├── ├── ├── ├── foo.f90
├── ├── └── ├── ├── ├── ├── ├── └── gh18403_mod.f90
├── ├── └── ├── ├── ├── ├── ├── array_from_pyobj/
├── ├── └── ├── ├── ├── ├── ├── └── wrapmodule.c
├── ├── └── ├── ├── ├── ├── ├── assumed_shape/
├── ├── └── ├── ├── ├── ├── ├── ├── foo_free.f90
├── ├── └── ├── ├── ├── ├── ├── ├── foo_mod.f90
├── ├── └── ├── ├── ├── ├── ├── ├── foo_use.f90
├── ├── └── ├── ├── ├── ├── ├── └── precision.f90
├── ├── └── ├── ├── ├── ├── ├── block_docstring/
├── ├── └── ├── ├── ├── ├── ├── └── foo.f
├── ├── └── ├── ├── ├── ├── ├── callback/
├── ├── └── ├── ├── ├── ├── ├── ├── foo.f
├── ├── └── ├── ├── ├── ├── ├── ├── gh17797.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh18335.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh25211.f
├── ├── └── ├── ├── ├── ├── ├── ├── gh25211.pyf
├── ├── └── ├── ├── ├── ├── ├── └── gh26681.f90
├── ├── └── ├── ├── ├── ├── ├── cli/
├── ├── └── ├── ├── ├── ├── ├── ├── gh_22819.pyf
├── ├── └── ├── ├── ├── ├── ├── ├── hi77.f
├── ├── └── ├── ├── ├── ├── ├── └── hiworld.f90
├── ├── └── ├── ├── ├── ├── ├── common/
├── ├── └── ├── ├── ├── ├── ├── ├── block.f
├── ├── └── ├── ├── ├── ├── ├── └── gh19161.f90
├── ├── └── ├── ├── ├── ├── ├── crackfortran/
├── ├── └── ├── ├── ├── ├── ├── ├── accesstype.f90
├── ├── └── ├── ├── ├── ├── ├── ├── common_with_division.f
├── ├── └── ├── ├── ├── ├── ├── ├── data_common.f
├── ├── └── ├── ├── ├── ├── ├── ├── data_multiplier.f
├── ├── └── ├── ├── ├── ├── ├── ├── data_stmts.f90
├── ├── └── ├── ├── ├── ├── ├── ├── data_with_comments.f
├── ├── └── ├── ├── ├── ├── ├── ├── foo_deps.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh15035.f
├── ├── └── ├── ├── ├── ├── ├── ├── gh17859.f
├── ├── └── ├── ├── ├── ├── ├── ├── gh22648.pyf
├── ├── └── ├── ├── ├── ├── ├── ├── gh23533.f
├── ├── └── ├── ├── ├── ├── ├── ├── gh23598.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh23598Warn.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh23879.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh27697.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh2848.f90
├── ├── └── ├── ├── ├── ├── ├── ├── operators.f90
├── ├── └── ├── ├── ├── ├── ├── ├── privatemod.f90
├── ├── └── ├── ├── ├── ├── ├── ├── publicmod.f90
├── ├── └── ├── ├── ├── ├── ├── ├── pubprivmod.f90
├── ├── └── ├── ├── ├── ├── ├── └── unicode_comment.f90
├── ├── └── ├── ├── ├── ├── ├── f2cmap/
├── ├── └── ├── ├── ├── ├── ├── └── isoFortranEnvMap.f90
├── ├── └── ├── ├── ├── ├── ├── isocintrin/
├── ├── └── ├── ├── ├── ├── ├── └── isoCtests.f90
├── ├── └── ├── ├── ├── ├── ├── kind/
├── ├── └── ├── ├── ├── ├── ├── └── foo.f90
├── ├── └── ├── ├── ├── ├── ├── mixed/
├── ├── └── ├── ├── ├── ├── ├── ├── foo.f
├── ├── └── ├── ├── ├── ├── ├── ├── foo_fixed.f90
├── ├── └── ├── ├── ├── ├── ├── └── foo_free.f90
├── ├── └── ├── ├── ├── ├── ├── modules/
├── ├── └── ├── ├── ├── ├── ├── ├── gh25337/
├── ├── └── ├── ├── ├── ├── ├── ├── ├── data.f90
├── ├── └── ├── ├── ├── ├── ├── ├── └── use_data.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh26920/
├── ├── └── ├── ├── ├── ├── ├── ├── ├── two_mods_with_no_public_entities.f90
├── ├── └── ├── ├── ├── ├── ├── ├── └── two_mods_with_one_public_routine.f90
├── ├── └── ├── ├── ├── ├── ├── ├── module_data_docstring.f90
├── ├── └── ├── ├── ├── ├── ├── └── use_modules.f90
├── ├── └── ├── ├── ├── ├── ├── negative_bounds/
├── ├── └── ├── ├── ├── ├── ├── └── issue_20853.f90
├── ├── └── ├── ├── ├── ├── ├── parameter/
├── ├── └── ├── ├── ├── ├── ├── ├── constant_array.f90
├── ├── └── ├── ├── ├── ├── ├── ├── constant_both.f90
├── ├── └── ├── ├── ├── ├── ├── ├── constant_compound.f90
├── ├── └── ├── ├── ├── ├── ├── ├── constant_integer.f90
├── ├── └── ├── ├── ├── ├── ├── ├── constant_non_compound.f90
├── ├── └── ├── ├── ├── ├── ├── └── constant_real.f90
├── ├── └── ├── ├── ├── ├── ├── quoted_character/
├── ├── └── ├── ├── ├── ├── ├── └── foo.f
├── ├── └── ├── ├── ├── ├── ├── regression/
├── ├── └── ├── ├── ├── ├── ├── ├── AB.inc
├── ├── └── ├── ├── ├── ├── ├── ├── assignOnlyModule.f90
├── ├── └── ├── ├── ├── ├── ├── ├── datonly.f90
├── ├── └── ├── ├── ├── ├── ├── ├── f77comments.f
├── ├── └── ├── ├── ├── ├── ├── ├── f77fixedform.f95
├── ├── └── ├── ├── ├── ├── ├── ├── f90continuation.f90
├── ├── └── ├── ├── ├── ├── ├── ├── incfile.f90
├── ├── └── ├── ├── ├── ├── ├── ├── inout.f90
├── ├── └── ├── ├── ├── ├── ├── ├── lower_f2py_fortran.f90
├── ├── └── ├── ├── ├── ├── ├── └── mod_derived_types.f90
├── ├── └── ├── ├── ├── ├── ├── return_character/
├── ├── └── ├── ├── ├── ├── ├── ├── foo77.f
├── ├── └── ├── ├── ├── ├── ├── └── foo90.f90
├── ├── └── ├── ├── ├── ├── ├── return_complex/
├── ├── └── ├── ├── ├── ├── ├── ├── foo77.f
├── ├── └── ├── ├── ├── ├── ├── └── foo90.f90
├── ├── └── ├── ├── ├── ├── ├── return_integer/
├── ├── └── ├── ├── ├── ├── ├── ├── foo77.f
├── ├── └── ├── ├── ├── ├── ├── └── foo90.f90
├── ├── └── ├── ├── ├── ├── ├── return_logical/
├── ├── └── ├── ├── ├── ├── ├── ├── foo77.f
├── ├── └── ├── ├── ├── ├── ├── └── foo90.f90
├── ├── └── ├── ├── ├── ├── ├── return_real/
├── ├── └── ├── ├── ├── ├── ├── ├── foo77.f
├── ├── └── ├── ├── ├── ├── ├── └── foo90.f90
├── ├── └── ├── ├── ├── ├── ├── routines/
├── ├── └── ├── ├── ├── ├── ├── ├── funcfortranname.f
├── ├── └── ├── ├── ├── ├── ├── ├── funcfortranname.pyf
├── ├── └── ├── ├── ├── ├── ├── ├── subrout.f
├── ├── └── ├── ├── ├── ├── ├── └── subrout.pyf
├── ├── └── ├── ├── ├── ├── ├── size/
├── ├── └── ├── ├── ├── ├── ├── └── foo.f90
├── ├── └── ├── ├── ├── ├── ├── string/
├── ├── └── ├── ├── ├── ├── ├── ├── char.f90
├── ├── └── ├── ├── ├── ├── ├── ├── fixed_string.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh24008.f
├── ├── └── ├── ├── ├── ├── ├── ├── gh24662.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh25286.f90
├── ├── └── ├── ├── ├── ├── ├── ├── gh25286.pyf
├── ├── └── ├── ├── ├── ├── ├── ├── gh25286_bc.pyf
├── ├── └── ├── ├── ├── ├── ├── ├── scalar_string.f90
├── ├── └── ├── ├── ├── ├── ├── └── string.f
├── ├── └── ├── ├── ├── ├── └── value_attrspec/
├── ├── └── ├── ├── ├── ├── └── └── gh21665.f90
├── ├── └── ├── ├── ├── ├── test_abstract_interface.py
├── ├── └── ├── ├── ├── ├── test_array_from_pyobj.py
├── ├── └── ├── ├── ├── ├── test_assumed_shape.py
├── ├── └── ├── ├── ├── ├── test_block_docstring.py
├── ├── └── ├── ├── ├── ├── test_callback.py
├── ├── └── ├── ├── ├── ├── test_character.py
├── ├── └── ├── ├── ├── ├── test_common.py
├── ├── └── ├── ├── ├── ├── test_crackfortran.py
├── ├── └── ├── ├── ├── ├── test_data.py
├── ├── └── ├── ├── ├── ├── test_docs.py
├── ├── └── ├── ├── ├── ├── test_f2cmap.py
├── ├── └── ├── ├── ├── ├── test_f2py2e.py
├── ├── └── ├── ├── ├── ├── test_isoc.py
├── ├── └── ├── ├── ├── ├── test_kind.py
├── ├── └── ├── ├── ├── ├── test_mixed.py
├── ├── └── ├── ├── ├── ├── test_modules.py
├── ├── └── ├── ├── ├── ├── test_parameter.py
├── ├── └── ├── ├── ├── ├── test_pyf_src.py
├── ├── └── ├── ├── ├── ├── test_quoted_character.py
├── ├── └── ├── ├── ├── ├── test_regression.py
├── ├── └── ├── ├── ├── ├── test_return_character.py
├── ├── └── ├── ├── ├── ├── test_return_complex.py
├── ├── └── ├── ├── ├── ├── test_return_integer.py
├── ├── └── ├── ├── ├── ├── test_return_logical.py
├── ├── └── ├── ├── ├── ├── test_return_real.py
├── ├── └── ├── ├── ├── ├── test_routines.py
├── ├── └── ├── ├── ├── ├── test_semicolon_split.py
├── ├── └── ├── ├── ├── ├── test_size.py
├── ├── └── ├── ├── ├── ├── test_string.py
├── ├── └── ├── ├── ├── ├── test_symbolic.py
├── ├── └── ├── ├── ├── ├── test_value_attrspec.py
├── ├── └── ├── ├── ├── └── util.py
├── ├── └── ├── ├── ├── use_rules.py
├── ├── └── ├── ├── └── use_rules.pyi
├── ├── └── ├── ├── fft/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _helper.py
├── ├── └── ├── ├── ├── _helper.pyi
├── ├── └── ├── ├── ├── _pocketfft.py
├── ├── └── ├── ├── ├── _pocketfft.pyi
├── ├── └── ├── ├── ├── _pocketfft_umath.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _pocketfft_umath.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── helper.py
├── ├── └── ├── ├── ├── helper.pyi
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── test_helper.py
├── ├── └── ├── ├── └── └── test_pocketfft.py
├── ├── └── ├── ├── lib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _array_utils_impl.py
├── ├── └── ├── ├── ├── _array_utils_impl.pyi
├── ├── └── ├── ├── ├── _arraypad_impl.py
├── ├── └── ├── ├── ├── _arraypad_impl.pyi
├── ├── └── ├── ├── ├── _arraysetops_impl.py
├── ├── └── ├── ├── ├── _arraysetops_impl.pyi
├── ├── └── ├── ├── ├── _arrayterator_impl.py
├── ├── └── ├── ├── ├── _arrayterator_impl.pyi
├── ├── └── ├── ├── ├── _datasource.py
├── ├── └── ├── ├── ├── _datasource.pyi
├── ├── └── ├── ├── ├── _format_impl.py
├── ├── └── ├── ├── ├── _format_impl.pyi
├── ├── └── ├── ├── ├── _function_base_impl.py
├── ├── └── ├── ├── ├── _function_base_impl.pyi
├── ├── └── ├── ├── ├── _histograms_impl.py
├── ├── └── ├── ├── ├── _histograms_impl.pyi
├── ├── └── ├── ├── ├── _index_tricks_impl.py
├── ├── └── ├── ├── ├── _index_tricks_impl.pyi
├── ├── └── ├── ├── ├── _iotools.py
├── ├── └── ├── ├── ├── _iotools.pyi
├── ├── └── ├── ├── ├── _nanfunctions_impl.py
├── ├── └── ├── ├── ├── _nanfunctions_impl.pyi
├── ├── └── ├── ├── ├── _npyio_impl.py
├── ├── └── ├── ├── ├── _npyio_impl.pyi
├── ├── └── ├── ├── ├── _polynomial_impl.py
├── ├── └── ├── ├── ├── _polynomial_impl.pyi
├── ├── └── ├── ├── ├── _scimath_impl.py
├── ├── └── ├── ├── ├── _scimath_impl.pyi
├── ├── └── ├── ├── ├── _shape_base_impl.py
├── ├── └── ├── ├── ├── _shape_base_impl.pyi
├── ├── └── ├── ├── ├── _stride_tricks_impl.py
├── ├── └── ├── ├── ├── _stride_tricks_impl.pyi
├── ├── └── ├── ├── ├── _twodim_base_impl.py
├── ├── └── ├── ├── ├── _twodim_base_impl.pyi
├── ├── └── ├── ├── ├── _type_check_impl.py
├── ├── └── ├── ├── ├── _type_check_impl.pyi
├── ├── └── ├── ├── ├── _ufunclike_impl.py
├── ├── └── ├── ├── ├── _ufunclike_impl.pyi
├── ├── └── ├── ├── ├── _user_array_impl.py
├── ├── └── ├── ├── ├── _user_array_impl.pyi
├── ├── └── ├── ├── ├── _utils_impl.py
├── ├── └── ├── ├── ├── _utils_impl.pyi
├── ├── └── ├── ├── ├── _version.py
├── ├── └── ├── ├── ├── _version.pyi
├── ├── └── ├── ├── ├── array_utils.py
├── ├── └── ├── ├── ├── array_utils.pyi
├── ├── └── ├── ├── ├── format.py
├── ├── └── ├── ├── ├── format.pyi
├── ├── └── ├── ├── ├── introspect.py
├── ├── └── ├── ├── ├── introspect.pyi
├── ├── └── ├── ├── ├── mixins.py
├── ├── └── ├── ├── ├── mixins.pyi
├── ├── └── ├── ├── ├── npyio.py
├── ├── └── ├── ├── ├── npyio.pyi
├── ├── └── ├── ├── ├── recfunctions.py
├── ├── └── ├── ├── ├── recfunctions.pyi
├── ├── └── ├── ├── ├── scimath.py
├── ├── └── ├── ├── ├── scimath.pyi
├── ├── └── ├── ├── ├── stride_tricks.py
├── ├── └── ├── ├── ├── stride_tricks.pyi
├── ├── └── ├── ├── ├── tests/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── data/
├── ├── └── ├── ├── ├── ├── ├── py2-np0-objarr.npy
├── ├── └── ├── ├── ├── ├── ├── py2-objarr.npy
├── ├── └── ├── ├── ├── ├── ├── py2-objarr.npz
├── ├── └── ├── ├── ├── ├── ├── py3-objarr.npy
├── ├── └── ├── ├── ├── ├── ├── py3-objarr.npz
├── ├── └── ├── ├── ├── ├── ├── python3.npy
├── ├── └── ├── ├── ├── ├── └── win64python2.npy
├── ├── └── ├── ├── ├── ├── test__datasource.py
├── ├── └── ├── ├── ├── ├── test__iotools.py
├── ├── └── ├── ├── ├── ├── test__version.py
├── ├── └── ├── ├── ├── ├── test_array_utils.py
├── ├── └── ├── ├── ├── ├── test_arraypad.py
├── ├── └── ├── ├── ├── ├── test_arraysetops.py
├── ├── └── ├── ├── ├── ├── test_arrayterator.py
├── ├── └── ├── ├── ├── ├── test_format.py
├── ├── └── ├── ├── ├── ├── test_function_base.py
├── ├── └── ├── ├── ├── ├── test_histograms.py
├── ├── └── ├── ├── ├── ├── test_index_tricks.py
├── ├── └── ├── ├── ├── ├── test_io.py
├── ├── └── ├── ├── ├── ├── test_loadtxt.py
├── ├── └── ├── ├── ├── ├── test_mixins.py
├── ├── └── ├── ├── ├── ├── test_nanfunctions.py
├── ├── └── ├── ├── ├── ├── test_packbits.py
├── ├── └── ├── ├── ├── ├── test_polynomial.py
├── ├── └── ├── ├── ├── ├── test_recfunctions.py
├── ├── └── ├── ├── ├── ├── test_regression.py
├── ├── └── ├── ├── ├── ├── test_shape_base.py
├── ├── └── ├── ├── ├── ├── test_stride_tricks.py
├── ├── └── ├── ├── ├── ├── test_twodim_base.py
├── ├── └── ├── ├── ├── ├── test_type_check.py
├── ├── └── ├── ├── ├── ├── test_ufunclike.py
├── ├── └── ├── ├── ├── └── test_utils.py
├── ├── └── ├── ├── ├── user_array.py
├── ├── └── ├── ├── └── user_array.pyi
├── ├── └── ├── ├── linalg/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _linalg.py
├── ├── └── ├── ├── ├── _linalg.pyi
├── ├── └── ├── ├── ├── _umath_linalg.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _umath_linalg.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _umath_linalg.pyi
├── ├── └── ├── ├── ├── lapack_lite.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── lapack_lite.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── lapack_lite.pyi
├── ├── └── ├── ├── ├── linalg.py
├── ├── └── ├── ├── ├── linalg.pyi
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── test_deprecations.py
├── ├── └── ├── ├── └── ├── test_linalg.py
├── ├── └── ├── ├── └── └── test_regression.py
├── ├── └── ├── ├── ma/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── API_CHANGES.txt
├── ├── └── ├── ├── ├── core.py
├── ├── └── ├── ├── ├── core.pyi
├── ├── └── ├── ├── ├── extras.py
├── ├── └── ├── ├── ├── extras.pyi
├── ├── └── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── mrecords.py
├── ├── └── ├── ├── ├── mrecords.pyi
├── ├── └── ├── ├── ├── README.rst
├── ├── └── ├── ├── ├── tests/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_arrayobject.py
├── ├── └── ├── ├── ├── ├── test_core.py
├── ├── └── ├── ├── ├── ├── test_deprecations.py
├── ├── └── ├── ├── ├── ├── test_extras.py
├── ├── └── ├── ├── ├── ├── test_mrecords.py
├── ├── └── ├── ├── ├── ├── test_old_ma.py
├── ├── └── ├── ├── ├── ├── test_regression.py
├── ├── └── ├── ├── ├── └── test_subclassing.py
├── ├── └── ├── ├── └── testutils.py
├── ├── └── ├── ├── matlib.py
├── ├── └── ├── ├── matlib.pyi
├── ├── └── ├── ├── matrixlib/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── defmatrix.py
├── ├── └── ├── ├── ├── defmatrix.pyi
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── test_defmatrix.py
├── ├── └── ├── ├── └── ├── test_interaction.py
├── ├── └── ├── ├── └── ├── test_masked_matrix.py
├── ├── └── ├── ├── └── ├── test_matrix_linalg.py
├── ├── └── ├── ├── └── ├── test_multiarray.py
├── ├── └── ├── ├── └── ├── test_numeric.py
├── ├── └── ├── ├── └── └── test_regression.py
├── ├── └── ├── ├── polynomial/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _polybase.py
├── ├── └── ├── ├── ├── _polybase.pyi
├── ├── └── ├── ├── ├── _polytypes.pyi
├── ├── └── ├── ├── ├── chebyshev.py
├── ├── └── ├── ├── ├── chebyshev.pyi
├── ├── └── ├── ├── ├── hermite.py
├── ├── └── ├── ├── ├── hermite.pyi
├── ├── └── ├── ├── ├── hermite_e.py
├── ├── └── ├── ├── ├── hermite_e.pyi
├── ├── └── ├── ├── ├── laguerre.py
├── ├── └── ├── ├── ├── laguerre.pyi
├── ├── └── ├── ├── ├── legendre.py
├── ├── └── ├── ├── ├── legendre.pyi
├── ├── └── ├── ├── ├── polynomial.py
├── ├── └── ├── ├── ├── polynomial.pyi
├── ├── └── ├── ├── ├── polyutils.py
├── ├── └── ├── ├── ├── polyutils.pyi
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── test_chebyshev.py
├── ├── └── ├── ├── └── ├── test_classes.py
├── ├── └── ├── ├── └── ├── test_hermite.py
├── ├── └── ├── ├── └── ├── test_hermite_e.py
├── ├── └── ├── ├── └── ├── test_laguerre.py
├── ├── └── ├── ├── └── ├── test_legendre.py
├── ├── └── ├── ├── └── ├── test_polynomial.py
├── ├── └── ├── ├── └── ├── test_polyutils.py
├── ├── └── ├── ├── └── ├── test_printing.py
├── ├── └── ├── ├── └── └── test_symbol.py
├── ├── └── ├── ├── py.typed
├── ├── └── ├── ├── random/
├── ├── └── ├── ├── ├── __init__.pxd
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _bounded_integers.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _bounded_integers.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _bounded_integers.pxd
├── ├── └── ├── ├── ├── _bounded_integers.pyi
├── ├── └── ├── ├── ├── _common.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _common.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _common.pxd
├── ├── └── ├── ├── ├── _common.pyi
├── ├── └── ├── ├── ├── _examples/
├── ├── └── ├── ├── ├── ├── cffi/
├── ├── └── ├── ├── ├── ├── ├── extending.py
├── ├── └── ├── ├── ├── ├── └── parse.py
├── ├── └── ├── ├── ├── ├── cython/
├── ├── └── ├── ├── ├── ├── ├── extending.pyx
├── ├── └── ├── ├── ├── ├── ├── extending_distributions.pyx
├── ├── └── ├── ├── ├── ├── └── meson.build
├── ├── └── ├── ├── ├── └── numba/
├── ├── └── ├── ├── ├── └── ├── extending.py
├── ├── └── ├── ├── ├── └── └── extending_distributions.py
├── ├── └── ├── ├── ├── _generator.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _generator.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _generator.pyi
├── ├── └── ├── ├── ├── _mt19937.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _mt19937.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _mt19937.pyi
├── ├── └── ├── ├── ├── _pcg64.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _pcg64.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _pcg64.pyi
├── ├── └── ├── ├── ├── _philox.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _philox.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _philox.pyi
├── ├── └── ├── ├── ├── _pickle.py
├── ├── └── ├── ├── ├── _pickle.pyi
├── ├── └── ├── ├── ├── _sfc64.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── _sfc64.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── _sfc64.pyi
├── ├── └── ├── ├── ├── bit_generator.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── bit_generator.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── bit_generator.pxd
├── ├── └── ├── ├── ├── bit_generator.pyi
├── ├── └── ├── ├── ├── c_distributions.pxd
├── ├── └── ├── ├── ├── lib/
├── ├── └── ├── ├── ├── └── npyrandom.lib
├── ├── └── ├── ├── ├── LICENSE.md
├── ├── └── ├── ├── ├── mtrand.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── mtrand.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── mtrand.pyi
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── data/
├── ├── └── ├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── └── ├── ├── generator_pcg64_np121.pkl.gz
├── ├── └── ├── ├── └── ├── ├── generator_pcg64_np126.pkl.gz
├── ├── └── ├── ├── └── ├── ├── mt19937-testset-1.csv
├── ├── └── ├── ├── └── ├── ├── mt19937-testset-2.csv
├── ├── └── ├── ├── └── ├── ├── pcg64-testset-1.csv
├── ├── └── ├── ├── └── ├── ├── pcg64-testset-2.csv
├── ├── └── ├── ├── └── ├── ├── pcg64dxsm-testset-1.csv
├── ├── └── ├── ├── └── ├── ├── pcg64dxsm-testset-2.csv
├── ├── └── ├── ├── └── ├── ├── philox-testset-1.csv
├── ├── └── ├── ├── └── ├── ├── philox-testset-2.csv
├── ├── └── ├── ├── └── ├── ├── sfc64-testset-1.csv
├── ├── └── ├── ├── └── ├── ├── sfc64-testset-2.csv
├── ├── └── ├── ├── └── ├── └── sfc64_np126.pkl.gz
├── ├── └── ├── ├── └── ├── test_direct.py
├── ├── └── ├── ├── └── ├── test_extending.py
├── ├── └── ├── ├── └── ├── test_generator_mt19937.py
├── ├── └── ├── ├── └── ├── test_generator_mt19937_regressions.py
├── ├── └── ├── ├── └── ├── test_random.py
├── ├── └── ├── ├── └── ├── test_randomstate.py
├── ├── └── ├── ├── └── ├── test_randomstate_regression.py
├── ├── └── ├── ├── └── ├── test_regression.py
├── ├── └── ├── ├── └── ├── test_seed_sequence.py
├── ├── └── ├── ├── └── └── test_smoke.py
├── ├── └── ├── ├── rec/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── └── __init__.pyi
├── ├── └── ├── ├── strings/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── └── __init__.pyi
├── ├── └── ├── ├── testing/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── _private/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── ├── extbuild.py
├── ├── └── ├── ├── ├── ├── extbuild.pyi
├── ├── └── ├── ├── ├── ├── utils.py
├── ├── └── ├── ├── ├── └── utils.pyi
├── ├── └── ├── ├── ├── overrides.py
├── ├── └── ├── ├── ├── overrides.pyi
├── ├── └── ├── ├── ├── print_coercion_tables.py
├── ├── └── ├── ├── ├── print_coercion_tables.pyi
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── └── test_utils.py
├── ├── └── ├── ├── tests/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── test__all__.py
├── ├── └── ├── ├── ├── test_configtool.py
├── ├── └── ├── ├── ├── test_ctypeslib.py
├── ├── └── ├── ├── ├── test_lazyloading.py
├── ├── └── ├── ├── ├── test_matlib.py
├── ├── └── ├── ├── ├── test_numpy_config.py
├── ├── └── ├── ├── ├── test_numpy_version.py
├── ├── └── ├── ├── ├── test_public_api.py
├── ├── └── ├── ├── ├── test_reloading.py
├── ├── └── ├── ├── ├── test_scripts.py
├── ├── └── ├── ├── └── test_warnings.py
├── ├── └── ├── ├── typing/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── mypy_plugin.py
├── ├── └── ├── ├── └── tests/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── data/
├── ├── └── ├── ├── └── ├── ├── fail/
├── ├── └── ├── ├── └── ├── ├── ├── arithmetic.pyi
├── ├── └── ├── ├── └── ├── ├── ├── array_constructors.pyi
├── ├── └── ├── ├── └── ├── ├── ├── array_like.pyi
├── ├── └── ├── ├── └── ├── ├── ├── array_pad.pyi
├── ├── └── ├── ├── └── ├── ├── ├── arrayprint.pyi
├── ├── └── ├── ├── └── ├── ├── ├── arrayterator.pyi
├── ├── └── ├── ├── └── ├── ├── ├── bitwise_ops.pyi
├── ├── └── ├── ├── └── ├── ├── ├── char.pyi
├── ├── └── ├── ├── └── ├── ├── ├── chararray.pyi
├── ├── └── ├── ├── └── ├── ├── ├── comparisons.pyi
├── ├── └── ├── ├── └── ├── ├── ├── constants.pyi
├── ├── └── ├── ├── └── ├── ├── ├── datasource.pyi
├── ├── └── ├── ├── └── ├── ├── ├── dtype.pyi
├── ├── └── ├── ├── └── ├── ├── ├── einsumfunc.pyi
├── ├── └── ├── ├── └── ├── ├── ├── flatiter.pyi
├── ├── └── ├── ├── └── ├── ├── ├── fromnumeric.pyi
├── ├── └── ├── ├── └── ├── ├── ├── histograms.pyi
├── ├── └── ├── ├── └── ├── ├── ├── index_tricks.pyi
├── ├── └── ├── ├── └── ├── ├── ├── lib_function_base.pyi
├── ├── └── ├── ├── └── ├── ├── ├── lib_polynomial.pyi
├── ├── └── ├── ├── └── ├── ├── ├── lib_utils.pyi
├── ├── └── ├── ├── └── ├── ├── ├── lib_version.pyi
├── ├── └── ├── ├── └── ├── ├── ├── linalg.pyi
├── ├── └── ├── ├── └── ├── ├── ├── ma.pyi
├── ├── └── ├── ├── └── ├── ├── ├── memmap.pyi
├── ├── └── ├── ├── └── ├── ├── ├── modules.pyi
├── ├── └── ├── ├── └── ├── ├── ├── multiarray.pyi
├── ├── └── ├── ├── └── ├── ├── ├── ndarray.pyi
├── ├── └── ├── ├── └── ├── ├── ├── ndarray_misc.pyi
├── ├── └── ├── ├── └── ├── ├── ├── nditer.pyi
├── ├── └── ├── ├── └── ├── ├── ├── nested_sequence.pyi
├── ├── └── ├── ├── └── ├── ├── ├── npyio.pyi
├── ├── └── ├── ├── └── ├── ├── ├── numerictypes.pyi
├── ├── └── ├── ├── └── ├── ├── ├── random.pyi
├── ├── └── ├── ├── └── ├── ├── ├── rec.pyi
├── ├── └── ├── ├── └── ├── ├── ├── scalars.pyi
├── ├── └── ├── ├── └── ├── ├── ├── shape.pyi
├── ├── └── ├── ├── └── ├── ├── ├── shape_base.pyi
├── ├── └── ├── ├── └── ├── ├── ├── stride_tricks.pyi
├── ├── └── ├── ├── └── ├── ├── ├── strings.pyi
├── ├── └── ├── ├── └── ├── ├── ├── testing.pyi
├── ├── └── ├── ├── └── ├── ├── ├── twodim_base.pyi
├── ├── └── ├── ├── └── ├── ├── ├── type_check.pyi
├── ├── └── ├── ├── └── ├── ├── ├── ufunc_config.pyi
├── ├── └── ├── ├── └── ├── ├── ├── ufunclike.pyi
├── ├── └── ├── ├── └── ├── ├── ├── ufuncs.pyi
├── ├── └── ├── ├── └── ├── ├── └── warnings_and_errors.pyi
├── ├── └── ├── ├── └── ├── ├── misc/
├── ├── └── ├── ├── └── ├── ├── └── extended_precision.pyi
├── ├── └── ├── ├── └── ├── ├── mypy.ini
├── ├── └── ├── ├── └── ├── ├── pass/
├── ├── └── ├── ├── └── ├── ├── ├── arithmetic.py
├── ├── └── ├── ├── └── ├── ├── ├── array_constructors.py
├── ├── └── ├── ├── └── ├── ├── ├── array_like.py
├── ├── └── ├── ├── └── ├── ├── ├── arrayprint.py
├── ├── └── ├── ├── └── ├── ├── ├── arrayterator.py
├── ├── └── ├── ├── └── ├── ├── ├── bitwise_ops.py
├── ├── └── ├── ├── └── ├── ├── ├── comparisons.py
├── ├── └── ├── ├── └── ├── ├── ├── dtype.py
├── ├── └── ├── ├── └── ├── ├── ├── einsumfunc.py
├── ├── └── ├── ├── └── ├── ├── ├── flatiter.py
├── ├── └── ├── ├── └── ├── ├── ├── fromnumeric.py
├── ├── └── ├── ├── └── ├── ├── ├── index_tricks.py
├── ├── └── ├── ├── └── ├── ├── ├── lib_user_array.py
├── ├── └── ├── ├── └── ├── ├── ├── lib_utils.py
├── ├── └── ├── ├── └── ├── ├── ├── lib_version.py
├── ├── └── ├── ├── └── ├── ├── ├── literal.py
├── ├── └── ├── ├── └── ├── ├── ├── ma.py
├── ├── └── ├── ├── └── ├── ├── ├── mod.py
├── ├── └── ├── ├── └── ├── ├── ├── modules.py
├── ├── └── ├── ├── └── ├── ├── ├── multiarray.py
├── ├── └── ├── ├── └── ├── ├── ├── ndarray_conversion.py
├── ├── └── ├── ├── └── ├── ├── ├── ndarray_misc.py
├── ├── └── ├── ├── └── ├── ├── ├── ndarray_shape_manipulation.py
├── ├── └── ├── ├── └── ├── ├── ├── nditer.py
├── ├── └── ├── ├── └── ├── ├── ├── numeric.py
├── ├── └── ├── ├── └── ├── ├── ├── numerictypes.py
├── ├── └── ├── ├── └── ├── ├── ├── random.py
├── ├── └── ├── ├── └── ├── ├── ├── recfunctions.py
├── ├── └── ├── ├── └── ├── ├── ├── scalars.py
├── ├── └── ├── ├── └── ├── ├── ├── shape.py
├── ├── └── ├── ├── └── ├── ├── ├── simple.py
├── ├── └── ├── ├── └── ├── ├── ├── simple_py3.py
├── ├── └── ├── ├── └── ├── ├── ├── ufunc_config.py
├── ├── └── ├── ├── └── ├── ├── ├── ufunclike.py
├── ├── └── ├── ├── └── ├── ├── ├── ufuncs.py
├── ├── └── ├── ├── └── ├── ├── └── warnings_and_errors.py
├── ├── └── ├── ├── └── ├── └── reveal/
├── ├── └── ├── ├── └── ├── └── ├── arithmetic.pyi
├── ├── └── ├── ├── └── ├── └── ├── array_api_info.pyi
├── ├── └── ├── ├── └── ├── └── ├── array_constructors.pyi
├── ├── └── ├── ├── └── ├── └── ├── arraypad.pyi
├── ├── └── ├── ├── └── ├── └── ├── arrayprint.pyi
├── ├── └── ├── ├── └── ├── └── ├── arraysetops.pyi
├── ├── └── ├── ├── └── ├── └── ├── arrayterator.pyi
├── ├── └── ├── ├── └── ├── └── ├── bitwise_ops.pyi
├── ├── └── ├── ├── └── ├── └── ├── char.pyi
├── ├── └── ├── ├── └── ├── └── ├── chararray.pyi
├── ├── └── ├── ├── └── ├── └── ├── comparisons.pyi
├── ├── └── ├── ├── └── ├── └── ├── constants.pyi
├── ├── └── ├── ├── └── ├── └── ├── ctypeslib.pyi
├── ├── └── ├── ├── └── ├── └── ├── datasource.pyi
├── ├── └── ├── ├── └── ├── └── ├── dtype.pyi
├── ├── └── ├── ├── └── ├── └── ├── einsumfunc.pyi
├── ├── └── ├── ├── └── ├── └── ├── emath.pyi
├── ├── └── ├── ├── └── ├── └── ├── fft.pyi
├── ├── └── ├── ├── └── ├── └── ├── flatiter.pyi
├── ├── └── ├── ├── └── ├── └── ├── fromnumeric.pyi
├── ├── └── ├── ├── └── ├── └── ├── getlimits.pyi
├── ├── └── ├── ├── └── ├── └── ├── histograms.pyi
├── ├── └── ├── ├── └── ├── └── ├── index_tricks.pyi
├── ├── └── ├── ├── └── ├── └── ├── lib_function_base.pyi
├── ├── └── ├── ├── └── ├── └── ├── lib_polynomial.pyi
├── ├── └── ├── ├── └── ├── └── ├── lib_utils.pyi
├── ├── └── ├── ├── └── ├── └── ├── lib_version.pyi
├── ├── └── ├── ├── └── ├── └── ├── linalg.pyi
├── ├── └── ├── ├── └── ├── └── ├── ma.pyi
├── ├── └── ├── ├── └── ├── └── ├── matrix.pyi
├── ├── └── ├── ├── └── ├── └── ├── memmap.pyi
├── ├── └── ├── ├── └── ├── └── ├── mod.pyi
├── ├── └── ├── ├── └── ├── └── ├── modules.pyi
├── ├── └── ├── ├── └── ├── └── ├── multiarray.pyi
├── ├── └── ├── ├── └── ├── └── ├── nbit_base_example.pyi
├── ├── └── ├── ├── └── ├── └── ├── ndarray_assignability.pyi
├── ├── └── ├── ├── └── ├── └── ├── ndarray_conversion.pyi
├── ├── └── ├── ├── └── ├── └── ├── ndarray_misc.pyi
├── ├── └── ├── ├── └── ├── └── ├── ndarray_shape_manipulation.pyi
├── ├── └── ├── ├── └── ├── └── ├── nditer.pyi
├── ├── └── ├── ├── └── ├── └── ├── nested_sequence.pyi
├── ├── └── ├── ├── └── ├── └── ├── npyio.pyi
├── ├── └── ├── ├── └── ├── └── ├── numeric.pyi
├── ├── └── ├── ├── └── ├── └── ├── numerictypes.pyi
├── ├── └── ├── ├── └── ├── └── ├── polynomial_polybase.pyi
├── ├── └── ├── ├── └── ├── └── ├── polynomial_polyutils.pyi
├── ├── └── ├── ├── └── ├── └── ├── polynomial_series.pyi
├── ├── └── ├── ├── └── ├── └── ├── random.pyi
├── ├── └── ├── ├── └── ├── └── ├── rec.pyi
├── ├── └── ├── ├── └── ├── └── ├── scalars.pyi
├── ├── └── ├── ├── └── ├── └── ├── shape.pyi
├── ├── └── ├── ├── └── ├── └── ├── shape_base.pyi
├── ├── └── ├── ├── └── ├── └── ├── stride_tricks.pyi
├── ├── └── ├── ├── └── ├── └── ├── strings.pyi
├── ├── └── ├── ├── └── ├── └── ├── testing.pyi
├── ├── └── ├── ├── └── ├── └── ├── twodim_base.pyi
├── ├── └── ├── ├── └── ├── └── ├── type_check.pyi
├── ├── └── ├── ├── └── ├── └── ├── ufunc_config.pyi
├── ├── └── ├── ├── └── ├── └── ├── ufunclike.pyi
├── ├── └── ├── ├── └── ├── └── ├── ufuncs.pyi
├── ├── └── ├── ├── └── ├── └── └── warnings_and_errors.pyi
├── ├── └── ├── ├── └── ├── test_isfile.py
├── ├── └── ├── ├── └── ├── test_runtime.py
├── ├── └── ├── ├── └── └── test_typing.py
├── ├── └── ├── ├── version.py
├── ├── └── ├── └── version.pyi
├── ├── └── ├── numpy-2.3.2.dist-info/
├── ├── └── ├── ├── DELVEWHEEL
├── ├── └── ├── ├── entry_points.txt
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE.txt
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── └── WHEEL
├── ├── └── ├── numpy.libs/
├── ├── └── ├── ├── libscipy_openblas64_-860d95b1c38e637ce4509f5fa24fbf2a.dll
├── ├── └── ├── └── msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
├── ├── └── ├── packaging/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── _elffile.py
├── ├── └── ├── ├── _manylinux.py
├── ├── └── ├── ├── _musllinux.py
├── ├── └── ├── ├── _parser.py
├── ├── └── ├── ├── _structures.py
├── ├── └── ├── ├── _tokenizer.py
├── ├── └── ├── ├── licenses/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── └── _spdx.py
├── ├── └── ├── ├── markers.py
├── ├── └── ├── ├── metadata.py
├── ├── └── ├── ├── py.typed
├── ├── └── ├── ├── requirements.py
├── ├── └── ├── ├── specifiers.py
├── ├── └── ├── ├── tags.py
├── ├── └── ├── ├── utils.py
├── ├── └── ├── └── version.py
├── ├── └── ├── packaging-25.0.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── licenses/
├── ├── └── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── LICENSE.APACHE
├── ├── └── ├── ├── └── LICENSE.BSD
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── └── WHEEL
├── ├── └── ├── pandas/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── _config/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── config.py
├── ├── └── ├── ├── ├── dates.py
├── ├── └── ├── ├── ├── display.py
├── ├── └── ├── ├── └── localization.py
├── ├── └── ├── ├── _libs/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── algos.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── algos.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── algos.pyi
├── ├── └── ├── ├── ├── arrays.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── arrays.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── arrays.pyi
├── ├── └── ├── ├── ├── byteswap.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── byteswap.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── byteswap.pyi
├── ├── └── ├── ├── ├── groupby.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── groupby.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── groupby.pyi
├── ├── └── ├── ├── ├── hashing.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── hashing.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── hashing.pyi
├── ├── └── ├── ├── ├── hashtable.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── hashtable.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── hashtable.pyi
├── ├── └── ├── ├── ├── index.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── index.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── index.pyi
├── ├── └── ├── ├── ├── indexing.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── indexing.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── indexing.pyi
├── ├── └── ├── ├── ├── internals.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── internals.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── internals.pyi
├── ├── └── ├── ├── ├── interval.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── interval.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── interval.pyi
├── ├── └── ├── ├── ├── join.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── join.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── join.pyi
├── ├── └── ├── ├── ├── json.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── json.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── json.pyi
├── ├── └── ├── ├── ├── lib.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── lib.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── lib.pyi
├── ├── └── ├── ├── ├── missing.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── missing.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── missing.pyi
├── ├── └── ├── ├── ├── ops.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ops.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ops.pyi
├── ├── └── ├── ├── ├── ops_dispatch.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ops_dispatch.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ops_dispatch.pyi
├── ├── └── ├── ├── ├── pandas_datetime.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── pandas_datetime.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── pandas_parser.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── pandas_parser.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── parsers.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── parsers.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── parsers.pyi
├── ├── └── ├── ├── ├── properties.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── properties.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── properties.pyi
├── ├── └── ├── ├── ├── reshape.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── reshape.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── reshape.pyi
├── ├── └── ├── ├── ├── sas.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── sas.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── sas.pyi
├── ├── └── ├── ├── ├── sparse.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── sparse.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── sparse.pyi
├── ├── └── ├── ├── ├── testing.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── testing.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── testing.pyi
├── ├── └── ├── ├── ├── tslib.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── tslib.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── tslib.pyi
├── ├── └── ├── ├── ├── tslibs/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── base.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── base.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── ccalendar.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── ccalendar.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── ccalendar.pyi
├── ├── └── ├── ├── ├── ├── conversion.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── conversion.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── conversion.pyi
├── ├── └── ├── ├── ├── ├── dtypes.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── dtypes.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── dtypes.pyi
├── ├── └── ├── ├── ├── ├── fields.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── fields.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── fields.pyi
├── ├── └── ├── ├── ├── ├── nattype.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── nattype.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── nattype.pyi
├── ├── └── ├── ├── ├── ├── np_datetime.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── np_datetime.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── np_datetime.pyi
├── ├── └── ├── ├── ├── ├── offsets.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── offsets.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── offsets.pyi
├── ├── └── ├── ├── ├── ├── parsing.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── parsing.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── parsing.pyi
├── ├── └── ├── ├── ├── ├── period.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── period.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── period.pyi
├── ├── └── ├── ├── ├── ├── strptime.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── strptime.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── strptime.pyi
├── ├── └── ├── ├── ├── ├── timedeltas.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── timedeltas.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── timedeltas.pyi
├── ├── └── ├── ├── ├── ├── timestamps.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── timestamps.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── timestamps.pyi
├── ├── └── ├── ├── ├── ├── timezones.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── timezones.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── timezones.pyi
├── ├── └── ├── ├── ├── ├── tzconversion.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── tzconversion.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── tzconversion.pyi
├── ├── └── ├── ├── ├── ├── vectorized.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── vectorized.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── └── vectorized.pyi
├── ├── └── ├── ├── ├── window/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── aggregations.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── aggregations.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── ├── aggregations.pyi
├── ├── └── ├── ├── ├── ├── indexers.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── ├── indexers.cp312-win_amd64.pyd
├── ├── └── ├── ├── ├── └── indexers.pyi
├── ├── └── ├── ├── ├── writers.cp312-win_amd64.lib
├── ├── └── ├── ├── ├── writers.cp312-win_amd64.pyd
├── ├── └── ├── ├── └── writers.pyi
├── ├── └── ├── ├── _testing/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _hypothesis.py
├── ├── └── ├── ├── ├── _io.py
├── ├── └── ├── ├── ├── _warnings.py
├── ├── └── ├── ├── ├── asserters.py
├── ├── └── ├── ├── ├── compat.py
├── ├── └── ├── ├── └── contexts.py
├── ├── └── ├── ├── _typing.py
├── ├── └── ├── ├── _version.py
├── ├── └── ├── ├── _version_meson.py
├── ├── └── ├── ├── api/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── extensions/
├── ├── └── ├── ├── ├── └── __init__.py
├── ├── └── ├── ├── ├── indexers/
├── ├── └── ├── ├── ├── └── __init__.py
├── ├── └── ├── ├── ├── interchange/
├── ├── └── ├── ├── ├── └── __init__.py
├── ├── └── ├── ├── ├── types/
├── ├── └── ├── ├── ├── └── __init__.py
├── ├── └── ├── ├── └── typing/
├── ├── └── ├── ├── └── └── __init__.py
├── ├── └── ├── ├── arrays/
├── ├── └── ├── ├── └── __init__.py
├── ├── └── ├── ├── compat/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _constants.py
├── ├── └── ├── ├── ├── _optional.py
├── ├── └── ├── ├── ├── compressors.py
├── ├── └── ├── ├── ├── numpy/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── function.py
├── ├── └── ├── ├── ├── pickle_compat.py
├── ├── └── ├── ├── └── pyarrow.py
├── ├── └── ├── ├── conftest.py
├── ├── └── ├── ├── core/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _numba/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── executor.py
├── ├── └── ├── ├── ├── ├── extensions.py
├── ├── └── ├── ├── ├── └── kernels/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── mean_.py
├── ├── └── ├── ├── ├── └── ├── min_max_.py
├── ├── └── ├── ├── ├── └── ├── shared.py
├── ├── └── ├── ├── ├── └── ├── sum_.py
├── ├── └── ├── ├── ├── └── └── var_.py
├── ├── └── ├── ├── ├── accessor.py
├── ├── └── ├── ├── ├── algorithms.py
├── ├── └── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── apply.py
├── ├── └── ├── ├── ├── array_algos/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── datetimelike_accumulations.py
├── ├── └── ├── ├── ├── ├── masked_accumulations.py
├── ├── └── ├── ├── ├── ├── masked_reductions.py
├── ├── └── ├── ├── ├── ├── putmask.py
├── ├── └── ├── ├── ├── ├── quantile.py
├── ├── └── ├── ├── ├── ├── replace.py
├── ├── └── ├── ├── ├── ├── take.py
├── ├── └── ├── ├── ├── └── transforms.py
├── ├── └── ├── ├── ├── arraylike.py
├── ├── └── ├── ├── ├── arrays/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _arrow_string_mixins.py
├── ├── └── ├── ├── ├── ├── _mixins.py
├── ├── └── ├── ├── ├── ├── _ranges.py
├── ├── └── ├── ├── ├── ├── _utils.py
├── ├── └── ├── ├── ├── ├── arrow/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── _arrow_utils.py
├── ├── └── ├── ├── ├── ├── ├── accessors.py
├── ├── └── ├── ├── ├── ├── ├── array.py
├── ├── └── ├── ├── ├── ├── └── extension_types.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── boolean.py
├── ├── └── ├── ├── ├── ├── categorical.py
├── ├── └── ├── ├── ├── ├── datetimelike.py
├── ├── └── ├── ├── ├── ├── datetimes.py
├── ├── └── ├── ├── ├── ├── floating.py
├── ├── └── ├── ├── ├── ├── integer.py
├── ├── └── ├── ├── ├── ├── interval.py
├── ├── └── ├── ├── ├── ├── masked.py
├── ├── └── ├── ├── ├── ├── numeric.py
├── ├── └── ├── ├── ├── ├── numpy_.py
├── ├── └── ├── ├── ├── ├── period.py
├── ├── └── ├── ├── ├── ├── sparse/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── accessor.py
├── ├── └── ├── ├── ├── ├── ├── array.py
├── ├── └── ├── ├── ├── ├── └── scipy_sparse.py
├── ├── └── ├── ├── ├── ├── string_.py
├── ├── └── ├── ├── ├── ├── string_arrow.py
├── ├── └── ├── ├── ├── └── timedeltas.py
├── ├── └── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── computation/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── align.py
├── ├── └── ├── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── ├── check.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── engines.py
├── ├── └── ├── ├── ├── ├── eval.py
├── ├── └── ├── ├── ├── ├── expr.py
├── ├── └── ├── ├── ├── ├── expressions.py
├── ├── └── ├── ├── ├── ├── ops.py
├── ├── └── ├── ├── ├── ├── parsing.py
├── ├── └── ├── ├── ├── ├── pytables.py
├── ├── └── ├── ├── ├── └── scope.py
├── ├── └── ├── ├── ├── config_init.py
├── ├── └── ├── ├── ├── construction.py
├── ├── └── ├── ├── ├── dtypes/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── ├── astype.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── cast.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── concat.py
├── ├── └── ├── ├── ├── ├── dtypes.py
├── ├── └── ├── ├── ├── ├── generic.py
├── ├── └── ├── ├── ├── ├── inference.py
├── ├── └── ├── ├── ├── └── missing.py
├── ├── └── ├── ├── ├── flags.py
├── ├── └── ├── ├── ├── frame.py
├── ├── └── ├── ├── ├── generic.py
├── ├── └── ├── ├── ├── groupby/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── categorical.py
├── ├── └── ├── ├── ├── ├── generic.py
├── ├── └── ├── ├── ├── ├── groupby.py
├── ├── └── ├── ├── ├── ├── grouper.py
├── ├── └── ├── ├── ├── ├── indexing.py
├── ├── └── ├── ├── ├── ├── numba_.py
├── ├── └── ├── ├── ├── └── ops.py
├── ├── └── ├── ├── ├── indexers/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── objects.py
├── ├── └── ├── ├── ├── └── utils.py
├── ├── └── ├── ├── ├── indexes/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── accessors.py
├── ├── └── ├── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── category.py
├── ├── └── ├── ├── ├── ├── datetimelike.py
├── ├── └── ├── ├── ├── ├── datetimes.py
├── ├── └── ├── ├── ├── ├── extension.py
├── ├── └── ├── ├── ├── ├── frozen.py
├── ├── └── ├── ├── ├── ├── interval.py
├── ├── └── ├── ├── ├── ├── multi.py
├── ├── └── ├── ├── ├── ├── period.py
├── ├── └── ├── ├── ├── ├── range.py
├── ├── └── ├── ├── ├── └── timedeltas.py
├── ├── └── ├── ├── ├── indexing.py
├── ├── └── ├── ├── ├── interchange/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── buffer.py
├── ├── └── ├── ├── ├── ├── column.py
├── ├── └── ├── ├── ├── ├── dataframe.py
├── ├── └── ├── ├── ├── ├── dataframe_protocol.py
├── ├── └── ├── ├── ├── ├── from_dataframe.py
├── ├── └── ├── ├── ├── └── utils.py
├── ├── └── ├── ├── ├── internals/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── ├── array_manager.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── blocks.py
├── ├── └── ├── ├── ├── ├── concat.py
├── ├── └── ├── ├── ├── ├── construction.py
├── ├── └── ├── ├── ├── ├── managers.py
├── ├── └── ├── ├── ├── └── ops.py
├── ├── └── ├── ├── ├── methods/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── describe.py
├── ├── └── ├── ├── ├── ├── selectn.py
├── ├── └── ├── ├── ├── └── to_dict.py
├── ├── └── ├── ├── ├── missing.py
├── ├── └── ├── ├── ├── nanops.py
├── ├── └── ├── ├── ├── ops/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── array_ops.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── dispatch.py
├── ├── └── ├── ├── ├── ├── docstrings.py
├── ├── └── ├── ├── ├── ├── invalid.py
├── ├── └── ├── ├── ├── ├── mask_ops.py
├── ├── └── ├── ├── ├── └── missing.py
├── ├── └── ├── ├── ├── resample.py
├── ├── └── ├── ├── ├── reshape/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── ├── concat.py
├── ├── └── ├── ├── ├── ├── encoding.py
├── ├── └── ├── ├── ├── ├── melt.py
├── ├── └── ├── ├── ├── ├── merge.py
├── ├── └── ├── ├── ├── ├── pivot.py
├── ├── └── ├── ├── ├── ├── reshape.py
├── ├── └── ├── ├── ├── ├── tile.py
├── ├── └── ├── ├── ├── └── util.py
├── ├── └── ├── ├── ├── roperator.py
├── ├── └── ├── ├── ├── sample.py
├── ├── └── ├── ├── ├── series.py
├── ├── └── ├── ├── ├── shared_docs.py
├── ├── └── ├── ├── ├── sorting.py
├── ├── └── ├── ├── ├── sparse/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── api.py
├── ├── └── ├── ├── ├── strings/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── accessor.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── └── object_array.py
├── ├── └── ├── ├── ├── tools/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── datetimes.py
├── ├── └── ├── ├── ├── ├── numeric.py
├── ├── └── ├── ├── ├── ├── timedeltas.py
├── ├── └── ├── ├── ├── └── times.py
├── ├── └── ├── ├── ├── util/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── hashing.py
├── ├── └── ├── ├── ├── └── numba_.py
├── ├── └── ├── ├── └── window/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── common.py
├── ├── └── ├── ├── └── ├── doc.py
├── ├── └── ├── ├── └── ├── ewm.py
├── ├── └── ├── ├── └── ├── expanding.py
├── ├── └── ├── ├── └── ├── numba_.py
├── ├── └── ├── ├── └── ├── online.py
├── ├── └── ├── ├── └── └── rolling.py
├── ├── └── ├── ├── errors/
├── ├── └── ├── ├── └── __init__.py
├── ├── └── ├── ├── io/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _util.py
├── ├── └── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── clipboard/
├── ├── └── ├── ├── ├── └── __init__.py
├── ├── └── ├── ├── ├── clipboards.py
├── ├── └── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── excel/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _base.py
├── ├── └── ├── ├── ├── ├── _calamine.py
├── ├── └── ├── ├── ├── ├── _odfreader.py
├── ├── └── ├── ├── ├── ├── _odswriter.py
├── ├── └── ├── ├── ├── ├── _openpyxl.py
├── ├── └── ├── ├── ├── ├── _pyxlsb.py
├── ├── └── ├── ├── ├── ├── _util.py
├── ├── └── ├── ├── ├── ├── _xlrd.py
├── ├── └── ├── ├── ├── └── _xlsxwriter.py
├── ├── └── ├── ├── ├── feather_format.py
├── ├── └── ├── ├── ├── formats/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _color_data.py
├── ├── └── ├── ├── ├── ├── console.py
├── ├── └── ├── ├── ├── ├── css.py
├── ├── └── ├── ├── ├── ├── csvs.py
├── ├── └── ├── ├── ├── ├── excel.py
├── ├── └── ├── ├── ├── ├── format.py
├── ├── └── ├── ├── ├── ├── html.py
├── ├── └── ├── ├── ├── ├── info.py
├── ├── └── ├── ├── ├── ├── printing.py
├── ├── └── ├── ├── ├── ├── string.py
├── ├── └── ├── ├── ├── ├── style.py
├── ├── └── ├── ├── ├── ├── style_render.py
├── ├── └── ├── ├── ├── ├── templates/
├── ├── └── ├── ├── ├── ├── ├── html.tpl
├── ├── └── ├── ├── ├── ├── ├── html_style.tpl
├── ├── └── ├── ├── ├── ├── ├── html_table.tpl
├── ├── └── ├── ├── ├── ├── ├── latex.tpl
├── ├── └── ├── ├── ├── ├── ├── latex_longtable.tpl
├── ├── └── ├── ├── ├── ├── ├── latex_table.tpl
├── ├── └── ├── ├── ├── ├── └── string.tpl
├── ├── └── ├── ├── ├── └── xml.py
├── ├── └── ├── ├── ├── gbq.py
├── ├── └── ├── ├── ├── html.py
├── ├── └── ├── ├── ├── json/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _json.py
├── ├── └── ├── ├── ├── ├── _normalize.py
├── ├── └── ├── ├── ├── └── _table_schema.py
├── ├── └── ├── ├── ├── orc.py
├── ├── └── ├── ├── ├── parquet.py
├── ├── └── ├── ├── ├── parsers/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── arrow_parser_wrapper.py
├── ├── └── ├── ├── ├── ├── base_parser.py
├── ├── └── ├── ├── ├── ├── c_parser_wrapper.py
├── ├── └── ├── ├── ├── ├── python_parser.py
├── ├── └── ├── ├── ├── └── readers.py
├── ├── └── ├── ├── ├── pickle.py
├── ├── └── ├── ├── ├── pytables.py
├── ├── └── ├── ├── ├── sas/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── sas7bdat.py
├── ├── └── ├── ├── ├── ├── sas_constants.py
├── ├── └── ├── ├── ├── ├── sas_xport.py
├── ├── └── ├── ├── ├── └── sasreader.py
├── ├── └── ├── ├── ├── spss.py
├── ├── └── ├── ├── ├── sql.py
├── ├── └── ├── ├── ├── stata.py
├── ├── └── ├── ├── └── xml.py
├── ├── └── ├── ├── plotting/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _core.py
├── ├── └── ├── ├── ├── _matplotlib/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── boxplot.py
├── ├── └── ├── ├── ├── ├── converter.py
├── ├── └── ├── ├── ├── ├── core.py
├── ├── └── ├── ├── ├── ├── groupby.py
├── ├── └── ├── ├── ├── ├── hist.py
├── ├── └── ├── ├── ├── ├── misc.py
├── ├── └── ├── ├── ├── ├── style.py
├── ├── └── ├── ├── ├── ├── timeseries.py
├── ├── └── ├── ├── ├── └── tools.py
├── ├── └── ├── ├── └── _misc.py
├── ├── └── ├── ├── pyproject.toml
├── ├── └── ├── ├── testing.py
├── ├── └── ├── ├── tests/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── api/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── └── test_types.py
├── ├── └── ├── ├── ├── apply/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── test_frame_apply.py
├── ├── └── ├── ├── ├── ├── test_frame_apply_relabeling.py
├── ├── └── ├── ├── ├── ├── test_frame_transform.py
├── ├── └── ├── ├── ├── ├── test_invalid_arg.py
├── ├── └── ├── ├── ├── ├── test_numba.py
├── ├── └── ├── ├── ├── ├── test_series_apply.py
├── ├── └── ├── ├── ├── ├── test_series_apply_relabeling.py
├── ├── └── ├── ├── ├── ├── test_series_transform.py
├── ├── └── ├── ├── ├── └── test_str.py
├── ├── └── ├── ├── ├── arithmetic/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── test_array_ops.py
├── ├── └── ├── ├── ├── ├── test_categorical.py
├── ├── └── ├── ├── ├── ├── test_datetime64.py
├── ├── └── ├── ├── ├── ├── test_interval.py
├── ├── └── ├── ├── ├── ├── test_numeric.py
├── ├── └── ├── ├── ├── ├── test_object.py
├── ├── └── ├── ├── ├── ├── test_period.py
├── ├── └── ├── ├── ├── └── test_timedelta64.py
├── ├── └── ├── ├── ├── arrays/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── boolean/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_comparison.py
├── ├── └── ├── ├── ├── ├── ├── test_construction.py
├── ├── └── ├── ├── ├── ├── ├── test_function.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_logical.py
├── ├── └── ├── ├── ├── ├── ├── test_ops.py
├── ├── └── ├── ├── ├── ├── ├── test_reduction.py
├── ├── └── ├── ├── ├── ├── └── test_repr.py
├── ├── └── ├── ├── ├── ├── categorical/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_algos.py
├── ├── └── ├── ├── ├── ├── ├── test_analytics.py
├── ├── └── ├── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_dtypes.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_map.py
├── ├── └── ├── ├── ├── ├── ├── test_missing.py
├── ├── └── ├── ├── ├── ├── ├── test_operators.py
├── ├── └── ├── ├── ├── ├── ├── test_replace.py
├── ├── └── ├── ├── ├── ├── ├── test_repr.py
├── ├── └── ├── ├── ├── ├── ├── test_sorting.py
├── ├── └── ├── ├── ├── ├── ├── test_subclass.py
├── ├── └── ├── ├── ├── ├── ├── test_take.py
├── ├── └── ├── ├── ├── ├── └── test_warnings.py
├── ├── └── ├── ├── ├── ├── datetimes/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_cumulative.py
├── ├── └── ├── ├── ├── ├── └── test_reductions.py
├── ├── └── ├── ├── ├── ├── floating/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_comparison.py
├── ├── └── ├── ├── ├── ├── ├── test_concat.py
├── ├── └── ├── ├── ├── ├── ├── test_construction.py
├── ├── └── ├── ├── ├── ├── ├── test_contains.py
├── ├── └── ├── ├── ├── ├── ├── test_function.py
├── ├── └── ├── ├── ├── ├── ├── test_repr.py
├── ├── └── ├── ├── ├── ├── └── test_to_numpy.py
├── ├── └── ├── ├── ├── ├── integer/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── ├── test_comparison.py
├── ├── └── ├── ├── ├── ├── ├── test_concat.py
├── ├── └── ├── ├── ├── ├── ├── test_construction.py
├── ├── └── ├── ├── ├── ├── ├── test_dtypes.py
├── ├── └── ├── ├── ├── ├── ├── test_function.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_reduction.py
├── ├── └── ├── ├── ├── ├── └── test_repr.py
├── ├── └── ├── ├── ├── ├── interval/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── ├── test_interval.py
├── ├── └── ├── ├── ├── ├── ├── test_interval_pyarrow.py
├── ├── └── ├── ├── ├── ├── └── test_overlaps.py
├── ├── └── ├── ├── ├── ├── masked/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── ├── test_arrow_compat.py
├── ├── └── ├── ├── ├── ├── ├── test_function.py
├── ├── └── ├── ├── ├── ├── └── test_indexing.py
├── ├── └── ├── ├── ├── ├── masked_shared.py
├── ├── └── ├── ├── ├── ├── numpy_/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── └── test_numpy.py
├── ├── └── ├── ├── ├── ├── period/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_arrow_compat.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── └── test_reductions.py
├── ├── └── ├── ├── ├── ├── sparse/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_accessor.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetics.py
├── ├── └── ├── ├── ├── ├── ├── test_array.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_combine_concat.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_dtype.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_libsparse.py
├── ├── └── ├── ├── ├── ├── ├── test_reductions.py
├── ├── └── ├── ├── ├── ├── └── test_unary.py
├── ├── └── ├── ├── ├── ├── string_/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_concat.py
├── ├── └── ├── ├── ├── ├── ├── test_string.py
├── ├── └── ├── ├── ├── ├── └── test_string_arrow.py
├── ├── └── ├── ├── ├── ├── test_array.py
├── ├── └── ├── ├── ├── ├── test_datetimelike.py
├── ├── └── ├── ├── ├── ├── test_datetimes.py
├── ├── └── ├── ├── ├── ├── test_ndarray_backed.py
├── ├── └── ├── ├── ├── ├── test_period.py
├── ├── └── ├── ├── ├── ├── test_timedeltas.py
├── ├── └── ├── ├── ├── └── timedeltas/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── test_constructors.py
├── ├── └── ├── ├── ├── └── ├── test_cumulative.py
├── ├── └── ├── ├── ├── └── └── test_reductions.py
├── ├── └── ├── ├── ├── base/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── test_conversion.py
├── ├── └── ├── ├── ├── ├── test_fillna.py
├── ├── └── ├── ├── ├── ├── test_misc.py
├── ├── └── ├── ├── ├── ├── test_transpose.py
├── ├── └── ├── ├── ├── ├── test_unique.py
├── ├── └── ├── ├── ├── └── test_value_counts.py
├── ├── └── ├── ├── ├── computation/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_compat.py
├── ├── └── ├── ├── ├── └── test_eval.py
├── ├── └── ├── ├── ├── config/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_config.py
├── ├── └── ├── ├── ├── └── test_localization.py
├── ├── └── ├── ├── ├── construction/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── test_extract_array.py
├── ├── └── ├── ├── ├── copy_view/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── index/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_datetimeindex.py
├── ├── └── ├── ├── ├── ├── ├── test_index.py
├── ├── └── ├── ├── ├── ├── ├── test_periodindex.py
├── ├── └── ├── ├── ├── ├── └── test_timedeltaindex.py
├── ├── └── ├── ├── ├── ├── test_array.py
├── ├── └── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── test_chained_assignment_deprecation.py
├── ├── └── ├── ├── ├── ├── test_clip.py
├── ├── └── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── test_core_functionalities.py
├── ├── └── ├── ├── ├── ├── test_functions.py
├── ├── └── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── test_internals.py
├── ├── └── ├── ├── ├── ├── test_interp_fillna.py
├── ├── └── ├── ├── ├── ├── test_methods.py
├── ├── └── ├── ├── ├── ├── test_replace.py
├── ├── └── ├── ├── ├── ├── test_setitem.py
├── ├── └── ├── ├── ├── ├── test_util.py
├── ├── └── ├── ├── ├── └── util.py
├── ├── └── ├── ├── ├── dtypes/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── cast/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_can_hold_element.py
├── ├── └── ├── ├── ├── ├── ├── test_construct_from_scalar.py
├── ├── └── ├── ├── ├── ├── ├── test_construct_ndarray.py
├── ├── └── ├── ├── ├── ├── ├── test_construct_object_arr.py
├── ├── └── ├── ├── ├── ├── ├── test_dict_compat.py
├── ├── └── ├── ├── ├── ├── ├── test_downcast.py
├── ├── └── ├── ├── ├── ├── ├── test_find_common_type.py
├── ├── └── ├── ├── ├── ├── ├── test_infer_datetimelike.py
├── ├── └── ├── ├── ├── ├── ├── test_infer_dtype.py
├── ├── └── ├── ├── ├── ├── ├── test_maybe_box_native.py
├── ├── └── ├── ├── ├── ├── └── test_promote.py
├── ├── └── ├── ├── ├── ├── test_common.py
├── ├── └── ├── ├── ├── ├── test_concat.py
├── ├── └── ├── ├── ├── ├── test_dtypes.py
├── ├── └── ├── ├── ├── ├── test_generic.py
├── ├── └── ├── ├── ├── ├── test_inference.py
├── ├── └── ├── ├── ├── └── test_missing.py
├── ├── └── ├── ├── ├── extension/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── array_with_attr/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── array.py
├── ├── └── ├── ├── ├── ├── └── test_array_with_attr.py
├── ├── └── ├── ├── ├── ├── base/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── accumulate.py
├── ├── └── ├── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── ├── casting.py
├── ├── └── ├── ├── ├── ├── ├── constructors.py
├── ├── └── ├── ├── ├── ├── ├── dim2.py
├── ├── └── ├── ├── ├── ├── ├── dtype.py
├── ├── └── ├── ├── ├── ├── ├── getitem.py
├── ├── └── ├── ├── ├── ├── ├── groupby.py
├── ├── └── ├── ├── ├── ├── ├── index.py
├── ├── └── ├── ├── ├── ├── ├── interface.py
├── ├── └── ├── ├── ├── ├── ├── io.py
├── ├── └── ├── ├── ├── ├── ├── methods.py
├── ├── └── ├── ├── ├── ├── ├── missing.py
├── ├── └── ├── ├── ├── ├── ├── ops.py
├── ├── └── ├── ├── ├── ├── ├── printing.py
├── ├── └── ├── ├── ├── ├── ├── reduce.py
├── ├── └── ├── ├── ├── ├── ├── reshaping.py
├── ├── └── ├── ├── ├── ├── └── setitem.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── date/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── array.py
├── ├── └── ├── ├── ├── ├── decimal/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── array.py
├── ├── └── ├── ├── ├── ├── └── test_decimal.py
├── ├── └── ├── ├── ├── ├── json/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── array.py
├── ├── └── ├── ├── ├── ├── └── test_json.py
├── ├── └── ├── ├── ├── ├── list/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── array.py
├── ├── └── ├── ├── ├── ├── └── test_list.py
├── ├── └── ├── ├── ├── ├── test_arrow.py
├── ├── └── ├── ├── ├── ├── test_categorical.py
├── ├── └── ├── ├── ├── ├── test_common.py
├── ├── └── ├── ├── ├── ├── test_datetime.py
├── ├── └── ├── ├── ├── ├── test_extension.py
├── ├── └── ├── ├── ├── ├── test_interval.py
├── ├── └── ├── ├── ├── ├── test_masked.py
├── ├── └── ├── ├── ├── ├── test_numpy.py
├── ├── └── ├── ├── ├── ├── test_period.py
├── ├── └── ├── ├── ├── ├── test_sparse.py
├── ├── └── ├── ├── ├── └── test_string.py
├── ├── └── ├── ├── ├── frame/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── constructors/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_from_dict.py
├── ├── └── ├── ├── ├── ├── └── test_from_records.py
├── ├── └── ├── ├── ├── ├── indexing/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_coercion.py
├── ├── └── ├── ├── ├── ├── ├── test_delitem.py
├── ├── └── ├── ├── ├── ├── ├── test_get.py
├── ├── └── ├── ├── ├── ├── ├── test_get_value.py
├── ├── └── ├── ├── ├── ├── ├── test_getitem.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_insert.py
├── ├── └── ├── ├── ├── ├── ├── test_mask.py
├── ├── └── ├── ├── ├── ├── ├── test_set_value.py
├── ├── └── ├── ├── ├── ├── ├── test_setitem.py
├── ├── └── ├── ├── ├── ├── ├── test_take.py
├── ├── └── ├── ├── ├── ├── ├── test_where.py
├── ├── └── ├── ├── ├── ├── └── test_xs.py
├── ├── └── ├── ├── ├── ├── methods/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_add_prefix_suffix.py
├── ├── └── ├── ├── ├── ├── ├── test_align.py
├── ├── └── ├── ├── ├── ├── ├── test_asfreq.py
├── ├── └── ├── ├── ├── ├── ├── test_asof.py
├── ├── └── ├── ├── ├── ├── ├── test_assign.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_at_time.py
├── ├── └── ├── ├── ├── ├── ├── test_between_time.py
├── ├── └── ├── ├── ├── ├── ├── test_clip.py
├── ├── └── ├── ├── ├── ├── ├── test_combine.py
├── ├── └── ├── ├── ├── ├── ├── test_combine_first.py
├── ├── └── ├── ├── ├── ├── ├── test_compare.py
├── ├── └── ├── ├── ├── ├── ├── test_convert_dtypes.py
├── ├── └── ├── ├── ├── ├── ├── test_copy.py
├── ├── └── ├── ├── ├── ├── ├── test_count.py
├── ├── └── ├── ├── ├── ├── ├── test_cov_corr.py
├── ├── └── ├── ├── ├── ├── ├── test_describe.py
├── ├── └── ├── ├── ├── ├── ├── test_diff.py
├── ├── └── ├── ├── ├── ├── ├── test_dot.py
├── ├── └── ├── ├── ├── ├── ├── test_drop.py
├── ├── └── ├── ├── ├── ├── ├── test_drop_duplicates.py
├── ├── └── ├── ├── ├── ├── ├── test_droplevel.py
├── ├── └── ├── ├── ├── ├── ├── test_dropna.py
├── ├── └── ├── ├── ├── ├── ├── test_dtypes.py
├── ├── └── ├── ├── ├── ├── ├── test_duplicated.py
├── ├── └── ├── ├── ├── ├── ├── test_equals.py
├── ├── └── ├── ├── ├── ├── ├── test_explode.py
├── ├── └── ├── ├── ├── ├── ├── test_fillna.py
├── ├── └── ├── ├── ├── ├── ├── test_filter.py
├── ├── └── ├── ├── ├── ├── ├── test_first_and_last.py
├── ├── └── ├── ├── ├── ├── ├── test_first_valid_index.py
├── ├── └── ├── ├── ├── ├── ├── test_get_numeric_data.py
├── ├── └── ├── ├── ├── ├── ├── test_head_tail.py
├── ├── └── ├── ├── ├── ├── ├── test_infer_objects.py
├── ├── └── ├── ├── ├── ├── ├── test_info.py
├── ├── └── ├── ├── ├── ├── ├── test_interpolate.py
├── ├── └── ├── ├── ├── ├── ├── test_is_homogeneous_dtype.py
├── ├── └── ├── ├── ├── ├── ├── test_isetitem.py
├── ├── └── ├── ├── ├── ├── ├── test_isin.py
├── ├── └── ├── ├── ├── ├── ├── test_iterrows.py
├── ├── └── ├── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── ├── test_map.py
├── ├── └── ├── ├── ├── ├── ├── test_matmul.py
├── ├── └── ├── ├── ├── ├── ├── test_nlargest.py
├── ├── └── ├── ├── ├── ├── ├── test_pct_change.py
├── ├── └── ├── ├── ├── ├── ├── test_pipe.py
├── ├── └── ├── ├── ├── ├── ├── test_pop.py
├── ├── └── ├── ├── ├── ├── ├── test_quantile.py
├── ├── └── ├── ├── ├── ├── ├── test_rank.py
├── ├── └── ├── ├── ├── ├── ├── test_reindex.py
├── ├── └── ├── ├── ├── ├── ├── test_reindex_like.py
├── ├── └── ├── ├── ├── ├── ├── test_rename.py
├── ├── └── ├── ├── ├── ├── ├── test_rename_axis.py
├── ├── └── ├── ├── ├── ├── ├── test_reorder_levels.py
├── ├── └── ├── ├── ├── ├── ├── test_replace.py
├── ├── └── ├── ├── ├── ├── ├── test_reset_index.py
├── ├── └── ├── ├── ├── ├── ├── test_round.py
├── ├── └── ├── ├── ├── ├── ├── test_sample.py
├── ├── └── ├── ├── ├── ├── ├── test_select_dtypes.py
├── ├── └── ├── ├── ├── ├── ├── test_set_axis.py
├── ├── └── ├── ├── ├── ├── ├── test_set_index.py
├── ├── └── ├── ├── ├── ├── ├── test_shift.py
├── ├── └── ├── ├── ├── ├── ├── test_size.py
├── ├── └── ├── ├── ├── ├── ├── test_sort_index.py
├── ├── └── ├── ├── ├── ├── ├── test_sort_values.py
├── ├── └── ├── ├── ├── ├── ├── test_swapaxes.py
├── ├── └── ├── ├── ├── ├── ├── test_swaplevel.py
├── ├── └── ├── ├── ├── ├── ├── test_to_csv.py
├── ├── └── ├── ├── ├── ├── ├── test_to_dict.py
├── ├── └── ├── ├── ├── ├── ├── test_to_dict_of_blocks.py
├── ├── └── ├── ├── ├── ├── ├── test_to_numpy.py
├── ├── └── ├── ├── ├── ├── ├── test_to_period.py
├── ├── └── ├── ├── ├── ├── ├── test_to_records.py
├── ├── └── ├── ├── ├── ├── ├── test_to_timestamp.py
├── ├── └── ├── ├── ├── ├── ├── test_transpose.py
├── ├── └── ├── ├── ├── ├── ├── test_truncate.py
├── ├── └── ├── ├── ├── ├── ├── test_tz_convert.py
├── ├── └── ├── ├── ├── ├── ├── test_tz_localize.py
├── ├── └── ├── ├── ├── ├── ├── test_update.py
├── ├── └── ├── ├── ├── ├── ├── test_value_counts.py
├── ├── └── ├── ├── ├── ├── └── test_values.py
├── ├── └── ├── ├── ├── ├── test_alter_axes.py
├── ├── └── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── test_arrow_interface.py
├── ├── └── ├── ├── ├── ├── test_block_internals.py
├── ├── └── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── test_cumulative.py
├── ├── └── ├── ├── ├── ├── test_iteration.py
├── ├── └── ├── ├── ├── ├── test_logical_ops.py
├── ├── └── ├── ├── ├── ├── test_nonunique_indexes.py
├── ├── └── ├── ├── ├── ├── test_npfuncs.py
├── ├── └── ├── ├── ├── ├── test_query_eval.py
├── ├── └── ├── ├── ├── ├── test_reductions.py
├── ├── └── ├── ├── ├── ├── test_repr.py
├── ├── └── ├── ├── ├── ├── test_stack_unstack.py
├── ├── └── ├── ├── ├── ├── test_subclass.py
├── ├── └── ├── ├── ├── ├── test_ufunc.py
├── ├── └── ├── ├── ├── ├── test_unary.py
├── ├── └── ├── ├── ├── └── test_validate.py
├── ├── └── ├── ├── ├── generic/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_duplicate_labels.py
├── ├── └── ├── ├── ├── ├── test_finalize.py
├── ├── └── ├── ├── ├── ├── test_frame.py
├── ├── └── ├── ├── ├── ├── test_generic.py
├── ├── └── ├── ├── ├── ├── test_label_or_level_utils.py
├── ├── └── ├── ├── ├── ├── test_series.py
├── ├── └── ├── ├── ├── └── test_to_xarray.py
├── ├── └── ├── ├── ├── groupby/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── aggregate/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_aggregate.py
├── ├── └── ├── ├── ├── ├── ├── test_cython.py
├── ├── └── ├── ├── ├── ├── ├── test_numba.py
├── ├── └── ├── ├── ├── ├── └── test_other.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── methods/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_corrwith.py
├── ├── └── ├── ├── ├── ├── ├── test_describe.py
├── ├── └── ├── ├── ├── ├── ├── test_groupby_shift_diff.py
├── ├── └── ├── ├── ├── ├── ├── test_is_monotonic.py
├── ├── └── ├── ├── ├── ├── ├── test_nlargest_nsmallest.py
├── ├── └── ├── ├── ├── ├── ├── test_nth.py
├── ├── └── ├── ├── ├── ├── ├── test_quantile.py
├── ├── └── ├── ├── ├── ├── ├── test_rank.py
├── ├── └── ├── ├── ├── ├── ├── test_sample.py
├── ├── └── ├── ├── ├── ├── ├── test_size.py
├── ├── └── ├── ├── ├── ├── ├── test_skew.py
├── ├── └── ├── ├── ├── ├── └── test_value_counts.py
├── ├── └── ├── ├── ├── ├── test_all_methods.py
├── ├── └── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── ├── test_apply.py
├── ├── └── ├── ├── ├── ├── test_apply_mutate.py
├── ├── └── ├── ├── ├── ├── test_bin_groupby.py
├── ├── └── ├── ├── ├── ├── test_categorical.py
├── ├── └── ├── ├── ├── ├── test_counting.py
├── ├── └── ├── ├── ├── ├── test_cumulative.py
├── ├── └── ├── ├── ├── ├── test_filters.py
├── ├── └── ├── ├── ├── ├── test_groupby.py
├── ├── └── ├── ├── ├── ├── test_groupby_dropna.py
├── ├── └── ├── ├── ├── ├── test_groupby_subclass.py
├── ├── └── ├── ├── ├── ├── test_grouping.py
├── ├── └── ├── ├── ├── ├── test_index_as_string.py
├── ├── └── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── test_libgroupby.py
├── ├── └── ├── ├── ├── ├── test_missing.py
├── ├── └── ├── ├── ├── ├── test_numba.py
├── ├── └── ├── ├── ├── ├── test_numeric_only.py
├── ├── └── ├── ├── ├── ├── test_pipe.py
├── ├── └── ├── ├── ├── ├── test_raises.py
├── ├── └── ├── ├── ├── ├── test_reductions.py
├── ├── └── ├── ├── ├── ├── test_timegrouper.py
├── ├── └── ├── ├── ├── └── transform/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── test_numba.py
├── ├── └── ├── ├── ├── └── └── test_transform.py
├── ├── └── ├── ├── ├── indexes/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── base_class/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_pickle.py
├── ├── └── ├── ├── ├── ├── ├── test_reshape.py
├── ├── └── ├── ├── ├── ├── ├── test_setops.py
├── ├── └── ├── ├── ├── ├── └── test_where.py
├── ├── └── ├── ├── ├── ├── categorical/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_append.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_category.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_equals.py
├── ├── └── ├── ├── ├── ├── ├── test_fillna.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_map.py
├── ├── └── ├── ├── ├── ├── ├── test_reindex.py
├── ├── └── ├── ├── ├── ├── └── test_setops.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── datetimelike_/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_drop_duplicates.py
├── ├── └── ├── ├── ├── ├── ├── test_equals.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_is_monotonic.py
├── ├── └── ├── ├── ├── ├── ├── test_nat.py
├── ├── └── ├── ├── ├── ├── ├── test_sort_values.py
├── ├── └── ├── ├── ├── ├── └── test_value_counts.py
├── ├── └── ├── ├── ├── ├── datetimes/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── methods/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_asof.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_delete.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_factorize.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_fillna.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_insert.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_isocalendar.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_map.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_normalize.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_repeat.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_resolution.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_round.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_shift.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_snap.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_to_frame.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_to_julian_date.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_to_period.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_to_pydatetime.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_to_series.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_tz_convert.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_tz_localize.py
├── ├── └── ├── ├── ├── ├── ├── └── test_unique.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_date_range.py
├── ├── └── ├── ├── ├── ├── ├── test_datetime.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── ├── test_freq_attr.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_iter.py
├── ├── └── ├── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── ├── test_npfuncs.py
├── ├── └── ├── ├── ├── ├── ├── test_ops.py
├── ├── └── ├── ├── ├── ├── ├── test_partial_slicing.py
├── ├── └── ├── ├── ├── ├── ├── test_pickle.py
├── ├── └── ├── ├── ├── ├── ├── test_reindex.py
├── ├── └── ├── ├── ├── ├── ├── test_scalar_compat.py
├── ├── └── ├── ├── ├── ├── ├── test_setops.py
├── ├── └── ├── ├── ├── ├── └── test_timezones.py
├── ├── └── ├── ├── ├── ├── interval/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_equals.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_interval.py
├── ├── └── ├── ├── ├── ├── ├── test_interval_range.py
├── ├── └── ├── ├── ├── ├── ├── test_interval_tree.py
├── ├── └── ├── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── ├── test_pickle.py
├── ├── └── ├── ├── ├── ├── └── test_setops.py
├── ├── └── ├── ├── ├── ├── multi/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── ├── test_analytics.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_compat.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_conversion.py
├── ├── └── ├── ├── ├── ├── ├── test_copy.py
├── ├── └── ├── ├── ├── ├── ├── test_drop.py
├── ├── └── ├── ├── ├── ├── ├── test_duplicates.py
├── ├── └── ├── ├── ├── ├── ├── test_equivalence.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── ├── test_get_level_values.py
├── ├── └── ├── ├── ├── ├── ├── test_get_set.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_integrity.py
├── ├── └── ├── ├── ├── ├── ├── test_isin.py
├── ├── └── ├── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── ├── test_lexsort.py
├── ├── └── ├── ├── ├── ├── ├── test_missing.py
├── ├── └── ├── ├── ├── ├── ├── test_monotonic.py
├── ├── └── ├── ├── ├── ├── ├── test_names.py
├── ├── └── ├── ├── ├── ├── ├── test_partial_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_pickle.py
├── ├── └── ├── ├── ├── ├── ├── test_reindex.py
├── ├── └── ├── ├── ├── ├── ├── test_reshape.py
├── ├── └── ├── ├── ├── ├── ├── test_setops.py
├── ├── └── ├── ├── ├── ├── ├── test_sorting.py
├── ├── └── ├── ├── ├── ├── └── test_take.py
├── ├── └── ├── ├── ├── ├── numeric/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── ├── test_numeric.py
├── ├── └── ├── ├── ├── ├── └── test_setops.py
├── ├── └── ├── ├── ├── ├── object/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── └── test_indexing.py
├── ├── └── ├── ├── ├── ├── period/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── methods/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_asfreq.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_factorize.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_fillna.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_insert.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_is_full.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_repeat.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_shift.py
├── ├── └── ├── ├── ├── ├── ├── └── test_to_timestamp.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── ├── test_freq_attr.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── ├── test_monotonic.py
├── ├── └── ├── ├── ├── ├── ├── test_partial_slicing.py
├── ├── └── ├── ├── ├── ├── ├── test_period.py
├── ├── └── ├── ├── ├── ├── ├── test_period_range.py
├── ├── └── ├── ├── ├── ├── ├── test_pickle.py
├── ├── └── ├── ├── ├── ├── ├── test_resolution.py
├── ├── └── ├── ├── ├── ├── ├── test_scalar_compat.py
├── ├── └── ├── ├── ├── ├── ├── test_searchsorted.py
├── ├── └── ├── ├── ├── ├── ├── test_setops.py
├── ├── └── ├── ├── ├── ├── └── test_tools.py
├── ├── └── ├── ├── ├── ├── ranges/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── ├── test_range.py
├── ├── └── ├── ├── ├── ├── └── test_setops.py
├── ├── └── ├── ├── ├── ├── string/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── └── test_indexing.py
├── ├── └── ├── ├── ├── ├── test_any_index.py
├── ├── └── ├── ├── ├── ├── test_base.py
├── ├── └── ├── ├── ├── ├── test_common.py
├── ├── └── ├── ├── ├── ├── test_datetimelike.py
├── ├── └── ├── ├── ├── ├── test_engines.py
├── ├── └── ├── ├── ├── ├── test_frozen.py
├── ├── └── ├── ├── ├── ├── test_index_new.py
├── ├── └── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── test_numpy_compat.py
├── ├── └── ├── ├── ├── ├── test_old_base.py
├── ├── └── ├── ├── ├── ├── test_setops.py
├── ├── └── ├── ├── ├── ├── test_subclass.py
├── ├── └── ├── ├── ├── └── timedeltas/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── methods/
├── ├── └── ├── ├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── └── ├── ├── test_factorize.py
├── ├── └── ├── ├── ├── └── ├── ├── test_fillna.py
├── ├── └── ├── ├── ├── └── ├── ├── test_insert.py
├── ├── └── ├── ├── ├── └── ├── ├── test_repeat.py
├── ├── └── ├── ├── ├── └── ├── └── test_shift.py
├── ├── └── ├── ├── ├── └── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── └── ├── test_constructors.py
├── ├── └── ├── ├── ├── └── ├── test_delete.py
├── ├── └── ├── ├── ├── └── ├── test_formats.py
├── ├── └── ├── ├── ├── └── ├── test_freq_attr.py
├── ├── └── ├── ├── ├── └── ├── test_indexing.py
├── ├── └── ├── ├── ├── └── ├── test_join.py
├── ├── └── ├── ├── ├── └── ├── test_ops.py
├── ├── └── ├── ├── ├── └── ├── test_pickle.py
├── ├── └── ├── ├── ├── └── ├── test_scalar_compat.py
├── ├── └── ├── ├── ├── └── ├── test_searchsorted.py
├── ├── └── ├── ├── ├── └── ├── test_setops.py
├── ├── └── ├── ├── ├── └── ├── test_timedelta.py
├── ├── └── ├── ├── ├── └── └── test_timedelta_range.py
├── ├── └── ├── ├── ├── indexing/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── interval/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_interval.py
├── ├── └── ├── ├── ├── ├── └── test_interval_new.py
├── ├── └── ├── ├── ├── ├── multiindex/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_chaining_and_caching.py
├── ├── └── ├── ├── ├── ├── ├── test_datetime.py
├── ├── └── ├── ├── ├── ├── ├── test_getitem.py
├── ├── └── ├── ├── ├── ├── ├── test_iloc.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing_slow.py
├── ├── └── ├── ├── ├── ├── ├── test_loc.py
├── ├── └── ├── ├── ├── ├── ├── test_multiindex.py
├── ├── └── ├── ├── ├── ├── ├── test_partial.py
├── ├── └── ├── ├── ├── ├── ├── test_setitem.py
├── ├── └── ├── ├── ├── ├── ├── test_slice.py
├── ├── └── ├── ├── ├── ├── └── test_sorted.py
├── ├── └── ├── ├── ├── ├── test_at.py
├── ├── └── ├── ├── ├── ├── test_categorical.py
├── ├── └── ├── ├── ├── ├── test_chaining_and_caching.py
├── ├── └── ├── ├── ├── ├── test_check_indexer.py
├── ├── └── ├── ├── ├── ├── test_coercion.py
├── ├── └── ├── ├── ├── ├── test_datetime.py
├── ├── └── ├── ├── ├── ├── test_floats.py
├── ├── └── ├── ├── ├── ├── test_iat.py
├── ├── └── ├── ├── ├── ├── test_iloc.py
├── ├── └── ├── ├── ├── ├── test_indexers.py
├── ├── └── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── test_loc.py
├── ├── └── ├── ├── ├── ├── test_na_indexing.py
├── ├── └── ├── ├── ├── ├── test_partial.py
├── ├── └── ├── ├── ├── └── test_scalar.py
├── ├── └── ├── ├── ├── interchange/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_impl.py
├── ├── └── ├── ├── ├── ├── test_spec_conformance.py
├── ├── └── ├── ├── ├── └── test_utils.py
├── ├── └── ├── ├── ├── internals/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── ├── test_internals.py
├── ├── └── ├── ├── ├── └── test_managers.py
├── ├── └── ├── ├── ├── io/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── excel/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_odf.py
├── ├── └── ├── ├── ├── ├── ├── test_odswriter.py
├── ├── └── ├── ├── ├── ├── ├── test_openpyxl.py
├── ├── └── ├── ├── ├── ├── ├── test_readers.py
├── ├── └── ├── ├── ├── ├── ├── test_style.py
├── ├── └── ├── ├── ├── ├── ├── test_writers.py
├── ├── └── ├── ├── ├── ├── ├── test_xlrd.py
├── ├── └── ├── ├── ├── ├── └── test_xlsxwriter.py
├── ├── └── ├── ├── ├── ├── formats/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── style/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_bar.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_exceptions.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_format.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_highlight.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_html.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_matplotlib.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_non_unique.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_style.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_to_latex.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_to_string.py
├── ├── └── ├── ├── ├── ├── ├── └── test_tooltip.py
├── ├── └── ├── ├── ├── ├── ├── test_console.py
├── ├── └── ├── ├── ├── ├── ├── test_css.py
├── ├── └── ├── ├── ├── ├── ├── test_eng_formatting.py
├── ├── └── ├── ├── ├── ├── ├── test_format.py
├── ├── └── ├── ├── ├── ├── ├── test_ipython_compat.py
├── ├── └── ├── ├── ├── ├── ├── test_printing.py
├── ├── └── ├── ├── ├── ├── ├── test_to_csv.py
├── ├── └── ├── ├── ├── ├── ├── test_to_excel.py
├── ├── └── ├── ├── ├── ├── ├── test_to_html.py
├── ├── └── ├── ├── ├── ├── ├── test_to_latex.py
├── ├── └── ├── ├── ├── ├── ├── test_to_markdown.py
├── ├── └── ├── ├── ├── ├── └── test_to_string.py
├── ├── └── ├── ├── ├── ├── generate_legacy_storage_files.py
├── ├── └── ├── ├── ├── ├── json/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── ├── test_compression.py
├── ├── └── ├── ├── ├── ├── ├── test_deprecated_kwargs.py
├── ├── └── ├── ├── ├── ├── ├── test_json_table_schema.py
├── ├── └── ├── ├── ├── ├── ├── test_json_table_schema_ext_dtype.py
├── ├── └── ├── ├── ├── ├── ├── test_normalize.py
├── ├── └── ├── ├── ├── ├── ├── test_pandas.py
├── ├── └── ├── ├── ├── ├── ├── test_readlines.py
├── ├── └── ├── ├── ├── ├── └── test_ujson.py
├── ├── └── ├── ├── ├── ├── parser/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── common/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_chunksize.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_common_basic.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_data_list.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_decimal.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_file_buffer_url.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_float.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_index.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_inf.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_ints.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_iterator.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_read_errors.py
├── ├── └── ├── ├── ├── ├── ├── └── test_verbose.py
├── ├── └── ├── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── ├── dtypes/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_categorical.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_dtypes_basic.py
├── ├── └── ├── ├── ├── ├── ├── └── test_empty.py
├── ├── └── ├── ├── ├── ├── ├── test_c_parser_only.py
├── ├── └── ├── ├── ├── ├── ├── test_comment.py
├── ├── └── ├── ├── ├── ├── ├── test_compression.py
├── ├── └── ├── ├── ├── ├── ├── test_concatenate_chunks.py
├── ├── └── ├── ├── ├── ├── ├── test_converters.py
├── ├── └── ├── ├── ├── ├── ├── test_dialect.py
├── ├── └── ├── ├── ├── ├── ├── test_encoding.py
├── ├── └── ├── ├── ├── ├── ├── test_header.py
├── ├── └── ├── ├── ├── ├── ├── test_index_col.py
├── ├── └── ├── ├── ├── ├── ├── test_mangle_dupes.py
├── ├── └── ├── ├── ├── ├── ├── test_multi_thread.py
├── ├── └── ├── ├── ├── ├── ├── test_na_values.py
├── ├── └── ├── ├── ├── ├── ├── test_network.py
├── ├── └── ├── ├── ├── ├── ├── test_parse_dates.py
├── ├── └── ├── ├── ├── ├── ├── test_python_parser_only.py
├── ├── └── ├── ├── ├── ├── ├── test_quoting.py
├── ├── └── ├── ├── ├── ├── ├── test_read_fwf.py
├── ├── └── ├── ├── ├── ├── ├── test_skiprows.py
├── ├── └── ├── ├── ├── ├── ├── test_textreader.py
├── ├── └── ├── ├── ├── ├── ├── test_unsupported.py
├── ├── └── ├── ├── ├── ├── ├── test_upcast.py
├── ├── └── ├── ├── ├── ├── └── usecols/
├── ├── └── ├── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── ├── test_parse_dates.py
├── ├── └── ├── ├── ├── ├── └── ├── test_strings.py
├── ├── └── ├── ├── ├── ├── └── └── test_usecols_basic.py
├── ├── └── ├── ├── ├── ├── pytables/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── ├── test_append.py
├── ├── └── ├── ├── ├── ├── ├── test_categorical.py
├── ├── └── ├── ├── ├── ├── ├── test_compat.py
├── ├── └── ├── ├── ├── ├── ├── test_complex.py
├── ├── └── ├── ├── ├── ├── ├── test_errors.py
├── ├── └── ├── ├── ├── ├── ├── test_file_handling.py
├── ├── └── ├── ├── ├── ├── ├── test_keys.py
├── ├── └── ├── ├── ├── ├── ├── test_put.py
├── ├── └── ├── ├── ├── ├── ├── test_pytables_missing.py
├── ├── └── ├── ├── ├── ├── ├── test_read.py
├── ├── └── ├── ├── ├── ├── ├── test_retain_attributes.py
├── ├── └── ├── ├── ├── ├── ├── test_round_trip.py
├── ├── └── ├── ├── ├── ├── ├── test_select.py
├── ├── └── ├── ├── ├── ├── ├── test_store.py
├── ├── └── ├── ├── ├── ├── ├── test_subclass.py
├── ├── └── ├── ├── ├── ├── ├── test_time_series.py
├── ├── └── ├── ├── ├── ├── └── test_timezones.py
├── ├── └── ├── ├── ├── ├── sas/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_byteswap.py
├── ├── └── ├── ├── ├── ├── ├── test_sas.py
├── ├── └── ├── ├── ├── ├── ├── test_sas7bdat.py
├── ├── └── ├── ├── ├── ├── └── test_xport.py
├── ├── └── ├── ├── ├── ├── test_clipboard.py
├── ├── └── ├── ├── ├── ├── test_common.py
├── ├── └── ├── ├── ├── ├── test_compression.py
├── ├── └── ├── ├── ├── ├── test_feather.py
├── ├── └── ├── ├── ├── ├── test_fsspec.py
├── ├── └── ├── ├── ├── ├── test_gbq.py
├── ├── └── ├── ├── ├── ├── test_gcs.py
├── ├── └── ├── ├── ├── ├── test_html.py
├── ├── └── ├── ├── ├── ├── test_http_headers.py
├── ├── └── ├── ├── ├── ├── test_orc.py
├── ├── └── ├── ├── ├── ├── test_parquet.py
├── ├── └── ├── ├── ├── ├── test_pickle.py
├── ├── └── ├── ├── ├── ├── test_s3.py
├── ├── └── ├── ├── ├── ├── test_spss.py
├── ├── └── ├── ├── ├── ├── test_sql.py
├── ├── └── ├── ├── ├── ├── test_stata.py
├── ├── └── ├── ├── ├── └── xml/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── conftest.py
├── ├── └── ├── ├── ├── └── ├── test_to_xml.py
├── ├── └── ├── ├── ├── └── ├── test_xml.py
├── ├── └── ├── ├── ├── └── └── test_xml_dtypes.py
├── ├── └── ├── ├── ├── libs/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_hashtable.py
├── ├── └── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── test_lib.py
├── ├── └── ├── ├── ├── └── test_libalgos.py
├── ├── └── ├── ├── ├── plotting/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── common.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── frame/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_frame.py
├── ├── └── ├── ├── ├── ├── ├── test_frame_color.py
├── ├── └── ├── ├── ├── ├── ├── test_frame_groupby.py
├── ├── └── ├── ├── ├── ├── ├── test_frame_legend.py
├── ├── └── ├── ├── ├── ├── ├── test_frame_subplots.py
├── ├── └── ├── ├── ├── ├── └── test_hist_box_by.py
├── ├── └── ├── ├── ├── ├── test_backend.py
├── ├── └── ├── ├── ├── ├── test_boxplot_method.py
├── ├── └── ├── ├── ├── ├── test_common.py
├── ├── └── ├── ├── ├── ├── test_converter.py
├── ├── └── ├── ├── ├── ├── test_datetimelike.py
├── ├── └── ├── ├── ├── ├── test_groupby.py
├── ├── └── ├── ├── ├── ├── test_hist_method.py
├── ├── └── ├── ├── ├── ├── test_misc.py
├── ├── └── ├── ├── ├── ├── test_series.py
├── ├── └── ├── ├── ├── └── test_style.py
├── ├── └── ├── ├── ├── reductions/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_reductions.py
├── ├── └── ├── ├── ├── └── test_stat_reductions.py
├── ├── └── ├── ├── ├── resample/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── test_base.py
├── ├── └── ├── ├── ├── ├── test_datetime_index.py
├── ├── └── ├── ├── ├── ├── test_period_index.py
├── ├── └── ├── ├── ├── ├── test_resample_api.py
├── ├── └── ├── ├── ├── ├── test_resampler_grouper.py
├── ├── └── ├── ├── ├── ├── test_time_grouper.py
├── ├── └── ├── ├── ├── └── test_timedelta.py
├── ├── └── ├── ├── ├── reshape/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── concat/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── ├── test_append.py
├── ├── └── ├── ├── ├── ├── ├── test_append_common.py
├── ├── └── ├── ├── ├── ├── ├── test_categorical.py
├── ├── └── ├── ├── ├── ├── ├── test_concat.py
├── ├── └── ├── ├── ├── ├── ├── test_dataframe.py
├── ├── └── ├── ├── ├── ├── ├── test_datetimes.py
├── ├── └── ├── ├── ├── ├── ├── test_empty.py
├── ├── └── ├── ├── ├── ├── ├── test_index.py
├── ├── └── ├── ├── ├── ├── ├── test_invalid.py
├── ├── └── ├── ├── ├── ├── ├── test_series.py
├── ├── └── ├── ├── ├── ├── └── test_sort.py
├── ├── └── ├── ├── ├── ├── merge/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_join.py
├── ├── └── ├── ├── ├── ├── ├── test_merge.py
├── ├── └── ├── ├── ├── ├── ├── test_merge_asof.py
├── ├── └── ├── ├── ├── ├── ├── test_merge_cross.py
├── ├── └── ├── ├── ├── ├── ├── test_merge_index_as_string.py
├── ├── └── ├── ├── ├── ├── ├── test_merge_ordered.py
├── ├── └── ├── ├── ├── ├── └── test_multi.py
├── ├── └── ├── ├── ├── ├── test_crosstab.py
├── ├── └── ├── ├── ├── ├── test_cut.py
├── ├── └── ├── ├── ├── ├── test_from_dummies.py
├── ├── └── ├── ├── ├── ├── test_get_dummies.py
├── ├── └── ├── ├── ├── ├── test_melt.py
├── ├── └── ├── ├── ├── ├── test_pivot.py
├── ├── └── ├── ├── ├── ├── test_pivot_multilevel.py
├── ├── └── ├── ├── ├── ├── test_qcut.py
├── ├── └── ├── ├── ├── ├── test_union_categoricals.py
├── ├── └── ├── ├── ├── └── test_util.py
├── ├── └── ├── ├── ├── scalar/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── interval/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_contains.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── ├── test_interval.py
├── ├── └── ├── ├── ├── ├── └── test_overlaps.py
├── ├── └── ├── ├── ├── ├── period/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── ├── test_asfreq.py
├── ├── └── ├── ├── ├── ├── └── test_period.py
├── ├── └── ├── ├── ├── ├── test_na_scalar.py
├── ├── └── ├── ├── ├── ├── test_nat.py
├── ├── └── ├── ├── ├── ├── timedelta/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── methods/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── test_as_unit.py
├── ├── └── ├── ├── ├── ├── ├── └── test_round.py
├── ├── └── ├── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── └── test_timedelta.py
├── ├── └── ├── ├── ├── └── timestamp/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── methods/
├── ├── └── ├── ├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── ├── test_as_unit.py
├── ├── └── ├── ├── ├── └── ├── ├── test_normalize.py
├── ├── └── ├── ├── ├── └── ├── ├── test_replace.py
├── ├── └── ├── ├── ├── └── ├── ├── test_round.py
├── ├── └── ├── ├── ├── └── ├── ├── test_timestamp_method.py
├── ├── └── ├── ├── ├── └── ├── ├── test_to_julian_date.py
├── ├── └── ├── ├── ├── └── ├── ├── test_to_pydatetime.py
├── ├── └── ├── ├── ├── └── ├── ├── test_tz_convert.py
├── ├── └── ├── ├── ├── └── ├── └── test_tz_localize.py
├── ├── └── ├── ├── ├── └── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── └── ├── test_comparisons.py
├── ├── └── ├── ├── ├── └── ├── test_constructors.py
├── ├── └── ├── ├── ├── └── ├── test_formats.py
├── ├── └── ├── ├── ├── └── ├── test_timestamp.py
├── ├── └── ├── ├── ├── └── └── test_timezones.py
├── ├── └── ├── ├── ├── series/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── accessors/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_cat_accessor.py
├── ├── └── ├── ├── ├── ├── ├── test_dt_accessor.py
├── ├── └── ├── ├── ├── ├── ├── test_list_accessor.py
├── ├── └── ├── ├── ├── ├── ├── test_sparse_accessor.py
├── ├── └── ├── ├── ├── ├── ├── test_str_accessor.py
├── ├── └── ├── ├── ├── ├── └── test_struct_accessor.py
├── ├── └── ├── ├── ├── ├── indexing/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_datetime.py
├── ├── └── ├── ├── ├── ├── ├── test_delitem.py
├── ├── └── ├── ├── ├── ├── ├── test_get.py
├── ├── └── ├── ├── ├── ├── ├── test_getitem.py
├── ├── └── ├── ├── ├── ├── ├── test_indexing.py
├── ├── └── ├── ├── ├── ├── ├── test_mask.py
├── ├── └── ├── ├── ├── ├── ├── test_set_value.py
├── ├── └── ├── ├── ├── ├── ├── test_setitem.py
├── ├── └── ├── ├── ├── ├── ├── test_take.py
├── ├── └── ├── ├── ├── ├── ├── test_where.py
├── ├── └── ├── ├── ├── ├── └── test_xs.py
├── ├── └── ├── ├── ├── ├── methods/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_add_prefix_suffix.py
├── ├── └── ├── ├── ├── ├── ├── test_align.py
├── ├── └── ├── ├── ├── ├── ├── test_argsort.py
├── ├── └── ├── ├── ├── ├── ├── test_asof.py
├── ├── └── ├── ├── ├── ├── ├── test_astype.py
├── ├── └── ├── ├── ├── ├── ├── test_autocorr.py
├── ├── └── ├── ├── ├── ├── ├── test_between.py
├── ├── └── ├── ├── ├── ├── ├── test_case_when.py
├── ├── └── ├── ├── ├── ├── ├── test_clip.py
├── ├── └── ├── ├── ├── ├── ├── test_combine.py
├── ├── └── ├── ├── ├── ├── ├── test_combine_first.py
├── ├── └── ├── ├── ├── ├── ├── test_compare.py
├── ├── └── ├── ├── ├── ├── ├── test_convert_dtypes.py
├── ├── └── ├── ├── ├── ├── ├── test_copy.py
├── ├── └── ├── ├── ├── ├── ├── test_count.py
├── ├── └── ├── ├── ├── ├── ├── test_cov_corr.py
├── ├── └── ├── ├── ├── ├── ├── test_describe.py
├── ├── └── ├── ├── ├── ├── ├── test_diff.py
├── ├── └── ├── ├── ├── ├── ├── test_drop.py
├── ├── └── ├── ├── ├── ├── ├── test_drop_duplicates.py
├── ├── └── ├── ├── ├── ├── ├── test_dropna.py
├── ├── └── ├── ├── ├── ├── ├── test_dtypes.py
├── ├── └── ├── ├── ├── ├── ├── test_duplicated.py
├── ├── └── ├── ├── ├── ├── ├── test_equals.py
├── ├── └── ├── ├── ├── ├── ├── test_explode.py
├── ├── └── ├── ├── ├── ├── ├── test_fillna.py
├── ├── └── ├── ├── ├── ├── ├── test_get_numeric_data.py
├── ├── └── ├── ├── ├── ├── ├── test_head_tail.py
├── ├── └── ├── ├── ├── ├── ├── test_infer_objects.py
├── ├── └── ├── ├── ├── ├── ├── test_info.py
├── ├── └── ├── ├── ├── ├── ├── test_interpolate.py
├── ├── └── ├── ├── ├── ├── ├── test_is_monotonic.py
├── ├── └── ├── ├── ├── ├── ├── test_is_unique.py
├── ├── └── ├── ├── ├── ├── ├── test_isin.py
├── ├── └── ├── ├── ├── ├── ├── test_isna.py
├── ├── └── ├── ├── ├── ├── ├── test_item.py
├── ├── └── ├── ├── ├── ├── ├── test_map.py
├── ├── └── ├── ├── ├── ├── ├── test_matmul.py
├── ├── └── ├── ├── ├── ├── ├── test_nlargest.py
├── ├── └── ├── ├── ├── ├── ├── test_nunique.py
├── ├── └── ├── ├── ├── ├── ├── test_pct_change.py
├── ├── └── ├── ├── ├── ├── ├── test_pop.py
├── ├── └── ├── ├── ├── ├── ├── test_quantile.py
├── ├── └── ├── ├── ├── ├── ├── test_rank.py
├── ├── └── ├── ├── ├── ├── ├── test_reindex.py
├── ├── └── ├── ├── ├── ├── ├── test_reindex_like.py
├── ├── └── ├── ├── ├── ├── ├── test_rename.py
├── ├── └── ├── ├── ├── ├── ├── test_rename_axis.py
├── ├── └── ├── ├── ├── ├── ├── test_repeat.py
├── ├── └── ├── ├── ├── ├── ├── test_replace.py
├── ├── └── ├── ├── ├── ├── ├── test_reset_index.py
├── ├── └── ├── ├── ├── ├── ├── test_round.py
├── ├── └── ├── ├── ├── ├── ├── test_searchsorted.py
├── ├── └── ├── ├── ├── ├── ├── test_set_name.py
├── ├── └── ├── ├── ├── ├── ├── test_size.py
├── ├── └── ├── ├── ├── ├── ├── test_sort_index.py
├── ├── └── ├── ├── ├── ├── ├── test_sort_values.py
├── ├── └── ├── ├── ├── ├── ├── test_to_csv.py
├── ├── └── ├── ├── ├── ├── ├── test_to_dict.py
├── ├── └── ├── ├── ├── ├── ├── test_to_frame.py
├── ├── └── ├── ├── ├── ├── ├── test_to_numpy.py
├── ├── └── ├── ├── ├── ├── ├── test_tolist.py
├── ├── └── ├── ├── ├── ├── ├── test_truncate.py
├── ├── └── ├── ├── ├── ├── ├── test_tz_localize.py
├── ├── └── ├── ├── ├── ├── ├── test_unique.py
├── ├── └── ├── ├── ├── ├── ├── test_unstack.py
├── ├── └── ├── ├── ├── ├── ├── test_update.py
├── ├── └── ├── ├── ├── ├── ├── test_value_counts.py
├── ├── └── ├── ├── ├── ├── ├── test_values.py
├── ├── └── ├── ├── ├── ├── └── test_view.py
├── ├── └── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── ├── test_arithmetic.py
├── ├── └── ├── ├── ├── ├── test_constructors.py
├── ├── └── ├── ├── ├── ├── test_cumulative.py
├── ├── └── ├── ├── ├── ├── test_formats.py
├── ├── └── ├── ├── ├── ├── test_iteration.py
├── ├── └── ├── ├── ├── ├── test_logical_ops.py
├── ├── └── ├── ├── ├── ├── test_missing.py
├── ├── └── ├── ├── ├── ├── test_npfuncs.py
├── ├── └── ├── ├── ├── ├── test_reductions.py
├── ├── └── ├── ├── ├── ├── test_subclass.py
├── ├── └── ├── ├── ├── ├── test_ufunc.py
├── ├── └── ├── ├── ├── ├── test_unary.py
├── ├── └── ├── ├── ├── └── test_validate.py
├── ├── └── ├── ├── ├── strings/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── ├── test_case_justify.py
├── ├── └── ├── ├── ├── ├── test_cat.py
├── ├── └── ├── ├── ├── ├── test_extract.py
├── ├── └── ├── ├── ├── ├── test_find_replace.py
├── ├── └── ├── ├── ├── ├── test_get_dummies.py
├── ├── └── ├── ├── ├── ├── test_split_partition.py
├── ├── └── ├── ├── ├── ├── test_string_array.py
├── ├── └── ├── ├── ├── └── test_strings.py
├── ├── └── ├── ├── ├── test_aggregation.py
├── ├── └── ├── ├── ├── test_algos.py
├── ├── └── ├── ├── ├── test_common.py
├── ├── └── ├── ├── ├── test_downstream.py
├── ├── └── ├── ├── ├── test_errors.py
├── ├── └── ├── ├── ├── test_expressions.py
├── ├── └── ├── ├── ├── test_flags.py
├── ├── └── ├── ├── ├── test_multilevel.py
├── ├── └── ├── ├── ├── test_nanops.py
├── ├── └── ├── ├── ├── test_optional_dependency.py
├── ├── └── ├── ├── ├── test_register_accessor.py
├── ├── └── ├── ├── ├── test_sorting.py
├── ├── └── ├── ├── ├── test_take.py
├── ├── └── ├── ├── ├── tools/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_to_datetime.py
├── ├── └── ├── ├── ├── ├── test_to_numeric.py
├── ├── └── ├── ├── ├── ├── test_to_time.py
├── ├── └── ├── ├── ├── └── test_to_timedelta.py
├── ├── └── ├── ├── ├── tseries/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── frequencies/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_freq_code.py
├── ├── └── ├── ├── ├── ├── ├── test_frequencies.py
├── ├── └── ├── ├── ├── ├── └── test_inference.py
├── ├── └── ├── ├── ├── ├── holiday/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── test_calendar.py
├── ├── └── ├── ├── ├── ├── ├── test_federal.py
├── ├── └── ├── ├── ├── ├── ├── test_holiday.py
├── ├── └── ├── ├── ├── ├── └── test_observance.py
├── ├── └── ├── ├── ├── └── offsets/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── common.py
├── ├── └── ├── ├── ├── └── ├── test_business_day.py
├── ├── └── ├── ├── ├── └── ├── test_business_hour.py
├── ├── └── ├── ├── ├── └── ├── test_business_month.py
├── ├── └── ├── ├── ├── └── ├── test_business_quarter.py
├── ├── └── ├── ├── ├── └── ├── test_business_year.py
├── ├── └── ├── ├── ├── └── ├── test_common.py
├── ├── └── ├── ├── ├── └── ├── test_custom_business_day.py
├── ├── └── ├── ├── ├── └── ├── test_custom_business_hour.py
├── ├── └── ├── ├── ├── └── ├── test_custom_business_month.py
├── ├── └── ├── ├── ├── └── ├── test_dst.py
├── ├── └── ├── ├── ├── └── ├── test_easter.py
├── ├── └── ├── ├── ├── └── ├── test_fiscal.py
├── ├── └── ├── ├── ├── └── ├── test_index.py
├── ├── └── ├── ├── ├── └── ├── test_month.py
├── ├── └── ├── ├── ├── └── ├── test_offsets.py
├── ├── └── ├── ├── ├── └── ├── test_offsets_properties.py
├── ├── └── ├── ├── ├── └── ├── test_quarter.py
├── ├── └── ├── ├── ├── └── ├── test_ticks.py
├── ├── └── ├── ├── ├── └── ├── test_week.py
├── ├── └── ├── ├── ├── └── └── test_year.py
├── ├── └── ├── ├── ├── tslibs/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── test_api.py
├── ├── └── ├── ├── ├── ├── test_array_to_datetime.py
├── ├── └── ├── ├── ├── ├── test_ccalendar.py
├── ├── └── ├── ├── ├── ├── test_conversion.py
├── ├── └── ├── ├── ├── ├── test_fields.py
├── ├── └── ├── ├── ├── ├── test_libfrequencies.py
├── ├── └── ├── ├── ├── ├── test_liboffsets.py
├── ├── └── ├── ├── ├── ├── test_np_datetime.py
├── ├── └── ├── ├── ├── ├── test_npy_units.py
├── ├── └── ├── ├── ├── ├── test_parse_iso8601.py
├── ├── └── ├── ├── ├── ├── test_parsing.py
├── ├── └── ├── ├── ├── ├── test_period.py
├── ├── └── ├── ├── ├── ├── test_resolution.py
├── ├── └── ├── ├── ├── ├── test_strptime.py
├── ├── └── ├── ├── ├── ├── test_timedeltas.py
├── ├── └── ├── ├── ├── ├── test_timezones.py
├── ├── └── ├── ├── ├── ├── test_to_offset.py
├── ├── └── ├── ├── ├── └── test_tzconversion.py
├── ├── └── ├── ├── ├── util/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── conftest.py
├── ├── └── ├── ├── ├── ├── test_assert_almost_equal.py
├── ├── └── ├── ├── ├── ├── test_assert_attr_equal.py
├── ├── └── ├── ├── ├── ├── test_assert_categorical_equal.py
├── ├── └── ├── ├── ├── ├── test_assert_extension_array_equal.py
├── ├── └── ├── ├── ├── ├── test_assert_frame_equal.py
├── ├── └── ├── ├── ├── ├── test_assert_index_equal.py
├── ├── └── ├── ├── ├── ├── test_assert_interval_array_equal.py
├── ├── └── ├── ├── ├── ├── test_assert_numpy_array_equal.py
├── ├── └── ├── ├── ├── ├── test_assert_produces_warning.py
├── ├── └── ├── ├── ├── ├── test_assert_series_equal.py
├── ├── └── ├── ├── ├── ├── test_deprecate.py
├── ├── └── ├── ├── ├── ├── test_deprecate_kwarg.py
├── ├── └── ├── ├── ├── ├── test_deprecate_nonkeyword_arguments.py
├── ├── └── ├── ├── ├── ├── test_doc.py
├── ├── └── ├── ├── ├── ├── test_hashing.py
├── ├── └── ├── ├── ├── ├── test_numba.py
├── ├── └── ├── ├── ├── ├── test_rewrite_warning.py
├── ├── └── ├── ├── ├── ├── test_shares_memory.py
├── ├── └── ├── ├── ├── ├── test_show_versions.py
├── ├── └── ├── ├── ├── ├── test_util.py
├── ├── └── ├── ├── ├── ├── test_validate_args.py
├── ├── └── ├── ├── ├── ├── test_validate_args_and_kwargs.py
├── ├── └── ├── ├── ├── ├── test_validate_inclusive.py
├── ├── └── ├── ├── ├── └── test_validate_kwargs.py
├── ├── └── ├── ├── └── window/
├── ├── └── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── └── ├── conftest.py
├── ├── └── ├── ├── └── ├── moments/
├── ├── └── ├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── └── ├── ├── conftest.py
├── ├── └── ├── ├── └── ├── ├── test_moments_consistency_ewm.py
├── ├── └── ├── ├── └── ├── ├── test_moments_consistency_expanding.py
├── ├── └── ├── ├── └── ├── └── test_moments_consistency_rolling.py
├── ├── └── ├── ├── └── ├── test_api.py
├── ├── └── ├── ├── └── ├── test_apply.py
├── ├── └── ├── ├── └── ├── test_base_indexer.py
├── ├── └── ├── ├── └── ├── test_cython_aggregations.py
├── ├── └── ├── ├── └── ├── test_dtypes.py
├── ├── └── ├── ├── └── ├── test_ewm.py
├── ├── └── ├── ├── └── ├── test_expanding.py
├── ├── └── ├── ├── └── ├── test_groupby.py
├── ├── └── ├── ├── └── ├── test_numba.py
├── ├── └── ├── ├── └── ├── test_online.py
├── ├── └── ├── ├── └── ├── test_pairwise.py
├── ├── └── ├── ├── └── ├── test_rolling.py
├── ├── └── ├── ├── └── ├── test_rolling_functions.py
├── ├── └── ├── ├── └── ├── test_rolling_quantile.py
├── ├── └── ├── ├── └── ├── test_rolling_skew_kurt.py
├── ├── └── ├── ├── └── ├── test_timeseries_window.py
├── ├── └── ├── ├── └── └── test_win_type.py
├── ├── └── ├── ├── tseries/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── frequencies.py
├── ├── └── ├── ├── ├── holiday.py
├── ├── └── ├── ├── └── offsets.py
├── ├── └── ├── └── util/
├── ├── └── ├── └── ├── __init__.py
├── ├── └── ├── └── ├── _decorators.py
├── ├── └── ├── └── ├── _doctools.py
├── ├── └── ├── └── ├── _exceptions.py
├── ├── └── ├── └── ├── _print_versions.py
├── ├── └── ├── └── ├── _test_decorators.py
├── ├── └── ├── └── ├── _tester.py
├── ├── └── ├── └── ├── _validators.py
├── ├── └── ├── └── └── version/
├── ├── └── ├── └── └── └── __init__.py
├── ├── └── ├── pandas-2.3.1.dist-info/
├── ├── └── ├── ├── DELVEWHEEL
├── ├── └── ├── ├── entry_points.txt
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── REQUESTED
├── ├── └── ├── └── WHEEL
├── ├── └── ├── pandas.libs/
├── ├── └── ├── └── msvcp140-1a0962f2a91a74c6d7136a768987a591.dll
├── ├── └── ├── PIL/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── __main__.py
├── ├── └── ├── ├── _avif.cp312-win_amd64.pyd
├── ├── └── ├── ├── _avif.pyi
├── ├── └── ├── ├── _binary.py
├── ├── └── ├── ├── _deprecate.py
├── ├── └── ├── ├── _imaging.cp312-win_amd64.pyd
├── ├── └── ├── ├── _imaging.pyi
├── ├── └── ├── ├── _imagingcms.cp312-win_amd64.pyd
├── ├── └── ├── ├── _imagingcms.pyi
├── ├── └── ├── ├── _imagingft.cp312-win_amd64.pyd
├── ├── └── ├── ├── _imagingft.pyi
├── ├── └── ├── ├── _imagingmath.cp312-win_amd64.pyd
├── ├── └── ├── ├── _imagingmath.pyi
├── ├── └── ├── ├── _imagingmorph.cp312-win_amd64.pyd
├── ├── └── ├── ├── _imagingmorph.pyi
├── ├── └── ├── ├── _imagingtk.cp312-win_amd64.pyd
├── ├── └── ├── ├── _imagingtk.pyi
├── ├── └── ├── ├── _tkinter_finder.py
├── ├── └── ├── ├── _typing.py
├── ├── └── ├── ├── _util.py
├── ├── └── ├── ├── _version.py
├── ├── └── ├── ├── _webp.cp312-win_amd64.pyd
├── ├── └── ├── ├── _webp.pyi
├── ├── └── ├── ├── AvifImagePlugin.py
├── ├── └── ├── ├── BdfFontFile.py
├── ├── └── ├── ├── BlpImagePlugin.py
├── ├── └── ├── ├── BmpImagePlugin.py
├── ├── └── ├── ├── BufrStubImagePlugin.py
├── ├── └── ├── ├── ContainerIO.py
├── ├── └── ├── ├── CurImagePlugin.py
├── ├── └── ├── ├── DcxImagePlugin.py
├── ├── └── ├── ├── DdsImagePlugin.py
├── ├── └── ├── ├── EpsImagePlugin.py
├── ├── └── ├── ├── ExifTags.py
├── ├── └── ├── ├── features.py
├── ├── └── ├── ├── FitsImagePlugin.py
├── ├── └── ├── ├── FliImagePlugin.py
├── ├── └── ├── ├── FontFile.py
├── ├── └── ├── ├── FpxImagePlugin.py
├── ├── └── ├── ├── FtexImagePlugin.py
├── ├── └── ├── ├── GbrImagePlugin.py
├── ├── └── ├── ├── GdImageFile.py
├── ├── └── ├── ├── GifImagePlugin.py
├── ├── └── ├── ├── GimpGradientFile.py
├── ├── └── ├── ├── GimpPaletteFile.py
├── ├── └── ├── ├── GribStubImagePlugin.py
├── ├── └── ├── ├── Hdf5StubImagePlugin.py
├── ├── └── ├── ├── IcnsImagePlugin.py
├── ├── └── ├── ├── IcoImagePlugin.py
├── ├── └── ├── ├── Image.py
├── ├── └── ├── ├── ImageChops.py
├── ├── └── ├── ├── ImageCms.py
├── ├── └── ├── ├── ImageColor.py
├── ├── └── ├── ├── ImageDraw.py
├── ├── └── ├── ├── ImageDraw2.py
├── ├── └── ├── ├── ImageEnhance.py
├── ├── └── ├── ├── ImageFile.py
├── ├── └── ├── ├── ImageFilter.py
├── ├── └── ├── ├── ImageFont.py
├── ├── └── ├── ├── ImageGrab.py
├── ├── └── ├── ├── ImageMath.py
├── ├── └── ├── ├── ImageMode.py
├── ├── └── ├── ├── ImageMorph.py
├── ├── └── ├── ├── ImageOps.py
├── ├── └── ├── ├── ImagePalette.py
├── ├── └── ├── ├── ImagePath.py
├── ├── └── ├── ├── ImageQt.py
├── ├── └── ├── ├── ImageSequence.py
├── ├── └── ├── ├── ImageShow.py
├── ├── └── ├── ├── ImageStat.py
├── ├── └── ├── ├── ImageTk.py
├── ├── └── ├── ├── ImageTransform.py
├── ├── └── ├── ├── ImageWin.py
├── ├── └── ├── ├── ImImagePlugin.py
├── ├── └── ├── ├── ImtImagePlugin.py
├── ├── └── ├── ├── IptcImagePlugin.py
├── ├── └── ├── ├── Jpeg2KImagePlugin.py
├── ├── └── ├── ├── JpegImagePlugin.py
├── ├── └── ├── ├── JpegPresets.py
├── ├── └── ├── ├── McIdasImagePlugin.py
├── ├── └── ├── ├── MicImagePlugin.py
├── ├── └── ├── ├── MpegImagePlugin.py
├── ├── └── ├── ├── MpoImagePlugin.py
├── ├── └── ├── ├── MspImagePlugin.py
├── ├── └── ├── ├── PaletteFile.py
├── ├── └── ├── ├── PalmImagePlugin.py
├── ├── └── ├── ├── PcdImagePlugin.py
├── ├── └── ├── ├── PcfFontFile.py
├── ├── └── ├── ├── PcxImagePlugin.py
├── ├── └── ├── ├── PdfImagePlugin.py
├── ├── └── ├── ├── PdfParser.py
├── ├── └── ├── ├── PixarImagePlugin.py
├── ├── └── ├── ├── PngImagePlugin.py
├── ├── └── ├── ├── PpmImagePlugin.py
├── ├── └── ├── ├── PsdImagePlugin.py
├── ├── └── ├── ├── PSDraw.py
├── ├── └── ├── ├── py.typed
├── ├── └── ├── ├── QoiImagePlugin.py
├── ├── └── ├── ├── report.py
├── ├── └── ├── ├── SgiImagePlugin.py
├── ├── └── ├── ├── SpiderImagePlugin.py
├── ├── └── ├── ├── SunImagePlugin.py
├── ├── └── ├── ├── TarIO.py
├── ├── └── ├── ├── TgaImagePlugin.py
├── ├── └── ├── ├── TiffImagePlugin.py
├── ├── └── ├── ├── TiffTags.py
├── ├── └── ├── ├── WalImageFile.py
├── ├── └── ├── ├── WebPImagePlugin.py
├── ├── └── ├── ├── WmfImagePlugin.py
├── ├── └── ├── ├── XbmImagePlugin.py
├── ├── └── ├── ├── XpmImagePlugin.py
├── ├── └── ├── └── XVThumbImagePlugin.py
├── ├── └── ├── pillow-11.3.0.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── licenses/
├── ├── └── ├── ├── └── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── ├── WHEEL
├── ├── └── ├── └── zip-safe
├── ├── └── ├── pip/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── __main__.py
├── ├── └── ├── ├── __pip-runner__.py
├── ├── └── ├── ├── _internal/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── build_env.py
├── ├── └── ├── ├── ├── cache.py
├── ├── └── ├── ├── ├── cli/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── autocompletion.py
├── ├── └── ├── ├── ├── ├── base_command.py
├── ├── └── ├── ├── ├── ├── cmdoptions.py
├── ├── └── ├── ├── ├── ├── command_context.py
├── ├── └── ├── ├── ├── ├── index_command.py
├── ├── └── ├── ├── ├── ├── main.py
├── ├── └── ├── ├── ├── ├── main_parser.py
├── ├── └── ├── ├── ├── ├── parser.py
├── ├── └── ├── ├── ├── ├── progress_bars.py
├── ├── └── ├── ├── ├── ├── req_command.py
├── ├── └── ├── ├── ├── ├── spinners.py
├── ├── └── ├── ├── ├── └── status_codes.py
├── ├── └── ├── ├── ├── commands/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── cache.py
├── ├── └── ├── ├── ├── ├── check.py
├── ├── └── ├── ├── ├── ├── completion.py
├── ├── └── ├── ├── ├── ├── configuration.py
├── ├── └── ├── ├── ├── ├── debug.py
├── ├── └── ├── ├── ├── ├── download.py
├── ├── └── ├── ├── ├── ├── freeze.py
├── ├── └── ├── ├── ├── ├── hash.py
├── ├── └── ├── ├── ├── ├── help.py
├── ├── └── ├── ├── ├── ├── index.py
├── ├── └── ├── ├── ├── ├── inspect.py
├── ├── └── ├── ├── ├── ├── install.py
├── ├── └── ├── ├── ├── ├── list.py
├── ├── └── ├── ├── ├── ├── lock.py
├── ├── └── ├── ├── ├── ├── search.py
├── ├── └── ├── ├── ├── ├── show.py
├── ├── └── ├── ├── ├── ├── uninstall.py
├── ├── └── ├── ├── ├── └── wheel.py
├── ├── └── ├── ├── ├── configuration.py
├── ├── └── ├── ├── ├── distributions/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── installed.py
├── ├── └── ├── ├── ├── ├── sdist.py
├── ├── └── ├── ├── ├── └── wheel.py
├── ├── └── ├── ├── ├── exceptions.py
├── ├── └── ├── ├── ├── index/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── collector.py
├── ├── └── ├── ├── ├── ├── package_finder.py
├── ├── └── ├── ├── ├── └── sources.py
├── ├── └── ├── ├── ├── locations/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _distutils.py
├── ├── └── ├── ├── ├── ├── _sysconfig.py
├── ├── └── ├── ├── ├── └── base.py
├── ├── └── ├── ├── ├── main.py
├── ├── └── ├── ├── ├── metadata/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _json.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── importlib/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── _compat.py
├── ├── └── ├── ├── ├── ├── ├── _dists.py
├── ├── └── ├── ├── ├── ├── └── _envs.py
├── ├── └── ├── ├── ├── └── pkg_resources.py
├── ├── └── ├── ├── ├── models/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── candidate.py
├── ├── └── ├── ├── ├── ├── direct_url.py
├── ├── └── ├── ├── ├── ├── format_control.py
├── ├── └── ├── ├── ├── ├── index.py
├── ├── └── ├── ├── ├── ├── installation_report.py
├── ├── └── ├── ├── ├── ├── link.py
├── ├── └── ├── ├── ├── ├── pylock.py
├── ├── └── ├── ├── ├── ├── scheme.py
├── ├── └── ├── ├── ├── ├── search_scope.py
├── ├── └── ├── ├── ├── ├── selection_prefs.py
├── ├── └── ├── ├── ├── ├── target_python.py
├── ├── └── ├── ├── ├── └── wheel.py
├── ├── └── ├── ├── ├── network/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── auth.py
├── ├── └── ├── ├── ├── ├── cache.py
├── ├── └── ├── ├── ├── ├── download.py
├── ├── └── ├── ├── ├── ├── lazy_wheel.py
├── ├── └── ├── ├── ├── ├── session.py
├── ├── └── ├── ├── ├── ├── utils.py
├── ├── └── ├── ├── ├── └── xmlrpc.py
├── ├── └── ├── ├── ├── operations/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── build/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── build_tracker.py
├── ├── └── ├── ├── ├── ├── ├── metadata.py
├── ├── └── ├── ├── ├── ├── ├── metadata_editable.py
├── ├── └── ├── ├── ├── ├── ├── metadata_legacy.py
├── ├── └── ├── ├── ├── ├── ├── wheel.py
├── ├── └── ├── ├── ├── ├── ├── wheel_editable.py
├── ├── └── ├── ├── ├── ├── └── wheel_legacy.py
├── ├── └── ├── ├── ├── ├── check.py
├── ├── └── ├── ├── ├── ├── freeze.py
├── ├── └── ├── ├── ├── ├── install/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── editable_legacy.py
├── ├── └── ├── ├── ├── ├── └── wheel.py
├── ├── └── ├── ├── ├── └── prepare.py
├── ├── └── ├── ├── ├── pyproject.py
├── ├── └── ├── ├── ├── req/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── constructors.py
├── ├── └── ├── ├── ├── ├── req_dependency_group.py
├── ├── └── ├── ├── ├── ├── req_file.py
├── ├── └── ├── ├── ├── ├── req_install.py
├── ├── └── ├── ├── ├── ├── req_set.py
├── ├── └── ├── ├── ├── └── req_uninstall.py
├── ├── └── ├── ├── ├── resolution/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── base.py
├── ├── └── ├── ├── ├── ├── legacy/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── resolver.py
├── ├── └── ├── ├── ├── └── resolvelib/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── base.py
├── ├── └── ├── ├── ├── └── ├── candidates.py
├── ├── └── ├── ├── ├── └── ├── factory.py
├── ├── └── ├── ├── ├── └── ├── found_candidates.py
├── ├── └── ├── ├── ├── └── ├── provider.py
├── ├── └── ├── ├── ├── └── ├── reporter.py
├── ├── └── ├── ├── ├── └── ├── requirements.py
├── ├── └── ├── ├── ├── └── └── resolver.py
├── ├── └── ├── ├── ├── self_outdated_check.py
├── ├── └── ├── ├── ├── utils/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _jaraco_text.py
├── ├── └── ├── ├── ├── ├── _log.py
├── ├── └── ├── ├── ├── ├── appdirs.py
├── ├── └── ├── ├── ├── ├── compat.py
├── ├── └── ├── ├── ├── ├── compatibility_tags.py
├── ├── └── ├── ├── ├── ├── datetime.py
├── ├── └── ├── ├── ├── ├── deprecation.py
├── ├── └── ├── ├── ├── ├── direct_url_helpers.py
├── ├── └── ├── ├── ├── ├── egg_link.py
├── ├── └── ├── ├── ├── ├── entrypoints.py
├── ├── └── ├── ├── ├── ├── filesystem.py
├── ├── └── ├── ├── ├── ├── filetypes.py
├── ├── └── ├── ├── ├── ├── glibc.py
├── ├── └── ├── ├── ├── ├── hashes.py
├── ├── └── ├── ├── ├── ├── logging.py
├── ├── └── ├── ├── ├── ├── misc.py
├── ├── └── ├── ├── ├── ├── packaging.py
├── ├── └── ├── ├── ├── ├── retry.py
├── ├── └── ├── ├── ├── ├── setuptools_build.py
├── ├── └── ├── ├── ├── ├── subprocess.py
├── ├── └── ├── ├── ├── ├── temp_dir.py
├── ├── └── ├── ├── ├── ├── unpacking.py
├── ├── └── ├── ├── ├── ├── urls.py
├── ├── └── ├── ├── ├── ├── virtualenv.py
├── ├── └── ├── ├── ├── └── wheel.py
├── ├── └── ├── ├── ├── vcs/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── bazaar.py
├── ├── └── ├── ├── ├── ├── git.py
├── ├── └── ├── ├── ├── ├── mercurial.py
├── ├── └── ├── ├── ├── ├── subversion.py
├── ├── └── ├── ├── ├── └── versioncontrol.py
├── ├── └── ├── ├── └── wheel_builder.py
├── ├── └── ├── ├── _vendor/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── cachecontrol/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _cmd.py
├── ├── └── ├── ├── ├── ├── adapter.py
├── ├── └── ├── ├── ├── ├── cache.py
├── ├── └── ├── ├── ├── ├── caches/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── file_cache.py
├── ├── └── ├── ├── ├── ├── └── redis_cache.py
├── ├── └── ├── ├── ├── ├── controller.py
├── ├── └── ├── ├── ├── ├── filewrapper.py
├── ├── └── ├── ├── ├── ├── heuristics.py
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── ├── serialize.py
├── ├── └── ├── ├── ├── └── wrapper.py
├── ├── └── ├── ├── ├── certifi/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── cacert.pem
├── ├── └── ├── ├── ├── ├── core.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── dependency_groups/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── _implementation.py
├── ├── └── ├── ├── ├── ├── _lint_dependency_groups.py
├── ├── └── ├── ├── ├── ├── _pip_wrapper.py
├── ├── └── ├── ├── ├── ├── _toml_compat.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── distlib/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── compat.py
├── ├── └── ├── ├── ├── ├── resources.py
├── ├── └── ├── ├── ├── ├── scripts.py
├── ├── └── ├── ├── ├── ├── t32.exe
├── ├── └── ├── ├── ├── ├── t64-arm.exe
├── ├── └── ├── ├── ├── ├── t64.exe
├── ├── └── ├── ├── ├── ├── util.py
├── ├── └── ├── ├── ├── ├── w32.exe
├── ├── └── ├── ├── ├── ├── w64-arm.exe
├── ├── └── ├── ├── ├── └── w64.exe
├── ├── └── ├── ├── ├── distro/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── distro.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── idna/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── codec.py
├── ├── └── ├── ├── ├── ├── compat.py
├── ├── └── ├── ├── ├── ├── core.py
├── ├── └── ├── ├── ├── ├── idnadata.py
├── ├── └── ├── ├── ├── ├── intranges.py
├── ├── └── ├── ├── ├── ├── package_data.py
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── └── uts46data.py
├── ├── └── ├── ├── ├── msgpack/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── exceptions.py
├── ├── └── ├── ├── ├── ├── ext.py
├── ├── └── ├── ├── ├── └── fallback.py
├── ├── └── ├── ├── ├── packaging/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _elffile.py
├── ├── └── ├── ├── ├── ├── _manylinux.py
├── ├── └── ├── ├── ├── ├── _musllinux.py
├── ├── └── ├── ├── ├── ├── _parser.py
├── ├── └── ├── ├── ├── ├── _structures.py
├── ├── └── ├── ├── ├── ├── _tokenizer.py
├── ├── └── ├── ├── ├── ├── licenses/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── _spdx.py
├── ├── └── ├── ├── ├── ├── markers.py
├── ├── └── ├── ├── ├── ├── metadata.py
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── ├── requirements.py
├── ├── └── ├── ├── ├── ├── specifiers.py
├── ├── └── ├── ├── ├── ├── tags.py
├── ├── └── ├── ├── ├── ├── utils.py
├── ├── └── ├── ├── ├── └── version.py
├── ├── └── ├── ├── ├── pkg_resources/
├── ├── └── ├── ├── ├── └── __init__.py
├── ├── └── ├── ├── ├── platformdirs/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── android.py
├── ├── └── ├── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── ├── macos.py
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── ├── unix.py
├── ├── └── ├── ├── ├── ├── version.py
├── ├── └── ├── ├── ├── └── windows.py
├── ├── └── ├── ├── ├── pygments/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── console.py
├── ├── └── ├── ├── ├── ├── filter.py
├── ├── └── ├── ├── ├── ├── filters/
├── ├── └── ├── ├── ├── ├── └── __init__.py
├── ├── └── ├── ├── ├── ├── formatter.py
├── ├── └── ├── ├── ├── ├── formatters/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── _mapping.py
├── ├── └── ├── ├── ├── ├── lexer.py
├── ├── └── ├── ├── ├── ├── lexers/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── _mapping.py
├── ├── └── ├── ├── ├── ├── └── python.py
├── ├── └── ├── ├── ├── ├── modeline.py
├── ├── └── ├── ├── ├── ├── plugin.py
├── ├── └── ├── ├── ├── ├── regexopt.py
├── ├── └── ├── ├── ├── ├── scanner.py
├── ├── └── ├── ├── ├── ├── sphinxext.py
├── ├── └── ├── ├── ├── ├── style.py
├── ├── └── ├── ├── ├── ├── styles/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── _mapping.py
├── ├── └── ├── ├── ├── ├── token.py
├── ├── └── ├── ├── ├── ├── unistring.py
├── ├── └── ├── ├── ├── └── util.py
├── ├── └── ├── ├── ├── pyproject_hooks/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _impl.py
├── ├── └── ├── ├── ├── ├── _in_process/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── _in_process.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── requests/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __version__.py
├── ├── └── ├── ├── ├── ├── _internal_utils.py
├── ├── └── ├── ├── ├── ├── adapters.py
├── ├── └── ├── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── ├── auth.py
├── ├── └── ├── ├── ├── ├── certs.py
├── ├── └── ├── ├── ├── ├── compat.py
├── ├── └── ├── ├── ├── ├── cookies.py
├── ├── └── ├── ├── ├── ├── exceptions.py
├── ├── └── ├── ├── ├── ├── help.py
├── ├── └── ├── ├── ├── ├── hooks.py
├── ├── └── ├── ├── ├── ├── models.py
├── ├── └── ├── ├── ├── ├── packages.py
├── ├── └── ├── ├── ├── ├── sessions.py
├── ├── └── ├── ├── ├── ├── status_codes.py
├── ├── └── ├── ├── ├── ├── structures.py
├── ├── └── ├── ├── ├── └── utils.py
├── ├── └── ├── ├── ├── resolvelib/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── providers.py
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── ├── reporters.py
├── ├── └── ├── ├── ├── ├── resolvers/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── abstract.py
├── ├── └── ├── ├── ├── ├── ├── criterion.py
├── ├── └── ├── ├── ├── ├── ├── exceptions.py
├── ├── └── ├── ├── ├── ├── └── resolution.py
├── ├── └── ├── ├── ├── └── structs.py
├── ├── └── ├── ├── ├── rich/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── _cell_widths.py
├── ├── └── ├── ├── ├── ├── _emoji_codes.py
├── ├── └── ├── ├── ├── ├── _emoji_replace.py
├── ├── └── ├── ├── ├── ├── _export_format.py
├── ├── └── ├── ├── ├── ├── _extension.py
├── ├── └── ├── ├── ├── ├── _fileno.py
├── ├── └── ├── ├── ├── ├── _inspect.py
├── ├── └── ├── ├── ├── ├── _log_render.py
├── ├── └── ├── ├── ├── ├── _loop.py
├── ├── └── ├── ├── ├── ├── _null_file.py
├── ├── └── ├── ├── ├── ├── _palettes.py
├── ├── └── ├── ├── ├── ├── _pick.py
├── ├── └── ├── ├── ├── ├── _ratio.py
├── ├── └── ├── ├── ├── ├── _spinners.py
├── ├── └── ├── ├── ├── ├── _stack.py
├── ├── └── ├── ├── ├── ├── _timer.py
├── ├── └── ├── ├── ├── ├── _win32_console.py
├── ├── └── ├── ├── ├── ├── _windows.py
├── ├── └── ├── ├── ├── ├── _windows_renderer.py
├── ├── └── ├── ├── ├── ├── _wrap.py
├── ├── └── ├── ├── ├── ├── abc.py
├── ├── └── ├── ├── ├── ├── align.py
├── ├── └── ├── ├── ├── ├── ansi.py
├── ├── └── ├── ├── ├── ├── bar.py
├── ├── └── ├── ├── ├── ├── box.py
├── ├── └── ├── ├── ├── ├── cells.py
├── ├── └── ├── ├── ├── ├── color.py
├── ├── └── ├── ├── ├── ├── color_triplet.py
├── ├── └── ├── ├── ├── ├── columns.py
├── ├── └── ├── ├── ├── ├── console.py
├── ├── └── ├── ├── ├── ├── constrain.py
├── ├── └── ├── ├── ├── ├── containers.py
├── ├── └── ├── ├── ├── ├── control.py
├── ├── └── ├── ├── ├── ├── default_styles.py
├── ├── └── ├── ├── ├── ├── diagnose.py
├── ├── └── ├── ├── ├── ├── emoji.py
├── ├── └── ├── ├── ├── ├── errors.py
├── ├── └── ├── ├── ├── ├── file_proxy.py
├── ├── └── ├── ├── ├── ├── filesize.py
├── ├── └── ├── ├── ├── ├── highlighter.py
├── ├── └── ├── ├── ├── ├── json.py
├── ├── └── ├── ├── ├── ├── jupyter.py
├── ├── └── ├── ├── ├── ├── layout.py
├── ├── └── ├── ├── ├── ├── live.py
├── ├── └── ├── ├── ├── ├── live_render.py
├── ├── └── ├── ├── ├── ├── logging.py
├── ├── └── ├── ├── ├── ├── markup.py
├── ├── └── ├── ├── ├── ├── measure.py
├── ├── └── ├── ├── ├── ├── padding.py
├── ├── └── ├── ├── ├── ├── pager.py
├── ├── └── ├── ├── ├── ├── palette.py
├── ├── └── ├── ├── ├── ├── panel.py
├── ├── └── ├── ├── ├── ├── pretty.py
├── ├── └── ├── ├── ├── ├── progress.py
├── ├── └── ├── ├── ├── ├── progress_bar.py
├── ├── └── ├── ├── ├── ├── prompt.py
├── ├── └── ├── ├── ├── ├── protocol.py
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── ├── region.py
├── ├── └── ├── ├── ├── ├── repr.py
├── ├── └── ├── ├── ├── ├── rule.py
├── ├── └── ├── ├── ├── ├── scope.py
├── ├── └── ├── ├── ├── ├── screen.py
├── ├── └── ├── ├── ├── ├── segment.py
├── ├── └── ├── ├── ├── ├── spinner.py
├── ├── └── ├── ├── ├── ├── status.py
├── ├── └── ├── ├── ├── ├── style.py
├── ├── └── ├── ├── ├── ├── styled.py
├── ├── └── ├── ├── ├── ├── syntax.py
├── ├── └── ├── ├── ├── ├── table.py
├── ├── └── ├── ├── ├── ├── terminal_theme.py
├── ├── └── ├── ├── ├── ├── text.py
├── ├── └── ├── ├── ├── ├── theme.py
├── ├── └── ├── ├── ├── ├── themes.py
├── ├── └── ├── ├── ├── ├── traceback.py
├── ├── └── ├── ├── ├── └── tree.py
├── ├── └── ├── ├── ├── tomli/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _parser.py
├── ├── └── ├── ├── ├── ├── _re.py
├── ├── └── ├── ├── ├── ├── _types.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── tomli_w/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _writer.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── truststore/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _api.py
├── ├── └── ├── ├── ├── ├── _macos.py
├── ├── └── ├── ├── ├── ├── _openssl.py
├── ├── └── ├── ├── ├── ├── _ssl_constants.py
├── ├── └── ├── ├── ├── ├── _windows.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── urllib3/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _collections.py
├── ├── └── ├── ├── ├── ├── _version.py
├── ├── └── ├── ├── ├── ├── connection.py
├── ├── └── ├── ├── ├── ├── connectionpool.py
├── ├── └── ├── ├── ├── ├── contrib/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── _appengine_environ.py
├── ├── └── ├── ├── ├── ├── ├── _securetransport/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── bindings.py
├── ├── └── ├── ├── ├── ├── ├── └── low_level.py
├── ├── └── ├── ├── ├── ├── ├── appengine.py
├── ├── └── ├── ├── ├── ├── ├── ntlmpool.py
├── ├── └── ├── ├── ├── ├── ├── pyopenssl.py
├── ├── └── ├── ├── ├── ├── ├── securetransport.py
├── ├── └── ├── ├── ├── ├── └── socks.py
├── ├── └── ├── ├── ├── ├── exceptions.py
├── ├── └── ├── ├── ├── ├── fields.py
├── ├── └── ├── ├── ├── ├── filepost.py
├── ├── └── ├── ├── ├── ├── packages/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── backports/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── makefile.py
├── ├── └── ├── ├── ├── ├── ├── └── weakref_finalize.py
├── ├── └── ├── ├── ├── ├── └── six.py
├── ├── └── ├── ├── ├── ├── poolmanager.py
├── ├── └── ├── ├── ├── ├── request.py
├── ├── └── ├── ├── ├── ├── response.py
├── ├── └── ├── ├── ├── └── util/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── connection.py
├── ├── └── ├── ├── ├── └── ├── proxy.py
├── ├── └── ├── ├── ├── └── ├── queue.py
├── ├── └── ├── ├── ├── └── ├── request.py
├── ├── └── ├── ├── ├── └── ├── response.py
├── ├── └── ├── ├── ├── └── ├── retry.py
├── ├── └── ├── ├── ├── └── ├── ssl_.py
├── ├── └── ├── ├── ├── └── ├── ssl_match_hostname.py
├── ├── └── ├── ├── ├── └── ├── ssltransport.py
├── ├── └── ├── ├── ├── └── ├── timeout.py
├── ├── └── ├── ├── ├── └── ├── url.py
├── ├── └── ├── ├── ├── └── └── wait.py
├── ├── └── ├── ├── └── vendor.txt
├── ├── └── ├── └── py.typed
├── ├── └── ├── pip-25.2.dist-info/
├── ├── └── ├── ├── entry_points.txt
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── licenses/
├── ├── └── ├── ├── ├── AUTHORS.txt
├── ├── └── ├── ├── ├── LICENSE.txt
├── ├── └── ├── ├── └── src/
├── ├── └── ├── ├── └── └── pip/
├── ├── └── ├── ├── └── └── └── _vendor/
├── ├── └── ├── ├── └── └── └── ├── cachecontrol/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE.txt
├── ├── └── ├── ├── └── └── └── ├── certifi/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── dependency_groups/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE.txt
├── ├── └── ├── ├── └── └── └── ├── distlib/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE.txt
├── ├── └── ├── ├── └── └── └── ├── distro/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── idna/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE.md
├── ├── └── ├── ├── └── └── └── ├── msgpack/
├── ├── └── ├── ├── └── └── └── ├── └── COPYING
├── ├── └── ├── ├── └── └── └── ├── packaging/
├── ├── └── ├── ├── └── └── └── ├── ├── LICENSE
├── ├── └── ├── ├── └── └── └── ├── ├── LICENSE.APACHE
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE.BSD
├── ├── └── ├── ├── └── └── └── ├── pkg_resources/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── platformdirs/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── pygments/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── pyproject_hooks/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── requests/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── resolvelib/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── rich/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── tomli/
├── ├── └── ├── ├── └── └── └── ├── ├── LICENSE
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE-HEADER
├── ├── └── ├── ├── └── └── └── ├── tomli_w/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── ├── truststore/
├── ├── └── ├── ├── └── └── └── ├── └── LICENSE
├── ├── └── ├── ├── └── └── └── └── urllib3/
├── ├── └── ├── ├── └── └── └── └── └── LICENSE.txt
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── REQUESTED
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── └── WHEEL
├── ├── └── ├── pkg_resources/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── api_tests.txt
├── ├── └── ├── ├── py.typed
├── ├── └── ├── └── tests/
├── ├── └── ├── └── ├── __init__.py
├── ├── └── ├── └── ├── data/
├── ├── └── ├── └── ├── ├── my-test-package-source/
├── ├── └── ├── └── ├── ├── ├── setup.cfg
├── ├── └── ├── └── ├── ├── └── setup.py
├── ├── └── ├── └── ├── ├── my-test-package-zip/
├── ├── └── ├── └── ├── ├── └── my-test-package.zip
├── ├── └── ├── └── ├── ├── my-test-package_unpacked-egg/
├── ├── └── ├── └── ├── ├── └── my_test_package-1.0-py3.7.egg/
├── ├── └── ├── └── ├── ├── └── └── EGG-INFO/
├── ├── └── ├── └── ├── ├── └── └── ├── dependency_links.txt
├── ├── └── ├── └── ├── ├── └── └── ├── PKG-INFO
├── ├── └── ├── └── ├── ├── └── └── ├── SOURCES.txt
├── ├── └── ├── └── ├── ├── └── └── ├── top_level.txt
├── ├── └── ├── └── ├── ├── └── └── └── zip-safe
├── ├── └── ├── └── ├── └── my-test-package_zipped-egg/
├── ├── └── ├── └── ├── └── └── my_test_package-1.0-py3.7.egg
├── ├── └── ├── └── ├── test_find_distributions.py
├── ├── └── ├── └── ├── test_integration_zope_interface.py
├── ├── └── ├── └── ├── test_markers.py
├── ├── └── ├── └── ├── test_pkg_resources.py
├── ├── └── ├── └── ├── test_resources.py
├── ├── └── ├── └── └── test_working_set.py
├── ├── └── ├── pylab.py
├── ├── └── ├── pyparsing/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── actions.py
├── ├── └── ├── ├── common.py
├── ├── └── ├── ├── core.py
├── ├── └── ├── ├── diagram/
├── ├── └── ├── ├── └── __init__.py
├── ├── └── ├── ├── exceptions.py
├── ├── └── ├── ├── helpers.py
├── ├── └── ├── ├── py.typed
├── ├── └── ├── ├── results.py
├── ├── └── ├── ├── testing.py
├── ├── └── ├── ├── tools/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── └── cvt_pyparsing_pep8_names.py
├── ├── └── ├── ├── unicode.py
├── ├── └── ├── └── util.py
├── ├── └── ├── pyparsing-3.2.3.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── └── WHEEL
├── ├── └── ├── python_dateutil-2.9.0.post0.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── ├── WHEEL
├── ├── └── ├── └── zip-safe
├── ├── └── ├── pytz/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── exceptions.py
├── ├── └── ├── ├── lazy.py
├── ├── └── ├── ├── reference.py
├── ├── └── ├── ├── tzfile.py
├── ├── └── ├── ├── tzinfo.py
├── ├── └── ├── └── zoneinfo/
├── ├── └── ├── └── ├── Africa/
├── ├── └── ├── └── ├── ├── Abidjan
├── ├── └── ├── └── ├── ├── Accra
├── ├── └── ├── └── ├── ├── Addis_Ababa
├── ├── └── ├── └── ├── ├── Algiers
├── ├── └── ├── └── ├── ├── Asmara
├── ├── └── ├── └── ├── ├── Asmera
├── ├── └── ├── └── ├── ├── Bamako
├── ├── └── ├── └── ├── ├── Bangui
├── ├── └── ├── └── ├── ├── Banjul
├── ├── └── ├── └── ├── ├── Bissau
├── ├── └── ├── └── ├── ├── Blantyre
├── ├── └── ├── └── ├── ├── Brazzaville
├── ├── └── ├── └── ├── ├── Bujumbura
├── ├── └── ├── └── ├── ├── Cairo
├── ├── └── ├── └── ├── ├── Casablanca
├── ├── └── ├── └── ├── ├── Ceuta
├── ├── └── ├── └── ├── ├── Conakry
├── ├── └── ├── └── ├── ├── Dakar
├── ├── └── ├── └── ├── ├── Dar_es_Salaam
├── ├── └── ├── └── ├── ├── Djibouti
├── ├── └── ├── └── ├── ├── Douala
├── ├── └── ├── └── ├── ├── El_Aaiun
├── ├── └── ├── └── ├── ├── Freetown
├── ├── └── ├── └── ├── ├── Gaborone
├── ├── └── ├── └── ├── ├── Harare
├── ├── └── ├── └── ├── ├── Johannesburg
├── ├── └── ├── └── ├── ├── Juba
├── ├── └── ├── └── ├── ├── Kampala
├── ├── └── ├── └── ├── ├── Khartoum
├── ├── └── ├── └── ├── ├── Kigali
├── ├── └── ├── └── ├── ├── Kinshasa
├── ├── └── ├── └── ├── ├── Lagos
├── ├── └── ├── └── ├── ├── Libreville
├── ├── └── ├── └── ├── ├── Lome
├── ├── └── ├── └── ├── ├── Luanda
├── ├── └── ├── └── ├── ├── Lubumbashi
├── ├── └── ├── └── ├── ├── Lusaka
├── ├── └── ├── └── ├── ├── Malabo
├── ├── └── ├── └── ├── ├── Maputo
├── ├── └── ├── └── ├── ├── Maseru
├── ├── └── ├── └── ├── ├── Mbabane
├── ├── └── ├── └── ├── ├── Mogadishu
├── ├── └── ├── └── ├── ├── Monrovia
├── ├── └── ├── └── ├── ├── Nairobi
├── ├── └── ├── └── ├── ├── Ndjamena
├── ├── └── ├── └── ├── ├── Niamey
├── ├── └── ├── └── ├── ├── Nouakchott
├── ├── └── ├── └── ├── ├── Ouagadougou
├── ├── └── ├── └── ├── ├── Porto-Novo
├── ├── └── ├── └── ├── ├── Sao_Tome
├── ├── └── ├── └── ├── ├── Timbuktu
├── ├── └── ├── └── ├── ├── Tripoli
├── ├── └── ├── └── ├── ├── Tunis
├── ├── └── ├── └── ├── └── Windhoek
├── ├── └── ├── └── ├── America/
├── ├── └── ├── └── ├── ├── Adak
├── ├── └── ├── └── ├── ├── Anchorage
├── ├── └── ├── └── ├── ├── Anguilla
├── ├── └── ├── └── ├── ├── Antigua
├── ├── └── ├── └── ├── ├── Araguaina
├── ├── └── ├── └── ├── ├── Argentina/
├── ├── └── ├── └── ├── ├── ├── Buenos_Aires
├── ├── └── ├── └── ├── ├── ├── Catamarca
├── ├── └── ├── └── ├── ├── ├── ComodRivadavia
├── ├── └── ├── └── ├── ├── ├── Cordoba
├── ├── └── ├── └── ├── ├── ├── Jujuy
├── ├── └── ├── └── ├── ├── ├── La_Rioja
├── ├── └── ├── └── ├── ├── ├── Mendoza
├── ├── └── ├── └── ├── ├── ├── Rio_Gallegos
├── ├── └── ├── └── ├── ├── ├── Salta
├── ├── └── ├── └── ├── ├── ├── San_Juan
├── ├── └── ├── └── ├── ├── ├── San_Luis
├── ├── └── ├── └── ├── ├── ├── Tucuman
├── ├── └── ├── └── ├── ├── └── Ushuaia
├── ├── └── ├── └── ├── ├── Aruba
├── ├── └── ├── └── ├── ├── Asuncion
├── ├── └── ├── └── ├── ├── Atikokan
├── ├── └── ├── └── ├── ├── Atka
├── ├── └── ├── └── ├── ├── Bahia
├── ├── └── ├── └── ├── ├── Bahia_Banderas
├── ├── └── ├── └── ├── ├── Barbados
├── ├── └── ├── └── ├── ├── Belem
├── ├── └── ├── └── ├── ├── Belize
├── ├── └── ├── └── ├── ├── Blanc-Sablon
├── ├── └── ├── └── ├── ├── Boa_Vista
├── ├── └── ├── └── ├── ├── Bogota
├── ├── └── ├── └── ├── ├── Boise
├── ├── └── ├── └── ├── ├── Buenos_Aires
├── ├── └── ├── └── ├── ├── Cambridge_Bay
├── ├── └── ├── └── ├── ├── Campo_Grande
├── ├── └── ├── └── ├── ├── Cancun
├── ├── └── ├── └── ├── ├── Caracas
├── ├── └── ├── └── ├── ├── Catamarca
├── ├── └── ├── └── ├── ├── Cayenne
├── ├── └── ├── └── ├── ├── Cayman
├── ├── └── ├── └── ├── ├── Chicago
├── ├── └── ├── └── ├── ├── Chihuahua
├── ├── └── ├── └── ├── ├── Ciudad_Juarez
├── ├── └── ├── └── ├── ├── Coral_Harbour
├── ├── └── ├── └── ├── ├── Cordoba
├── ├── └── ├── └── ├── ├── Costa_Rica
├── ├── └── ├── └── ├── ├── Coyhaique
├── ├── └── ├── └── ├── ├── Creston
├── ├── └── ├── └── ├── ├── Cuiaba
├── ├── └── ├── └── ├── ├── Curacao
├── ├── └── ├── └── ├── ├── Danmarkshavn
├── ├── └── ├── └── ├── ├── Dawson
├── ├── └── ├── └── ├── ├── Dawson_Creek
├── ├── └── ├── └── ├── ├── Denver
├── ├── └── ├── └── ├── ├── Detroit
├── ├── └── ├── └── ├── ├── Dominica
├── ├── └── ├── └── ├── ├── Edmonton
├── ├── └── ├── └── ├── ├── Eirunepe
├── ├── └── ├── └── ├── ├── El_Salvador
├── ├── └── ├── └── ├── ├── Ensenada
├── ├── └── ├── └── ├── ├── Fort_Nelson
├── ├── └── ├── └── ├── ├── Fort_Wayne
├── ├── └── ├── └── ├── ├── Fortaleza
├── ├── └── ├── └── ├── ├── Glace_Bay
├── ├── └── ├── └── ├── ├── Godthab
├── ├── └── ├── └── ├── ├── Goose_Bay
├── ├── └── ├── └── ├── ├── Grand_Turk
├── ├── └── ├── └── ├── ├── Grenada
├── ├── └── ├── └── ├── ├── Guadeloupe
├── ├── └── ├── └── ├── ├── Guatemala
├── ├── └── ├── └── ├── ├── Guayaquil
├── ├── └── ├── └── ├── ├── Guyana
├── ├── └── ├── └── ├── ├── Halifax
├── ├── └── ├── └── ├── ├── Havana
├── ├── └── ├── └── ├── ├── Hermosillo
├── ├── └── ├── └── ├── ├── Indiana/
├── ├── └── ├── └── ├── ├── ├── Indianapolis
├── ├── └── ├── └── ├── ├── ├── Knox
├── ├── └── ├── └── ├── ├── ├── Marengo
├── ├── └── ├── └── ├── ├── ├── Petersburg
├── ├── └── ├── └── ├── ├── ├── Tell_City
├── ├── └── ├── └── ├── ├── ├── Vevay
├── ├── └── ├── └── ├── ├── ├── Vincennes
├── ├── └── ├── └── ├── ├── └── Winamac
├── ├── └── ├── └── ├── ├── Indianapolis
├── ├── └── ├── └── ├── ├── Inuvik
├── ├── └── ├── └── ├── ├── Iqaluit
├── ├── └── ├── └── ├── ├── Jamaica
├── ├── └── ├── └── ├── ├── Jujuy
├── ├── └── ├── └── ├── ├── Juneau
├── ├── └── ├── └── ├── ├── Kentucky/
├── ├── └── ├── └── ├── ├── ├── Louisville
├── ├── └── ├── └── ├── ├── └── Monticello
├── ├── └── ├── └── ├── ├── Knox_IN
├── ├── └── ├── └── ├── ├── Kralendijk
├── ├── └── ├── └── ├── ├── La_Paz
├── ├── └── ├── └── ├── ├── Lima
├── ├── └── ├── └── ├── ├── Los_Angeles
├── ├── └── ├── └── ├── ├── Louisville
├── ├── └── ├── └── ├── ├── Lower_Princes
├── ├── └── ├── └── ├── ├── Maceio
├── ├── └── ├── └── ├── ├── Managua
├── ├── └── ├── └── ├── ├── Manaus
├── ├── └── ├── └── ├── ├── Marigot
├── ├── └── ├── └── ├── ├── Martinique
├── ├── └── ├── └── ├── ├── Matamoros
├── ├── └── ├── └── ├── ├── Mazatlan
├── ├── └── ├── └── ├── ├── Mendoza
├── ├── └── ├── └── ├── ├── Menominee
├── ├── └── ├── └── ├── ├── Merida
├── ├── └── ├── └── ├── ├── Metlakatla
├── ├── └── ├── └── ├── ├── Mexico_City
├── ├── └── ├── └── ├── ├── Miquelon
├── ├── └── ├── └── ├── ├── Moncton
├── ├── └── ├── └── ├── ├── Monterrey
├── ├── └── ├── └── ├── ├── Montevideo
├── ├── └── ├── └── ├── ├── Montreal
├── ├── └── ├── └── ├── ├── Montserrat
├── ├── └── ├── └── ├── ├── Nassau
├── ├── └── ├── └── ├── ├── New_York
├── ├── └── ├── └── ├── ├── Nipigon
├── ├── └── ├── └── ├── ├── Nome
├── ├── └── ├── └── ├── ├── Noronha
├── ├── └── ├── └── ├── ├── North_Dakota/
├── ├── └── ├── └── ├── ├── ├── Beulah
├── ├── └── ├── └── ├── ├── ├── Center
├── ├── └── ├── └── ├── ├── └── New_Salem
├── ├── └── ├── └── ├── ├── Nuuk
├── ├── └── ├── └── ├── ├── Ojinaga
├── ├── └── ├── └── ├── ├── Panama
├── ├── └── ├── └── ├── ├── Pangnirtung
├── ├── └── ├── └── ├── ├── Paramaribo
├── ├── └── ├── └── ├── ├── Phoenix
├── ├── └── ├── └── ├── ├── Port-au-Prince
├── ├── └── ├── └── ├── ├── Port_of_Spain
├── ├── └── ├── └── ├── ├── Porto_Acre
├── ├── └── ├── └── ├── ├── Porto_Velho
├── ├── └── ├── └── ├── ├── Puerto_Rico
├── ├── └── ├── └── ├── ├── Punta_Arenas
├── ├── └── ├── └── ├── ├── Rainy_River
├── ├── └── ├── └── ├── ├── Rankin_Inlet
├── ├── └── ├── └── ├── ├── Recife
├── ├── └── ├── └── ├── ├── Regina
├── ├── └── ├── └── ├── ├── Resolute
├── ├── └── ├── └── ├── ├── Rio_Branco
├── ├── └── ├── └── ├── ├── Rosario
├── ├── └── ├── └── ├── ├── Santa_Isabel
├── ├── └── ├── └── ├── ├── Santarem
├── ├── └── ├── └── ├── ├── Santiago
├── ├── └── ├── └── ├── ├── Santo_Domingo
├── ├── └── ├── └── ├── ├── Sao_Paulo
├── ├── └── ├── └── ├── ├── Scoresbysund
├── ├── └── ├── └── ├── ├── Shiprock
├── ├── └── ├── └── ├── ├── Sitka
├── ├── └── ├── └── ├── ├── St_Barthelemy
├── ├── └── ├── └── ├── ├── St_Johns
├── ├── └── ├── └── ├── ├── St_Kitts
├── ├── └── ├── └── ├── ├── St_Lucia
├── ├── └── ├── └── ├── ├── St_Thomas
├── ├── └── ├── └── ├── ├── St_Vincent
├── ├── └── ├── └── ├── ├── Swift_Current
├── ├── └── ├── └── ├── ├── Tegucigalpa
├── ├── └── ├── └── ├── ├── Thule
├── ├── └── ├── └── ├── ├── Thunder_Bay
├── ├── └── ├── └── ├── ├── Tijuana
├── ├── └── ├── └── ├── ├── Toronto
├── ├── └── ├── └── ├── ├── Tortola
├── ├── └── ├── └── ├── ├── Vancouver
├── ├── └── ├── └── ├── ├── Virgin
├── ├── └── ├── └── ├── ├── Whitehorse
├── ├── └── ├── └── ├── ├── Winnipeg
├── ├── └── ├── └── ├── ├── Yakutat
├── ├── └── ├── └── ├── └── Yellowknife
├── ├── └── ├── └── ├── Antarctica/
├── ├── └── ├── └── ├── ├── Casey
├── ├── └── ├── └── ├── ├── Davis
├── ├── └── ├── └── ├── ├── DumontDUrville
├── ├── └── ├── └── ├── ├── Macquarie
├── ├── └── ├── └── ├── ├── Mawson
├── ├── └── ├── └── ├── ├── McMurdo
├── ├── └── ├── └── ├── ├── Palmer
├── ├── └── ├── └── ├── ├── Rothera
├── ├── └── ├── └── ├── ├── South_Pole
├── ├── └── ├── └── ├── ├── Syowa
├── ├── └── ├── └── ├── ├── Troll
├── ├── └── ├── └── ├── └── Vostok
├── ├── └── ├── └── ├── Arctic/
├── ├── └── ├── └── ├── └── Longyearbyen
├── ├── └── ├── └── ├── Asia/
├── ├── └── ├── └── ├── ├── Aden
├── ├── └── ├── └── ├── ├── Almaty
├── ├── └── ├── └── ├── ├── Amman
├── ├── └── ├── └── ├── ├── Anadyr
├── ├── └── ├── └── ├── ├── Aqtau
├── ├── └── ├── └── ├── ├── Aqtobe
├── ├── └── ├── └── ├── ├── Ashgabat
├── ├── └── ├── └── ├── ├── Ashkhabad
├── ├── └── ├── └── ├── ├── Atyrau
├── ├── └── ├── └── ├── ├── Baghdad
├── ├── └── ├── └── ├── ├── Bahrain
├── ├── └── ├── └── ├── ├── Baku
├── ├── └── ├── └── ├── ├── Bangkok
├── ├── └── ├── └── ├── ├── Barnaul
├── ├── └── ├── └── ├── ├── Beirut
├── ├── └── ├── └── ├── ├── Bishkek
├── ├── └── ├── └── ├── ├── Brunei
├── ├── └── ├── └── ├── ├── Calcutta
├── ├── └── ├── └── ├── ├── Chita
├── ├── └── ├── └── ├── ├── Choibalsan
├── ├── └── ├── └── ├── ├── Chongqing
├── ├── └── ├── └── ├── ├── Chungking
├── ├── └── ├── └── ├── ├── Colombo
├── ├── └── ├── └── ├── ├── Dacca
├── ├── └── ├── └── ├── ├── Damascus
├── ├── └── ├── └── ├── ├── Dhaka
├── ├── └── ├── └── ├── ├── Dili
├── ├── └── ├── └── ├── ├── Dubai
├── ├── └── ├── └── ├── ├── Dushanbe
├── ├── └── ├── └── ├── ├── Famagusta
├── ├── └── ├── └── ├── ├── Gaza
├── ├── └── ├── └── ├── ├── Harbin
├── ├── └── ├── └── ├── ├── Hebron
├── ├── └── ├── └── ├── ├── Ho_Chi_Minh
├── ├── └── ├── └── ├── ├── Hong_Kong
├── ├── └── ├── └── ├── ├── Hovd
├── ├── └── ├── └── ├── ├── Irkutsk
├── ├── └── ├── └── ├── ├── Istanbul
├── ├── └── ├── └── ├── ├── Jakarta
├── ├── └── ├── └── ├── ├── Jayapura
├── ├── └── ├── └── ├── ├── Jerusalem
├── ├── └── ├── └── ├── ├── Kabul
├── ├── └── ├── └── ├── ├── Kamchatka
├── ├── └── ├── └── ├── ├── Karachi
├── ├── └── ├── └── ├── ├── Kashgar
├── ├── └── ├── └── ├── ├── Kathmandu
├── ├── └── ├── └── ├── ├── Katmandu
├── ├── └── ├── └── ├── ├── Khandyga
├── ├── └── ├── └── ├── ├── Kolkata
├── ├── └── ├── └── ├── ├── Krasnoyarsk
├── ├── └── ├── └── ├── ├── Kuala_Lumpur
├── ├── └── ├── └── ├── ├── Kuching
├── ├── └── ├── └── ├── ├── Kuwait
├── ├── └── ├── └── ├── ├── Macao
├── ├── └── ├── └── ├── ├── Macau
├── ├── └── ├── └── ├── ├── Magadan
├── ├── └── ├── └── ├── ├── Makassar
├── ├── └── ├── └── ├── ├── Manila
├── ├── └── ├── └── ├── ├── Muscat
├── ├── └── ├── └── ├── ├── Nicosia
├── ├── └── ├── └── ├── ├── Novokuznetsk
├── ├── └── ├── └── ├── ├── Novosibirsk
├── ├── └── ├── └── ├── ├── Omsk
├── ├── └── ├── └── ├── ├── Oral
├── ├── └── ├── └── ├── ├── Phnom_Penh
├── ├── └── ├── └── ├── ├── Pontianak
├── ├── └── ├── └── ├── ├── Pyongyang
├── ├── └── ├── └── ├── ├── Qatar
├── ├── └── ├── └── ├── ├── Qostanay
├── ├── └── ├── └── ├── ├── Qyzylorda
├── ├── └── ├── └── ├── ├── Rangoon
├── ├── └── ├── └── ├── ├── Riyadh
├── ├── └── ├── └── ├── ├── Saigon
├── ├── └── ├── └── ├── ├── Sakhalin
├── ├── └── ├── └── ├── ├── Samarkand
├── ├── └── ├── └── ├── ├── Seoul
├── ├── └── ├── └── ├── ├── Shanghai
├── ├── └── ├── └── ├── ├── Singapore
├── ├── └── ├── └── ├── ├── Srednekolymsk
├── ├── └── ├── └── ├── ├── Taipei
├── ├── └── ├── └── ├── ├── Tashkent
├── ├── └── ├── └── ├── ├── Tbilisi
├── ├── └── ├── └── ├── ├── Tehran
├── ├── └── ├── └── ├── ├── Tel_Aviv
├── ├── └── ├── └── ├── ├── Thimbu
├── ├── └── ├── └── ├── ├── Thimphu
├── ├── └── ├── └── ├── ├── Tokyo
├── ├── └── ├── └── ├── ├── Tomsk
├── ├── └── ├── └── ├── ├── Ujung_Pandang
├── ├── └── ├── └── ├── ├── Ulaanbaatar
├── ├── └── ├── └── ├── ├── Ulan_Bator
├── ├── └── ├── └── ├── ├── Urumqi
├── ├── └── ├── └── ├── ├── Ust-Nera
├── ├── └── ├── └── ├── ├── Vientiane
├── ├── └── ├── └── ├── ├── Vladivostok
├── ├── └── ├── └── ├── ├── Yakutsk
├── ├── └── ├── └── ├── ├── Yangon
├── ├── └── ├── └── ├── ├── Yekaterinburg
├── ├── └── ├── └── ├── └── Yerevan
├── ├── └── ├── └── ├── Atlantic/
├── ├── └── ├── └── ├── ├── Azores
├── ├── └── ├── └── ├── ├── Bermuda
├── ├── └── ├── └── ├── ├── Canary
├── ├── └── ├── └── ├── ├── Cape_Verde
├── ├── └── ├── └── ├── ├── Faeroe
├── ├── └── ├── └── ├── ├── Faroe
├── ├── └── ├── └── ├── ├── Jan_Mayen
├── ├── └── ├── └── ├── ├── Madeira
├── ├── └── ├── └── ├── ├── Reykjavik
├── ├── └── ├── └── ├── ├── South_Georgia
├── ├── └── ├── └── ├── ├── St_Helena
├── ├── └── ├── └── ├── └── Stanley
├── ├── └── ├── └── ├── Australia/
├── ├── └── ├── └── ├── ├── ACT
├── ├── └── ├── └── ├── ├── Adelaide
├── ├── └── ├── └── ├── ├── Brisbane
├── ├── └── ├── └── ├── ├── Broken_Hill
├── ├── └── ├── └── ├── ├── Canberra
├── ├── └── ├── └── ├── ├── Currie
├── ├── └── ├── └── ├── ├── Darwin
├── ├── └── ├── └── ├── ├── Eucla
├── ├── └── ├── └── ├── ├── Hobart
├── ├── └── ├── └── ├── ├── LHI
├── ├── └── ├── └── ├── ├── Lindeman
├── ├── └── ├── └── ├── ├── Lord_Howe
├── ├── └── ├── └── ├── ├── Melbourne
├── ├── └── ├── └── ├── ├── North
├── ├── └── ├── └── ├── ├── NSW
├── ├── └── ├── └── ├── ├── Perth
├── ├── └── ├── └── ├── ├── Queensland
├── ├── └── ├── └── ├── ├── South
├── ├── └── ├── └── ├── ├── Sydney
├── ├── └── ├── └── ├── ├── Tasmania
├── ├── └── ├── └── ├── ├── Victoria
├── ├── └── ├── └── ├── ├── West
├── ├── └── ├── └── ├── └── Yancowinna
├── ├── └── ├── └── ├── Brazil/
├── ├── └── ├── └── ├── ├── Acre
├── ├── └── ├── └── ├── ├── DeNoronha
├── ├── └── ├── └── ├── ├── East
├── ├── └── ├── └── ├── └── West
├── ├── └── ├── └── ├── Canada/
├── ├── └── ├── └── ├── ├── Atlantic
├── ├── └── ├── └── ├── ├── Central
├── ├── └── ├── └── ├── ├── Eastern
├── ├── └── ├── └── ├── ├── Mountain
├── ├── └── ├── └── ├── ├── Newfoundland
├── ├── └── ├── └── ├── ├── Pacific
├── ├── └── ├── └── ├── ├── Saskatchewan
├── ├── └── ├── └── ├── └── Yukon
├── ├── └── ├── └── ├── CET
├── ├── └── ├── └── ├── Chile/
├── ├── └── ├── └── ├── ├── Continental
├── ├── └── ├── └── ├── └── EasterIsland
├── ├── └── ├── └── ├── CST6CDT
├── ├── └── ├── └── ├── Cuba
├── ├── └── ├── └── ├── EET
├── ├── └── ├── └── ├── Egypt
├── ├── └── ├── └── ├── Eire
├── ├── └── ├── └── ├── EST
├── ├── └── ├── └── ├── EST5EDT
├── ├── └── ├── └── ├── Etc/
├── ├── └── ├── └── ├── ├── GMT
├── ├── └── ├── └── ├── ├── GMT+0
├── ├── └── ├── └── ├── ├── GMT+1
├── ├── └── ├── └── ├── ├── GMT+10
├── ├── └── ├── └── ├── ├── GMT+11
├── ├── └── ├── └── ├── ├── GMT+12
├── ├── └── ├── └── ├── ├── GMT+2
├── ├── └── ├── └── ├── ├── GMT+3
├── ├── └── ├── └── ├── ├── GMT+4
├── ├── └── ├── └── ├── ├── GMT+5
├── ├── └── ├── └── ├── ├── GMT+6
├── ├── └── ├── └── ├── ├── GMT+7
├── ├── └── ├── └── ├── ├── GMT+8
├── ├── └── ├── └── ├── ├── GMT+9
├── ├── └── ├── └── ├── ├── GMT-0
├── ├── └── ├── └── ├── ├── GMT-1
├── ├── └── ├── └── ├── ├── GMT-10
├── ├── └── ├── └── ├── ├── GMT-11
├── ├── └── ├── └── ├── ├── GMT-12
├── ├── └── ├── └── ├── ├── GMT-13
├── ├── └── ├── └── ├── ├── GMT-14
├── ├── └── ├── └── ├── ├── GMT-2
├── ├── └── ├── └── ├── ├── GMT-3
├── ├── └── ├── └── ├── ├── GMT-4
├── ├── └── ├── └── ├── ├── GMT-5
├── ├── └── ├── └── ├── ├── GMT-6
├── ├── └── ├── └── ├── ├── GMT-7
├── ├── └── ├── └── ├── ├── GMT-8
├── ├── └── ├── └── ├── ├── GMT-9
├── ├── └── ├── └── ├── ├── GMT0
├── ├── └── ├── └── ├── ├── Greenwich
├── ├── └── ├── └── ├── ├── UCT
├── ├── └── ├── └── ├── ├── Universal
├── ├── └── ├── └── ├── ├── UTC
├── ├── └── ├── └── ├── └── Zulu
├── ├── └── ├── └── ├── Europe/
├── ├── └── ├── └── ├── ├── Amsterdam
├── ├── └── ├── └── ├── ├── Andorra
├── ├── └── ├── └── ├── ├── Astrakhan
├── ├── └── ├── └── ├── ├── Athens
├── ├── └── ├── └── ├── ├── Belfast
├── ├── └── ├── └── ├── ├── Belgrade
├── ├── └── ├── └── ├── ├── Berlin
├── ├── └── ├── └── ├── ├── Bratislava
├── ├── └── ├── └── ├── ├── Brussels
├── ├── └── ├── └── ├── ├── Bucharest
├── ├── └── ├── └── ├── ├── Budapest
├── ├── └── ├── └── ├── ├── Busingen
├── ├── └── ├── └── ├── ├── Chisinau
├── ├── └── ├── └── ├── ├── Copenhagen
├── ├── └── ├── └── ├── ├── Dublin
├── ├── └── ├── └── ├── ├── Gibraltar
├── ├── └── ├── └── ├── ├── Guernsey
├── ├── └── ├── └── ├── ├── Helsinki
├── ├── └── ├── └── ├── ├── Isle_of_Man
├── ├── └── ├── └── ├── ├── Istanbul
├── ├── └── ├── └── ├── ├── Jersey
├── ├── └── ├── └── ├── ├── Kaliningrad
├── ├── └── ├── └── ├── ├── Kiev
├── ├── └── ├── └── ├── ├── Kirov
├── ├── └── ├── └── ├── ├── Kyiv
├── ├── └── ├── └── ├── ├── Lisbon
├── ├── └── ├── └── ├── ├── Ljubljana
├── ├── └── ├── └── ├── ├── London
├── ├── └── ├── └── ├── ├── Luxembourg
├── ├── └── ├── └── ├── ├── Madrid
├── ├── └── ├── └── ├── ├── Malta
├── ├── └── ├── └── ├── ├── Mariehamn
├── ├── └── ├── └── ├── ├── Minsk
├── ├── └── ├── └── ├── ├── Monaco
├── ├── └── ├── └── ├── ├── Moscow
├── ├── └── ├── └── ├── ├── Nicosia
├── ├── └── ├── └── ├── ├── Oslo
├── ├── └── ├── └── ├── ├── Paris
├── ├── └── ├── └── ├── ├── Podgorica
├── ├── └── ├── └── ├── ├── Prague
├── ├── └── ├── └── ├── ├── Riga
├── ├── └── ├── └── ├── ├── Rome
├── ├── └── ├── └── ├── ├── Samara
├── ├── └── ├── └── ├── ├── San_Marino
├── ├── └── ├── └── ├── ├── Sarajevo
├── ├── └── ├── └── ├── ├── Saratov
├── ├── └── ├── └── ├── ├── Simferopol
├── ├── └── ├── └── ├── ├── Skopje
├── ├── └── ├── └── ├── ├── Sofia
├── ├── └── ├── └── ├── ├── Stockholm
├── ├── └── ├── └── ├── ├── Tallinn
├── ├── └── ├── └── ├── ├── Tirane
├── ├── └── ├── └── ├── ├── Tiraspol
├── ├── └── ├── └── ├── ├── Ulyanovsk
├── ├── └── ├── └── ├── ├── Uzhgorod
├── ├── └── ├── └── ├── ├── Vaduz
├── ├── └── ├── └── ├── ├── Vatican
├── ├── └── ├── └── ├── ├── Vienna
├── ├── └── ├── └── ├── ├── Vilnius
├── ├── └── ├── └── ├── ├── Volgograd
├── ├── └── ├── └── ├── ├── Warsaw
├── ├── └── ├── └── ├── ├── Zagreb
├── ├── └── ├── └── ├── ├── Zaporozhye
├── ├── └── ├── └── ├── └── Zurich
├── ├── └── ├── └── ├── Factory
├── ├── └── ├── └── ├── GB
├── ├── └── ├── └── ├── GB-Eire
├── ├── └── ├── └── ├── GMT
├── ├── └── ├── └── ├── GMT+0
├── ├── └── ├── └── ├── GMT-0
├── ├── └── ├── └── ├── GMT0
├── ├── └── ├── └── ├── Greenwich
├── ├── └── ├── └── ├── Hongkong
├── ├── └── ├── └── ├── HST
├── ├── └── ├── └── ├── Iceland
├── ├── └── ├── └── ├── Indian/
├── ├── └── ├── └── ├── ├── Antananarivo
├── ├── └── ├── └── ├── ├── Chagos
├── ├── └── ├── └── ├── ├── Christmas
├── ├── └── ├── └── ├── ├── Cocos
├── ├── └── ├── └── ├── ├── Comoro
├── ├── └── ├── └── ├── ├── Kerguelen
├── ├── └── ├── └── ├── ├── Mahe
├── ├── └── ├── └── ├── ├── Maldives
├── ├── └── ├── └── ├── ├── Mauritius
├── ├── └── ├── └── ├── ├── Mayotte
├── ├── └── ├── └── ├── └── Reunion
├── ├── └── ├── └── ├── Iran
├── ├── └── ├── └── ├── iso3166.tab
├── ├── └── ├── └── ├── Israel
├── ├── └── ├── └── ├── Jamaica
├── ├── └── ├── └── ├── Japan
├── ├── └── ├── └── ├── Kwajalein
├── ├── └── ├── └── ├── leapseconds
├── ├── └── ├── └── ├── Libya
├── ├── └── ├── └── ├── MET
├── ├── └── ├── └── ├── Mexico/
├── ├── └── ├── └── ├── ├── BajaNorte
├── ├── └── ├── └── ├── ├── BajaSur
├── ├── └── ├── └── ├── └── General
├── ├── └── ├── └── ├── MST
├── ├── └── ├── └── ├── MST7MDT
├── ├── └── ├── └── ├── Navajo
├── ├── └── ├── └── ├── NZ
├── ├── └── ├── └── ├── NZ-CHAT
├── ├── └── ├── └── ├── Pacific/
├── ├── └── ├── └── ├── ├── Apia
├── ├── └── ├── └── ├── ├── Auckland
├── ├── └── ├── └── ├── ├── Bougainville
├── ├── └── ├── └── ├── ├── Chatham
├── ├── └── ├── └── ├── ├── Chuuk
├── ├── └── ├── └── ├── ├── Easter
├── ├── └── ├── └── ├── ├── Efate
├── ├── └── ├── └── ├── ├── Enderbury
├── ├── └── ├── └── ├── ├── Fakaofo
├── ├── └── ├── └── ├── ├── Fiji
├── ├── └── ├── └── ├── ├── Funafuti
├── ├── └── ├── └── ├── ├── Galapagos
├── ├── └── ├── └── ├── ├── Gambier
├── ├── └── ├── └── ├── ├── Guadalcanal
├── ├── └── ├── └── ├── ├── Guam
├── ├── └── ├── └── ├── ├── Honolulu
├── ├── └── ├── └── ├── ├── Johnston
├── ├── └── ├── └── ├── ├── Kanton
├── ├── └── ├── └── ├── ├── Kiritimati
├── ├── └── ├── └── ├── ├── Kosrae
├── ├── └── ├── └── ├── ├── Kwajalein
├── ├── └── ├── └── ├── ├── Majuro
├── ├── └── ├── └── ├── ├── Marquesas
├── ├── └── ├── └── ├── ├── Midway
├── ├── └── ├── └── ├── ├── Nauru
├── ├── └── ├── └── ├── ├── Niue
├── ├── └── ├── └── ├── ├── Norfolk
├── ├── └── ├── └── ├── ├── Noumea
├── ├── └── ├── └── ├── ├── Pago_Pago
├── ├── └── ├── └── ├── ├── Palau
├── ├── └── ├── └── ├── ├── Pitcairn
├── ├── └── ├── └── ├── ├── Pohnpei
├── ├── └── ├── └── ├── ├── Ponape
├── ├── └── ├── └── ├── ├── Port_Moresby
├── ├── └── ├── └── ├── ├── Rarotonga
├── ├── └── ├── └── ├── ├── Saipan
├── ├── └── ├── └── ├── ├── Samoa
├── ├── └── ├── └── ├── ├── Tahiti
├── ├── └── ├── └── ├── ├── Tarawa
├── ├── └── ├── └── ├── ├── Tongatapu
├── ├── └── ├── └── ├── ├── Truk
├── ├── └── ├── └── ├── ├── Wake
├── ├── └── ├── └── ├── ├── Wallis
├── ├── └── ├── └── ├── └── Yap
├── ├── └── ├── └── ├── Poland
├── ├── └── ├── └── ├── Portugal
├── ├── └── ├── └── ├── PRC
├── ├── └── ├── └── ├── PST8PDT
├── ├── └── ├── └── ├── ROC
├── ├── └── ├── └── ├── ROK
├── ├── └── ├── └── ├── Singapore
├── ├── └── ├── └── ├── Turkey
├── ├── └── ├── └── ├── tzdata.zi
├── ├── └── ├── └── ├── UCT
├── ├── └── ├── └── ├── Universal
├── ├── └── ├── └── ├── US/
├── ├── └── ├── └── ├── ├── Alaska
├── ├── └── ├── └── ├── ├── Aleutian
├── ├── └── ├── └── ├── ├── Arizona
├── ├── └── ├── └── ├── ├── Central
├── ├── └── ├── └── ├── ├── East-Indiana
├── ├── └── ├── └── ├── ├── Eastern
├── ├── └── ├── └── ├── ├── Hawaii
├── ├── └── ├── └── ├── ├── Indiana-Starke
├── ├── └── ├── └── ├── ├── Michigan
├── ├── └── ├── └── ├── ├── Mountain
├── ├── └── ├── └── ├── ├── Pacific
├── ├── └── ├── └── ├── └── Samoa
├── ├── └── ├── └── ├── UTC
├── ├── └── ├── └── ├── W-SU
├── ├── └── ├── └── ├── WET
├── ├── └── ├── └── ├── zone.tab
├── ├── └── ├── └── ├── zone1970.tab
├── ├── └── ├── └── ├── zonenow.tab
├── ├── └── ├── └── └── Zulu
├── ├── └── ├── pytz-2025.2.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE.txt
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── ├── WHEEL
├── ├── └── ├── └── zip-safe
├── ├── └── ├── PyYAML-6.0.2.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── REQUESTED
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── └── WHEEL
├── ├── └── ├── setuptools/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── _core_metadata.py
├── ├── └── ├── ├── _discovery.py
├── ├── └── ├── ├── _distutils/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _log.py
├── ├── └── ├── ├── ├── _macos_compat.py
├── ├── └── ├── ├── ├── _modified.py
├── ├── └── ├── ├── ├── _msvccompiler.py
├── ├── └── ├── ├── ├── archive_util.py
├── ├── └── ├── ├── ├── ccompiler.py
├── ├── └── ├── ├── ├── cmd.py
├── ├── └── ├── ├── ├── command/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _framework_compat.py
├── ├── └── ├── ├── ├── ├── bdist.py
├── ├── └── ├── ├── ├── ├── bdist_dumb.py
├── ├── └── ├── ├── ├── ├── bdist_rpm.py
├── ├── └── ├── ├── ├── ├── build.py
├── ├── └── ├── ├── ├── ├── build_clib.py
├── ├── └── ├── ├── ├── ├── build_ext.py
├── ├── └── ├── ├── ├── ├── build_py.py
├── ├── └── ├── ├── ├── ├── build_scripts.py
├── ├── └── ├── ├── ├── ├── check.py
├── ├── └── ├── ├── ├── ├── clean.py
├── ├── └── ├── ├── ├── ├── config.py
├── ├── └── ├── ├── ├── ├── install.py
├── ├── └── ├── ├── ├── ├── install_data.py
├── ├── └── ├── ├── ├── ├── install_egg_info.py
├── ├── └── ├── ├── ├── ├── install_headers.py
├── ├── └── ├── ├── ├── ├── install_lib.py
├── ├── └── ├── ├── ├── ├── install_scripts.py
├── ├── └── ├── ├── ├── └── sdist.py
├── ├── └── ├── ├── ├── compat/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── numpy.py
├── ├── └── ├── ├── ├── └── py39.py
├── ├── └── ├── ├── ├── compilers/
├── ├── └── ├── ├── ├── └── C/
├── ├── └── ├── ├── ├── └── ├── base.py
├── ├── └── ├── ├── ├── └── ├── cygwin.py
├── ├── └── ├── ├── ├── └── ├── errors.py
├── ├── └── ├── ├── ├── └── ├── msvc.py
├── ├── └── ├── ├── ├── └── ├── tests/
├── ├── └── ├── ├── ├── └── ├── ├── test_base.py
├── ├── └── ├── ├── ├── └── ├── ├── test_cygwin.py
├── ├── └── ├── ├── ├── └── ├── ├── test_mingw.py
├── ├── └── ├── ├── ├── └── ├── ├── test_msvc.py
├── ├── └── ├── ├── ├── └── ├── └── test_unix.py
├── ├── └── ├── ├── ├── └── ├── unix.py
├── ├── └── ├── ├── ├── └── └── zos.py
├── ├── └── ├── ├── ├── core.py
├── ├── └── ├── ├── ├── cygwinccompiler.py
├── ├── └── ├── ├── ├── debug.py
├── ├── └── ├── ├── ├── dep_util.py
├── ├── └── ├── ├── ├── dir_util.py
├── ├── └── ├── ├── ├── dist.py
├── ├── └── ├── ├── ├── errors.py
├── ├── └── ├── ├── ├── extension.py
├── ├── └── ├── ├── ├── fancy_getopt.py
├── ├── └── ├── ├── ├── file_util.py
├── ├── └── ├── ├── ├── filelist.py
├── ├── └── ├── ├── ├── log.py
├── ├── └── ├── ├── ├── spawn.py
├── ├── └── ├── ├── ├── sysconfig.py
├── ├── └── ├── ├── ├── tests/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── compat/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── py39.py
├── ├── └── ├── ├── ├── ├── support.py
├── ├── └── ├── ├── ├── ├── test_archive_util.py
├── ├── └── ├── ├── ├── ├── test_bdist.py
├── ├── └── ├── ├── ├── ├── test_bdist_dumb.py
├── ├── └── ├── ├── ├── ├── test_bdist_rpm.py
├── ├── └── ├── ├── ├── ├── test_build.py
├── ├── └── ├── ├── ├── ├── test_build_clib.py
├── ├── └── ├── ├── ├── ├── test_build_ext.py
├── ├── └── ├── ├── ├── ├── test_build_py.py
├── ├── └── ├── ├── ├── ├── test_build_scripts.py
├── ├── └── ├── ├── ├── ├── test_check.py
├── ├── └── ├── ├── ├── ├── test_clean.py
├── ├── └── ├── ├── ├── ├── test_cmd.py
├── ├── └── ├── ├── ├── ├── test_config_cmd.py
├── ├── └── ├── ├── ├── ├── test_core.py
├── ├── └── ├── ├── ├── ├── test_dir_util.py
├── ├── └── ├── ├── ├── ├── test_dist.py
├── ├── └── ├── ├── ├── ├── test_extension.py
├── ├── └── ├── ├── ├── ├── test_file_util.py
├── ├── └── ├── ├── ├── ├── test_filelist.py
├── ├── └── ├── ├── ├── ├── test_install.py
├── ├── └── ├── ├── ├── ├── test_install_data.py
├── ├── └── ├── ├── ├── ├── test_install_headers.py
├── ├── └── ├── ├── ├── ├── test_install_lib.py
├── ├── └── ├── ├── ├── ├── test_install_scripts.py
├── ├── └── ├── ├── ├── ├── test_log.py
├── ├── └── ├── ├── ├── ├── test_modified.py
├── ├── └── ├── ├── ├── ├── test_sdist.py
├── ├── └── ├── ├── ├── ├── test_spawn.py
├── ├── └── ├── ├── ├── ├── test_sysconfig.py
├── ├── └── ├── ├── ├── ├── test_text_file.py
├── ├── └── ├── ├── ├── ├── test_util.py
├── ├── └── ├── ├── ├── ├── test_version.py
├── ├── └── ├── ├── ├── ├── test_versionpredicate.py
├── ├── └── ├── ├── ├── └── unix_compat.py
├── ├── └── ├── ├── ├── text_file.py
├── ├── └── ├── ├── ├── unixccompiler.py
├── ├── └── ├── ├── ├── util.py
├── ├── └── ├── ├── ├── version.py
├── ├── └── ├── ├── ├── versionpredicate.py
├── ├── └── ├── ├── └── zosccompiler.py
├── ├── └── ├── ├── _entry_points.py
├── ├── └── ├── ├── _imp.py
├── ├── └── ├── ├── _importlib.py
├── ├── └── ├── ├── _itertools.py
├── ├── └── ├── ├── _normalization.py
├── ├── └── ├── ├── _path.py
├── ├── └── ├── ├── _reqs.py
├── ├── └── ├── ├── _scripts.py
├── ├── └── ├── ├── _shutil.py
├── ├── └── ├── ├── _static.py
├── ├── └── ├── ├── _vendor/
├── ├── └── ├── ├── ├── autocommand/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── autoasync.py
├── ├── └── ├── ├── ├── ├── autocommand.py
├── ├── └── ├── ├── ├── ├── automain.py
├── ├── └── ├── ├── ├── ├── autoparse.py
├── ├── └── ├── ├── ├── └── errors.py
├── ├── └── ├── ├── ├── autocommand-2.2.2.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── backports/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── tarfile/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── __main__.py
├── ├── └── ├── ├── ├── └── └── compat/
├── ├── └── ├── ├── ├── └── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── └── └── py38.py
├── ├── └── ├── ├── ├── backports.tarfile-1.2.0.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── importlib_metadata/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _adapters.py
├── ├── └── ├── ├── ├── ├── _collections.py
├── ├── └── ├── ├── ├── ├── _compat.py
├── ├── └── ├── ├── ├── ├── _functools.py
├── ├── └── ├── ├── ├── ├── _itertools.py
├── ├── └── ├── ├── ├── ├── _meta.py
├── ├── └── ├── ├── ├── ├── _text.py
├── ├── └── ├── ├── ├── ├── compat/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── py311.py
├── ├── └── ├── ├── ├── ├── └── py39.py
├── ├── └── ├── ├── ├── ├── diagnose.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── importlib_metadata-8.0.0.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── inflect/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── compat/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── py38.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── inflect-7.3.1.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── jaraco/
├── ├── └── ├── ├── ├── ├── collections/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── ├── context.py
├── ├── └── ├── ├── ├── ├── functools/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── └── text/
├── ├── └── ├── ├── ├── └── ├── __init__.py
├── ├── └── ├── ├── ├── └── ├── layouts.py
├── ├── └── ├── ├── ├── └── ├── Lorem ipsum.txt
├── ├── └── ├── ├── ├── └── ├── show-newlines.py
├── ├── └── ├── ├── ├── └── ├── strip-prefix.py
├── ├── └── ├── ├── ├── └── ├── to-dvorak.py
├── ├── └── ├── ├── ├── └── └── to-qwerty.py
├── ├── └── ├── ├── ├── jaraco.collections-5.1.0.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── jaraco.context-5.3.0.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── jaraco.functools-4.0.1.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── jaraco.text-3.12.1.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── more_itertools/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __init__.pyi
├── ├── └── ├── ├── ├── ├── more.py
├── ├── └── ├── ├── ├── ├── more.pyi
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── ├── recipes.py
├── ├── └── ├── ├── ├── └── recipes.pyi
├── ├── └── ├── ├── ├── more_itertools-10.3.0.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── packaging/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _elffile.py
├── ├── └── ├── ├── ├── ├── _manylinux.py
├── ├── └── ├── ├── ├── ├── _musllinux.py
├── ├── └── ├── ├── ├── ├── _parser.py
├── ├── └── ├── ├── ├── ├── _structures.py
├── ├── └── ├── ├── ├── ├── _tokenizer.py
├── ├── └── ├── ├── ├── ├── licenses/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── _spdx.py
├── ├── └── ├── ├── ├── ├── markers.py
├── ├── └── ├── ├── ├── ├── metadata.py
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── ├── requirements.py
├── ├── └── ├── ├── ├── ├── specifiers.py
├── ├── └── ├── ├── ├── ├── tags.py
├── ├── └── ├── ├── ├── ├── utils.py
├── ├── └── ├── ├── ├── └── version.py
├── ├── └── ├── ├── ├── packaging-24.2.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── LICENSE.APACHE
├── ├── └── ├── ├── ├── ├── LICENSE.BSD
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── platformdirs/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── android.py
├── ├── └── ├── ├── ├── ├── api.py
├── ├── └── ├── ├── ├── ├── macos.py
├── ├── └── ├── ├── ├── ├── py.typed
├── ├── └── ├── ├── ├── ├── unix.py
├── ├── └── ├── ├── ├── ├── version.py
├── ├── └── ├── ├── ├── └── windows.py
├── ├── └── ├── ├── ├── platformdirs-4.2.2.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── licenses/
├── ├── └── ├── ├── ├── ├── └── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── tomli/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _parser.py
├── ├── └── ├── ├── ├── ├── _re.py
├── ├── └── ├── ├── ├── ├── _types.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── tomli-2.0.1.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── typeguard/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _checkers.py
├── ├── └── ├── ├── ├── ├── _config.py
├── ├── └── ├── ├── ├── ├── _decorators.py
├── ├── └── ├── ├── ├── ├── _exceptions.py
├── ├── └── ├── ├── ├── ├── _functions.py
├── ├── └── ├── ├── ├── ├── _importhook.py
├── ├── └── ├── ├── ├── ├── _memo.py
├── ├── └── ├── ├── ├── ├── _pytest_plugin.py
├── ├── └── ├── ├── ├── ├── _suppression.py
├── ├── └── ├── ├── ├── ├── _transformer.py
├── ├── └── ├── ├── ├── ├── _union_transformer.py
├── ├── └── ├── ├── ├── ├── _utils.py
├── ├── └── ├── ├── ├── └── py.typed
├── ├── └── ├── ├── ├── typeguard-4.3.0.dist-info/
├── ├── └── ├── ├── ├── ├── entry_points.txt
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── top_level.txt
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── typing_extensions-4.12.2.dist-info/
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── typing_extensions.py
├── ├── └── ├── ├── ├── wheel/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── __main__.py
├── ├── └── ├── ├── ├── ├── _bdist_wheel.py
├── ├── └── ├── ├── ├── ├── _setuptools_logging.py
├── ├── └── ├── ├── ├── ├── bdist_wheel.py
├── ├── └── ├── ├── ├── ├── cli/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── convert.py
├── ├── └── ├── ├── ├── ├── ├── pack.py
├── ├── └── ├── ├── ├── ├── ├── tags.py
├── ├── └── ├── ├── ├── ├── └── unpack.py
├── ├── └── ├── ├── ├── ├── macosx_libfile.py
├── ├── └── ├── ├── ├── ├── metadata.py
├── ├── └── ├── ├── ├── ├── util.py
├── ├── └── ├── ├── ├── ├── vendored/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── packaging/
├── ├── └── ├── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── ├── _elffile.py
├── ├── └── ├── ├── ├── ├── ├── ├── _manylinux.py
├── ├── └── ├── ├── ├── ├── ├── ├── _musllinux.py
├── ├── └── ├── ├── ├── ├── ├── ├── _parser.py
├── ├── └── ├── ├── ├── ├── ├── ├── _structures.py
├── ├── └── ├── ├── ├── ├── ├── ├── _tokenizer.py
├── ├── └── ├── ├── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── ├── ├── LICENSE.APACHE
├── ├── └── ├── ├── ├── ├── ├── ├── LICENSE.BSD
├── ├── └── ├── ├── ├── ├── ├── ├── markers.py
├── ├── └── ├── ├── ├── ├── ├── ├── requirements.py
├── ├── └── ├── ├── ├── ├── ├── ├── specifiers.py
├── ├── └── ├── ├── ├── ├── ├── ├── tags.py
├── ├── └── ├── ├── ├── ├── ├── ├── utils.py
├── ├── └── ├── ├── ├── ├── ├── └── version.py
├── ├── └── ├── ├── ├── ├── └── vendor.txt
├── ├── └── ├── ├── ├── └── wheelfile.py
├── ├── └── ├── ├── ├── wheel-0.45.1.dist-info/
├── ├── └── ├── ├── ├── ├── entry_points.txt
├── ├── └── ├── ├── ├── ├── INSTALLER
├── ├── └── ├── ├── ├── ├── LICENSE.txt
├── ├── └── ├── ├── ├── ├── METADATA
├── ├── └── ├── ├── ├── ├── RECORD
├── ├── └── ├── ├── ├── ├── REQUESTED
├── ├── └── ├── ├── ├── └── WHEEL
├── ├── └── ├── ├── ├── zipp/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── compat/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── py310.py
├── ├── └── ├── ├── ├── └── glob.py
├── ├── └── ├── ├── └── zipp-3.19.2.dist-info/
├── ├── └── ├── ├── └── ├── INSTALLER
├── ├── └── ├── ├── └── ├── LICENSE
├── ├── └── ├── ├── └── ├── METADATA
├── ├── └── ├── ├── └── ├── RECORD
├── ├── └── ├── ├── └── ├── REQUESTED
├── ├── └── ├── ├── └── ├── top_level.txt
├── ├── └── ├── ├── └── └── WHEEL
├── ├── └── ├── ├── archive_util.py
├── ├── └── ├── ├── build_meta.py
├── ├── └── ├── ├── cli-32.exe
├── ├── └── ├── ├── cli-64.exe
├── ├── └── ├── ├── cli-arm64.exe
├── ├── └── ├── ├── cli.exe
├── ├── └── ├── ├── command/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _requirestxt.py
├── ├── └── ├── ├── ├── alias.py
├── ├── └── ├── ├── ├── bdist_egg.py
├── ├── └── ├── ├── ├── bdist_rpm.py
├── ├── └── ├── ├── ├── bdist_wheel.py
├── ├── └── ├── ├── ├── build.py
├── ├── └── ├── ├── ├── build_clib.py
├── ├── └── ├── ├── ├── build_ext.py
├── ├── └── ├── ├── ├── build_py.py
├── ├── └── ├── ├── ├── develop.py
├── ├── └── ├── ├── ├── dist_info.py
├── ├── └── ├── ├── ├── easy_install.py
├── ├── └── ├── ├── ├── editable_wheel.py
├── ├── └── ├── ├── ├── egg_info.py
├── ├── └── ├── ├── ├── install.py
├── ├── └── ├── ├── ├── install_egg_info.py
├── ├── └── ├── ├── ├── install_lib.py
├── ├── └── ├── ├── ├── install_scripts.py
├── ├── └── ├── ├── ├── launcher manifest.xml
├── ├── └── ├── ├── ├── rotate.py
├── ├── └── ├── ├── ├── saveopts.py
├── ├── └── ├── ├── ├── sdist.py
├── ├── └── ├── ├── ├── setopt.py
├── ├── └── ├── ├── └── test.py
├── ├── └── ├── ├── compat/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── py310.py
├── ├── └── ├── ├── ├── py311.py
├── ├── └── ├── ├── ├── py312.py
├── ├── └── ├── ├── └── py39.py
├── ├── └── ├── ├── config/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── _apply_pyprojecttoml.py
├── ├── └── ├── ├── ├── _validate_pyproject/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── error_reporting.py
├── ├── └── ├── ├── ├── ├── extra_validations.py
├── ├── └── ├── ├── ├── ├── fastjsonschema_exceptions.py
├── ├── └── ├── ├── ├── ├── fastjsonschema_validations.py
├── ├── └── ├── ├── ├── ├── formats.py
├── ├── └── ├── ├── ├── └── NOTICE
├── ├── └── ├── ├── ├── distutils.schema.json
├── ├── └── ├── ├── ├── expand.py
├── ├── └── ├── ├── ├── NOTICE
├── ├── └── ├── ├── ├── pyprojecttoml.py
├── ├── └── ├── ├── ├── setupcfg.py
├── ├── └── ├── ├── └── setuptools.schema.json
├── ├── └── ├── ├── depends.py
├── ├── └── ├── ├── discovery.py
├── ├── └── ├── ├── dist.py
├── ├── └── ├── ├── errors.py
├── ├── └── ├── ├── extension.py
├── ├── └── ├── ├── glob.py
├── ├── └── ├── ├── gui-32.exe
├── ├── └── ├── ├── gui-64.exe
├── ├── └── ├── ├── gui-arm64.exe
├── ├── └── ├── ├── gui.exe
├── ├── └── ├── ├── installer.py
├── ├── └── ├── ├── launch.py
├── ├── └── ├── ├── logging.py
├── ├── └── ├── ├── modified.py
├── ├── └── ├── ├── monkey.py
├── ├── └── ├── ├── msvc.py
├── ├── └── ├── ├── namespaces.py
├── ├── └── ├── ├── script (dev).tmpl
├── ├── └── ├── ├── script.tmpl
├── ├── └── ├── ├── tests/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── compat/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── py39.py
├── ├── └── ├── ├── ├── config/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── downloads/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── └── preload.py
├── ├── └── ├── ├── ├── ├── setupcfg_examples.txt
├── ├── └── ├── ├── ├── ├── test_apply_pyprojecttoml.py
├── ├── └── ├── ├── ├── ├── test_expand.py
├── ├── └── ├── ├── ├── ├── test_pyprojecttoml.py
├── ├── └── ├── ├── ├── ├── test_pyprojecttoml_dynamic_deps.py
├── ├── └── ├── ├── ├── └── test_setupcfg.py
├── ├── └── ├── ├── ├── contexts.py
├── ├── └── ├── ├── ├── environment.py
├── ├── └── ├── ├── ├── fixtures.py
├── ├── └── ├── ├── ├── indexes/
├── ├── └── ├── ├── ├── └── test_links_priority/
├── ├── └── ├── ├── ├── └── ├── external.html
├── ├── └── ├── ├── ├── └── └── simple/
├── ├── └── ├── ├── ├── └── └── └── foobar/
├── ├── └── ├── ├── ├── └── └── └── └── index.html
├── ├── └── ├── ├── ├── integration/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── helpers.py
├── ├── └── ├── ├── ├── ├── test_pbr.py
├── ├── └── ├── ├── ├── └── test_pip_install_sdist.py
├── ├── └── ├── ├── ├── mod_with_constant.py
├── ├── └── ├── ├── ├── namespaces.py
├── ├── └── ├── ├── ├── script-with-bom.py
├── ├── └── ├── ├── ├── test_archive_util.py
├── ├── └── ├── ├── ├── test_bdist_deprecations.py
├── ├── └── ├── ├── ├── test_bdist_egg.py
├── ├── └── ├── ├── ├── test_bdist_wheel.py
├── ├── └── ├── ├── ├── test_build.py
├── ├── └── ├── ├── ├── test_build_clib.py
├── ├── └── ├── ├── ├── test_build_ext.py
├── ├── └── ├── ├── ├── test_build_meta.py
├── ├── └── ├── ├── ├── test_build_py.py
├── ├── └── ├── ├── ├── test_config_discovery.py
├── ├── └── ├── ├── ├── test_core_metadata.py
├── ├── └── ├── ├── ├── test_depends.py
├── ├── └── ├── ├── ├── test_develop.py
├── ├── └── ├── ├── ├── test_dist.py
├── ├── └── ├── ├── ├── test_dist_info.py
├── ├── └── ├── ├── ├── test_distutils_adoption.py
├── ├── └── ├── ├── ├── test_editable_install.py
├── ├── └── ├── ├── ├── test_egg_info.py
├── ├── └── ├── ├── ├── test_extern.py
├── ├── └── ├── ├── ├── test_find_packages.py
├── ├── └── ├── ├── ├── test_find_py_modules.py
├── ├── └── ├── ├── ├── test_glob.py
├── ├── └── ├── ├── ├── test_install_scripts.py
├── ├── └── ├── ├── ├── test_logging.py
├── ├── └── ├── ├── ├── test_manifest.py
├── ├── └── ├── ├── ├── test_namespaces.py
├── ├── └── ├── ├── ├── test_scripts.py
├── ├── └── ├── ├── ├── test_sdist.py
├── ├── └── ├── ├── ├── test_setopt.py
├── ├── └── ├── ├── ├── test_setuptools.py
├── ├── └── ├── ├── ├── test_shutil_wrapper.py
├── ├── └── ├── ├── ├── test_unicode_utils.py
├── ├── └── ├── ├── ├── test_virtualenv.py
├── ├── └── ├── ├── ├── test_warnings.py
├── ├── └── ├── ├── ├── test_wheel.py
├── ├── └── ├── ├── ├── test_windows_wrappers.py
├── ├── └── ├── ├── ├── text.py
├── ├── └── ├── ├── └── textwrap.py
├── ├── └── ├── ├── unicode_utils.py
├── ├── └── ├── ├── version.py
├── ├── └── ├── ├── warnings.py
├── ├── └── ├── ├── wheel.py
├── ├── └── ├── └── windows_support.py
├── ├── └── ├── setuptools-80.9.0.dist-info/
├── ├── └── ├── ├── entry_points.txt
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── licenses/
├── ├── └── ├── ├── └── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── REQUESTED
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── └── WHEEL
├── ├── └── ├── six-1.17.0.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── └── WHEEL
├── ├── └── ├── six.py
├── ├── └── ├── tzdata/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── zoneinfo/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── Africa/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Abidjan
├── ├── └── ├── ├── ├── ├── Accra
├── ├── └── ├── ├── ├── ├── Addis_Ababa
├── ├── └── ├── ├── ├── ├── Algiers
├── ├── └── ├── ├── ├── ├── Asmara
├── ├── └── ├── ├── ├── ├── Asmera
├── ├── └── ├── ├── ├── ├── Bamako
├── ├── └── ├── ├── ├── ├── Bangui
├── ├── └── ├── ├── ├── ├── Banjul
├── ├── └── ├── ├── ├── ├── Bissau
├── ├── └── ├── ├── ├── ├── Blantyre
├── ├── └── ├── ├── ├── ├── Brazzaville
├── ├── └── ├── ├── ├── ├── Bujumbura
├── ├── └── ├── ├── ├── ├── Cairo
├── ├── └── ├── ├── ├── ├── Casablanca
├── ├── └── ├── ├── ├── ├── Ceuta
├── ├── └── ├── ├── ├── ├── Conakry
├── ├── └── ├── ├── ├── ├── Dakar
├── ├── └── ├── ├── ├── ├── Dar_es_Salaam
├── ├── └── ├── ├── ├── ├── Djibouti
├── ├── └── ├── ├── ├── ├── Douala
├── ├── └── ├── ├── ├── ├── El_Aaiun
├── ├── └── ├── ├── ├── ├── Freetown
├── ├── └── ├── ├── ├── ├── Gaborone
├── ├── └── ├── ├── ├── ├── Harare
├── ├── └── ├── ├── ├── ├── Johannesburg
├── ├── └── ├── ├── ├── ├── Juba
├── ├── └── ├── ├── ├── ├── Kampala
├── ├── └── ├── ├── ├── ├── Khartoum
├── ├── └── ├── ├── ├── ├── Kigali
├── ├── └── ├── ├── ├── ├── Kinshasa
├── ├── └── ├── ├── ├── ├── Lagos
├── ├── └── ├── ├── ├── ├── Libreville
├── ├── └── ├── ├── ├── ├── Lome
├── ├── └── ├── ├── ├── ├── Luanda
├── ├── └── ├── ├── ├── ├── Lubumbashi
├── ├── └── ├── ├── ├── ├── Lusaka
├── ├── └── ├── ├── ├── ├── Malabo
├── ├── └── ├── ├── ├── ├── Maputo
├── ├── └── ├── ├── ├── ├── Maseru
├── ├── └── ├── ├── ├── ├── Mbabane
├── ├── └── ├── ├── ├── ├── Mogadishu
├── ├── └── ├── ├── ├── ├── Monrovia
├── ├── └── ├── ├── ├── ├── Nairobi
├── ├── └── ├── ├── ├── ├── Ndjamena
├── ├── └── ├── ├── ├── ├── Niamey
├── ├── └── ├── ├── ├── ├── Nouakchott
├── ├── └── ├── ├── ├── ├── Ouagadougou
├── ├── └── ├── ├── ├── ├── Porto-Novo
├── ├── └── ├── ├── ├── ├── Sao_Tome
├── ├── └── ├── ├── ├── ├── Timbuktu
├── ├── └── ├── ├── ├── ├── Tripoli
├── ├── └── ├── ├── ├── ├── Tunis
├── ├── └── ├── ├── ├── └── Windhoek
├── ├── └── ├── ├── ├── America/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Adak
├── ├── └── ├── ├── ├── ├── Anchorage
├── ├── └── ├── ├── ├── ├── Anguilla
├── ├── └── ├── ├── ├── ├── Antigua
├── ├── └── ├── ├── ├── ├── Araguaina
├── ├── └── ├── ├── ├── ├── Argentina/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── Buenos_Aires
├── ├── └── ├── ├── ├── ├── ├── Catamarca
├── ├── └── ├── ├── ├── ├── ├── ComodRivadavia
├── ├── └── ├── ├── ├── ├── ├── Cordoba
├── ├── └── ├── ├── ├── ├── ├── Jujuy
├── ├── └── ├── ├── ├── ├── ├── La_Rioja
├── ├── └── ├── ├── ├── ├── ├── Mendoza
├── ├── └── ├── ├── ├── ├── ├── Rio_Gallegos
├── ├── └── ├── ├── ├── ├── ├── Salta
├── ├── └── ├── ├── ├── ├── ├── San_Juan
├── ├── └── ├── ├── ├── ├── ├── San_Luis
├── ├── └── ├── ├── ├── ├── ├── Tucuman
├── ├── └── ├── ├── ├── ├── └── Ushuaia
├── ├── └── ├── ├── ├── ├── Aruba
├── ├── └── ├── ├── ├── ├── Asuncion
├── ├── └── ├── ├── ├── ├── Atikokan
├── ├── └── ├── ├── ├── ├── Atka
├── ├── └── ├── ├── ├── ├── Bahia
├── ├── └── ├── ├── ├── ├── Bahia_Banderas
├── ├── └── ├── ├── ├── ├── Barbados
├── ├── └── ├── ├── ├── ├── Belem
├── ├── └── ├── ├── ├── ├── Belize
├── ├── └── ├── ├── ├── ├── Blanc-Sablon
├── ├── └── ├── ├── ├── ├── Boa_Vista
├── ├── └── ├── ├── ├── ├── Bogota
├── ├── └── ├── ├── ├── ├── Boise
├── ├── └── ├── ├── ├── ├── Buenos_Aires
├── ├── └── ├── ├── ├── ├── Cambridge_Bay
├── ├── └── ├── ├── ├── ├── Campo_Grande
├── ├── └── ├── ├── ├── ├── Cancun
├── ├── └── ├── ├── ├── ├── Caracas
├── ├── └── ├── ├── ├── ├── Catamarca
├── ├── └── ├── ├── ├── ├── Cayenne
├── ├── └── ├── ├── ├── ├── Cayman
├── ├── └── ├── ├── ├── ├── Chicago
├── ├── └── ├── ├── ├── ├── Chihuahua
├── ├── └── ├── ├── ├── ├── Ciudad_Juarez
├── ├── └── ├── ├── ├── ├── Coral_Harbour
├── ├── └── ├── ├── ├── ├── Cordoba
├── ├── └── ├── ├── ├── ├── Costa_Rica
├── ├── └── ├── ├── ├── ├── Coyhaique
├── ├── └── ├── ├── ├── ├── Creston
├── ├── └── ├── ├── ├── ├── Cuiaba
├── ├── └── ├── ├── ├── ├── Curacao
├── ├── └── ├── ├── ├── ├── Danmarkshavn
├── ├── └── ├── ├── ├── ├── Dawson
├── ├── └── ├── ├── ├── ├── Dawson_Creek
├── ├── └── ├── ├── ├── ├── Denver
├── ├── └── ├── ├── ├── ├── Detroit
├── ├── └── ├── ├── ├── ├── Dominica
├── ├── └── ├── ├── ├── ├── Edmonton
├── ├── └── ├── ├── ├── ├── Eirunepe
├── ├── └── ├── ├── ├── ├── El_Salvador
├── ├── └── ├── ├── ├── ├── Ensenada
├── ├── └── ├── ├── ├── ├── Fort_Nelson
├── ├── └── ├── ├── ├── ├── Fort_Wayne
├── ├── └── ├── ├── ├── ├── Fortaleza
├── ├── └── ├── ├── ├── ├── Glace_Bay
├── ├── └── ├── ├── ├── ├── Godthab
├── ├── └── ├── ├── ├── ├── Goose_Bay
├── ├── └── ├── ├── ├── ├── Grand_Turk
├── ├── └── ├── ├── ├── ├── Grenada
├── ├── └── ├── ├── ├── ├── Guadeloupe
├── ├── └── ├── ├── ├── ├── Guatemala
├── ├── └── ├── ├── ├── ├── Guayaquil
├── ├── └── ├── ├── ├── ├── Guyana
├── ├── └── ├── ├── ├── ├── Halifax
├── ├── └── ├── ├── ├── ├── Havana
├── ├── └── ├── ├── ├── ├── Hermosillo
├── ├── └── ├── ├── ├── ├── Indiana/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── Indianapolis
├── ├── └── ├── ├── ├── ├── ├── Knox
├── ├── └── ├── ├── ├── ├── ├── Marengo
├── ├── └── ├── ├── ├── ├── ├── Petersburg
├── ├── └── ├── ├── ├── ├── ├── Tell_City
├── ├── └── ├── ├── ├── ├── ├── Vevay
├── ├── └── ├── ├── ├── ├── ├── Vincennes
├── ├── └── ├── ├── ├── ├── └── Winamac
├── ├── └── ├── ├── ├── ├── Indianapolis
├── ├── └── ├── ├── ├── ├── Inuvik
├── ├── └── ├── ├── ├── ├── Iqaluit
├── ├── └── ├── ├── ├── ├── Jamaica
├── ├── └── ├── ├── ├── ├── Jujuy
├── ├── └── ├── ├── ├── ├── Juneau
├── ├── └── ├── ├── ├── ├── Kentucky/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── Louisville
├── ├── └── ├── ├── ├── ├── └── Monticello
├── ├── └── ├── ├── ├── ├── Knox_IN
├── ├── └── ├── ├── ├── ├── Kralendijk
├── ├── └── ├── ├── ├── ├── La_Paz
├── ├── └── ├── ├── ├── ├── Lima
├── ├── └── ├── ├── ├── ├── Los_Angeles
├── ├── └── ├── ├── ├── ├── Louisville
├── ├── └── ├── ├── ├── ├── Lower_Princes
├── ├── └── ├── ├── ├── ├── Maceio
├── ├── └── ├── ├── ├── ├── Managua
├── ├── └── ├── ├── ├── ├── Manaus
├── ├── └── ├── ├── ├── ├── Marigot
├── ├── └── ├── ├── ├── ├── Martinique
├── ├── └── ├── ├── ├── ├── Matamoros
├── ├── └── ├── ├── ├── ├── Mazatlan
├── ├── └── ├── ├── ├── ├── Mendoza
├── ├── └── ├── ├── ├── ├── Menominee
├── ├── └── ├── ├── ├── ├── Merida
├── ├── └── ├── ├── ├── ├── Metlakatla
├── ├── └── ├── ├── ├── ├── Mexico_City
├── ├── └── ├── ├── ├── ├── Miquelon
├── ├── └── ├── ├── ├── ├── Moncton
├── ├── └── ├── ├── ├── ├── Monterrey
├── ├── └── ├── ├── ├── ├── Montevideo
├── ├── └── ├── ├── ├── ├── Montreal
├── ├── └── ├── ├── ├── ├── Montserrat
├── ├── └── ├── ├── ├── ├── Nassau
├── ├── └── ├── ├── ├── ├── New_York
├── ├── └── ├── ├── ├── ├── Nipigon
├── ├── └── ├── ├── ├── ├── Nome
├── ├── └── ├── ├── ├── ├── Noronha
├── ├── └── ├── ├── ├── ├── North_Dakota/
├── ├── └── ├── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ├── Beulah
├── ├── └── ├── ├── ├── ├── ├── Center
├── ├── └── ├── ├── ├── ├── └── New_Salem
├── ├── └── ├── ├── ├── ├── Nuuk
├── ├── └── ├── ├── ├── ├── Ojinaga
├── ├── └── ├── ├── ├── ├── Panama
├── ├── └── ├── ├── ├── ├── Pangnirtung
├── ├── └── ├── ├── ├── ├── Paramaribo
├── ├── └── ├── ├── ├── ├── Phoenix
├── ├── └── ├── ├── ├── ├── Port-au-Prince
├── ├── └── ├── ├── ├── ├── Port_of_Spain
├── ├── └── ├── ├── ├── ├── Porto_Acre
├── ├── └── ├── ├── ├── ├── Porto_Velho
├── ├── └── ├── ├── ├── ├── Puerto_Rico
├── ├── └── ├── ├── ├── ├── Punta_Arenas
├── ├── └── ├── ├── ├── ├── Rainy_River
├── ├── └── ├── ├── ├── ├── Rankin_Inlet
├── ├── └── ├── ├── ├── ├── Recife
├── ├── └── ├── ├── ├── ├── Regina
├── ├── └── ├── ├── ├── ├── Resolute
├── ├── └── ├── ├── ├── ├── Rio_Branco
├── ├── └── ├── ├── ├── ├── Rosario
├── ├── └── ├── ├── ├── ├── Santa_Isabel
├── ├── └── ├── ├── ├── ├── Santarem
├── ├── └── ├── ├── ├── ├── Santiago
├── ├── └── ├── ├── ├── ├── Santo_Domingo
├── ├── └── ├── ├── ├── ├── Sao_Paulo
├── ├── └── ├── ├── ├── ├── Scoresbysund
├── ├── └── ├── ├── ├── ├── Shiprock
├── ├── └── ├── ├── ├── ├── Sitka
├── ├── └── ├── ├── ├── ├── St_Barthelemy
├── ├── └── ├── ├── ├── ├── St_Johns
├── ├── └── ├── ├── ├── ├── St_Kitts
├── ├── └── ├── ├── ├── ├── St_Lucia
├── ├── └── ├── ├── ├── ├── St_Thomas
├── ├── └── ├── ├── ├── ├── St_Vincent
├── ├── └── ├── ├── ├── ├── Swift_Current
├── ├── └── ├── ├── ├── ├── Tegucigalpa
├── ├── └── ├── ├── ├── ├── Thule
├── ├── └── ├── ├── ├── ├── Thunder_Bay
├── ├── └── ├── ├── ├── ├── Tijuana
├── ├── └── ├── ├── ├── ├── Toronto
├── ├── └── ├── ├── ├── ├── Tortola
├── ├── └── ├── ├── ├── ├── Vancouver
├── ├── └── ├── ├── ├── ├── Virgin
├── ├── └── ├── ├── ├── ├── Whitehorse
├── ├── └── ├── ├── ├── ├── Winnipeg
├── ├── └── ├── ├── ├── ├── Yakutat
├── ├── └── ├── ├── ├── └── Yellowknife
├── ├── └── ├── ├── ├── Antarctica/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Casey
├── ├── └── ├── ├── ├── ├── Davis
├── ├── └── ├── ├── ├── ├── DumontDUrville
├── ├── └── ├── ├── ├── ├── Macquarie
├── ├── └── ├── ├── ├── ├── Mawson
├── ├── └── ├── ├── ├── ├── McMurdo
├── ├── └── ├── ├── ├── ├── Palmer
├── ├── └── ├── ├── ├── ├── Rothera
├── ├── └── ├── ├── ├── ├── South_Pole
├── ├── └── ├── ├── ├── ├── Syowa
├── ├── └── ├── ├── ├── ├── Troll
├── ├── └── ├── ├── ├── └── Vostok
├── ├── └── ├── ├── ├── Arctic/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── └── Longyearbyen
├── ├── └── ├── ├── ├── Asia/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Aden
├── ├── └── ├── ├── ├── ├── Almaty
├── ├── └── ├── ├── ├── ├── Amman
├── ├── └── ├── ├── ├── ├── Anadyr
├── ├── └── ├── ├── ├── ├── Aqtau
├── ├── └── ├── ├── ├── ├── Aqtobe
├── ├── └── ├── ├── ├── ├── Ashgabat
├── ├── └── ├── ├── ├── ├── Ashkhabad
├── ├── └── ├── ├── ├── ├── Atyrau
├── ├── └── ├── ├── ├── ├── Baghdad
├── ├── └── ├── ├── ├── ├── Bahrain
├── ├── └── ├── ├── ├── ├── Baku
├── ├── └── ├── ├── ├── ├── Bangkok
├── ├── └── ├── ├── ├── ├── Barnaul
├── ├── └── ├── ├── ├── ├── Beirut
├── ├── └── ├── ├── ├── ├── Bishkek
├── ├── └── ├── ├── ├── ├── Brunei
├── ├── └── ├── ├── ├── ├── Calcutta
├── ├── └── ├── ├── ├── ├── Chita
├── ├── └── ├── ├── ├── ├── Choibalsan
├── ├── └── ├── ├── ├── ├── Chongqing
├── ├── └── ├── ├── ├── ├── Chungking
├── ├── └── ├── ├── ├── ├── Colombo
├── ├── └── ├── ├── ├── ├── Dacca
├── ├── └── ├── ├── ├── ├── Damascus
├── ├── └── ├── ├── ├── ├── Dhaka
├── ├── └── ├── ├── ├── ├── Dili
├── ├── └── ├── ├── ├── ├── Dubai
├── ├── └── ├── ├── ├── ├── Dushanbe
├── ├── └── ├── ├── ├── ├── Famagusta
├── ├── └── ├── ├── ├── ├── Gaza
├── ├── └── ├── ├── ├── ├── Harbin
├── ├── └── ├── ├── ├── ├── Hebron
├── ├── └── ├── ├── ├── ├── Ho_Chi_Minh
├── ├── └── ├── ├── ├── ├── Hong_Kong
├── ├── └── ├── ├── ├── ├── Hovd
├── ├── └── ├── ├── ├── ├── Irkutsk
├── ├── └── ├── ├── ├── ├── Istanbul
├── ├── └── ├── ├── ├── ├── Jakarta
├── ├── └── ├── ├── ├── ├── Jayapura
├── ├── └── ├── ├── ├── ├── Jerusalem
├── ├── └── ├── ├── ├── ├── Kabul
├── ├── └── ├── ├── ├── ├── Kamchatka
├── ├── └── ├── ├── ├── ├── Karachi
├── ├── └── ├── ├── ├── ├── Kashgar
├── ├── └── ├── ├── ├── ├── Kathmandu
├── ├── └── ├── ├── ├── ├── Katmandu
├── ├── └── ├── ├── ├── ├── Khandyga
├── ├── └── ├── ├── ├── ├── Kolkata
├── ├── └── ├── ├── ├── ├── Krasnoyarsk
├── ├── └── ├── ├── ├── ├── Kuala_Lumpur
├── ├── └── ├── ├── ├── ├── Kuching
├── ├── └── ├── ├── ├── ├── Kuwait
├── ├── └── ├── ├── ├── ├── Macao
├── ├── └── ├── ├── ├── ├── Macau
├── ├── └── ├── ├── ├── ├── Magadan
├── ├── └── ├── ├── ├── ├── Makassar
├── ├── └── ├── ├── ├── ├── Manila
├── ├── └── ├── ├── ├── ├── Muscat
├── ├── └── ├── ├── ├── ├── Nicosia
├── ├── └── ├── ├── ├── ├── Novokuznetsk
├── ├── └── ├── ├── ├── ├── Novosibirsk
├── ├── └── ├── ├── ├── ├── Omsk
├── ├── └── ├── ├── ├── ├── Oral
├── ├── └── ├── ├── ├── ├── Phnom_Penh
├── ├── └── ├── ├── ├── ├── Pontianak
├── ├── └── ├── ├── ├── ├── Pyongyang
├── ├── └── ├── ├── ├── ├── Qatar
├── ├── └── ├── ├── ├── ├── Qostanay
├── ├── └── ├── ├── ├── ├── Qyzylorda
├── ├── └── ├── ├── ├── ├── Rangoon
├── ├── └── ├── ├── ├── ├── Riyadh
├── ├── └── ├── ├── ├── ├── Saigon
├── ├── └── ├── ├── ├── ├── Sakhalin
├── ├── └── ├── ├── ├── ├── Samarkand
├── ├── └── ├── ├── ├── ├── Seoul
├── ├── └── ├── ├── ├── ├── Shanghai
├── ├── └── ├── ├── ├── ├── Singapore
├── ├── └── ├── ├── ├── ├── Srednekolymsk
├── ├── └── ├── ├── ├── ├── Taipei
├── ├── └── ├── ├── ├── ├── Tashkent
├── ├── └── ├── ├── ├── ├── Tbilisi
├── ├── └── ├── ├── ├── ├── Tehran
├── ├── └── ├── ├── ├── ├── Tel_Aviv
├── ├── └── ├── ├── ├── ├── Thimbu
├── ├── └── ├── ├── ├── ├── Thimphu
├── ├── └── ├── ├── ├── ├── Tokyo
├── ├── └── ├── ├── ├── ├── Tomsk
├── ├── └── ├── ├── ├── ├── Ujung_Pandang
├── ├── └── ├── ├── ├── ├── Ulaanbaatar
├── ├── └── ├── ├── ├── ├── Ulan_Bator
├── ├── └── ├── ├── ├── ├── Urumqi
├── ├── └── ├── ├── ├── ├── Ust-Nera
├── ├── └── ├── ├── ├── ├── Vientiane
├── ├── └── ├── ├── ├── ├── Vladivostok
├── ├── └── ├── ├── ├── ├── Yakutsk
├── ├── └── ├── ├── ├── ├── Yangon
├── ├── └── ├── ├── ├── ├── Yekaterinburg
├── ├── └── ├── ├── ├── └── Yerevan
├── ├── └── ├── ├── ├── Atlantic/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Azores
├── ├── └── ├── ├── ├── ├── Bermuda
├── ├── └── ├── ├── ├── ├── Canary
├── ├── └── ├── ├── ├── ├── Cape_Verde
├── ├── └── ├── ├── ├── ├── Faeroe
├── ├── └── ├── ├── ├── ├── Faroe
├── ├── └── ├── ├── ├── ├── Jan_Mayen
├── ├── └── ├── ├── ├── ├── Madeira
├── ├── └── ├── ├── ├── ├── Reykjavik
├── ├── └── ├── ├── ├── ├── South_Georgia
├── ├── └── ├── ├── ├── ├── St_Helena
├── ├── └── ├── ├── ├── └── Stanley
├── ├── └── ├── ├── ├── Australia/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── ACT
├── ├── └── ├── ├── ├── ├── Adelaide
├── ├── └── ├── ├── ├── ├── Brisbane
├── ├── └── ├── ├── ├── ├── Broken_Hill
├── ├── └── ├── ├── ├── ├── Canberra
├── ├── └── ├── ├── ├── ├── Currie
├── ├── └── ├── ├── ├── ├── Darwin
├── ├── └── ├── ├── ├── ├── Eucla
├── ├── └── ├── ├── ├── ├── Hobart
├── ├── └── ├── ├── ├── ├── LHI
├── ├── └── ├── ├── ├── ├── Lindeman
├── ├── └── ├── ├── ├── ├── Lord_Howe
├── ├── └── ├── ├── ├── ├── Melbourne
├── ├── └── ├── ├── ├── ├── North
├── ├── └── ├── ├── ├── ├── NSW
├── ├── └── ├── ├── ├── ├── Perth
├── ├── └── ├── ├── ├── ├── Queensland
├── ├── └── ├── ├── ├── ├── South
├── ├── └── ├── ├── ├── ├── Sydney
├── ├── └── ├── ├── ├── ├── Tasmania
├── ├── └── ├── ├── ├── ├── Victoria
├── ├── └── ├── ├── ├── ├── West
├── ├── └── ├── ├── ├── └── Yancowinna
├── ├── └── ├── ├── ├── Brazil/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Acre
├── ├── └── ├── ├── ├── ├── DeNoronha
├── ├── └── ├── ├── ├── ├── East
├── ├── └── ├── ├── ├── └── West
├── ├── └── ├── ├── ├── Canada/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Atlantic
├── ├── └── ├── ├── ├── ├── Central
├── ├── └── ├── ├── ├── ├── Eastern
├── ├── └── ├── ├── ├── ├── Mountain
├── ├── └── ├── ├── ├── ├── Newfoundland
├── ├── └── ├── ├── ├── ├── Pacific
├── ├── └── ├── ├── ├── ├── Saskatchewan
├── ├── └── ├── ├── ├── └── Yukon
├── ├── └── ├── ├── ├── CET
├── ├── └── ├── ├── ├── Chile/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Continental
├── ├── └── ├── ├── ├── └── EasterIsland
├── ├── └── ├── ├── ├── CST6CDT
├── ├── └── ├── ├── ├── Cuba
├── ├── └── ├── ├── ├── EET
├── ├── └── ├── ├── ├── Egypt
├── ├── └── ├── ├── ├── Eire
├── ├── └── ├── ├── ├── EST
├── ├── └── ├── ├── ├── EST5EDT
├── ├── └── ├── ├── ├── Etc/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── GMT
├── ├── └── ├── ├── ├── ├── GMT+0
├── ├── └── ├── ├── ├── ├── GMT+1
├── ├── └── ├── ├── ├── ├── GMT+10
├── ├── └── ├── ├── ├── ├── GMT+11
├── ├── └── ├── ├── ├── ├── GMT+12
├── ├── └── ├── ├── ├── ├── GMT+2
├── ├── └── ├── ├── ├── ├── GMT+3
├── ├── └── ├── ├── ├── ├── GMT+4
├── ├── └── ├── ├── ├── ├── GMT+5
├── ├── └── ├── ├── ├── ├── GMT+6
├── ├── └── ├── ├── ├── ├── GMT+7
├── ├── └── ├── ├── ├── ├── GMT+8
├── ├── └── ├── ├── ├── ├── GMT+9
├── ├── └── ├── ├── ├── ├── GMT-0
├── ├── └── ├── ├── ├── ├── GMT-1
├── ├── └── ├── ├── ├── ├── GMT-10
├── ├── └── ├── ├── ├── ├── GMT-11
├── ├── └── ├── ├── ├── ├── GMT-12
├── ├── └── ├── ├── ├── ├── GMT-13
├── ├── └── ├── ├── ├── ├── GMT-14
├── ├── └── ├── ├── ├── ├── GMT-2
├── ├── └── ├── ├── ├── ├── GMT-3
├── ├── └── ├── ├── ├── ├── GMT-4
├── ├── └── ├── ├── ├── ├── GMT-5
├── ├── └── ├── ├── ├── ├── GMT-6
├── ├── └── ├── ├── ├── ├── GMT-7
├── ├── └── ├── ├── ├── ├── GMT-8
├── ├── └── ├── ├── ├── ├── GMT-9
├── ├── └── ├── ├── ├── ├── GMT0
├── ├── └── ├── ├── ├── ├── Greenwich
├── ├── └── ├── ├── ├── ├── UCT
├── ├── └── ├── ├── ├── ├── Universal
├── ├── └── ├── ├── ├── ├── UTC
├── ├── └── ├── ├── ├── └── Zulu
├── ├── └── ├── ├── ├── Europe/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Amsterdam
├── ├── └── ├── ├── ├── ├── Andorra
├── ├── └── ├── ├── ├── ├── Astrakhan
├── ├── └── ├── ├── ├── ├── Athens
├── ├── └── ├── ├── ├── ├── Belfast
├── ├── └── ├── ├── ├── ├── Belgrade
├── ├── └── ├── ├── ├── ├── Berlin
├── ├── └── ├── ├── ├── ├── Bratislava
├── ├── └── ├── ├── ├── ├── Brussels
├── ├── └── ├── ├── ├── ├── Bucharest
├── ├── └── ├── ├── ├── ├── Budapest
├── ├── └── ├── ├── ├── ├── Busingen
├── ├── └── ├── ├── ├── ├── Chisinau
├── ├── └── ├── ├── ├── ├── Copenhagen
├── ├── └── ├── ├── ├── ├── Dublin
├── ├── └── ├── ├── ├── ├── Gibraltar
├── ├── └── ├── ├── ├── ├── Guernsey
├── ├── └── ├── ├── ├── ├── Helsinki
├── ├── └── ├── ├── ├── ├── Isle_of_Man
├── ├── └── ├── ├── ├── ├── Istanbul
├── ├── └── ├── ├── ├── ├── Jersey
├── ├── └── ├── ├── ├── ├── Kaliningrad
├── ├── └── ├── ├── ├── ├── Kiev
├── ├── └── ├── ├── ├── ├── Kirov
├── ├── └── ├── ├── ├── ├── Kyiv
├── ├── └── ├── ├── ├── ├── Lisbon
├── ├── └── ├── ├── ├── ├── Ljubljana
├── ├── └── ├── ├── ├── ├── London
├── ├── └── ├── ├── ├── ├── Luxembourg
├── ├── └── ├── ├── ├── ├── Madrid
├── ├── └── ├── ├── ├── ├── Malta
├── ├── └── ├── ├── ├── ├── Mariehamn
├── ├── └── ├── ├── ├── ├── Minsk
├── ├── └── ├── ├── ├── ├── Monaco
├── ├── └── ├── ├── ├── ├── Moscow
├── ├── └── ├── ├── ├── ├── Nicosia
├── ├── └── ├── ├── ├── ├── Oslo
├── ├── └── ├── ├── ├── ├── Paris
├── ├── └── ├── ├── ├── ├── Podgorica
├── ├── └── ├── ├── ├── ├── Prague
├── ├── └── ├── ├── ├── ├── Riga
├── ├── └── ├── ├── ├── ├── Rome
├── ├── └── ├── ├── ├── ├── Samara
├── ├── └── ├── ├── ├── ├── San_Marino
├── ├── └── ├── ├── ├── ├── Sarajevo
├── ├── └── ├── ├── ├── ├── Saratov
├── ├── └── ├── ├── ├── ├── Simferopol
├── ├── └── ├── ├── ├── ├── Skopje
├── ├── └── ├── ├── ├── ├── Sofia
├── ├── └── ├── ├── ├── ├── Stockholm
├── ├── └── ├── ├── ├── ├── Tallinn
├── ├── └── ├── ├── ├── ├── Tirane
├── ├── └── ├── ├── ├── ├── Tiraspol
├── ├── └── ├── ├── ├── ├── Ulyanovsk
├── ├── └── ├── ├── ├── ├── Uzhgorod
├── ├── └── ├── ├── ├── ├── Vaduz
├── ├── └── ├── ├── ├── ├── Vatican
├── ├── └── ├── ├── ├── ├── Vienna
├── ├── └── ├── ├── ├── ├── Vilnius
├── ├── └── ├── ├── ├── ├── Volgograd
├── ├── └── ├── ├── ├── ├── Warsaw
├── ├── └── ├── ├── ├── ├── Zagreb
├── ├── └── ├── ├── ├── ├── Zaporozhye
├── ├── └── ├── ├── ├── └── Zurich
├── ├── └── ├── ├── ├── Factory
├── ├── └── ├── ├── ├── GB
├── ├── └── ├── ├── ├── GB-Eire
├── ├── └── ├── ├── ├── GMT
├── ├── └── ├── ├── ├── GMT+0
├── ├── └── ├── ├── ├── GMT-0
├── ├── └── ├── ├── ├── GMT0
├── ├── └── ├── ├── ├── Greenwich
├── ├── └── ├── ├── ├── Hongkong
├── ├── └── ├── ├── ├── HST
├── ├── └── ├── ├── ├── Iceland
├── ├── └── ├── ├── ├── Indian/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Antananarivo
├── ├── └── ├── ├── ├── ├── Chagos
├── ├── └── ├── ├── ├── ├── Christmas
├── ├── └── ├── ├── ├── ├── Cocos
├── ├── └── ├── ├── ├── ├── Comoro
├── ├── └── ├── ├── ├── ├── Kerguelen
├── ├── └── ├── ├── ├── ├── Mahe
├── ├── └── ├── ├── ├── ├── Maldives
├── ├── └── ├── ├── ├── ├── Mauritius
├── ├── └── ├── ├── ├── ├── Mayotte
├── ├── └── ├── ├── ├── └── Reunion
├── ├── └── ├── ├── ├── Iran
├── ├── └── ├── ├── ├── iso3166.tab
├── ├── └── ├── ├── ├── Israel
├── ├── └── ├── ├── ├── Jamaica
├── ├── └── ├── ├── ├── Japan
├── ├── └── ├── ├── ├── Kwajalein
├── ├── └── ├── ├── ├── leapseconds
├── ├── └── ├── ├── ├── Libya
├── ├── └── ├── ├── ├── MET
├── ├── └── ├── ├── ├── Mexico/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── BajaNorte
├── ├── └── ├── ├── ├── ├── BajaSur
├── ├── └── ├── ├── ├── └── General
├── ├── └── ├── ├── ├── MST
├── ├── └── ├── ├── ├── MST7MDT
├── ├── └── ├── ├── ├── Navajo
├── ├── └── ├── ├── ├── NZ
├── ├── └── ├── ├── ├── NZ-CHAT
├── ├── └── ├── ├── ├── Pacific/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Apia
├── ├── └── ├── ├── ├── ├── Auckland
├── ├── └── ├── ├── ├── ├── Bougainville
├── ├── └── ├── ├── ├── ├── Chatham
├── ├── └── ├── ├── ├── ├── Chuuk
├── ├── └── ├── ├── ├── ├── Easter
├── ├── └── ├── ├── ├── ├── Efate
├── ├── └── ├── ├── ├── ├── Enderbury
├── ├── └── ├── ├── ├── ├── Fakaofo
├── ├── └── ├── ├── ├── ├── Fiji
├── ├── └── ├── ├── ├── ├── Funafuti
├── ├── └── ├── ├── ├── ├── Galapagos
├── ├── └── ├── ├── ├── ├── Gambier
├── ├── └── ├── ├── ├── ├── Guadalcanal
├── ├── └── ├── ├── ├── ├── Guam
├── ├── └── ├── ├── ├── ├── Honolulu
├── ├── └── ├── ├── ├── ├── Johnston
├── ├── └── ├── ├── ├── ├── Kanton
├── ├── └── ├── ├── ├── ├── Kiritimati
├── ├── └── ├── ├── ├── ├── Kosrae
├── ├── └── ├── ├── ├── ├── Kwajalein
├── ├── └── ├── ├── ├── ├── Majuro
├── ├── └── ├── ├── ├── ├── Marquesas
├── ├── └── ├── ├── ├── ├── Midway
├── ├── └── ├── ├── ├── ├── Nauru
├── ├── └── ├── ├── ├── ├── Niue
├── ├── └── ├── ├── ├── ├── Norfolk
├── ├── └── ├── ├── ├── ├── Noumea
├── ├── └── ├── ├── ├── ├── Pago_Pago
├── ├── └── ├── ├── ├── ├── Palau
├── ├── └── ├── ├── ├── ├── Pitcairn
├── ├── └── ├── ├── ├── ├── Pohnpei
├── ├── └── ├── ├── ├── ├── Ponape
├── ├── └── ├── ├── ├── ├── Port_Moresby
├── ├── └── ├── ├── ├── ├── Rarotonga
├── ├── └── ├── ├── ├── ├── Saipan
├── ├── └── ├── ├── ├── ├── Samoa
├── ├── └── ├── ├── ├── ├── Tahiti
├── ├── └── ├── ├── ├── ├── Tarawa
├── ├── └── ├── ├── ├── ├── Tongatapu
├── ├── └── ├── ├── ├── ├── Truk
├── ├── └── ├── ├── ├── ├── Wake
├── ├── └── ├── ├── ├── ├── Wallis
├── ├── └── ├── ├── ├── └── Yap
├── ├── └── ├── ├── ├── Poland
├── ├── └── ├── ├── ├── Portugal
├── ├── └── ├── ├── ├── PRC
├── ├── └── ├── ├── ├── PST8PDT
├── ├── └── ├── ├── ├── ROC
├── ├── └── ├── ├── ├── ROK
├── ├── └── ├── ├── ├── Singapore
├── ├── └── ├── ├── ├── Turkey
├── ├── └── ├── ├── ├── tzdata.zi
├── ├── └── ├── ├── ├── UCT
├── ├── └── ├── ├── ├── Universal
├── ├── └── ├── ├── ├── US/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── Alaska
├── ├── └── ├── ├── ├── ├── Aleutian
├── ├── └── ├── ├── ├── ├── Arizona
├── ├── └── ├── ├── ├── ├── Central
├── ├── └── ├── ├── ├── ├── East-Indiana
├── ├── └── ├── ├── ├── ├── Eastern
├── ├── └── ├── ├── ├── ├── Hawaii
├── ├── └── ├── ├── ├── ├── Indiana-Starke
├── ├── └── ├── ├── ├── ├── Michigan
├── ├── └── ├── ├── ├── ├── Mountain
├── ├── └── ├── ├── ├── ├── Pacific
├── ├── └── ├── ├── ├── └── Samoa
├── ├── └── ├── ├── ├── UTC
├── ├── └── ├── ├── ├── W-SU
├── ├── └── ├── ├── ├── WET
├── ├── └── ├── ├── ├── zone.tab
├── ├── └── ├── ├── ├── zone1970.tab
├── ├── └── ├── ├── ├── zonenow.tab
├── ├── └── ├── ├── └── Zulu
├── ├── └── ├── └── zones
├── ├── └── ├── tzdata-2025.2.dist-info/
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── licenses/
├── ├── └── ├── ├── ├── LICENSE
├── ├── └── ├── ├── └── licenses/
├── ├── └── ├── ├── └── └── LICENSE_APACHE
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── top_level.txt
├── ├── └── ├── └── WHEEL
├── ├── └── ├── wheel/
├── ├── └── ├── ├── __init__.py
├── ├── └── ├── ├── __main__.py
├── ├── └── ├── ├── _bdist_wheel.py
├── ├── └── ├── ├── _setuptools_logging.py
├── ├── └── ├── ├── bdist_wheel.py
├── ├── └── ├── ├── cli/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── convert.py
├── ├── └── ├── ├── ├── pack.py
├── ├── └── ├── ├── ├── tags.py
├── ├── └── ├── ├── └── unpack.py
├── ├── └── ├── ├── macosx_libfile.py
├── ├── └── ├── ├── metadata.py
├── ├── └── ├── ├── util.py
├── ├── └── ├── ├── vendored/
├── ├── └── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── packaging/
├── ├── └── ├── ├── ├── ├── __init__.py
├── ├── └── ├── ├── ├── ├── _elffile.py
├── ├── └── ├── ├── ├── ├── _manylinux.py
├── ├── └── ├── ├── ├── ├── _musllinux.py
├── ├── └── ├── ├── ├── ├── _parser.py
├── ├── └── ├── ├── ├── ├── _structures.py
├── ├── └── ├── ├── ├── ├── _tokenizer.py
├── ├── └── ├── ├── ├── ├── LICENSE
├── ├── └── ├── ├── ├── ├── LICENSE.APACHE
├── ├── └── ├── ├── ├── ├── LICENSE.BSD
├── ├── └── ├── ├── ├── ├── markers.py
├── ├── └── ├── ├── ├── ├── requirements.py
├── ├── └── ├── ├── ├── ├── specifiers.py
├── ├── └── ├── ├── ├── ├── tags.py
├── ├── └── ├── ├── ├── ├── utils.py
├── ├── └── ├── ├── ├── └── version.py
├── ├── └── ├── ├── └── vendor.txt
├── ├── └── ├── └── wheelfile.py
├── ├── └── ├── wheel-0.45.1.dist-info/
├── ├── └── ├── ├── entry_points.txt
├── ├── └── ├── ├── INSTALLER
├── ├── └── ├── ├── LICENSE.txt
├── ├── └── ├── ├── METADATA
├── ├── └── ├── ├── RECORD
├── ├── └── ├── ├── REQUESTED
├── ├── └── ├── └── WHEEL
├── ├── └── └── yaml/
├── ├── └── └── ├── __init__.py
├── ├── └── └── ├── _yaml.cp312-win_amd64.pyd
├── ├── └── └── ├── composer.py
├── ├── └── └── ├── constructor.py
├── ├── └── └── ├── cyaml.py
├── ├── └── └── ├── dumper.py
├── ├── └── └── ├── emitter.py
├── ├── └── └── ├── error.py
├── ├── └── └── ├── events.py
├── ├── └── └── ├── loader.py
├── ├── └── └── ├── nodes.py
├── ├── └── └── ├── parser.py
├── ├── └── └── ├── reader.py
├── ├── └── └── ├── representer.py
├── ├── └── └── ├── resolver.py
├── ├── └── └── ├── scanner.py
├── ├── └── └── ├── serializer.py
├── ├── └── └── └── tokens.py
├── ├── pyvenv.cfg
├── ├── Scripts/
├── ├── ├── activate
├── ├── ├── activate.bat
├── ├── ├── Activate.ps1
├── ├── ├── deactivate.bat
├── ├── ├── f2py.exe
├── ├── ├── fonttools.exe
├── ├── ├── numpy-config.exe
├── ├── ├── pip.exe
├── ├── ├── pip3.12.exe
├── ├── ├── pip3.exe
├── ├── ├── pyftmerge.exe
├── ├── ├── pyftsubset.exe
├── ├── ├── python.exe
├── ├── ├── pythonw.exe
├── ├── ├── ttx.exe
├── ├── └── wheel.exe
├── └── share/
├── └── └── man/
├── └── └── └── man1/
├── └── └── └── └── ttx.1
└── vireon_preview_release_notes_v0.1.md
```
