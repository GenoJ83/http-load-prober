from src.models.result import RequestResult

def test_request_result():
    r = RequestResult(status_code=200, latency_ms=12.4, bytes_received=1024)
    assert r.status_code == 200
    assert r.latency_ms == 12.4
