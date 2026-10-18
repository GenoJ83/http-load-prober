import json
def load_bench_config(path: str):
    with open(path) as f: return json.load(f)
