def print_live_metrics(completed, total, rps):
    print(f'Done: {completed}/{total} | RPS: {rps:.1f}', end='\r')
