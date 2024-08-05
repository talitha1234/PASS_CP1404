class Number:
    def __init__(self, value=0):
        """Initialize the number with a value."""
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        """Return a string representation of the number."""
        return str(self.value)


# Example usage
if __name__ == "__main__":
    num1 = Number(10)
    num2 = Number(20)
    num3 = num1 + num2

    print(num1)
    print(num2)
    print(num3)

    if num1 + num2 == num3:
        print("Same")
    else:
        print("Different")

