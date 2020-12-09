import os
import core.patients
import core.employees
import core.admins

clrscr = lambda : os.system('cls||clear') # Clears terminal viewport

def patients() :

    patient = core.patients.Patient()

    clrscr()
    print("\nLogin or Signup:")
    patient.name = input("\nEnter your name: ")

    if patient.patient_exists() :

        while True :

            clrscr()
            print("\nPatient Dashboard\n\n1. Make an appointment\n2. View Appointments\n3. Update personal information\n4. Logout")
            choice = int(input("\nEnter your choice: "))
            clrscr()

            if choice == 1 :
                specialization = input("\nWhat specialization of doctor would you like to consult with? (Ortho/Surgeon/Physician) ")
                doctors = patient.get_doctors(specialization)
                if doctors == 0 :
                    print("No doctors of that specialization")
                else :
                    for i in range(len(doctors)) :
                        print(f"\n{i + 1} : {doctors[i]}")
                    selected_doctor = input("\nEnter choice of doctor: ")
                    while(True) :
                        clrscr()
                        time = int(input("\nWhen would you like to make an appointment?\n1. Today\n2. Tomorrow\n3. Day After tomorrow\nEnter choice: "))
                        if patient.make_appointment(selected_doctor, time) == 1 :
                            break
                        else :
                            print("\nInvalid Input")
                    input("\nAppointment made successfully\nPress enter to continue...")
            
            elif choice == 2 :
                appointments = patient.get_appointments()
                print(appointments)
                input("\nPress enter to continue...")

            elif choice == 3 :
                name = input("\nEnter your name: ")
                age = int(input("Enter your age: "))
                patient.update_user(name, age)
                input("\nDetails updated successfully\nPress enter to continue...")
            
            else :
                del patient
                break
    
    else :

        patient.age = int(input("Enter your age: "))
        patient.gender = input("Gender ( male/female ): ")
        patient.create_user()
        input("\nNew user created successfully\nPress enter to continue...")
        patients()

def doctors() :

    clrscr()
    name = input("\nLogin\n\nEnter your name: ")
    doctor = core.employees.Doctor(name)

    while doctor != 0 :

        clrscr()
        print("\nDoctor's Dashboard\n\n1. See appointments\n2. Prescribe medicine\n3. Logout")
        choice = int(input("\nEnter your choice: "))

        if choice == 1 :
            appointments = doctor.get_appointments()
            print(appointments)
            input("\nPress enter to continue...")
        
        elif choice == 2 :
            patient_name = input("Enter name of patient: ")
            prescription = input("Enter prescription for patient: ")
            doctor.prescribe_medicine(patient_name, prescription)
            input("\nPrescription sent\nPress enter to continue...")

        else :
            del doctor
            break
    
    else :
        print("Doctor name does not exist")
        input("\nPress enter to continue...")

def admins() :

    admin = core.admins.Admin()

    while True :

        clrscr()
        print("\nAdmin's Dashboard\n\n1. View employees\n2. View patients\n3. Add Employee\n4. Update Employee\n5. Logout")
        choice = int(input("\nEnter your choice: "))
        clrscr()

        if choice == 1 :
            print("\nEmployees")
            doctors, nurses, pharmacists = admin.view_all_employees()
            print(doctors, nurses, pharmacists)
            input("\nPress enter to continue...")

        elif choice == 2 :
            print("\nPatients")
            patients = admin.view_all_patients()
            print(patients)
            input("\nPress enter to continue...")

        elif choice == 3 :
            print("\nAdd Employee")
            name = input("\nEnter name: ")
            role = input("Enter role: ")
            specialization = input("Enter specialization: ")
            admin.add_employee(name, role, specialization)
            input("\nEmployee Added Successfully\nPress enter to continue...")

        elif choice == 4 :
            print("\nUpdate Employee")
            name = input("\nEnter name: ")
            role = input("Enter role: ")
            specialization = input("Enter specialization: ")
            admin.update_employee(name, role, specialization)
            input("\nEmployee Details Updated Successfully\nPress enter to continue...")

        else :
            del admin
            break

def main() :

    ''' FLow of control starts here '''

    run = True
    while run :

        clrscr()
        print("\nLogin for:\n\n1. Patients\n2. Doctors\n3. Managers\n4. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1 :
            patients()
        
        elif choice == 2 :
            doctors()

        elif choice == 3 :
            admins()
        
        else : 
            clrscr()
            run = False

if __name__ == "__main__" :
    main()