def generate_dashboard(stats: dict) -> str:
    return f"<html><body><h1>HTTP Load Prober</h1><p>Requests: {stats.get('total')}</p><p>P95: {stats.get('p95')}ms</p></body></html>"
