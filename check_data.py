from sqlalchemy import create_engine, text

DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"
engine = create_engine(DATABASE_URL, connect_args={"ssl": {"ssl_mode": "REQUIRED"}})

try:
    with engine.connect() as connection:
        print("--- DATABASE CONNECTION: SUCCESS ---")
        
        # 1. Check if the table exists and what columns it has
        print("Checking table structure...")
        columns = connection.execute(text("DESCRIBE products"))
        for col in columns:
            print(f"Column found: {col}")

        print("\n--- FETCHING ROWS ---")
        # 2. Try to get the actual data
        result = connection.execute(text("SELECT id, name, image_url FROM products"))
        rows = result.all()
        
        if not rows:
            print("WARNING: The table is EMPTY. No shoes found.")
        else:
            for row in rows:
                print(f"ID: {row} | Name: {row} | Image: {row}")
                
except Exception as e:
    print(f"ERROR: Something went wrong: {e}")