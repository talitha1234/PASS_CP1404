"""
Extension: remove the score parameter input and instead create a list that stores the student’s scores (it will be initially
empty when the instance is created)
Write methods for:
    add_score() – stores a float value between 0 and 100 to the scores list (NOTE: Do not make this a user input,
    the score should be an input parameter to the method)
    average_score() – calculates and returns the average grade using the scores in the student’s list
    display_score() - display the students score with the format:
    “{student_name} score/s: [55, 92]


"""


class Student:
    def __init__(self, name="", student_number=0):
        """Initialise a student instance with a name, and student number"""

    def __str__(self):
        """Return the string representation of a student."""

    def add_score(self, score):
        """Add the score to a list."""

    def average_score(self):
        """Return the average score."""

    def grade(self):
        """Return the score of the average grade."""

    def display_score(self):
        """Return a string representation of the score."""


if __name__ == '__main__':
    James = Student("James", 132439849)
    print(James.display_score())
    print(James)
    James.add_score(55)
    print(James.display_score())
    James.add_score(92)
    print(James.display_score())
    print(James.grade())
