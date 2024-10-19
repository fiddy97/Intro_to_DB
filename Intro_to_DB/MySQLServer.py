import mysql.connector

def create_db():
    try:
        #Database connection details
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                )
        if mydb.is_connected():
            cursor = connection.cursor()

            cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print(f"Database alx_book_store created successfully!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_db()