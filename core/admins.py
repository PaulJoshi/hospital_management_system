import pickle

class Admin :

    def add_employee(self, name, role, specialization) :

        ''' Adds a new employee to "/database/doctors.pkl" or "/database/nurses.pkl" or "/database/pharmacists.pkl" in database '''
    
        with open("database/doctors.pkl", "wb+") as file :
            doctors=pickle.load(file)
            doctor=[name,specialization]
            doctors.append(doctor)
            pickle.dump(doctors, file)

    def update_employee(self, name, role, specialization) :

        ''' Updates an employee's details in "/database/doctors.pkl" or "/database/nurses.pkl" or "/database/pharmacists.pkl" in database '''


    def view_all_employees(self) :

        ''' Get details of all doctors from database '''


        doctors = []

        return doctors

    def view_all_patients(self) :

        ''' Get details of all patients from database '''


        patients = []

        return patients