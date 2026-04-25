from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Exact Aiven URL from your console
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"

engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {"ssl_mode": "REQUIRED"}}, # Corrected SSL key
    pool_pre_ping=True
)

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    # Adding autoincrement ensures the database handles the ID for you
    id = Column(Integer, primary_key=True, autoincrement=True) 
    product_name = Column(String(100))
    quantity = Column(Integer)
    total_price = Column(Integer)

Session = sessionmaker(bind=engine)
session = Session()

def setup_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    setup_database()