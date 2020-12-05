import pickle
import datetime

class Patient :

    def __init__(self):

        self.name = ""
        self.age = None
        self.gender = ""
    

    def create_user(self) :

        ''' Adds a new patient to "/database/patients.pkl" in database '''

    def patient_exists(self) :

        ''' Returns 1 if patient already exists, else, returns 0 '''

        return 1
    

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
            next_date = b.day+1, b.month, b.year
            appointment = [doctor, self.name, next_date]
        elif date == 3:
            c = datetime.datetime.today()
            next_next_date = c.day+2, c.month, c.year
            appointment = [doctor, self.name, next_next_date]
        else:
            return 0

        with open("database/appointments.pkl", "rb") as file :
            appointments=pickle.load(file)
        with open("database/appointments.pkl", "wb") as file :    
            appointments.append(appointment)
            pickle.dump(appointments, file)
        
        return 1
           

    def update_user(self) :

        ''' Changes the details of given user in "/database/patients.pkl" in database '''

    def get_appointments(self) :

        ''' Get all appointments of given patient name '''

        appointments = [        #temporary hardcoded values
            {
                "doctor_name" : "Stephen Strange",
                "time" : None
            },
            {
                "doctor_name" : "Doc Hudson",
                "time" : None
            },
        ]

        return appointments
