from typing import Optional
import uuid
import datetime

class Doctor:
    def __init__(self,
                 id: Optional[str],
                 name: str,
                 surname: str,
                 email: str,
                 username: str,
                 password: str,
                 price: float,
                 specialization: str,
                 ):
        self.id: str = id if id is not None else str(uuid.uuid4())
        self.name: str = name
        self.surname: str = surname
        self.email: str = email
        self.username: str = username
        self.password: str = password
        self.price: float = price
        self.specialization: str = specialization

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):#Way of show information
        return f"{self.id} -  {self.name} {self.surname} {self.email}  {self.price}  ({self.specialization}) account info {self.username} {self.password}"

    def __repr__(self):
        return f"Books('{self.id}', '{self.name}', '{self.surname}' , '{self.email}' , '{self.price}' , '{self.specialization}' , '{self.username}' , '{self.password}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "price": self.price,
            "specialization": self.specialization            
        }

    def from_dict(self, data):
        self.id = data.get("id") if data.get("id") is not None else self.id
        self.id = data.get("name") if data.get("name") is not None else self.name
        self.id = data.get("surname") if data.get("surname") is not None else self.surname
        self.id = data.get("email") if data.get("email") is not None else self.email
        self.id = data.get("username") if data.get("username") is not None else self.username
        self.id = data.get("password") if data.get("password") is not None else self.password
        self.id = data.get("price") if data.get("price") is not None else self.price
        self.id = data.get("specialization") if data.get("specialization") is not None else self.specialization
