from urllib.parse import urlparse

def validate_target_url(url: str):
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        raise ValueError('Invalid protocol scheme')
    return True
