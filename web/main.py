class DataBaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection_status='Connested'
            print('made new connection')
        return cls._instance
db1 = DataBaseConnection()
db2 = DataBaseConnection()
print(db1 is db2)