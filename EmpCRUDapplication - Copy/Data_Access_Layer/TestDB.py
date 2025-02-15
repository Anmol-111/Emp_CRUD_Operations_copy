import pymssql


def m_Connect_MSSQL(self):
    global constr, cursor
    try:
        print("Attempting to connect to the database...")  # Debugging step
        # Correct connection string with the right server name and credentials
        constr = pymssql.connect(
            server='LAPTOP-8T8MA06J\SQLEXPRESS',  # Ensure the server and instance name is correct
            user='anmol',  # Your SQL Server username
            password='root',  # Your SQL Server password
            database='TestDB'  # Your database name
        )
        print("Connection successful!")  # If the connection is successful, print this

        cursor = constr.cursor()  # Initialize the cursor
        cursor.execute("SELECT * from emp")  # Execute a simple query

        # Fetch and print the data if available
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)  # Print the rows fetched from the EMP table
        else:
            print("No data found in the EMP table.")

    except pymssql.OperationalError as e:
        print(f"OperationalError: Connection failed: {e}")  # More specific error
    except pymssql.DatabaseError as e:
        print(f"DatabaseError: A database error occurred: {e}")  # Specific database error
    except Exception as e:
        print(f"An error occurred: {e}")  # Catch any other general errors
    finally:
        if constr:
            constr.close()  # Close the connection if it was successful
            print("Connection closed.")