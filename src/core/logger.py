import logging

def get_logger():
    l = logging.getLogger('prober')
    l.setLevel(logging.INFO)
    return l
