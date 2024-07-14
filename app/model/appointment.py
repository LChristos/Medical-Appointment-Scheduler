from typing import Optional
import uuid
import datetime

class Appointment:
    def __init__(self,
                 id: Optional[str],
                 ap_date: datetime.datetime,
                 ap_hour: datetime.datetime ,
                 patient_username: str,
                 disc: str,
                 price: float,
                 specialization: str,
                 doctor_username:str
                 ):
        self.id: str = id if id is not None else str(uuid.uuid4())
        self.ap_date: datetime.datetime = ap_date
        self.ap_hour: datetime.datetime = ap_hour
        self.patient_username: str = patient_username
        self.disc: str = disc
        self.price: float = price
        self.specialization: str = specialization
        self.doctor_username: str = doctor_username

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):#Way of show information
        return f"{self.id} - {self.ap_date} {self.ap_hour} from {self.patient_username}  {self.disc} for {self.price} by {self.doctor_username} ({self.specialization})"

    def __repr__(self):
        return f"Books('{self.id}', '{self.ap_date}',{self.ap_hour} , '{self.patient_username}' , '{self.disc}' , '{self.price}' , '{self.specialization}' , '{self.doctor_username}')"

    def to_dict(self):
        return {
            "id": self.id,
            "ap_date": self.ap_date,
            "ap_hour": self.ap_hour,
            "patient_username": self.patient_username,
            "disc": self.disc,
            "price": self.price,
            "specialization": self.specialization,
            "doctor_username": self.doctor_username
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("id"),
            data.get("ap_date"),
            data.get("ap_hour"),
            data.get("patient_username"),
            data.get("disc"),
            data.get("price"),
            data.get("specialization"),
            data.get("doctor_username")
        )