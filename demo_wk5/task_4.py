MENU = "(D)etermine grade\n(C)alculate GPA\n(A)dd subject score\n(Q)uit"
FILENAME = "subjects.txt"


def main():
    """GPA program."""
    name = input("Name: ")
    print(f"Hi {name}. Choose:\n{MENU}")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            score = float(input("What is your total score? "))
            grade = determine_grade(score)
            print(grade)

        elif choice == "C":
            subjects = get_subjects_from_file()
            subject_grades = determine_subject_grades(subjects)
            final_gpa = calculate_gpa(subject_grades)
            print_subjects(subject_grades)
            print(f"Your GPA for {len(subject_grades)} subject(s) is {final_gpa:.2f}")

        elif choice == "A":
            subject_code = input("Subject code: ")
            subject_score = input("Total score: ")
            add_subject_to_file(subject_code, subject_score)
            print(f"{subject_code} with a score of {subject_score}, was added to your record.")

        else:
            print("Invalid choice. Please choose again.")

        print(f"Hi {name}. Choose:\n{MENU}")
        choice = input(">>> ").upper()
    print("Thank you")


def print_subjects(subject_grades):
    """Print the subjects."""
    for subject in subject_grades:
        print(*subject)


def determine_grade(score):
    """Determine grade from the score."""
    if score >= 85:
        grade = "HD"
    elif 75 <= score <= 84:
        grade = "D"
    elif 65 <= score <= 74:
        grade = "C"
    elif 50 <= score <= 64:
        grade = "P"
    else:
        grade = "N"
    return grade


def determine_gpa(grade):
    """Determine GPA from a grade."""
    if grade == "HD":
        gpa = 7
    elif grade == "D":
        gpa = 6
    elif grade == "C":
        gpa = 5
    elif grade == "P":
        gpa = 4
    else:
        gpa = 1.5
    return gpa


def add_subject_to_file(subject_code, subject_score):
    """Add a subject and score to a file."""
    out_file = open(FILENAME, "a")
    out_file.write(f"{subject_code},{subject_score}\n")
    out_file.close()


def get_subjects_from_file():
    """Get subjects from a file."""
    in_file = open(FILENAME, "r")
    subjects = []
    for line in in_file:
        words = line.strip().split(",")
        words[1] = int(words[1])  # ignore error
        subjects.append(words)
    in_file.close()
    return subjects


def determine_subject_grades(subjects):
    """Display all subjects, scores, and grades."""
    subject_gpas = []
    for subject in subjects:
        grade = determine_grade(subject[1])
        subject_gpas.append([subject[0], subject[1], grade])
    subject_gpas.sort()
    return subject_gpas


def calculate_gpa(subjects):
    """Calculate the total GPA."""
    total_gpa = 0
    for subject in subjects:
        weight = determine_gpa(subject[2])
        total_gpa += weight
    return total_gpa / len(subjects)


main()
