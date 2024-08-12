"""
Activity 3 - Create Questions

Let’s put our “Lindsay thinking hats” on and create some exam questions using the below topics.


Topics - Part A (Multi Choice)
Create multiple choice questions for each of the below topics. Each question should have at least 4 different choices.

Loops	Equality	Lists	Functions
Errors	Data Structure Choice	Inheritance	SRP
Files	Exceptions	Dictionaries	Sets
Strings	Importing	Data Structures


Topics - Part B (Short Answer)
Create questions that can be answered in 4 sentences or less.


Evaluate Expressions	Write good names	Write output [loops, enumerate]	Write code [dictionary & string formatting]
Describe version control	Compare data structures	Write code [implement pseudocode, strings] 	Write code [refactoring, function & tuples]
Write output [lists, list comprehension]	Write code [class]

Paste your questions here then we’ll answer on collaborate


"""

#TODO: Put your questions here and then we can all answer.



"""Questions from previous years"""

# Names
names = ['sam', 'john', 'mike', 'fred']
for i, name in enumerate(names):
    print(len(name) + i)

# Options
# a. 3 5 6 7
# b. 4 6 7 8
# c. sam 1 john 2 mike 3 fred 4
# d. sam 0 john 3 mike 4 fred 5



# Equality
print(11 < 2 and 3 <= 3)

# Options
# a. False
# b. True
# c. 11 < 2 and 3 <= 3
# d. None of the above




# Lists
a = [11, "ted", "apple", 5, 2.34]
a.append("carrot")
a.pop(3)
print(a)

# Options
# a. [11, "ted", "apple", 5, 2.34]
# b. [11, "ted", "apple", 5, 2.34, "carrot"]
# c. ["ted", "apple", 5, 2.34, "carrot"]
# d. [11, "ted", "apple", 2.34, "carrot"]



# Errors:
data, z = ["a", "b", 1, 2], 4
print(data[str(z)])

# Options
# a. IndexError
# b. NameError
# c. TypeError
# d. ValueError



# Which of these is a Valid example of inheritance
# a. Guitar inherits from Band
# b. Instrument inherits from Guitar
# c. Band inherits from Student
# d. None of the above. They are all incorrect



# Describe these Git Version Control Terms
# a. Commit
# b. Repository
# c. Pull
# d. Push
# e. Branch



# Explain the Naming Rules, Conventions, and Suggestions for:
# a. Constants
# b. Lists
# c. Functions



# Tuples vs. Lists in Python
# Compare the similarities and differences between tuples and lists, and describe scenarios where you would choose one over the other.
