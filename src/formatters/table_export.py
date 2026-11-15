def format_summary_table(stats: dict) -> str:
    return f"Requests: {stats.get('total')}\np50: {stats.get('p50')}ms\np95: {stats.get('p95')}ms\np99: {stats.get('p99')}ms"
