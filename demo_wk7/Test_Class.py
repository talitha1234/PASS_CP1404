"""
Activity 2 - Student Class
Write a Student class that allows you to store these fields (attributes):

name
student_number
score

Define the following methods:
__init__ - with defaults name as an empty string, student_number as default integer 0, score default 0 as a float
__str__ - which uses string formatting to return something like (using the values from above):
Henry Roberts, Student no: 13154348, Score: 66.4

get_grade() - which returns the corresponding worded grade to their score
(Fail < 50, Pass < 65, Credit < 75, Distinction < 85,
High Distinction <= 100)
Remember that methods should not take in any data that the object already knows.
"""


class Student:
    def __init__(self, name="", student_number=0, score=0.0):
        """Initialize a student instance with a name, student number, and score."""
        self.name = name
        self.student_number = student_number
        self.score = score

    def __str__(self):
        """Return the string representation of a student."""
        return f"{self.name}, {self.student_number}, {self.score}"

    def get_grade(self):
        """Return the grade of the score."""
        if self.score < 50:
            return "Fail"
        elif self.score < 65:
            return "Pass"
        elif self.score < 75:
            return "Credit"
        elif self.score < 85:
            return "Distinction"
        else:
            return "High Distinction"


def main():
    # this will create the example output
    """
    James, Student no: 132439849, Score: 60
    James grade was: Pass
    """

    James = Student("James", 132439849, 60)
    print(James)
    print(f"{James.name} grade was: {James.get_grade()}")
