import argparse

def parse_args():
    p = argparse.ArgumentParser(prog='httpprober')
    p.add_argument('--url', required=True)
    p.add_argument('--concurrency', type=int, default=10)
    p.add_argument('--requests', type=int, default=100)
    return p
