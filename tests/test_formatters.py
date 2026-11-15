from src.formatters.table_export import format_summary_table

def test_table():
    s = format_summary_table({'total': 10, 'p50': 5, 'p95': 20, 'p99': 30})
    assert 'p95: 20' in s
