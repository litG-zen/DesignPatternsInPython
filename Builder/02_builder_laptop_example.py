# Builder design pattern is a creational design pattern that allows for the step-by-step construction of complex objects. 
# It separates the construction of an object from its representation,
# allowing the same construction process to create different representations.

# Problem : construct a complex object in step-by-step and readable manner.
# Solution : method-chaining (fluent interface) to build the object step-by-step.


# Builder Pattern Example: Laptop Configuration


# Bad Example: Directly creating a Laptop object with many parameters can lead to confusion and errors,
# especially when there are optional parameters.
class Laptop:
    def __init__(self, cpu:str, ram:str, storage:str, gpu:str=None, color:str=None, backlit_keyboard:bool=False, screen_size:str=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.color = color
        self.screen_size = screen_size
        self.backlit_keyboard = backlit_keyboard

    
    def display_specs(self):
        specs = f"Laptop Specifications:\n"
        specs += f"CPU: {self.cpu}\n"
        specs += f"RAM: {self.ram}\n"
        specs += f"Storage: {self.storage}\n"
        if self.gpu:
            specs += f"GPU: {self.gpu}\n"
        if self.color:
            specs += f"Color: {self.color}\n"
        if self.screen_size:
            specs += f"Screen Size: {self.screen_size}\n"
        specs += f"Backlit Keyboard: {'Yes' if self.backlit_keyboard else 'No'}\n"
        print(specs)


laptop1 = Laptop(cpu="Intel i7", ram="16GB", storage="512GB SSD", gpu="NVIDIA GTX 1650", color="Silver", backlit_keyboard=True, screen_size="15.6 inches")
laptop1.display_specs()



# Good Example

class LaptopNew:
    processor = None
    ram = None
    storage = None
    gpu = None
    color = None
    backlit_keyboard = False
    screen_size = None

    def display_specs(self):
        if self.processor:
            print(f"Processor: {self.processor}\n")
        if self.ram:
            print(f"RAM: {self.ram}\n")
        if self.storage:
            print(f"Storage: {self.storage}\n")
        if self.gpu:
            print(f"GPU: {self.gpu}\n")
        if self.color:
            print(f"Color: {self.color}\n")
        if self.backlit_keyboard:
            print(f"Backlit Keyboard: {self.backlit_keyboard}\n")
        if self.screen_size:
            print(f"Screen Size: {self.screen_size}\n")

class LaptopBuilder:
    def __init__(self):
        self.__laptop = LaptopNew()

    def set_processor(self, processor):
        self.__laptop.processor = processor
        return self

    def set_ram(self, ram):
        self.__laptop.ram = ram
        return self

    def set_storage(self, storage):
        self.__laptop.storage = storage
        return self

    def set_gpu(self, gpu):
        self.__laptop.gpu = gpu
        return self

    def set_color(self, color):
        self.__laptop.color = color
        return self

    def set_backlit_keyboard(self, backlit_keyboard):
        self.__laptop.backlit_keyboard = backlit_keyboard
        return self

    def set_screen_size(self, screen_size):
        self.__laptop.screen_size = screen_size
        return self

    def build(self):
        return self.__laptop
    

laptop_builder = LaptopBuilder()
laptop2 = (laptop_builder.set_processor("Intel i9")
            .set_ram("32GB")
            .set_storage("1TB SSD")
            .set_gpu("NVIDIA RTX 3080")
            .set_color("Black")
            .set_backlit_keyboard(True)
            .set_screen_size("17 inches")
            .build())
laptop2.display_specs()