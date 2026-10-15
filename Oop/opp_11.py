class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display_details(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")
        print("-" * 30)


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        for p in self.patients:
            if p.patient_id == patient.patient_id:
                print("Patient ID already exists!")
                return

        self.patients.append(patient)
        print("Patient added successfully!")

    def display_patients(self):
        if not self.patients:
            print("No patient records found.")
            return

        print("\n--- Patient Records ---")
        for patient in self.patients:
            patient.display_details()

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print("\nPatient found:")
                patient.display_details()
                return

        print("Patient not found!")



hospital = Hospital()

while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")

        try:
            age = int(input("Enter patient age: "))
            if age <= 0:
                print("Age must be positive!")
                continue
        except ValueError:
            print("Please enter a valid age!")
            continue

        disease = input("Enter disease: ")

        patient = Patient(patient_id, name, age, disease)
        hospital.add_patient(patient)

    elif choice == "2":
        hospital.display_patients()

    elif choice == "3":
        patient_id = input("Enter patient ID to search: ")
        hospital.search_patient(patient_id)

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
