from db import Database
import pyodbc


class Command(Database):
    def __init__(self):
        super().__init__()
        self.conn = pyodbc.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def cat_command(self):
        user_cat = self.get_user_cat()
        sql_query = f'''SELECT * FROM Movie WHERE categoryID = {user_cat};'''
        self.execute_select_query(sql_query)

    def year_command(self):
        user_year = input("\nEnter a Movie Year: ")
        sql_query = f'''SELECT * FROM Movie WHERE year = {user_year};'''
        self.execute_select_query(sql_query)

    def min_command(self):
        user_minutes = input("\nEnter movie's minutes: ")
        sql_query = f'''SELECT * FROM Movie WHERE minutes = {user_minutes};'''
        self.execute_select_query(sql_query)

    def add_command(self):
        user_catID = int(input("\nCATEGORIES\n1.Animation\n2.Comedy\n3.History\nCategory of movie: "))
        user_name = input("Movie Name: ")
        user_year = int(input("Year of Movie: "))
        user_minutes = int(input("Minutes: "))

        sql_query = f'''INSERT INTO Movie (categoryID, name, year, minutes)
                    VALUES ({user_catID}, '{user_name}', {user_year}, {user_minutes});'''
        self.execute_query(sql_query)

    def update_command(self):
        existing_movie = input("Please enter the ID of the movie you want to update: ")
        new_catID = int(input("Enter new catID: "))
        new_name = input("Enter new name: ")
        new_year = int(input("Enter new year = "))
        new_minutes = int(input("Enter new minutes: "))
        sql_query = f'''UPDATE Movie SET categoryID = {new_catID}, name = '{new_name}', year = {new_year}, 
                        minutes = {new_minutes} WHERE movieID = {existing_movie};'''
        self.execute_query(sql_query)

    def delete_command(self):
        user_movie_name = input("Enter movie name: ")
        sql_query = f'''DELETE FROM Movie WHERE name = '{user_movie_name}';'''
        self.execute_query(sql_query)

    def get_user_cat(self):
        category = input("\nCATEGORIES"
                         "\n1.Animation"
                         "\n2.Comedy"
                         "\n3.History"
                         "\nWhich category do you need? ")
        return category

    def close_db_connection(self):
        self.cursor.close()
        self.conn.close()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def execute_select_query(self, query):
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)

        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
