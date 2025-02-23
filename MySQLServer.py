import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without specifying a database)
    conn = mysql.connector.connect(
        host="localhost",      # Your MySQL server host, e.g., 'localhost'
        user="alxroot",  # Your MySQL username
        password="fire948F!Y"  # Your MySQL password
    )

    # Create a cursor object
    cursor = conn.cursor()

    # SQL statement to create the database
    create_database_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

    # Execute the query to create the database
    cursor.execute(create_database_query)

    # Commit the transaction
    conn.commit()

    # Switch to the newly created database
    cursor.execute("USE alx_book_store")

    # Query to create authors table (first)
    create_authors_table_query = """
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    )
    """

    # Query to create books table (after authors table)
    create_books_table_query = """
    CREATE TABLE IF NOT EXISTS Books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(130) NOT NULL,
        author_id INT,
        price DOUBLE NOT NULL,
        publication_date DATE,
        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    )
    """

    # Query to create customers table (before orders table)
    create_customers_table_query = """
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(215) NOT NULL,
        email VARCHAR(215) UNIQUE,
        address TEXT
    )
    """

    # Query to create orders table (after customers table)
    create_orders_table_query = """
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    """

    # Query to create orders details table (after orders table and books table)
    create_orders_details_table_query = """
    CREATE TABLE IF NOT EXISTS Order_Details (
        orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        book_id INT,
        quantity DOUBLE NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
    """

    # Execute the queries to create tables in the correct order
    cursor.execute(create_authors_table_query)
    cursor.execute(create_books_table_query)
    cursor.execute(create_customers_table_query)
    cursor.execute(create_orders_table_query)
    cursor.execute(create_orders_details_table_query)

    # Commit the transaction
    conn.commit()

    print("Database 'alx_book_store' and tables created successfully.")

except mysql.connector.Error as err:
    # Handle MySQL-related errors
    print(f"Error: {err}")
except Exception as e:
    # Handle any other exceptions
    print(f"An unexpected error occurred: {e}")
finally:
    # Ensure the connection is closed
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")
