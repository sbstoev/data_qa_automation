import psycopg2

class DatabaseManager:

    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.config)
            print("Database connection established")
            return self.connection
        except Exception as e:
            print("Database connection failed:", e)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")
