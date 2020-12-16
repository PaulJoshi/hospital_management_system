import pickle
import datetime

class Patient :

    def __init__(self):

        self.name = ""
        self.age = None
        self.gender = ""
    

    def create_user(self,age,gender) :

        ''' Adds a new patient to "/database/patients.pkl" in database '''

        self.age = age
        self.gender = gender

        patient = [self.name, self.age, self.gender]
        with open("database/patients.pkl", "rb") as file:
            all_patients = pickle.load(file)

        all_patients.append(patient)

        with open("database/patients.pkl", "wb") as file:
            pickle.dump(all_patients, file)


    def patient_exists(self) :

        ''' Returns 1 if patient already exists, else, returns 0 '''

        with open("database/patients.pkl", "rb") as file:
            all_patients = pickle.load(file)
        for patient in all_patients:
            if patient[0].lower() == self.name.lower():
                return 1
        return 0
    

    def get_doctors(self, specialization) :

        ''' Returns list of doctors with specified specialization '''

        doctors = []
        with open("database/doctors.pkl", "rb") as file :
            all_doctors = pickle.load(file)
            for doctor in all_doctors:
                if doctor[1].lower() == specialization.lower() :
                    doctors.append(doctor)
        if len(doctors) == 0:
            return 0
        return doctors


    def make_appointment(self, doctor, date) :

        ''' Adds an appointment to "/database/appointments.pkl" in database '''
         
        if date == 1:
            a = datetime.datetime.today()
            current_date = a.day, a.month, a.year
            appointment = [doctor, self.name, current_date]

        elif date == 2:
            b = datetime.datetime.today()
            next_date = b.day + 1, b.month, b.year
            appointment = [doctor, self.name, next_date]

        elif date == 3:
            c = datetime.datetime.today()
            next_next_date = c.day + 2, c.month, c.year
            appointment = [doctor, self.name, next_next_date]

        else:
            return 0

        with open("database/appointments.pkl", "rb") as file :
            appointments=pickle.load(file)
        with open("database/appointments.pkl", "wb") as file :    
            appointments.append(appointment)
            pickle.dump(appointments, file)
        return 1
           

    def update_user(self,name, age) :

        ''' Changes the details of given user in "/database/patients.pkl" in database '''

        with open("database/patients.pkl", "rb") as file:
            patients = pickle.load(file)
        
        for patient in patients:
            if patient[0].lower() == self.name.lower():
                patient[0] = name
                patient[1] = age

        with open("database/patients.pkl", "wb") as file:
            pickle.dump(patients,file)

        
        with open("database/appointments.pkl", "rb") as file:
            appointments = pickle.load(file)
        
        for appointment in appointments:
            if appointment[1].lower() == self.name.lower():
                appointment[1] = name
                
        with open("database/appointments.pkl", "wb") as file:
            pickle.dump(appointments, file)

        self.name = name
        self.age = age


    def get_appointments(self) :

        ''' Get all appointments of given patient name '''

        appointments = []
        with open("database/appointments.pkl", "rb") as file:
            all_appointments = pickle.load(file)

        for appointment in all_appointments:
            if appointment[1].lower() == self.name.lower():
                appointments.append(appointment)

        return appointments