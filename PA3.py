import sys
from users import read_credentials, authenticate_user
from patients import Hospital
from actions import perform_admin_actions, perform_clinician_nurse_actions
from reports import generate_statistics_report
from data_handling import read_patient_data

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <credentials_file_path> <patients_file_path>")
        return

    credentials_file = sys.argv[1]
    patients_file = sys.argv[2]

    # Load hospital data
    hospital = read_patient_data(patients_file)

    # Load user credentials
    users = read_credentials(credentials_file)

    authenticated_user = None
    while authenticated_user is None:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authenticated_user = authenticate_user(username, password, users)
        if authenticated_user is None:
            print("Invalid credentials. Please try again.")

    if authenticated_user.role == 'admin':
        print("You have admin role. You can perform count_visits.")
        perform_admin_actions(hospital)
    elif authenticated_user.role in ['clinician', 'nurse']:
        print("You have clinician/nurse role.")
        perform_clinician_nurse_actions(hospital)
    elif authenticated_user.role == 'management':
        generate_statistics_report(hospital)

if __name__ == "__main__":
    main()
