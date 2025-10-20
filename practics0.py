class Human:
    def __init__(self, name, years, numberPhone, city, country, adress):
        self._name = name
        self._years = years
        self.__numberPhone = numberPhone
        self.__city = city
        self.__country = country
        self.__adress = adress
    def outputInfo(self):
        print(self._name)
        print(self._years)
student = Human('andrey', 17, 79999999999, 'Moscow', 'Russia', '250-years old for chelybinsk')
student.outputInfo()
