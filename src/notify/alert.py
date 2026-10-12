def trigger_slo_alert(p99_latency: float, threshold: float):
    if p99_latency > threshold:
        print(f'[SLO BREACH] P99 {p99_latency}ms exceeds threshold {threshold}ms')
