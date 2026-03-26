class SQLRunner:

    def __init__(self, connection):
        self.connection = connection

    def run_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print("Query execution failed:", e)
            return None
