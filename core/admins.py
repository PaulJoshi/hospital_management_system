import pickle

class Admin :

    def add_employee(self, name, role, specialization) :

        ''' Adds a new employee to database '''
    
        if role.lower() == 'doctor':
            with open("database/doctors.pkl", "rb") as file :
                doctors = pickle.load(file)
            with open("database/doctors.pkl", "wb") as file :
                doctor = [name, specialization]
                doctors.append(doctor)
                pickle.dump(doctors, file)
            return 1

        elif role.lower() == 'nurse':
            with open("database/nurses.pkl", "rb") as file :
                nurses = pickle.load(file)
            with open("database/nurses.pkl", "wb") as file :
                nurse = [name, specialization]
                nurses.append(nurse)
                pickle.dump(nurses, file)
            return 1

        elif role.lower() == 'pharmacist':
            with open("database/pharmacists.pkl", "rb") as file :
                pharmacists = pickle.load(file)
            with open("database/pharmacists.pkl", "wb") as file :
                pharmacist = [name, specialization]
                pharmacists.append(pharmacist)
                pickle.dump(pharmacists, file)
            return 1

        return 0


    def update_employee(self, name, role, specialization) :

        ''' Updates an employee's details in database '''

        with open("database/doctors.pkl", "rb") as file :
            doctors=pickle.load(file)
        for doctor in doctors:
            if doctor[0].lower()==name.lower():
                doctors.remove(doctor)
                with open("database/doctors.pkl", "wb") as file :
                    pickle.dump(doctors, file)

        with open("database/pharmacists.pkl", "rb") as file :
            pharmacists=pickle.load(file)
        for pharmacist in pharmacists:
            if pharmacist[0].lower()==name.lower():
                pharmacists.remove(pharmacist)
                with open("database/pharmacists.pkl", "wb") as file :
                    pickle.dump(pharmacists, file)

        with open("database/nurses.pkl", "rb") as file :
            nurses=pickle.load(file)
        for nurse in nurses:
            if nurse[0].lower()==name.lower():
                nurses.remove(nurse)
                with open("database/nurses.pkl", "wb") as file :
                    pickle.dump(nurses, file)
        
        self.add_employee(name, role, specialization)
        

    def view_all_employees(self) :

        ''' Returns details of all doctors from database '''

        with open("database/doctors.pkl", "rb") as file:
            doctors = pickle.load(file)

        with open("database/nurses.pkl", "rb") as file:
            nurses = pickle.load(file)

        with open("database/pharmacists.pkl", "rb") as file:
            pharmacists = pickle.load(file)
      
        return doctors, nurses, pharmacists


    def view_all_patients(self) :

        ''' Returns details of all patients from database '''

        with open("database/patients.pkl", "rb") as file:
            patients = pickle.load(file)
        
        return patients 