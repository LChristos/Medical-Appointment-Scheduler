import pymongo
import json
import os

from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.appointment import Appointment
from app.utils.crypto_utils import encrypt_password

if __name__ == "__main__":
    # Connection with db
    client = pymongo.MongoClient("localhost", 27017)
    db = client.HospitalDB

    # Populate the medical appointments
    try:
        with open(os.path.join("assets", "appointment.json"), "r", encoding="utf-8") as appointment_file:
            appointments:list[Appointment] = json.load(appointment_file)
        result = db["appointment"].insert_many(appointments)
        print(len(result.inserted_ids), "appointments created")
    except json.decoder.JSONDecodeError as e:
        print(f"Error loading appointments JSON: {e}")

    #Populate the Patients
    try:
        with open(os.path.join("assets", "patient.json"), "r", encoding="utf-8") as users_file:
            users:list[Patient] = json.load(users_file)
        for user in users:
            user["password"] = encrypt_password(user["password"])
        result = db["patient"].insert_many(users)
        print(len(result.inserted_ids), "Patients account created")
    except json.decoder.JSONDecodeError as e:
        print(f"Error loading patients JSON: {e}")


    #Populate the Doctors
    try:
        with open(os.path.join("assets", "doctor.json"), "r", encoding="utf-8") as doctor_file:
            doctors:list[Doctor] = json.load(doctor_file)
        result = db["doctor"].insert_many(doctors)
        print(len(result.inserted_ids), "Doctors created")
    except json.decoder.JSONDecodeError as e:
        print(f"Error loading doctors JSON: {e}")


