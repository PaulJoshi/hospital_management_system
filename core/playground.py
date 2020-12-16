import pickle

with open("database/doctors.pkl", "wb") as file :
    doctors = [["Stephen Strange", "Surgeon"], ["Henry Wu", "Physician"], ["Raheem Pate", "Ortho"], ["Rahul Mayya", "Physician"], ["Abdul Nasir", "Ortho"], ["Karthik Kiran", "Surgeon"]]
    pickle.dump(doctors, file)


with open("database/nurses.pkl", "wb") as file : 
    nurses = [["Gloria Coates", "None"], ["Scarlett Mill", "None"], ["Delilah Abbott", "Ortho"]]
    pickle.dump(nurses, file)


with open("database/pharmacists.pkl", "wb") as file :
    pharmacists = [["Jodi Rivera", "None"], ["Florence Bloom", "None"], ["Jermaine Bennett", "None"]]
    pickle.dump(pharmacists, file)


with open("database/doctors.pkl", "rb") as file :
    print(pickle.load(file))


with open("database/patients.pkl", "wb") as file :
    patients = [["Catnis Everdeen", 21, "female"], ["Peeta Mellark", 19, "male"]]
    pickle.dump(patients, file)


with open("database/patients.pkl", "rb") as file :
    print(pickle.load(file))


with open("database/appointments.pkl", "wb") as file :
    appointments = [["Stephen Strange", "Catnis Everdeen",(4,12,2020)], ["Henry Wu", "Peeta Mellark", (5,12,2020)]]
    pickle.dump(appointments, file)