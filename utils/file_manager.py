'''This class handles file operations.'''

class FileManager:

    def read_sql_file(self, file_path):         # Provide the path to the SQL file.
        try:
            with open(file_path, "r") as file: 
                query = file.read()
                return query                    # This file wil be run by the SQLRunner class.
        except Exception as e:
            print("Error reading SQL file:", e)
            return None