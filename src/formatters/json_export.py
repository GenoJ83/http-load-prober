import json

def export_metrics_json(stats: dict) -> str:
    return json.dumps(stats, indent=2)
