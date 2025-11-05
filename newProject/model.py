class phoneBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone, mail):
        contact = {
            "name": name,
            "phone": phone,

            "mail": mail
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")
        return contact
    
    def find_contact(self, search_item):
        results = []
        for contact in self.contacts:
            if (search_item.lower() in contact["name"].lower() or 
                search_item in contact["phone"]):
                results.append(contact)
        
        if results:
            print("Found contacts:")
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['mail']}")            
            print("No contacts found.")
        return results
    
    def show_all_contacts(self):
        if not self.contacts:
            print('List is empty!')
        else:
            print("All contacts:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['mail']}")
    def save_all_to_file(self):
        self.nameFile = input('Enter name of your file: ')
        with open(self.nameFile, 'w') as f:
            f.write(str(self.contacts))