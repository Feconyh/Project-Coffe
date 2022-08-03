import mysql.connector

class Db_estoque:

    def __init__(self):
        self.cConnect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'q1w2e3',
            database = 'cafeteria'
        )
        self.mycursor = self.cConnect.cursor()