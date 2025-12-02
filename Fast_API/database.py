from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:12345@localhost:5432/telusko"
#                        server:pass @ host:portnumber/database_name
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush = False, bind = engine)
#                                 no idea     ,  no idea         , engine = postgres or mssql 
