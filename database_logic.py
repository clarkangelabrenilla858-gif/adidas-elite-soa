from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Your exact Aiven URL
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"
                                          
engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {"ssl_mode": "REQUIRED"}},
    pool_pre_ping=True
)

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)
    stock = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(100))
    quantity = Column(Integer)
    total_price = Column(Integer)

Session = sessionmaker(bind=engine)
session = Session()

# This is CRITICAL: It creates the table in Aiven for you
def setup_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    setup_db()