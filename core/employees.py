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
    
    def __init__(self, name) :
        self.name = name
        self.specialization = specialization
    

    def get_appointments(self) :

        ''' Get all appointments of given doctor name '''

        with open ("database/appointments.pkl","rb") as file:
            all_appointments=pickle.load(file)
        appointments=[]
        dictionary={}
        for appointment in all_appointments:
            if appointment[0].lower()==self.name.lower():
                dictionary[ "patient_name"]=appointment[1]
                dictionary[ "time"]=appointment[2]
                appointments.append(dictionary)


        return appointments
    
    def prescribe_medicine(self, patient_name) :

        ''' Write medicine prescription name into most recent appointment list in database '''
        


class Nurse :

    ''' Methods '''
    pass

class Pharmacist :

    ''' Methods '''
    pass