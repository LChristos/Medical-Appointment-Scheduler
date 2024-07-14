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
            appointments = json.load(appointment_file)
        if appointments:
            result = db["appointment"].insert_many(appointments)
            print(len(result.inserted_ids), "appointments created")
        else:
            print("No appointments to insert")
    except json.decoder.JSONDecodeError as e:
        print(f"Error loading appointments JSON: {e}")

    #Populate the Patients
    try:
        with open(os.path.join("assets", "patient.json"), "r", encoding="utf-8") as users_file:
            users = json.load(users_file)
        if users:
            result = db["patient"].insert_many(users)
            print(len(result.inserted_ids), "Patients account created")
        else:
            print("No patients to insert")
    except json.decoder.JSONDecodeError as e:
        print(f"Error loading patients JSON: {e}")


    #Populate the Doctors
    try:
        with open(os.path.join("assets", "doctor.json"), "r", encoding="utf-8") as doctor_file:
            doctors = json.load(doctor_file)
        if doctors:
            result = db["doctor"].insert_many(doctors)
            print(len(result.inserted_ids), "Doctors created")
        else:
            print("No doctors to insert")
    except json.decoder.JSONDecodeError as e:
        print(f"Error loading doctors JSON: {e}")

