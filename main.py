import os


def open_xml():
    os.system('cls')
    inp1 = input("Input name of your file(XXX.xml):  ")
    file_xml = inp1
    with open(file_xml, 'r+') as f:
        xml_string = f.read()
    print(xml_string)
def open_json():
    os.system('cls')
    inp2 = input("Input name of file(XXX.json):  ")
    file_json = inp2
    with open(file_json, 'r+') as f:
        json_string = f.read()
    print(json_string)
def write_file():
    inp4 = input("input name of file:  ")
    message = input("Введите строку: ")
    with open(inp4, 'r') as file:
        file.read()
    with open(inp4, "w") as file:
        file.write(message)
        #file.read()


os.system("cls")
print("Selct json 1 /xml 2, edit 3")
inp3 = int(input(":  "))
if inp3 == 1:
    open_json()
elif inp3 == 2:
    open_xml()
elif inp3 == 3:
    write_file()
else:
    print("err")
