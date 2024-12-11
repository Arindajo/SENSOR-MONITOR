class BaseSensor:
    def __init__(self, name):
        self.name = name

    def connect(self):
        raise NotImplementedError("The 'connect' method must be implemented by subclasses.")

    def read_processed(self):
        raise NotImplementedError("The 'read_processed' method must be implemented by subclasses.")
