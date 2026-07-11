# The Liskov Substitution Principle states that objects of a superclass     
# should be replaceable with objects of its subclasses without affecting the correctness of the program.


# Antipattern Example:
class Bird:
    def fly(self):
        pass
    def eat(self):
        pass


class Duck(Bird):
    def fly(self):
        print("Duck is flying")
    def eat(self):
        print("Duck is eating") 

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly") # Child class should not break the behavior of the parent class
    def eat(self):
        print("Penguin is eating")  


# Bad Example:
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance 
    
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds in savings account")
        else:
            self.balance -= amount
            print(f"Withdrawing ${amount} from savings account. New balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing ${amount} into savings account")


class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def withdraw(self, amount):
        raise Exception("Withdrawals are not allowed from a fixed deposit account") # Child class should not break the behavior of the parent class
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing ${amount} into fixed deposit account")

s = SavingsAccount(1000)
s.withdraw(500)  # Works fine
s.deposit(200)   # Works fine


f = FixedDepositAccount(5000)
f.deposit(1000)  # Works fine
#f.withdraw(500)  # Raises Exception: Withdrawals are not allowed from a fixed deposit



# Now the Liskov Substitution Principle states that we need to futher break the base class in such a way
# that the child classes do not break the behavior of the parent class. 
# We can do this by creating a new base class for accounts that allow withdrawals
# and another base class for accounts that do not allow withdrawals.
class BankAccountNew(ABC):
    def __init__(self, balance):
        self.balance = balance 
    
    @abstractmethod
    def deposit(self):
        pass

    def __str__(self):
        return f"Balance: ${self.balance}"

class WithdrawableAccount(BankAccountNew):   
    @abstractmethod
    def withdraw(self):
        pass

class SavingsAccountNew(WithdrawableAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds in savings account")
        else:
            self.balance -= amount
            print(f"Withdrawing ${amount} from savings account. New balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing ${amount} into savings account")


class FixedDepositAccountNew(BankAccountNew):
    def __init__(self, balance):
        super().__init__(balance)
    
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing ${amount} into fixed deposit account")



s2 = SavingsAccountNew(1000)
s2.withdraw(500)  # Works fine
s2.deposit(200)   # Works fine
print(s2)

f2 = FixedDepositAccountNew(5000)
f2.deposit(1000)  # Works fine
print(f2)