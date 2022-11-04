
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class User(Base):
    __tablename__ = "T3"
    id = Column(Integer, primary_key=True)
    grade = Column(String)
    financials = Column(String)    
    time_avaliable = Column(String)
    institution_name = Column(String)
    cost = Column(String)
    opp_type = Column(String)
    need_based = Column(String)
    city = Column(String)
    size = Column(String)
    pub_priv = Column(String)


    

