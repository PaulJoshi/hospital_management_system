import pickle
import time

class Doctor :

    def __init__(self, name):

        self.name = name
        self.specialization = None  # Get specialization from database
    

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