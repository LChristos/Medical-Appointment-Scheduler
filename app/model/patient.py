from typing import Optional
import uuid
import datetime

class Patient:
    def __init__(self,
                 id: Optional[str],
                 name: str,
                 surname: str,
                 email: str,
                 amka: str,
                 birth: datetime.date,
                 username: str,
                 password: str,
                 ):
        self.id: str = id if id is not None else str(uuid.uuid4())
        self.name: str = name
        self.surname: str = surname
        self.email: str = email
        self.amka: str = amka
        self.birth: datetime.date = birth
        self.username: str = username
        self.password: str = password

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):#Way of show information
        return f"{self.id} -  {self.name} {self.surname} {self.email}  {self.amka}  ({self.birth}) account info {self.username} {self.password}"

    def __repr__(self):
        return f"Books('{self.id}', '{self.name}', '{self.surname}' , '{self.email}' , '{self.amka}' , '{self.birth}' , '{self.username}' , '{self.password}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "amka": self.amka,
            "birth": self.birth,
            "username": self.username,
            "password": self.password          
        }

    def from_dict(self, data):
        self.id = data.get("id") if data.get("id") is not None else self.id
        self.id = data.get("name") if data.get("name") is not None else self.name
        self.id = data.get("surname") if data.get("surname") is not None else self.surname
        self.id = data.get("email") if data.get("email") is not None else self.email
        self.id = data.get("username") if data.get("username") is not None else self.username
        self.id = data.get("password") if data.get("password") is not None else self.password
        self.id = data.get("amka") if data.get("amka") is not None else self.amka
        self.id = data.get("birth") if data.get("birth") is not None else self.birth
