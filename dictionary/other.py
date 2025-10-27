class CountryManager():
    def __init__(self, **items):
        self.items = items
    
    def add_item(self, country, capital):
        self.items[country] = capital
countrys = CountryManager(Russia='Moscow', Germany='Berlin', France='Paris')
print(countrys.items['Russia'])
countrys.add_item('Spain', 'Madrid')
print(countrys.items['Spain'])