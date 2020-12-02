import pickle

class Doctor :

    '''Methods'''

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


class Nurse :

    ''' Methods '''
    pass

class Pharmacist :

    ''' Methods '''
    pass