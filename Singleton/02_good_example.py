class Logger:
    _instance = None

    def __new__(cls,file_name):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.file_name = file_name
            cls._instance.log_count = 0
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")
        self.log_count += 1



log1 = Logger("main")
log2 = Logger("main")

print(log1 is log2)  # Output: True
print(id(log1))
print(id(log2))

print(log1.log("User created"))
print(log2.log("OTP sent"))
print(log1.log_count)  # Output: 2
print(log2.log_count)  # Output: 2