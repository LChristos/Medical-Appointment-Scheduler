from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymongo
from pymongo import MongoClient
from app import server
from typing import List, Optional
from app.utils.crypto_utils import decrypt_password, encrypt_password
import app.model
from datetime import datetime, date, time
from bson.objectid import ObjectId






client = MongoClient('mongodb://mongodb:27017/')  # Adjust the host and port if necessary
db = client["HospitalDB"]  # Database name
appointment_collection = db["appointment"]
doctor_collection = db["doctor"]
patient_collection = db["patient"]


#_instance = None  # Repository object

def __init__(self) -> None:
    """
    Αυτή η υλοποίηση δεν επιτρέπει στον προγραμματιστή να δημιουργήσει νέο αντικείμενο από τον constructor της python.  
    """
    raise RuntimeError('Call instance() instead')

@server.route('/')
def home():
    if 'username' in session:
        username = session['username']
        role = session['role']
        return render_template('home.html', username=username , role=role)
    
    # Redirect to login if not logged in
    return redirect(url_for('login'))


@server.route('/login', methods=['GET', 'POST'])
def login():#Μαλλον έχει και άλλη δουλειά
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username == 'admin' and password == '@dm1n'):
            session['username'] = username
            session['role'] = 'admin'
            flash('Welcome Administrator'  , 'success')
            return redirect(url_for('home'))
        else:
            doctor = doctor_collection.find_one({'username': username})
            patient =  patient_collection.find_one({'username': username})
            if doctor:
                if password == decrypt_password(doctor['password']):
                    session['username'] = username
                    session['role'] = 'doctor'
                    flash('Welcome Doctor' , 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Wrong Password' , 'danger')
            elif patient:
                if password == decrypt_password(patient['password']):
                    session['username'] = username
                    session['role'] = 'patient'
                    flash('Welcome Patient', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Wrong Password' , 'danger')
            else:
                flash('Invalid Credentials', 'danger')
    return render_template('login.html')

@server.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))



#ADMIN actions
@server.route('/admin/add_doctor', methods=['GET', 'POST'])
def new_doctor():
    if session['role'] != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))    
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email= request.form['email']
        username= request.form['username']
        password= request.form['password']
        password = encrypt_password(password)
        price= request.form['price']
        specialization= request.form['specialization']
        if name and surname and email and price and specialization and username and password:
            doctor = {'name': name, 'surname': surname , 'email': email ,  'username': username , 'password':password , 'price':price ,  'specialization':specialization}
            doctor_collection.insert_one(doctor)
            flash('Doctor added successfully!', 'success')
        else:
            flash('A field is not complete', 'danger')
    return render_template('add_doctor.html')

@server.route('/admin/delete_doctor', methods=['GET', 'POST'])
def delete_doctor():
    if session['role'] != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))    
    if request.method == 'POST':
        username = request.form['username']
        if username:
            doctor = doctor_collection.delete_one({'username': username})
            appointment_collection.delete_many({'doctor_username': username})
            if doctor.deleted_count > 0:
                flash('Doctor deleted successfully!', 'success')
            else:
                flash('Doctor does not exist' , 'danger')
        else:
            flash('Username field is empty' , 'danger')
    return render_template('delete_doctor.html')

@server.route('/admin/delete_patient', methods=['GET', 'POST'])
def delete_patient():
    if session['role'] != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        if username:
            patient_collection.delete_one({'username': username})
            appointment_collection.delete_many({'patient_username': username})
            flash('Patient deleted successfully!', 'success')
        else:
            flash('Username field is empty' , 'danger')
    return render_template('delete_patient.html')

@server.route('/admin/change_password', methods=['GET', 'POST'])
def change_password_admin():
    if session['role'] != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        doctor_username = request.form['username']
        password = request.form['password']
        if password:
            password = encrypt_password(password)
            doctor_collection.update_one({'username': doctor_username}, {'$set': {'password': password}})
            flash('Password changed successfully!', 'success')
        else:
            flash('Price field is empty' , 'danger')
    return render_template('change_doctor_password.html')


#DOCTORS actions
@server.route('/doctor/change_password', methods=['GET', 'POST'])
def change_password():
    if session['role'] != 'doctor':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        doctor_username = session['username']
        password = request.form['password']
        if password:
            password = encrypt_password(password)
            doctor_collection.update_one({'username': doctor_username}, {'$set': {'password': password}})
            flash('Password changed successfully!', 'success')
        else:
            flash('Price field is empty' , 'danger')
    return render_template('change_password.html')

