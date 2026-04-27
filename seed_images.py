from sqlalchemy import create_engine, text

# Your Aiven Connection
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"
engine = create_engine(DATABASE_URL, connect_args={"ssl": {"ssl_mode": "REQUIRED"}})

with engine.connect() as connection:
    print("--- SEEDING CLOUD DATABASE ---")
    
    # 1. Add the shoes into the empty table
    # We include the image_url here so it's NOT hardcoded!
    sql = text("""
        INSERT INTO products (name, price, stock, image_url) 
        VALUES 
        ('Response Super', 6500, 10, 'response.png'),
        ('Daily 3.0', 4000, 15, 'daily.png'),
        ('Yeezy Boost', 18000, 5, 'yeezy.png'),
        ('Stan Smith', 5300, 20, 'stansmith.png')
    """)
    
    connection.execute(sql)
    connection.commit()
    print("SUCCESS: 4 shoes added to Aiven with their image links!")