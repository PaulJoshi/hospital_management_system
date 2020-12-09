import pickle
import time

class Doctor :

    def __new__(cls, name):

        with open("database/doctors.pkl", "rb") as file :
            for doctor in pickle.load(file) :
                if doctor[0].lower() == name.lower() :
                    specialization = doctor[1]
                    return super(Doctor, cls).__new__(cls) 
        return 0
    
    def __init(self, name) :
        self.name = name
        self.specialization = specialization
    

    def get_appointments(self, doctor_name) :

        ''' Get all appointments of given doctor name '''





        appointments = [        #temporary hardcoded values
            {
                "patient_name" : "John Doe",
                "time" : None
            },
            {
                "patient_name" : "Jane Austen",
                "time" : None
            },
        ]

        return appointments
    
    def prescribe_medicine(self, patient_name) :

        ''' Write medicine prescription name into most recent appointment list in database '''
        


class Nurse :

    ''' Methods '''
    pass

class Pharmacist :

    ''' Methods '''
    pass