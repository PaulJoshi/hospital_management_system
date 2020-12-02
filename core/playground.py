import pickle

with open("../database/doctors.pkl", "wb") as file :
    
    doctors = [["Stephen Strange", "Surgeon"], ["Henry Wu", "Veterinary"]]
    pickle.dump(doctors, file)

with open("../database/doctors.pkl", "rb") as file :
    print(pickle.load(file))



with open("../database/patients.pkl", "wb") as file :

    patients = [["Catnis Everdeen", 21, "female"], ["Peeta Mellark", 19, "male"]]
    pickle.dump(patients, file)

with open("../database/patients.pkl", "rb") as file :
    print(pickle.load(file))