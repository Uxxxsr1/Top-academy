class Capitals:
    def __init__(self):
        self.capitals = {
            'Russia': 'Moscow',
            'USA': 'Washington',
            'Germany': 'Berlin'
        }
    
    def search_elements(self, country):
        if country in self.capitals:
            print(self.capitals[country])
        else:
            print(f"Страна '{country}' не найдена")
    
    def add_elements(self, country_add, capital_add):
        self.capitals[country_add] = capital_add
        print(f"Добавлено: {country_add} - {capital_add}")
    
    def del_elements(self, country_del):
        if country_del in self.capitals:
            self.capitals.pop(country_del)
            print(f"Удалено: {country_del}")
        else:
            print(f"Страна '{country_del}' не найдена")
capitals_manager = Capitals()
capitals_manager.search_elements('Russia')
capitals_manager.add_elements('Test', 'Test')
capitals_manager.search_elements('Test')
capitals_manager.del_elements('Test')
capitals_manager.search_elements('Test')
