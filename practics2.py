class Country:
    def __init__(self, nameContinet, countHuman, phoneCode, nameCapitals):
        self.nameContinet = nameContinet
        self.countHuman = countHuman
        self.phoneCode = phoneCode
        self.nameCapitals = nameCapitals
    def printInfo(self):
        print(f'{self.countHuman}, {self.nameCapitals}, {self.nameContinet}, {self.phoneCode}')
Russia = Country('Евразия', 750000, 1234,'Москва')
Russia.printInfo()