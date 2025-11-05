class PhooneBookView:
    def displayMainMenu(self):
        menu = '''
        1. Показать все контакты
        2. Найти контакты
        3. Добавить контакты
        4. Выйти
        '''
        print(menu)
    
    def choose(self):
        self.displayMainMenu()
        try:
            choice = int(input("Choose an option (1-4): "))
            return choice
        except ValueError:
            print("Please enter a valid number")
            # return 0