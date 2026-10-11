class EventBus:
    def __init__(self):
        self.listeners = {}
    def on(self, event, fn):
        self.listeners.setdefault(event, []).append(fn)
    def emit(self, event, *args):
        for fn in self.listeners.get(event, []):
            fn(*args)
