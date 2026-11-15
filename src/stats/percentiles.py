import numpy as np
from typing import List

def compute_percentiles(latencies: List[float]):
    if not latencies: return {}
    arr = np.array(latencies)
    return {
        'p50': float(np.percentile(arr, 50)),
        'p90': float(np.percentile(arr, 90)),
        'p95': float(np.percentile(arr, 95)),
        'p99': float(np.percentile(arr, 99)),
        'mean': float(np.mean(arr)),
        'total': len(arr)
    }
