'''This class manages database connections and operations.'''

import psycopg2

class DatabaseManager:

    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.config) # the ** means Take dictionary values and pass them as arguments(value) to parameters(key). As many key-values as you want.
            print("Database connection established")
            return self.connection
        except Exception as e:
            print("Database connection failed:", e)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")
