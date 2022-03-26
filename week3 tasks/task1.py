import time

patient_data = [
    {'MRN': '10130001', 'Name': 'Ahmed Ali', 'Age': 55, 'Nationality': 'Saudi',
        'Gender': 'M', 'Status': 'M', 'Procedure Time': '10:30AM', 'Status Title': 'Addmitted'},
    {'MRN': '10152001', 'Name': 'Sara Mohammad', 'Age': 39, 'Nationality': 'Saudi',
        'Gender': 'F', 'Status': 'A', 'Procedure Time': '09:50AM', 'Status Title': 'Arrive'},
    {'MRN': '20133601', 'Name': 'Yuosuf Hassan', 'Age': 10, 'Nationality': 'Egyption',
        'Gender': 'M', 'Status': 'A', 'Procedure Time': '08:30AM', 'Status Title': 'Arrive'},
    {'MRN': '20163690', 'Name': 'Ameerah Khalid', 'Age': 44, 'Nationality': 'Pakistan',
        'Gender': 'F', 'Status': 'D', 'Procedure Time': '01:00AM', 'Status Title': 'Discharged'},
    {'MRN': '10136914', 'Name': 'Maha Majed', 'Age': 60, 'Nationality': 'Saudi',
        'Gender': 'F', 'Status': 'M', 'Procedure Time': '09:00AM', 'Status Title': 'Addmitted'}
]


class Patient:
    patients = []  
    
    # create class attributes
    def __init__(self, mrn, name, age, nationality, gender, status, procedure_time, status_title):
        self.mrn = mrn
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.status = status
        self.procedure_time = procedure_time
        self.status_title = status_title

    @staticmethod
    def add_patient(mrn, name, age, nationality, gender, status, procedure_time, status_title):
        p = Patient(mrn, name, age, nationality, gender, status, procedure_time, status_title)
        Patient.patients.append(p)

    @staticmethod
    def search(by, value):
        searched = []
        for patient in Patient.patients:
            if str(getattr(patient, by)) == value:
                searched.append(patient)
        return searched

    @staticmethod
    def sort(option):
        if option == '1':
            sorted_list = sorted(Patient.patients, key=lambda x: x.age)
            return sorted_list
        elif option == '2':
            sorted_list = sorted(Patient.patients,
                                 key=lambda x: x.age, reverse=True)
            return sorted_list
        else:
            return []

    @staticmethod
    def statics():
        # all
        # Arrived -> A
        # Discharged -> D
        # Admitted -> M
        admitted_patients = len([p for p in Patient.patients if p.status == "A"])
        discharged_patients = len([p for p in Patient.patients if p.status == "D"])
        print('No of patients:', len(Patient.patients), '\nNo of admitted:', admitted_patients, '\nNo of discharged:', discharged_patients)
    
    @staticmethod
    def display_by_nationality():
        saudi_patients = [p.mrn for p in Patient.patients if p.nationality == 'Saudi']
        print('Saudi Patients Count: ', len(saudi_patients))
        for p in saudi_patients:
            print(p)
        print('-'*20)    
        non_saudi_patients = [p.mrn for p in Patient.patients if p.nationality != 'Saudi']
        print('Non Saudi Patients Count: ', len(non_saudi_patients))
        for p in non_saudi_patients:
            print(p)
            
    @staticmethod
    def display_status_title():
        saudi_patients = [(p.mrn, p.status_title) for p in Patient.patients if p.nationality == 'Saudi']
        non_saudi_patients = [(p.mrn, p.status_title) for p in Patient.patients if p.nationality != 'Saudi']
        print('Saudi Patients MRN , Status Title: ')
        for p in saudi_patients:
            print(p)
        print('-'*20)
        print('Non Saudi Patients MRN , Status Title: ')
        for p in non_saudi_patients:
            print(p)
        print('-'*20)  
    
    @staticmethod
    def display_procedure_time(option):
        if option == '1':
            sorted_list = sorted(Patient.patients, key=lambda x: x.procedure_time)
            return sorted_list
        elif option == '2':
            sorted_list = sorted(Patient.patients,
                                 key=lambda x: x.procedure_time, reverse=True)
            return sorted_list
        else:
            return []
    
    def __str__(self):
        return f"Patient(MRN={self.mrn}, NAME={self.name}, AGE={self.age}, NATIONALITY={self.nationality}, GENDER={self.gender}, STATUS={self.status}, PROCEDURE_TIME={self.procedure_time}, STATUS_TITLE={self.status_title})"

    def __repr__(self):
        return self.__str__()


for p_data in patient_data:
    Patient.add_patient(p_data['MRN'], p_data['Name'], p_data['Age'], p_data['Nationality'], p_data['Gender'], p_data['Status'], p_data['Procedure Time'], p_data['Status Title'])
print(Patient.patients)


# -------- Helper functions --------
def print_msg(msg):
    print('\n'+"=" * 20+f'\n{msg}\n'+"=" * 20)
    
def print_result(result):
    print('\nResult\n'+'='*10)
    for item in result:
        print(item)
        
def format_time(pro_time):
    format = '%I:%M%p'
    time_hour = time.strptime(pro_time, format)
    result = time.strftime(format, time_hour)
    return result

# start program
if __name__ == "__main__":
    print_msg('Welcome to our program')
    while True:
        print('\nSelect an option:\n1. Add Patient\n2. Search Patient\n3. Sort by age\n4. Statistics\n5. MRN By Nationality\n6. MRN status Title\n7. Sort by Procedure Time\nq. Quit')
        option = input('Select Option: ')
        if(option == '1'):
            try:
                mrn = input('Enter MRN number: ')
                name = input('Enter Name: ').capitalize()
                age = int(input('Enter Age: '))
                nationality = input('Enter Nationality: ').capitalize()
                gender = input('Enter Gender: ').upper()
                status = input('Enter Status (A, D, M): ').upper()
                procedure_time = format_time(input('Enter Procedure Time: '))
                status_title = input('Enter Status Title (Addmitted, Arrive, Discharge): ').capitalize()
                Patient.add_patient(mrn, name, age, nationality, gender, status, procedure_time, status_title)
                print_msg("Patient Added")
            except Exception as e:
                print(e)
                print_msg("Invalid Inputs")
        elif(option == "2"):
            attrs = ['mrn', 'age', 'name', 'nationality', 'gender', 'status']
            print_msg("Search By: ")
            for i, attr in enumerate(attrs):  # [(0, value), (2, value), ...]
                print(f"{i}. {attr}")
            try:
                by = int(input("Choice: "))
                value = input("Enter Value: ").lower().capitalize()
                results = Patient.search(attrs[by], value)
                if len(results) != 0:
                    print_msg(f"Found: {len(results)}")
                    print_result(results)
                else:
                    print_msg('Patient not found!')
            except:
                print_msg("Invalid Choice.")
        elif(option == "3"):
            print_msg("Sort type by age:")
            print("1. Ascending\n2. Descending")
            results = Patient.sort(input("Type: "))
            print_result(results)
        elif(option == "4"):
            print_msg("Statistics:")
            Patient.statics()
        elif(option == '5'):
            print_msg("Count Saudi and Non Saudi patients")
            Patient.display_by_nationality()
        elif(option == '6'):
            Patient.display_status_title()
        elif(option == '7'):
            print_msg("Sort type by Procedure Time:")
            print("1. Ascending\n2. Descending")
            results = Patient.display_procedure_time(input("Type: "))
            print_result(results)
        elif(option.lower() == "q"):
            print_msg("Thanks for using our program")
            break
        else:
            print_msg("Invalid option.")