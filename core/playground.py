import pickle

with open("database/doctors.pkl", "wb") as file :
    
<<<<<<< HEAD
    doctors = [["Stephen Strange", "Surgeon"], ["Henry Wu", "Veterinary"],["George","Ortho"]]
    pickle.dump(doctors, file)

specialization = "Ortho"
with open("../database/doctors.pkl", "rb") as file :
    all_doctors = pickle.load(file)
    for doctor in all_doctors:
        if doctor[1] == specialization :
            print(doctor)
=======
    doctors = [["Stephen Strange", "Surgeon"], ["Henry Wu", "Veterinary"], ["Raheem Pate", "Ortho"]]
    pickle.dump(doctors, file)


with open("database/nurses.pkl", "wb") as file :
    
    nurses = [["Gloria Coates", "None"], ["Scarlett Mill", "None"], ["Delilah Abbott", "Ortho"]]
    pickle.dump(nurses, file)


with open("database/pharmacists.pkl", "wb") as file :
    
    pharmacists = [["Jodi Rivera", "None"], ["Florence Bloom", "None"], ["Jermaine Bennett", "Ortho"]]
    pickle.dump(pharmacists, file)


with open("database/doctors.pkl", "rb") as file :
    print(pickle.load(file))
>>>>>>> edb3009f7e7192401fc0bf9341ec31161dcd67b7




with open("database/patients.pkl", "wb") as file :

    patients = [["Catnis Everdeen", 21, "female"], ["Peeta Mellark", 19, "male"]]
    pickle.dump(patients, file)

with open("database/patients.pkl", "rb") as file :
    print(pickle.load(file))