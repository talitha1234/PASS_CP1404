"""Activity 2 Extension"""


class Student:
    def __init__(self, name="", student_number=0):
        """Initialise a student instance with a name, and student number"""
        self.name = name
        self.student_number = student_number
        self.scores = []

    def __str__(self):
        """Return the string representation of a student."""
        return f"{self.name}, Student no: {self.student_number}"

    def add_score(self, score):
        """Add the score to a list."""
        self.scores.append(score)

    def average_score(self):
        """Return the average score."""
        return sum(self.scores) / len(self.scores)

    def grade(self):
        """Return the score of the average grade."""
        score = self.average_score()
        if score >= 85:
            grade = "High Distinction"
        elif score >= 75:
            grade = "Distinction"
        elif score >= 65:
            grade = "Credit"
        elif score <= 50:
            grade = "Pass"
        else:
            grade = "Fail"
        return grade

    def display_score(self):
        """Return a string representation of the score."""
        if len(self.scores) != 0:
            score_string = f"{self.name} score/s: {''.join(str(self.scores))}"
        else:
            score_string = f"{self.name} does not have any scores"
        return score_string


if __name__ == '__main__':
    James = Student("James", 132439849)
    print(James.display_score())
    print(James)
    James.add_score(55)
    print(James.display_score())
    James.add_score(92)
    print(James.display_score())
    print(James.grade())
