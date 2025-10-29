class Computer:
    def __init__(self):
        self.motherboard = None
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.storage = None
    def __str__(self):
        print(f'{self.cpu}\n {self.gpu}\n {self.motherboard} ')
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_motherboard(self, model):
        self.computer.motherboard = model
        return self

    def set_cpu(self, model):
        self.computer.cpu = model
        return self

    def set_ram(self, model):
        self.computer.ram = model
        return self

    def set_gpu(self, model):
        self.computer.gpu = model
        return self

    def set_storage(self, model):
        self.computer.storage = model
        return self

    def build(self):
        return self.computer
builder = ComputerBuilder()
pc = builder.set_cpu('i9-14900k').set_gpu('nvidia 2060 super').set_motherboard('asrog blabla')
