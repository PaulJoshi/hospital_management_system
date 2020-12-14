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

        with open(r"database\doctors.pkl","rb")as file:
            doctors=pickle.load(file)

        with open(r"database\nurses.pkl","rb")as file:
            nurses=pickle.load(file)

        with open(r"database\pharmacists.pkl","rb")as file:
            pharmacists=pickle.load(file)
      

        return doctors,nurses,pharmacists

    def view_all_patients(self) :

        ''' Get details of all patients from database '''

        with open(r"database\patients.pkl","rb")as file:
            patients=pickle.load(file)
        

        return patients 