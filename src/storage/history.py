import json
import os

def save_run(path: str, stats: dict):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w') as f:
        json.dump(stats, f)
