from model import phoneBook
from view import PhooneBookView
from controller import PhoneController

if __name__ == "__main__":
    model = phoneBook()
    view = PhooneBookView()
    controller = PhoneController(model, view)
    controller.run()