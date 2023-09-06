import pyodbc
import json
import subprocess

def load_secrets_from_powershell():
    result = subprocess.run(["pwsh", "-File", ".secrets.ps1"], capture_output=True, text=True)
    secrets = json.loads(result.stdout)
    return secrets

def test_sql_connection(server, database, username, password):
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    
    try:
        # Establishing the connection
        connection = pyodbc.connect(connection_string)
        print("Successfully connected to the database!")

        # Closing the connection
        connection.close()
    except Exception as e:
        print(f"Error: {e}")

def fetch_data_from_database(server, database, username, password):
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    
    try:
        # Establishing the connection
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Execute the query
        cursor.execute("SELECT TOP 10 * FROM FactSales")
        
        # Fetch the results
        rows = cursor.fetchall()
        
        # Display the results
        for row in rows:
            print(row)

        # Closing the connection
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    secrets = load_secrets_from_powershell()
    
    SERVER = "localhost"
    DATABASE = secrets["DB"]
    USERNAME = secrets["USER"]
    PASSWORD = secrets["PASSWORD"]
    
    test_sql_connection(SERVER, DATABASE, USERNAME, PASSWORD)
    # fetch_data_from_database(SERVER, DATABASE, USERNAME, PASSWORD)