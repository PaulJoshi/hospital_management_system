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
            print(f"\nWelcome {patient.name}\n\n1. Make an appointment\n2. View Appointments\n3. Update personal information\n4. Logout")
            choice = int(input("\nEnter your choice: "))
            clrscr()

            if choice == 1 :
                specialization = input("\nWhat specialization of doctor would you like to consult with? (Ortho/Surgeon/Physician) ")
                doctors = patient.get_doctors(specialization)
                if doctors == 0 :
                    print("\nNo doctors of that specialization")
                else :
                    print(f"\n\n \tDOCTOR{19 * ' '}SPECIALIZATION\n")
                    for i in range(len(doctors)) :
                        print(f"{i + 1}\t{doctors[i][0]}{(25 - len(doctors[i][0])) * ' '}{doctors[i][1]}")
                    selected_doctor = int(input("\n\nEnter choice of doctor: "))
                    while(True) :
                        clrscr()
                        time = int(input("\nWhen would you like to make an appointment?\n\n1. Today\n2. Tomorrow\n3. Day After tomorrow\n\nEnter choice: "))
                        if patient.make_appointment(doctors[selected_doctor-1][0], time) == 1 :
                            break
                        else :
                            print("\nInvalid Input")
                    input("\nAppointment made successfully\nPress enter to continue...")
            
            elif choice == 2 :
                appointments = patient.get_appointments()
                if len(appointments) == 0 :
                    print("\nNo appointments booked")
                else :
                    print(f"\nDOCTOR{19 * ' '}DATE{18 * ' '}PRESCRIPTION\n")
                    for appointment in appointments :
                        if len(appointment) == 3 :
                            print(f"{appointment[0]}{(25 - len(appointment[0])) * ' '}{appointment[2]}{(22 - len(str(appointment[2]))) * ' '}None")
                        else :
                            print(f"{appointment[0]}{(25 - len(appointment[0])) * ' '}{appointment[2]}{(22 - len(str(appointment[2]))) * ' '}{appointment[3]}")
                input("\nPress enter to continue...")

            elif choice == 3 :
                print("\nUpdate Personal Information")
                name = input("\nEnter your name: ")
                age = int(input("Enter your age: "))
                patient.update_user(name, age)
                input("\nDetails updated successfully\nPress enter to continue...")
            
            else :
                del patient
                break
    
    else :

        age = int(input("Enter your age: "))
        gender = input("Gender ( male/female ): ")
        patient.create_user(age,gender)
        input("\nNew user created successfully\nPress enter to continue...")
        patients()

def doctors() :

    clrscr()
    name = input("\nLogin\n\nEnter your name: ")
    doctor = core.employees.Doctor(name)

    while doctor != 0 :

        clrscr()
        print(f"\nWelcome Dr. {doctor.name}\n\n1. See appointments\n2. Prescribe medicine\n3. Logout")
        choice = int(input("\nEnter your choice: "))
        clrscr()

        if choice == 1 :
            appointments = doctor.get_appointments()
            print(f"\nPATIENT{18 * ' '}DATE\n")
            for appointment in appointments :
                print(appointment["patient_name"], (23 - len(appointment["patient_name"])) * ' ', appointment["date"])
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
            print(f"\nDOCTOR{19 * ' '}SPECIALIZATION{9 * ' '}\n")
            for doctor in doctors :
                print(f"{doctor[0]}{(25 - len(doctor[0])) * ' '}{doctor[1]}")
            print(f"\n\nNURSE{20 * ' '}SPECIALIZATION{9 * ' '}\n")
            for nurse in nurses :
                print(f"{nurse[0]}{(25 - len(nurse[0])) * ' '}{nurse[1]}")
            print(f"\n\nPHARMACIST{15 * ' '}SPECIALIZATION{9 * ' '}\n")
            for pharmacist in pharmacists :
                print(f"{pharmacist[0]}{(25 - len(pharmacist[0])) * ' '}{pharmacist[1]}")
            input("\n\nPress enter to continue...")

        elif choice == 2 :
            print("\nPatients")
            patients = admin.view_all_patients()
            print(f"\n\nNAME{21 * ' '}AGE{15 * ' '}GENDER\n")
            for patient in patients :
                print(f"{patient[0]}{(25 - len(patient[0])) * ' '}{patient[1]}{(18 - len(str(patient[1]))) * ' '}{patient[2]}")
            input("\n\nPress enter to continue...")

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