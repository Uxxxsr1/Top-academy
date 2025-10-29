class GlobalCache:
    _pattern = None
    
    def __new__(cls):
        if cls._pattern is None:
            cls._pattern = super().__new__(cls)
            cls._pattern.status = 'True'
            print('true')
        return cls._pattern
    
    def __init__(self):
        self.data = {}
    
    def set_data(self, key, value):
        self.data[key] = value
c1 = GlobalCache()
c2 = GlobalCache()
print(c1 is c2) 
c1.set_data('name', 'John')
c1.set_data('age', 25)
for key, value in c2.data.items():
    print(f"{key}: {value}")
c2.set_data('city', 'New York')
for key, value in c1.data.items():
    print(f"{key}: {value}")