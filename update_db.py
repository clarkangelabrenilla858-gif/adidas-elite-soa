from sqlalchemy import create_engine, text

# Your Aiven URL from your screenshots
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"

engine = create_engine(DATABASE_URL, connect_args={"ssl": {"ssl_mode": "REQUIRED"}})

with engine.connect() as connection:
    print("--- UPDATING TABLE STRUCTURE ---")
    # This SQL command adds the new column without deleting your data
    connection.execute(text("ALTER TABLE products ADD COLUMN image_url VARCHAR(255)"))
    connection.commit()
    print("SUCCESS: image_url column added to Aiven!")