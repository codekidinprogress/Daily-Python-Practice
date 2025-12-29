class Doctor:
    def consult(self):
        print("Doctor: Patient consultation done")

class Pharmacy:
    def medicine(self):
        print("Pharmacy: Medicines provided")

class Patient(Doctor, Pharmacy):
    def admit(self):
        print("Patient: Admitted to hospital")

p = Patient()
p.consult()
p.medicine()
p.admit()
