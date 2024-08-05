"""Activity 2"""


class Student:
    def __init__(self, name="", student_number=0, score=0.0):
        """Initialize a student instance with a name, student number, and score."""
        self.name = name
        self.student_number = student_number
        self.score = score

    def __str__(self):
        """Return the string representation of a student."""
        return f"{self.name}, Student no: {self.student_number}, Score: {self.score}"

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
        return "High Distinction"


if __name__ == '__main__':
    # this will create the example output
    """
    James, Student no: 132439849, Score: 60
    James grade was: Pass
    """

    James = Student("James", 132439849, 99)
    print(James)
    print(f"{James.name} grade was: {James.get_grade()}")
