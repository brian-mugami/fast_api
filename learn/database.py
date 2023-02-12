import os.path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
db = os.path.join(basedir, "itemsdb")
#SQLALCHEMY_DATABASE_URL = f"sqlite:///{db}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://user:root@db:3309/mydb'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

Base = declarative_base()