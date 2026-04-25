import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Database Configuration
# We removed the ?ssl_mode from the end because it caused the "unexpected keyword" error
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ReVnZeAjyn8LHJv_Vv8@mysql-2a07ba0b-clarkangelabrenilla858-6f67.c.aivencloud.com:19056/defaultdb"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {"ssl_mode": "REQUIRED"}, # This is the correct way to tell Python to use SSL
        "connect_timeout": 60 
    },
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True
)