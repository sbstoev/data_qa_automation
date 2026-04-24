''' This class recieves the results from the SQLRunner 
and generates a report in a .csv file.
Things to improve:
- there is no output folder
'''

import csv
import logging

class ReportGenerator:

    def __init__(self):
        logging.basicConfig(
            filename="validation.log",
            level=logging.INFO,
            format="%(asctime)s - %(message)s"
        )

    def log_results(self, message):             # Write message to log.
        logging.info(message)                   # Write message to log file.
        print(message)
    
    def export_csv(self, results, output_file):
        try:
            with open(output_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(results)
        except Exception as e:
            print("CSV export failed:", e)