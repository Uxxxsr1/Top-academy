class City:
    def __init__(self, nameCity, nameRegion, nameCountry, countHuman, mailIndex, phoneCode):
        self.nameCity = nameCity
        self.nameRegion = nameRegion
        self.nameCountry = nameCountry
        self.__countHuman = countHuman
        self.__mailIndex = mailIndex
        self.__phoneCode = phoneCode
    def printInfo(self):
        print(f'Название города: {self.nameCity}\n Название региона: {self.nameRegion}\n Название страны: {self.nameCountry}')
Moscow = City('Moscow', 'Moscow region', 'Russia', '~13 274 285', '12345', '54321')
Moscow.printInfo()
