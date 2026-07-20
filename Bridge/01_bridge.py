from abc import ABC,abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine start")

class DieselEngine(Engine):
    def start(self):
        print("Diesel engine start")

class ElectricEngine(Engine):
    def start(self):
        print("Electric engine start")


class Car(ABC):
    def __init__(self,engine:Engine):
        self.engine = engine
    def drive(self):
        pass

class SUV(Car):
    def drive(self):
        self.engine.start()
        print("SUV drive mode on! lets go")
    

class Sedan(Car):
    def drive(self):
        self.engine.start()
        print("Sedan drive mode on! lets go")

class Hatchback(Car):
    def drive(self):
        self.engine.start()
        print("Hatchback drive mode on! lets go")
    

if __name__=="__main__":
    petrol_eng = PetrolEngine()
    diesel_eng = DieselEngine()
    elec_eng = ElectricEngine()

    petrol_eng.start()
    tesla = Sedan(elec_eng)
    tesla.drive()