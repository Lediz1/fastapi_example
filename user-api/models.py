from database import Base
from sqlalchemy import Column, Float, Integer, String, DateTime
from datetime import datetime


class Prod(Base):
    __tablename__ = "Prod"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    pricing = Column("pricing", String)
    description = Column("description", String)
    availability = Column("availability", String)
    category = Column("category", String)
   


mapping = ''' 
{ 
  "mappings": { 
    "properties": { 
      "name": { 
        "type": "keyword" 
      }, 
      "pricing": { 
        "type": "keyword" 
      },
      "description": { 
        "type": "keyword" 
      },
      "availability": { 
        "type": "keyword" 
      },
      "category": { 
        "type": "keyword" 
      }   
    } 
  } 
}'''
