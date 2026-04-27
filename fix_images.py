from sqlalchemy import create_engine, text

# Your Aiven URL
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"
engine = create_engine(DATABASE_URL, connect_args={"ssl": {"ssl_mode": "REQUIRED"}})

with engine.connect() as connection:
    print("--- UPDATING IMAGE FILENAMES IN CLOUD ---")
    connection.execute(text("UPDATE products SET image_url = 'response.png' WHERE id = 1"))
    connection.execute(text("UPDATE products SET image_url = 'daily.png' WHERE id = 2"))
    connection.execute(text("UPDATE products SET image_url = 'yeezy.png' WHERE id = 3"))
    connection.execute(text("UPDATE products SET image_url = 'stansmith.png' WHERE id = 4"))
    connection.commit()
    print("SUCCESS: Aiven now knows the image names!")
    