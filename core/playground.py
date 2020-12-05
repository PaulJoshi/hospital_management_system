import pickle

with open("database/doctors.pkl", "wb") as file :
    
    doctors = [["Stephen Strange", "Surgeon"], ["Henry Wu", "Veterinary"],["George","Ortho"]]
    pickle.dump(doctors, file)

specialization = "Ortho"
with open("../database/doctors.pkl", "rb") as file :
    all_doctors = pickle.load(file)
    for doctor in all_doctors:
        if doctor[1] == specialization :
            print(doctor)




with open("database/patients.pkl", "wb") as file :

    patients = [["Catnis Everdeen", 21, "female"], ["Peeta Mellark", 19, "male"]]
    pickle.dump(patients, file)

with open("database/patients.pkl", "rb") as file :
    print(pickle.load(file))