class Observer1:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"{self.name} got message {message}")

class Observer2:
    def __init__(self, name):
        self.name = name
    def renew(self, message):
        print(f"{self.name} got message {message}")

class Observalbe:
    def __init__(self):
        self.observers = dict()
    def register(self, who, callback=None):
        if callback == None:
            callback = getattr(who, "update")
        self.observers[who] = callback
    def unregister(self, who):
        del self.observers[who]
    def dispatch(self, message):
        for _, callback in self.observers.items():
            callback(message)

    