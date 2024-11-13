from operator import itemgetter

# List of student records: (ID, First Name, Last Name, Age)
students = [('123', 'Derek', 'Smith', 8),
            ('124', 'Carrie', 'Brown', 7),
            ('125', 'Bob', 'Smith', 6),
            ('126', 'Aaron', 'Hewitt', 6)]

# 1. Sort by Age
"""Expected output: [('125', 'Bob', 'Smith', 6), ('126', 'Aaron', 'Hewitt', 6), ('123', 'Derek', 'Smith', 7), ('124', 
'Carrie', 'Brown', 7)]"""



# 2. Sort by ID (Descending)
"""Expected output: [('126', 'Aaron', 'Hewitt', 6), ('125', 'Bob', 'Smith', 6), ('124', 'Carrie', 'Brown', 7), 
('123', 'Derek', 'Smith', 7)]"""


# 3. Sort by Age and then ID
"""Expected output: [('125', 'Bob', 'Smith', 6), ('126', 'Aaron', 'Hewitt', 6), ('123', 'Derek', 'Smith', 7), ('124', 
'Carrie', 'Brown', 7)]"""


