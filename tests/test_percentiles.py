from src.stats.percentiles import compute_percentiles

def test_percentiles():
    data = [10.0, 20.0, 30.0, 40.0, 50.0, 100.0]
    p = compute_percentiles(data)
    assert p['total'] == 6
    assert p['p50'] >= 20.0
