import pyodbc

server = 'localhost'
database = 'Library'

connect = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

try:
    conn = pyodbc.connect(connect)
    print('Успешно подключено')

    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Products')
    conn.commit()

    create_table_query = '''
    CREATE TABLE Products(
        Id INT IDENTITY(1,1) PRIMARY KEY,
        Name NVARCHAR(100),
        Price DECIMAL(10, 2), 
        Quantity INT
    )'''
    
    cursor.execute(create_table_query)
    conn.commit()
    
    print('Таблица Products успешно создана')
    
    product_name = 'notebook'
    product_price = 55555
    product_qty = 100

    insert_query = """
      INSERT INTO Products(Name, Price, Quantity)
      VALUES (?, ?, ?)
    """    

    cursor.execute(insert_query, product_name, product_price, product_qty)
    conn.commit()
    
    print('Данные успешно добавлены')
    
    select_query = "SELECT * FROM Products"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        print(f'ID: {row.Id}, tovar: {row.Name}, cena {row.Price}, qty: {row.Quantity}')


except pyodbc.Error as e:
    print(f'Ошибка: {e}')