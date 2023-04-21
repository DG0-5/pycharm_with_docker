class Database:
    def __init__(self):
        self.server = 'localhost'
        self.database = '--'
        self.username = '--'
        self.password = '--'
        self.driver = '{ODBC Driver 18 for SQL Server}'
        self.conn_str = f"DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};ENCRYPT=no;" \
                        f"UID={self.username};PWD={self.password}"
