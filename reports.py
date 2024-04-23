def generate_statistics_report(hospital):
    print("You have management role. Generating key statistics report...")

    # Initialize dictionaries to store counts
    visits_by_insurance = {}
    visits_by_race = {}
    visits_by_gender = {}
    visits_by_ethnicity = {}

    # Iterate through departments and patients to collect data
    for department in hospital.departments.values():
        for patient in department.patients:
            for visit in patient.visits:
                # Count visits by insurance
                insurance = patient.insurance
                if insurance not in visits_by_insurance:
                    visits_by_insurance[insurance] = 0
                visits_by_insurance[insurance] += 1

                # Count visits by race
                race = patient.race
                if race not in visits_by_race:
                    visits_by_race[race] = 0
                visits_by_race[race] += 1

                # Count visits by gender
                gender = patient.gender
                if gender not in visits_by_gender:
                    visits_by_gender[gender] = 0
                visits_by_gender[gender] += 1

                # Count visits by ethnicity
                ethnicity = patient.ethnicity
                if ethnicity not in visits_by_ethnicity:
                    visits_by_ethnicity[ethnicity] = 0
                visits_by_ethnicity[ethnicity] += 1

    # Print statistics for each category
    print("\n1. Temporal trend of the number of patients who visited the hospital with different types of insurances:")
    print("{:<30} {:<10}".format("Insurance", "Number of Patients"))
    for insurance, count in visits_by_insurance.items():
        print("{:<30} {:<10}".format(insurance, count))

    print("\n2. Temporal trend of the number of patients who visited the hospital in different demographics groups:")
    print("  - Race:")
    print("{:<20} {:<10}".format("Race", "Number of Patients"))
    for race, count in visits_by_race.items():
        print("{:<20} {:<10}".format(race, count))

    print("  - Gender:")
    print("{:<20} {:<10}".format("Gender", "Number of Patients"))
    for gender, count in visits_by_gender.items():
        print("{:<20} {:<10}".format(gender, count))

    print("  - Ethnicity:")
    print("{:<20} {:<10}".format("Ethnicity", "Number of Patients"))
    for ethnicity, count in visits_by_ethnicity.items():
        print("{:<20} {:<10}".format(ethnicity, count))
