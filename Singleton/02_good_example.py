class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            # Initialize any attributes here
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")



log1 = Logger()
log2 = Logger()

print(log1 is log2)  # Output: True
print(id(log1))
print(id(log2))