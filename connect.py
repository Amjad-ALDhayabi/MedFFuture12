import mysql.connector
from mysql.connector import Error

# Function to insert data into MySQL
def insert_data(lab, email, password):
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='localhost',        # Change to your MySQL host
            database='med',     # The database you created earlier
            user='root',             # Your MySQL username
            password=' ' # Your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL query to insert data
            insert_query = """INSERT INTO info (lab, email, password) VALUES (%s, %s, %s)"""
            data = (lab, email, password)
            
            cursor.execute(insert_query, data)
            connection.commit()
            print(f"Record inserted successfully into the users table")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

