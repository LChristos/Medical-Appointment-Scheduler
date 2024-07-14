# Υποχρεωτική Εργασία 2024 - Ιατρικά Ραντεβού

## Περιεχόμενα

1. [Επιπλέον Παραδοχές που Επιλέξατε](#επιπλέον-παραδοχές-που-επιλέξατε)
2. [Τεχνολογίες που Χρησιμοποιήθηκαν](#τεχνολογίες-που-χρησιμοποιήθηκαν)
3. [Περιγραφή των Αρχείων που Κατασκευάσατε](#περιγραφή-των-αρχείων-που-κατασκευάσατε)
4. [Τρόπος Εκτέλεσης Συστήματος](#τρόπος-εκτέλεσης-συστήματος)
5. [Τρόπος Χρήσης του Συστήματος](#τρόπος-χρήσης-του-συστήματος)
6. [Αναφορές που Χρησιμοποιήσατε](#αναφορές-που-χρησιμοποιήσατε)

## Επιπλέον Παραδοχές που Επιλέξατε

- Κάθε ιατρός μπορεί να έχει μόνο μία ειδικότητα.
- Οι ασθενείς δεν μπορούν να κάνουν δύο ραντεβού για την ίδια ώρα.

## Τεχνολογίες που Χρησιμοποιήθηκαν

- Python 3.12
- Flask
- MongoDB
- Docker
- Docker Compose
- HTML (για τα templates)
- Jinja2 (για τα templates)
- Fernet (για την κρυπτογράφηση των κωδικών)

## Περιγραφή των Αρχείων που Κατασκευάσατε

- **requirements.txt**: Περιέχει όλες τις βιβλιοθήκες που θα εγκαταστήσουμε για το έργο
- **main.py**: Το κύριο αρχείο που τρέχουμε για τον Flask API server.
- **docker-compose.yml**: Αρχείο για την εκκίνηση των containers για το API server και τη βάση δεδομένων MongoDB.
- **Dockerfile**: Αρχείο για τη δημιουργία του Docker image του API server.

### Φάκελος `data`

Περιέχει τους πίνακες (collections) και τα δεδομένα της βάσης δεδομένων

### Φάκελος `app`

Περιέχει τον κώδικα της εφαρμογής:

- **app/\_\_init\_\_.py**: Αρχείο αρχικοποίησης της εφαρμογής 
- **app/repository.py**: Περιέχει τις συναρτήσεις   για τη διαχείριση της βάσης δεδομένων και τα endpoints για τις διαδρομές  και τις μεθόδους του συστήματος
- **app/model/appointment.py**: Ορισμός του μοντέλου για τα ραντεβού.
- **app/model/doctor.py**: Ορισμός του μοντέλου για τους ιατρούς.
- **app/model/patient.py**: Ορισμός του μοντέλου για τους ασθενείς.
- **app/template**: Περιέχει τα HTML templates για την εμφάνιση των δεδομένων.
- **app/utils/crypto_utils.py**: Περιέχει τις συναρτήσεις για την κρυπτογράφηση των κωδικών.

### Φάκελος `app/template`

Περιέχει τα HTML templates για την εμφάνιση των δεδομένων. Σύμφωνα και με το *app/repository.py*:
- **home.html**(home): είναι η αρχική σελίδα και αν δεν έχει κάνει σύνδεση ο χρήστης τότε πάει στην login.html
- **login.html**(login):είναι η σελίδα σύνδεσης για έναν διαχειριστή , γιατρό ή χρήστη , όπου ο χρήστη θα πρέπει να κάνει πρώτα εγγράφή στην sign_up.html

**Αν γίνει σύνδεση ως Διαχειριστής**
- **add_doctor.html**(new_doctor): ο admin μπορεί να προσθέσει έναν νέο γιατρό στο σύστημα
- **delete_doctor.html**(delete_doctor): o admin μπορεί να διαγράψει έναν γιατρό με το username
- **delete_patient.html**(delete_patient): ο admin μπορεί να διαγράψει έναν ασθενή με το username
- **change_doctor_password.html**(change_password_admin): ο admin μπορεί να αλλάξει τον κωδικό ενός γιατρού

**Αν γίνει σύνδεση ως Ιατρός**
- **change_password.html**(change_password): o γιατρός μπορεί να αλλάξει τον κωδικό του 
- **change_price.html**(change_price): ο γιατρός μπορεί να αλλάξει την τιμή του 
- **show_doctor_appointments.html**(show_doctor_appointments): ο γιατρός μπορεί να δει όλα τα μελλοντικά ραντεβού

**Αν γίνει σύνδεση ως ασθενής**
- **sign_up.html**(sign_up): ο ασθενής κάνει την εγγραφή του
- **add_appointment.html**(new_appointment): ο ασθενής προσπαθεί να κάνει κράτηση ραντεβού
- **show_patient_appointments.html**(show_appointments): ο ασθενής εμφανίζει όλα τα μελλοντικά ραντεβού του
- **show_one_appointment.html**(show_oneappointment): ο ασθενής εμφανίζει ένα συγκεκριμένο ραντεβού
- (delete_appointment): ο ασθενής διαγράφει ένα ραντεβού


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
    