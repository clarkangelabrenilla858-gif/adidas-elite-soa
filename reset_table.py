from sqlalchemy import create_engine, text

# Your exact Aiven URL
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"

engine = create_engine(DATABASE_URL, connect_args={"ssl": {"ssl_mode": "REQUIRED"}})

with engine.connect() as connection:
    print("--- CONNECTING TO RESET TABLE ---")
    connection.execute(text("DROP TABLE IF EXISTS products"))
    connection.commit()
    print("SUCCESS: Table 'products' has been deleted.")