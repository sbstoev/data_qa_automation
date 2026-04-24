'''This class runs SQL queries.'''

class SQLRunner:

    def __init__(self, connection):
        self.connection = connection    # Must provide the psycorg connection to run.

    def run_query(self, query):         # Must provide a query string.
        try:
            cursor = self.connection.cursor()   # Creates a cursor. Cursor is the tool that runs SQL queries.
            cursor.execute(query)           # The cursor executes the query.
            results = cursor.fetchall()     # Retrieves all returned rows.
            cursor.close()
            return results
        except Exception as e:
            print("Query execution failed:", e)
            return None
