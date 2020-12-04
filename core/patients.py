import pickle
import time

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


    def make_appointment(self, doctor) :

        ''' Adds an appointment to "/database/appointments.pkl" in database '''


        return 0


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