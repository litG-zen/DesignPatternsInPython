# Dependancy inversion principle states that high-level modules should not depend on low-level modules. 
# Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.



# Bad Example:

from enum import Enum
from abc import ABC, abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person(object):
    def __init__(self, name):
        self.name = name 

class Relationships(object):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

class Research(object):
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'Lit' and r[1] == Relationship.PARENT:
                print(f"Lit has a child called {r[2].name}")


# As we can see, the Research class is tightly coupled to the Relationships class.
# If we change the internal data structure of the Relationships class, we will have to change the Research class as well.

# Improved Example:

class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass

class RelationshipsImproved(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        return [r[2] for r in self.relations if r[0].name == name and r[1] == Relationship.PARENT]

class Research(object):
    def __init__(self, relationships):
        for child in relationships.find_all_children_of('Lit'):
            print(f"Lit has a child called {child.name}")




