class ProbeError(Exception): pass
class ConnectionTimeoutError(ProbeError): pass
class RateLimitExceededError(ProbeError): pass