@server.route('/doctor/change_price', methods=['GET', 'POST'])
def change_price():
    if session['role'] != 'doctor':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = session['username']
        price = request.form['price']
        if price:
            doctor_collection.update_one({'username': username}, {'$set': {'price': price}})
            appointment_collection.update_many({'doctor_username':username} ,{'$set': {'price': price}})
            flash('Price per  appointment changed successfully!', 'success')
        else:
            flash('Price field is empty' , 'danger')
    return render_template('change_price.html')


@server.route('/doctor/show_appointments')
def show_doctor_appointments():
    if session['role'] != 'doctor':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    username = session['username']
    current_datetime = datetime.now()
    current_day = current_datetime.strftime('%Y-%m-%d')
    current_time = current_datetime.strftime('%H:%M')

    appointments = list(appointment_collection.find({'doctor_username': username , 'ap_date': {'$gte': current_day} , 'ap_hour': {'$gt': current_time}}))
    for appointment in appointments:
        patient = patient_collection.find_one({'username':appointment['patient_username']})
        if patient:
            appointment['patient_name'] = patient['name']
            appointment['patient_surname'] = patient['surname']
        else:
            flash('There is no Patient for this appointment' , 'danger')
    return render_template('show_doctor_appointments.html', appointments=appointments)

#PATIENT actioins
@server.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        amka = request.form['amka']
        birth = request.form['birth']
        username = request.form['username']
        password = request.form['password']
        if name and surname and email and amka and birth and username and password:
            patient = patient_collection.find_one({'username': username})
            if not patient or not email:
                password = encrypt_password(password)
                patient_collection.insert_one({'name': name , 'surname': surname , 'email': email , 'amka': amka , 'birth': birth , 'username':username , 'password': password})
                return redirect(url_for('login'))
            else:
                flash('This username or email exist' , 'danger')
        else:
            flash('Complete all the fields' , 'danger')
    return render_template('sign_up.html')


@server.route('/user/add_appointment', methods=['GET', 'POST'])
def new_appointment():
    if session['role'] != 'patient':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = session['username']
        date = request.form['date']
        specialization = request.form['specialization']
        disc = request.form['disc']
        hour = request.form['time']
        if date and specialization and disc and hour:
            doctors = doctor_collection.find({'specialization': specialization})
            for doctor in doctors:
                appointment_exist = appointment_collection.find_one({'doctor_username': doctor['username'] , 'ap_date': date , 'ap_hour': hour})
                if not appointment_exist:
                    appointment_collection.insert_one({'ap_date': date , 'ap_hour': hour , 'patient_username':username , 'disc': disc , 'price': doctor['price'] , 'specialization': specialization , 'doctor_username': doctor['username']})
                    flash('Appointment booked successfully' , 'success')  
        else:
            flash('A value in a field is empty' , 'danger')
    return render_template('add_appointment.html')
        
            
@server.route('/user/show_appointments')
def show_appointments():
    if session['role'] != 'patient':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    username = session['username']        
    current_datetime = datetime.now()
    current_day = current_datetime.strftime('%Y-%m-%d')
    current_time = current_datetime.strftime('%H:%M')
    appointments = list(appointment_collection.find({'patient_username': username , 'ap_date': {'$gt': current_day} , 'ap_hour': {'$gt': current_time}}))
    for appointment in appointments:
        doctor = doctor_collection.find_one({'username':appointment['doctor_username']})
        if doctor:
            appointment['doctor_name'] = doctor['name']
            appointment['doctor_surname'] = doctor['surname']
        else:
            appointment['doctor_name'] = 'Unknown'
            appointment['doctor_surname'] = 'Unknown'
            flash('There is no Patient for this appointment' , 'danger')
    return render_template('show_patient_appointments.html', appointments=appointments)

@server.route('/user/show_appointment/<appointment_id>' , methods=['GET'])
def show_oneappointment(appointment_id):
    if session['role'] != 'patient':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    appointment = appointment_collection.find_one({'_id': ObjectId(appointment_id)})
    if not appointment:
        flash('Appointment not found', 'danger')
        return redirect(url_for('show_appointments'))
    
    doctor = doctor_collection.find_one({'username': appointment['doctor_username']})
    if doctor:
        appointment['doctor_name'] = doctor['name']
        appointment['doctor_surname'] = doctor['surname']
    else:
        appointment['doctor_name'] = 'Unknown'
        appointment['doctor_surname'] = 'Unknown'

    return render_template('show_one_appointment.html', appointment=appointment)
    
@server.route('/user/delete_appointment' , methods=['POST' , 'GET'])
def delete_appointment():
    if session['role'] != 'patient':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        id = request.form['id']    
        appointment = appointment_collection.delete_one({'_id': ObjectId(id)})
        if appointment:
            flash('Appointment deleted' , 'success')
        else:
            flash('Appointment not found' , 'danger')
    return redirect(url_for('show_appointments'))


