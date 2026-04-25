import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Database Configuration
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {"ssl_mode": "REQUIRED"},
        "connect_timeout": 60 
    },
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True
)

Base = declarative_base()

# 2. Models
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)
    img_path = Column(String(255))

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    quantity = Column(Integer)
    total_price = Column(Integer)

# 3. Session Setup (CRITICAL: DO NOT DELETE THESE)
Session = sessionmaker(bind=engine)
session = Session()

def setup_database():
    try:
        Base.metadata.create_all(engine)
        print("Database tables verified!")
    except Exception as e:
        print(f"Setup warning: {e}")

if __name__ == "__main__":
    setup_database()