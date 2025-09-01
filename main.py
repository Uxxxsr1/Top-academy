import csv
import time
#открываем файл
with open('bd.csv', encoding='utf-8') as bd:
    #читаем построчно
    read = csv.reader(bd)
    #выводим циклом построчечно
    for row in read:
        print(row)
        time.sleep(0.1)
        
