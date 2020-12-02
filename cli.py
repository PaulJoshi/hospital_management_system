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

    if patient.user_exists() :

        while True :

            clrscr()
            print("\nPatient Dashboard\n\n1. Make an appointment\n2. View Appointments\n3. Update personal information\n4. Logout")
            choice = int(input("\nEnter your choice: "))

            if choice == 1 :
                patient.make_appointment()
            
            elif choice == 2 :
                appointments = patient.get_appointments()
                print(appointments)
                input("\nPress any key to continue...")

            elif choice == 3 :
                patient.name = input("\nEnter your name: ")
                patient.age = int(input("Enter your age: "))
                patient.update_user()
                input("\nDetails updated successfully\nPress any key to continue...")
            
            else :
                del patient
                main()
    
    else :

        patient.age = int(input("Enter your age: "))
        patient.gender = input("Gender ( male/female ): ")
        patient.create_user()
        patients()


def doctors() :


    clrscr()
    name = input("\nLogin\n\nEnter your name: ")
    doctor = core.employees.Doctor(name)

    while True :

        clrscr()
        print("\nDoctor's Dashboard\n\n1. See appointments\n2. Logout")
        choice = int(input("\nEnter your choice: "))

        if choice == 1 :
            appointments = doctor.get_appointment()
            print(appointments)
            input("\nPress any key to continue...")

        else :
            del doctor
            main()

def admins() :

    admin = core.admins.Admin()

    clrscr()

    while True :

        clrscr()
        print("\nAdmin's Dashboard\n\n1. View employees\n2. View patients\n3. Add Employee\n4. Update Employee\n5. Logout")
        choice = int(input("\nEnter your choice: "))

        if choice == 1 :
            clrscr()
            print("\nEmployees")
            doctors = admin.view_all_employees()
            print(doctors)
            input("\nPress any key to continue...")

        if choice == 2 :
            clrscr()
            print("\nPatients")
            patients = admin.view_all_patients()
            print(patients)
            input("\nPress any key to continue...")

        if choice == 3 :
            clrscr()
            print("\nAdd Employee")
            name = input("\nEnter name: ")
            role = input("Enter role: ")
            specialization = input("Enter specialization: ")
            admin.add_employee(name, role, specialization)
            input("\nEmployee Added Successfully\nPress any key to continue...")

        if choice == 4 :
            clrscr()
            print("\nUpdate Employee")
            name = input("\nEnter name: ")
            role = input("Enter role: ")
            specialization = input("Enter specialization: ")
            admin.update_employee(name, role, specialization)
            input("\nEmployee Details Updated Successfully\nPress any key to continue...")

        else :
            del admin
            main()

def main() :

    ''' FLow of control starts here '''

    run = True
    while run :

        clrscr()
        print("\nLogin for:\n\n1. Patients\n2. Doctors\n3. Managers")
        choice = int(input("\nEnter your choice: "))

        if choice == 1 :
            patients()
        
        elif choice == 2 :
            doctors()

        elif choice == 3 :
            admins()
        
        else : run = False

if __name__ == "__main__" :
    main()