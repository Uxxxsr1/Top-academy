import pyodbc

server = 'localhost'
database = 'Library'

connect_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)
try:
    conn = pyodbc.connect(connect_string)
    cursor = conn.cursor()
    create_table_query = '''
    if not exists (select * from sys.tables where name = 'people')
    begin
        create table people (
            personid int primary key identity(1,1),
            firstname nvarchar(50),
            lastname nvarchar(50),
            email nvarchar(100),
            phone nvarchar(20),
            birthdate date
        )
    end
    '''
    cursor.execute(create_table_query)
    conn.commit()
    
    print("таблица 'people' создана или уже существует")
    
    insert_queries = [
        "insert into people (firstname, lastname, email, phone, birthdate) values ('иван', 'иванов', 'ivan@mail.com', '1234567', '1990-01-15')",
        "insert into people (firstname, lastname, email, phone, birthdate) values ('петр', 'петров', 'peter@mail.com', '7654321', '1985-05-20')",
        "insert into people (firstname, lastname, email, phone, birthdate) values ('анна', 'сидорова', 'anna@mail.com', '5556677', '1995-11-30')"
    ]
    
    for query in insert_queries:
        cursor.execute(query)
    conn.commit()
    print("данные добавлены в таблицу")
    cursor.execute("select * from people")
    rows = cursor.fetchall()
    print("\nданные в таблице people:")
    for row in rows:
        print(row)
    
except pyodbc.Error as e:
    print(f"ошибка odbc: {e}")
except Exception as e:
    print(f"ошибка: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()