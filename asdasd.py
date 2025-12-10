import pyodbc
from datetime import datetime

server = 'localhost'
database = 'library'

connect_string = f'driver={{odbc driver 17 for sql server}};server={server};database={database};trusted_connection=yes;'

try:
    conn = pyodbc.connect(connect_string)
    cursor = conn.cursor()
    conn.commit()
    
    cursor.execute("select count(*) from people")
    
    while True:
        print("\n1 - поиск по фио")
        print("2 - добавить")
        print("3 - изменить")
        print("4 - удалить")
        print("5 - поиск по городу")
        print("6 - поиск по стране")
        print("7 - поиск по возрасту")
        print("8 - выйти")
        
        choice = input("выберите: ")
        
        if choice == '8':
            break
            
        elif choice == '1':
            name = input("имя: ").strip()
            surname = input("фамилия: ").strip()
            
            query = "select * from people where 1=1"
            params = []
            
            if name:
                query += " and firstname like ?"
                params.append(f'%{name}%')
            
            if surname:
                query += " and lastname like ?"
                params.append(f'%{surname}%')
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            rows = cursor.fetchall()
            
            if rows:
                for row in rows:
                    print(f"id: {row.personid}, имя: {row.firstname}, фамилия: {row.lastname}, email: {row.email}, телефон: {row.phone}, дата рождения: {row.birthdate}, город: {row.city}, страна: {row.country}")
            else:
                print("ничего не найдено")
                
        elif choice == '2':
            firstname = input("имя: ").strip()
            lastname = input("фамилия: ").strip()
            email = input("email: ").strip()
            phone = input("телефон: ").strip()
            birthdate = input("дата рождения (гггг-мм-дд): ").strip()
            city = input("город: ").strip()
            country = input("страна: ").strip()
            
            cursor.execute("insert into people (firstname, lastname, email, phone, birthdate, city, country) values (?, ?, ?, ?, ?, ?, ?)", 
                          firstname, lastname, email, phone, birthdate, city, country)
            conn.commit()
            print("добавлено")
            
        elif choice == '3':
            personid = input("id для изменения: ").strip()
            
            cursor.execute("select * from people where personid = ?", personid)
            row = cursor.fetchone()
            
            if row:
                print(f"текущие данные: id: {row.personid}, имя: {row.firstname}, фамилия: {row.lastname}, email: {row.email}, телефон: {row.phone}, дата рождения: {row.birthdate}, город: {row.city}, страна: {row.country}")
                
                new_firstname = input(f"новое имя ({row.firstname}): ").strip() or row.firstname
                new_lastname = input(f"новая фамилия ({row.lastname}): ").strip() or row.lastname
                new_email = input(f"новый email ({row.email}): ").strip() or row.email
                new_phone = input(f"новый телефон ({row.phone}): ").strip() or row.phone
                new_birthdate = input(f"новая дата рождения ({row.birthdate}): ").strip() or row.birthdate
                new_city = input(f"новый город ({row.city}): ").strip() or row.city
                new_country = input(f"новая страна ({row.country}): ").strip() or row.country
                
                cursor.execute("update people set firstname=?, lastname=?, email=?, phone=?, birthdate=?, city=?, country=? where personid=?", 
                              new_firstname, new_lastname, new_email, new_phone, new_birthdate, new_city, new_country, personid)
                conn.commit()
                print("изменено")
            else:
                print("не найдено")
                
        elif choice == '4':
            personid = input("id для удаления: ").strip()
            
            cursor.execute("select * from people where personid = ?", personid)
            if cursor.fetchone():
                cursor.execute("delete from people where personid = ?", personid)
                conn.commit()
                print("удалено")
            else:
                print("не найдено")
                
        elif choice == '5':
            city = input("введите город: ").strip()
            
            if city:
                cursor.execute("select * from people where city like ?", city)
                rows = cursor.fetchall()
                
                if rows:
                    for row in rows:
                        print(f"id: {row.personid}, имя: {row.firstname}, фамилия: {row.lastname}, город: {row.city}, страна: {row.country}")
                else:
                    print("ничего не найдено")
            else:
                print("город не указан")
            
        elif choice == '6':
            country = input("введите страну: ").strip()
            
            if country:
                cursor.execute("select * from people where country like ?", country)
                rows = cursor.fetchall()
                
                if rows:
                    for row in rows:
                        print(f"id: {row.personid}, имя: {row.firstname}, фамилия: {row.lastname}, город: {row.city}, страна: {row.country}")
                else:
                    print("ничего не найдено")
            else:
                print("страна не указана")
        
        elif choice == '7':
            try:
                min_age = int(input("минимальный возраст: ").strip())
                max_age = int(input("максимальный возраст: ").strip())
                
                current_year = datetime.now().year
                min_birth_year = current_year - max_age
                max_birth_year = current_year - min_age
                
                cursor.execute("select * from people where year(birthdate) between ? and ? order by birthdate", min_birth_year, max_birth_year)
                
                rows = cursor.fetchall()
                
                if rows:
                    for row in rows:
                        age = current_year - row.birthdate.year
                        print(f"id: {row.personid}, имя: {row.firstname}, фамилия: {row.lastname}, возраст: {age}, дата рождения: {row.birthdate}")
                else:
                    print("ничего не найдено")
                    
            except ValueError:
                print("введите корректные числа для возраста")
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"ошибка: {e}")