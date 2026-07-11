# The Single responsibility principle(aka SOC separation of concern) states that a class should have only one reason to change.
# This means that a class should only have one responsibility or job.
# If a class has more than one responsibility, it becomes more difficult to maintain and understand.


# Pattern Example
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)
    
    # The Journal class has two responsibilities: managing journal entries and persisting them to storage.

    '''
    The below mentioned functions are violating the single responsibility principle because 
    they are responsible for persisting the journal entries to storage, 
    which is not the responsibility of the Journal class.
    '''

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))
    
    def load(self, filename):
        with open(filename, 'r') as f:
            self.entries = f.read().splitlines()
            self.count = len(self.entries)
        print(f"Journal loaded from {filename}", self.entries)
    
    def load_from_web(self, url):
        # code to load journal entries from a web service
        pass  


# A better approach could be to create a separate class that
# is responsible for persisting the journal entries to storage. 
# This class could be called PersistenceManager and would have methods for saving and loading journal entries.

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal))

    @staticmethod
    def load_from_file(journal, filename):
        with open(filename, 'r') as f:
            journal.entries = f.read().splitlines()
            journal.count = len(journal.entries)
        print(f"Journal loaded from {filename}", journal.entries)




# The Antipattern Example : Antipattern(known as GodObject) for the single responsibility
# principle is to have a class that has multiple responsibilities.
class JournalWithPersistence:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))
    
    def load(self, filename):
        with open(filename, 'r') as f:
            self.entries = f.read().splitlines()
            self.count = len(self.entries)
        print(f"Journal loaded from {filename}", self.entries)
    
    def load_from_web(self, url):
        # code to load journal entries from a web service
        pass    

