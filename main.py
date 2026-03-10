import psycopg2
import logging

logging.basicConfig(
    filename='validation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def connect():
    return psycopg2.connect(
        dbname="qa_test_db",
        user="postgres",
        password="$@dMin12!",
        host="localhost",
        port="5432"
    )

def validate_row_count(cursor):
    cursor.execute("SELECT COUNT(*) FROM customers;")
    count = cursor.fetchone()[0]
    print(f"Row count: {count}")
    logging.info(f"Row count: {count}")

def validate_null_emails(cursor):
    cursor.execute("SELECT COUNT(*) FROM customers WHERE email IS NULL;")
    null_count = cursor.fetchone()[0]
    print(f"Null emails: {null_count}")
    logging.info(f"Null emails: {null_count}")

def validate_duplicates(cursor):
    cursor.execute("""
        SELECT email, COUNT(*)
        FROM customers
        GROUP BY email
        HAVING COUNT(*) > 1;
    """)
    duplicates = cursor.fetchall()
    print(f"Duplicates: {duplicates}")
    logging.info(f"Duplicates: {duplicates}")

def main():
    conn = connect()
    cursor = conn.cursor()

    validate_row_count(cursor)
    validate_null_emails(cursor)
    validate_duplicates(cursor)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
