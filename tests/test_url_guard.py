import pytest
from src.security.url_guard import validate_target_url

def test_valid_url():
    assert validate_target_url('https://example.com')
    with pytest.raises(ValueError):
        validate_target_url('ftp://bad.com')
