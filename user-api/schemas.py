
from datetime import date
from pydantic import BaseModel
from typing import Optional,Dict

class ProdDict(BaseModel):
    name: str
    pricing: Dict
    description: str
    availability: Dict
    category: str


    class Config:
        schema_extra = {
            "example": {
                "name": "leonardo diniz",
                "pricing": {
                "amount": 100.0,
                "currency": "BRL"
                },
                "description": "foo@domain.com",
                "availability": {
                "quantity": 50,
                "timestamp": "2024-06-12T12:00:00Z"
                },
                "category": "000000000"
            }

        }

class ProdIn(BaseModel):
    name: str
    pricing: str
    description: str
    availability: str
    category: str


    class Config:
        schema_extra = {
            "example": {
                "name": "leonardo diniz",
                "pricing": "00000000000",
                "description": "foo@domain.com",
                "availability": "000000000",
                "category": "000000000"
            }

        }


        


class ProdOut(BaseModel):
    id: int
    name: str
    pricing: str
    description: str
    availability: str
    category: str
    


class Message(BaseModel):
    tag: str


