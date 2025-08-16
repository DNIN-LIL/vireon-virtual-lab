# core/config_loader.py
import yaml
from pathlib import Path

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def _deep_update(dst, src):
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            _deep_update(dst[k], v)
        else:
            dst[k] = v

def merge_configs(default_path, local_path=None):
    cfg = load_config(default_path)
    if local_path and Path(local_path).exists():
        local = load_config(local_path)
        _deep_update(cfg, local)
    return cfg
