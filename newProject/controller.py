class PhoneController:
    def __init__(self, model, view):
     
        self.model = model
        self.view = view
    
    def run(self):
        while True:
            choice = self.view.choose()
            match choice:
                case 1:
                    self.model.show_all_contacts()
                case 2:
                    search_item = input("Enter name or phone to search: ")
                    self.model.find_contact(search_item)
                case 3:
                    name = input("Enter name: ")
                    phone = input("Enter phone: ")
                    mail = input("Enter email: ")
                    self.model.add_contact(name, phone, mail)
                case 4:
                    self.model.save_all_to_file()
                case _:
                    print("Invalid choice")
