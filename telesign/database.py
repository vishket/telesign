#!/usr/bin/env python

import os

import psycopg2
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = basedir + '/../.env'
load_dotenv(dotenv_path)

# Get database information
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
TABLE_NAME = os.getenv('DB_TABLE')
COLUMN_NAME = os.getenv('COLUMN_NAME')


class Database(object):
    def __init__(self):
        try:
            self.connection = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except psycopg2.DatabaseError as e:
            print "[Error] Connecting to Database {}, failed with error: {}".format(DB_NAME, e)

    def create_table(self):
        try:
            create_table_statement = "CREATE TABLE {} ({} varchar);".format(TABLE_NAME, COLUMN_NAME)
            self.cursor.execute(create_table_statement)
        except psycopg2.DatabaseError as e:
            print "[Error] Creating table {}, failed with error: {}".format(TABLE_NAME, e)

    def select_all(self):
        try:
            select_all_statement = "SELECT * FROM {};".format(TABLE_NAME)
            self.cursor.execute(select_all_statement)

        except psycopg2.DatabaseError as e:
            print "[Error] Selecting records from table {}, failed with error: {}".format(TABLE_NAME, e)

    def insert_data(self, data):
        try:
            insert_statement = "INSERT INTO {} VALUES ('{}');".format(TABLE_NAME, data)
            self.cursor.execute(insert_statement)
        except psycopg2.DatabaseError as e:
            print "[Error] Inserting {} into table {}, failed with error: {}".format(data, TABLE_NAME, e)

    def delete_all_data(self):
        try:
            delete_all_data_statement = "DELETE FROM {};".format(TABLE_NAME)
            self.cursor.execute(delete_all_data_statement)
        except psycopg2.DatabaseError as e:
            print "[Error] Deleting from table {}, failed with error: {}".format(TABLE_NAME, e)

    def delete_data(self, data):
        try:
            delete_data_statement = "DELETE FROM {} WHERE {} = '{}';".format(TABLE_NAME, COLUMN_NAME, data)
            self.cursor.execute(delete_data_statement)
        except psycopg2.DatabaseError as e:
            print "[Error] Deleting {} from table {}, failed with error: {}".format(data, TABLE_NAME, e)


if __name__ == '__main__':
    db = Database()
    db.create_table()


