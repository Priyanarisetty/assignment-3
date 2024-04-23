from datetime import datetime
from patients import Patient

def perform_admin_actions(hospital):
    action = input("Choose an action (count_visits): ").strip().lower()
    if action == 'count_visits':
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            total_visits = hospital.count_visits_on_date(date)
            print("Total visits on", date.strftime('%Y-%m-%d'), ":", total_visits)
        except ValueError:
            print("Invalid date format.")

def perform_clinician_nurse_actions(hospital):
    while True:
        action = input("Choose an action (add_patient, remove_patient, retrieve_patient, count_visits, stop): ").strip().lower()

        if action == "stop":
            break
        elif action == "add_patient":
            add_patient_action(hospital)
        elif action == "remove_patient":
            remove_patient_action(hospital)
        elif action == "retrieve_patient":
            retrieve_patient_action(hospital)
        elif action == "count_visits":
            count_visits_action(hospital)
        else:
            print("Invalid action.")

def add_patient_action(hospital):
    patient_id = input("Enter Patient_ID: ")
    department_name = input("Enter department name: ")
    gender = input("Enter Gender: ")
    race = input("Enter Race: ")
    age = int(input("Enter Age: "))
    ethnicity = input("Enter Ethnicity: ")
    insurance = input("Enter Insurance: ")
    zip_code = input("Enter Zip code: ")
    
    # Check if department exists, if not, add it
    if department_name not in hospital.departments:
        hospital.add_department(department_name)
        print(f"Department '{department_name}' added.")

    patient = Patient(patient_id, gender, race, age, ethnicity, insurance, zip_code)
    hospital.add_patient_to_department(department_name, patient)
    print("Patient added successfully.")


def remove_patient_action(hospital):
    patient_id = input("Enter Patient_ID: ")
    removed_patient = hospital.remove_patient(patient_id)
    if removed_patient:
        print("Patient removed successfully.")
    else:
        print("Patient not found.")

def retrieve_patient_action(hospital):
    patient_id = input("Enter Patient_ID: ")
    hospital.retrieve_patient(patient_id)

def count_visits_action(hospital):
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        total_visits = hospital.count_visits_on_date(date)
        print("Total visits on", date.strftime('%Y-%m-%d'), ":", total_visits)
    except ValueError:
        print("Invalid date format.")
