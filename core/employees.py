import pickle
import time

class Doctor :

    def __new__(cls, name):

        with open("database/doctors.pkl", "rb") as file :
            for doctor in pickle.load(file) :
                if doctor[0].lower() == name.lower() :
                    return super(Doctor, cls).__new__(cls) 
        return 0
    
    def __init__(self, name) :
        self.name = name
        with open("database/doctors.pkl", "rb") as file :
            for doctor in pickle.load(file) :
                if doctor[0].lower() == name.lower() :
                    self.specialization = doctor[1]
    

    def get_appointments(self) :

        ''' Get all appointments of given doctor name '''

        with open ("database/appointments.pkl", "rb") as file:
            all_appointments = pickle.load(file)

        appointments = []
        dictionary = {}

        for appointment in all_appointments:
            if appointment[0].lower() == self.name.lower():
                dictionary["patient_name"] = appointment[1]
                dictionary["date"] = appointment[2]
                appointments.append(dictionary)

        return appointments


    def prescribe_medicine(self, patient_name, prescription) :

        ''' Write medicine prescription name into most recent appointment list in database '''

        with open ("database/appointments.pkl", "rb") as file:
            all_appointments = pickle.load(file)

        for i in reversed(range(len(all_appointments))) :
            if all_appointments[i][0].lower() == self.name.lower() and all_appointments[i][1].lower() == patient_name.lower() :
                all_appointments[i].append(prescription)

        with open ("database/appointments.pkl", "wb") as file:
            pickle.dump(all_appointments, file)