import sqlite3
import datetime


class Database:
    DB_NAME = 'api.db'

    def __fetch_connection(self):
        return sqlite3.connect(self.DB_NAME)

    def save(self, table, token):
        sql = f"INSERT INTO {table}(token, insert_date) VALUES(?, ?)"
        insertion_date = datetime.datetime.now()
        conn = self.__fetch_connection()
        conn.cursor().execute(sql, (token, insertion_date))
        conn.commit()
        conn.close()

    def create_database(self):
        table_creation_sql = (" CREATE TABLE IF NOT EXISTS game(\n"
                              "     id integer PRIMARY KEY,\n"
                              "     token VARCHAR ,\n"
                              "     insert_date TEXT\n"
                              "     deactivate_date TEXT\n"
                              "     ); ")

        conn = self.__fetch_connection()
        conn.cursor().execute(table_creation_sql)
        conn.commit()
        conn.close()
