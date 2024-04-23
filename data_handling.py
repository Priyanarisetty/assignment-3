import csv
from patients import Hospital, Patient, Visit
from datetime import datetime

def read_patient_data(file_path):
    hospital = Hospital()
    with open(file_path, 'r') as file:
        if file_path.lower().endswith('.csv'):
            reader = csv.DictReader(file)
            for row in reader:
                patient_id = row['Patient_ID']
                department_name = row['Visit_department']
                hospital.add_department(department_name)
                patient = Patient(patient_id, row['Gender'], row['Race'], int(row['Age']), row['Ethnicity'], row['Insurance'], row['Zip_code'])
                hospital.add_patient_to_department(department_name, patient)
                visit_id = row['Visit_ID']  # No conversion needed
                visit_time = datetime.strptime(row['Visit_time'], '%Y-%m-%d')
                chief_complaint = row['Chief_complaint']
                visit = Visit(visit_id, visit_time, department_name, chief_complaint)
                patient.add_visit(visit)
                note_id = row['Note_ID']
                note_type = row['Note_type']
                patient.add_note(note_id, note_type)

        else:
            print("Unsupported file format.")
    return hospital
