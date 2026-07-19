class Logger:
    def __init__(self,file_name):
        self.file_name = file_name
        self.log_count = 0

    def log(self, message):
        print(f"Logging message to {self.file_name}: {message}")
        self.log_count += 1
    

# Now suppose that tht logger is used in multiple places in the code.
# file1 = userservice
log1 = Logger("app_logs.txt")
# file2 = otp
log2 = Logger("app_logs.txt")
# file3 = emailservice
log3 = Logger("app_logs.txt")


log1.log("User created")
log2.log("OTP sent")
log3.log("Email sent") 


print(log1.log_count)  # Output: 1
print(log2.log_count)  # Output: 1
print(log3.log_count)  # Output: 1

#this is happening bcz all three are diff diff instances of the logger class and they are not sharing the same state.

print(id(log1))
print(id(log2))
print(id(log3))
#All ids will be different which means they are different instances of the logger class.