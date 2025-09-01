from tabulate import tabulate
import csv
def print_menu_from_csv(filename):
    with open('bd.csv', 'r', encoding='utf-8') as file:
        # Читаем данные из файла
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)
        print(tabulate(data, headers="keys", tablefmt="grid"))
print_menu_from_csv('bd.csv')