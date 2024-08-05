from activity_1 import User
"""If we use the code outside of the if __main__"""
# sam = User("Sam")
# sam.give_taco()
print("In explanation file: __name__ = ", __name__)


"""
When a Python file is run, the special variable __name__ is set to '__main__' if the file is being run as the main 
program. If the file is being imported as a module in another file, __name__ is set to the file's name 
(without the .py extension).
"""