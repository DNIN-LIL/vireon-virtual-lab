import yaml
from pathlib import Path

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def merge_configs(default_path, local_path=None):
    cfg = load_config(default_path)
    if local_path and Path(local_path).exists():
        local = load_config(local_path)
        cfg.update(local)
    return cfg
