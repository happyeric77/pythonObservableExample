class Observer:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"{self.name} got message {message}")

class Observalbe:
    def __init__(self, events):
        self.observers = {event: dict() for event in events}

    def get_observers(self, event):
        return self.observers[event]

    def register(self, who, event, callback = None):
        if callback == None:
            callback = getattr(who, "update")
        self.get_observers(event)[who] = callback
        
    def unregister(self, event, who):
        del self.get_observers(event)[who]
    def dispatch(self, event, message):
        for _, callback in self.get_observers(event).items():
            callback(message)

    