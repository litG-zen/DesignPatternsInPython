# The interface segregation principle states that no client should be forced to depend on methods it does not use.
#  In other words, an interface should have only the methods that are relevant to the implementing class.


from abc import ABC, abstractmethod


# Bad Example:
class Machine(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

class Printer(Machine):
    def print(self, document):
        print(f"Printing document: {document}")

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan documents")

    def fax(self, document):
        raise NotImplementedError("Printer cannot fax documents")

class Scanner(Machine):
    def print(self, document):
        raise NotImplementedError("Scanner cannot print documents")

    def scan(self, document):
        print(f"Scanning document: {document}")

    def fax(self, document):
        raise NotImplementedError("Scanner cannot fax documents")   

class FaxMachine(Machine):
    def print(self, document):
        raise NotImplementedError("Fax machine cannot print documents")

    def scan(self, document):
        raise NotImplementedError("Fax machine cannot scan documents")

    def fax(self, document):
        print(f"Faxing document: {document}")   


# As we can see, it is not necessary for the implementing classes to have all the methods defined in the Machine interface. 
# This violates the Interface Segregation Principle, as clients are forced to depend on methods they do not use.


# Good Example:

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass    

class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class OnlyPrinter(Printer):
    def print(self, document):
        print(f"Printing document: {document}") 


class OnlyScanner(Scanner):
    def scan(self, document):
        print(f"Scanning document: {document}")

class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print(f"Printing document: {document}")

    def scan(self, document):
        print(f"Scanning document: {document}") 

class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    def print(self, document):
        print(f"Printing document: {document}")

    def scan(self, document):
        print(f"Scanning document: {document}")

    def fax(self, document):
        print(f"Faxing document: {document}")   