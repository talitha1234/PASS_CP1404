MENU = "(D)etermine grade\n(C)alculate GPA\n(A)dd subject score\n(Q)uit"
FILENAME = "subjects.txt"


def main():
    """GPA program."""
    name = input("Name: ")
    print(f"Hi {name}. Choose:\n{MENU}")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            # TODO: Add determine grade for a score input by the user (not related to TEXT file data)
            pass
        elif choice == "C":
            # TODO: calculate GPA based on scores stored in the list.
            #  It should read the scores from a file, convert the score to a grade,
            #  convert the grade to a weight, then calculate the average of those.
            #  The program should then print each subject (sorted alphabetically),
            #  score and the corresponding grade plus the final GPA at the end. (See example output).
            pass

        elif choice == "A":
            # TODO: add a subject and corresponding score to their record (file)
            pass

        else:
            print("Invalid choice. Please choose again.")

        print(f"Hi {name}. Choose:\n{MENU}")
        choice = input(">>> ").upper()
    print("Thank you")


def print_subjects(subject_grades):
    """Print the subjects."""


def determine_grade(score):
    """Determine grade from the score."""


def determine_gpa(grade):
    """Determine GPA from a grade."""


def add_subject_to_file(subject_code, subject_score):
    """Add a subject and score to a file."""


def get_subjects_from_file():
    """Get subjects from a file."""


def determine_subject_grades(subjects):
    """Display all subjects, scores, and grades."""


def calculate_gpa(subjects):
    """Calculate the total GPA."""


main()
