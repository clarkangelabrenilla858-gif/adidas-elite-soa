from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Connect to your Aiven Online Database
# Using the credentials from your Screenshot (138)
engine = create_engine("mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb")
Base = declarative_base()

# 2. Define the Product Model (For showing shoes)
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)
    img_path = Column(String(255))

# 3. Define the Order Model (For saving sales)
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    quantity = Column(Integer)
    total_price = Column(Integer)

# This ensures the 'orders' table is created if it doesn't exist yet
Base.metadata.create_all(engine)
# Create the session
Session = sessionmaker(bind=engine)
session = Session()

# Check the connection
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("Successfully connected to Aiven Online Database!")
    except Exception as e:
        print(f"Connection failed: {e}")