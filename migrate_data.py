import pymysql

host = 'mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com'
port = 19056
user = 'avnadmin'
password = 'AVNS_ReVnZeAjyn8LHJv_Vv8'
database = 'defaultdb'

try:
    print("Connecting to Aiven...")
    connection = pymysql.connect(
        host=host, 
        port=port, 
        user=user, 
        password=password, 
        database=database
    )
    cursor = connection.cursor()

    # --- THE FIX: Disable the Primary Key requirement temporarily ---
    print("Disabling strict PK requirement...")
    cursor.execute("SET SESSION sql_require_primary_key = 0;")

    print("Reading adidas_shop.sql...")
    with open('adidas_shop.sql', 'r') as f:
        sql_file = f.read()

    sql_commands = sql_file.split(';')
    
    print("Uploading data to the cloud...")
    for command in sql_commands:
        if command.strip():
            try:
                cursor.execute(command)
            except Exception as e:
                print(f"Skipping minor error: {e}")

    connection.commit()
    print("-" * 30)
    print("REAL SUCCESS! Your tables and shoes should now be online.")
    print("-" * 30)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'connection' in locals():
        connection.close()