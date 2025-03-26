# Mandatory Assignment 2024 - Medical Appointments

## Table of Contents

1. [Additional Assumptions Chosen](#additional-assumptions-chosen)
2. [Technologies Used](#technologies-used)
3. [Description of the Created Files](#description-of-the-created-files)
4. [How to Run the System](#how-to-run-the-system)
5. [How to Use the System](#how-to-use-the-system)
6. [References Used](#references-used)

## Additional Assumptions Chosen

- Each doctor can have only one specialty.
- Patients cannot book two appointments at the same time.

## Technologies Used

- Python 3.12
- Flask
- MongoDB
- Docker
- Docker Compose
- HTML (for the templates)
- Jinja2 (for the templates)
- Fernet (for password encryption)

## Description of the Created Files

- **requirements.txt**: Contains all the libraries to be installed for the project.
- **main.py**: The main file that runs the Flask API server.
- **docker-compose.yml**: File used to start the containers for both the API server and the MongoDB database.
- **Dockerfile**: File used to create the Docker image for the API server.

### Folder `data`

Contains the tables (collections) and the database data. If the database does not exist, it will create it.

### Folder `app`

Contains the application code:

- **app/\_\_init\_\_.py**: Application initialization file.
- **app/repository.py**: Contains functions for managing the database and endpoints for the system's routes and methods.
- **app/model/appointment.py**: Model definition for appointments.
- **app/model/doctor.py**: Model definition for doctors.
- **app/model/patient.py**: Model definition for patients.
- **app/template**: Contains the HTML templates for data display.
- **app/utils/crypto_utils.py**: Contains functions for password encryption.

### Folder `app/template`

Contains the HTML templates for data display. According to _app/repository.py_:

- **home.html** (home): This is the landing page. If the user is not logged in, they are redirected to login.html.
- **login.html** (login): The login page for an administrator, doctor, or user. The user must first sign up via sign_up.html.

**When logged in as an Administrator:**
- **add_doctor.html** (new_doctor): The admin can add a new doctor to the system.
- **delete_doctor.html** (delete_doctor): The admin can delete a doctor by username.
- **delete_patient.html** (delete_patient): The admin can delete a patient by username.
- **change_doctor_password.html** (change_password_admin): The admin can change a doctor's password.

**When logged in as a Doctor:**
- **change_password.html** (change_password): The doctor can change their password.
- **change_price.html** (change_price): The doctor can change the price per appointment.
- **show_doctor_appointments.html** (show_doctor_appointments): The doctor can view all upcoming appointments.

**When logged in as a Patient:**
- **sign_up.html** (sign_up): The patient registers for the first time.
- **add_appointment.html** (new_appointment): The patient attempts to book an appointment.
- **show_patient_appointments.html** (show_appointments): The patient displays all their upcoming appointments.
- **show_one_appointment.html**(show_oneappointment): The patient displays a specific appointment.
- (delete_appointment): The patient deletes an appointment.


## Τρόπος Εκτέλεσης Συστήματος

1. **Κλωνοποίηση του Repository**:

   ```sh
   git clone https://github.com/LChristos/YpoxreotikiErgasia24_E21090_Liakos_Christos-Konstantinos.git
   cd YpoxreotikiErgasia24_E21090_Liakos_Christos-Konstantinos

2. **Δημιουργία του image Mongodb για την βάση δεδομένων**:
    ```sh
    docker pull mongo:7.0.9

3. **Δημιουργία του image Flask API Server**:
    ```sh
    docker build --tag my-server:1.0.1 .

4. **Φτιάχνουμαι τα container για το flask και mongodb**:
    ```sh
    docker compose up -d

5. **Πρόσβαση στο σύστημα**:
    Πηγαίνουμε στη διεύθυνση http://localhost:5000


## Τρόπος Χρήσης του Συστήματος

### ΩΣ Διαχειριστής
1. Είσοδος στο Σύστημα με τα στοιχεία: Στο endpoint /login

        Username: admin
        Password: @dm1n

2. Του έχει τις επιλογές:

    Δημιουργία Ιατρού(Add Doctor): Στο endpoint /admin/add_doctor

    Αλλαγή Κωδικού Ιατρού(Change Doctor Password): Στο endpoint /admin/change_password

    Διαγραφή Λογαριασμού Ιατρού: Στο endpoint /admin/delete_doctor
    
    Διαγραφή Λογαριασμού Ασθενή: Στο endpoint /admin/delete_patient

    Αποσύνδεση:

### ΩΣ Ιατρός
1. Είσοδος στο Σύστημα με τα στοιχεία του Ιατρού: Στο endpoint /login

2. Του έχει τις επιλογές:

    Αλλαγή κωδικού: Στο endpoint /doctor/change_password

    Αλλαγή τιμής άνα ραντεβού: Στο endpoint /doctor/change_price

    Εμφάνιση μελλοντικών ραντεβού: Στο endpoint /doctor/show_appointments

    Αποσύνδεση:

### ΩΣ Ασθενής
1. Εγγραφή στο Σύστημα αν είναι η πρώτη φορά: Στο endpoint /sign_up

2. Είσοδος στο Σύστημα με τα στοιχεία του Ιατρού: Στο endpoint /login

3. Του έχει τις επιλογές:

    Αναζήτηση & Κράτηση Ραντεβού: Στο endpoint /user/add_appointment

    Προβολή Μελλοντικών Ραντεβού: Στο endpoint /user/show_appointments
    όπου μέσα στα ραντεβού μπορεί να:

        Προβολή ενός Ραντεβού με λεπτομέρεια:  Στο endpoint /user/show_appointment/<appointment_id>

        Ακύρωση Ραντεβού: Στο endpoint /user/delete_appointment
    
