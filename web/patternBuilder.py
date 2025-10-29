class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperony = None
        self.mushrooms = None
    def __str__(self):
        return f'Size: {self.size}\n {self.cheese}\n {self.mushrooms}\n'
class PizzaBuilder:
    def __init__(self):
        self.pizza  = Pizza()
    def set_size(self, size):
        self.pizza.size = size
        return self
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    def add_pepperony(self):
        self.pizza.pepperony = True
        return self
    def add_mushrooms(self):
        self.pizza.mushrooms = False
        return self
    def build(self):
        return self.pizza
builder = PizzaBuilder()
pizza1 = builder.set_size('L').add_cheese().add_pepperony()