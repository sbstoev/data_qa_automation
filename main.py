from utils.config_loader import ConfigLoader
from utils.db_manager import DatabaseManager
from utils.sql_runner import SQLRunner
from utils.file_manager import FileManager
from utils.report_generator import ReportGenerator


def main():

    config_loader = ConfigLoader("config.json")
    config = config_loader.load_config()

    db_manager = DatabaseManager(config)
    connection = db_manager.connect()

    sql_runner = SQLRunner(connection)
    file_manager = FileManager()
    reporter = ReportGenerator()

    query = file_manager.read_sql_file("sql_tests/row_count.sql")

    results = sql_runner.run_query(query)

    reporter.log_result(f"Query results: {results}")

    reporter.export_csv(results, "results/results.csv")

    db_manager.close()


if __name__ == "__main__":
    main()
