from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Accurate Database URL and Engine
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"

engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {"ssl_mode": "REQUIRED"}}, # Correct SSL format
    pool_pre_ping=True
)

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    quantity = Column(Integer)
    total_price = Column(Integer)

# This is the 'session' variable your order_service.py is looking for
Session = sessionmaker(bind=engine)
session = Session()

def setup_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    setup_database()