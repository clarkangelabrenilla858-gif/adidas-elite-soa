from sqlalchemy import create_engine, text

DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"

engine = create_engine(DATABASE_URL, connect_args={"ssl": {"ssl_mode": "REQUIRED"}})

with engine.connect() as connection:
    print("--- LINKING IMAGES TO PRODUCTS ---")
    # This puts the filename into the cloud database
    connection.execute(text("UPDATE products SET image_url = 'stansmith.png' WHERE name = 'STAN SMITH'"))
    connection.execute(text("UPDATE products SET image_url = 'yeezy.png' WHERE name = 'YEEZY BOOST'"))
    connection.commit()
    print("DONE: Your cloud data now knows which images to show!")