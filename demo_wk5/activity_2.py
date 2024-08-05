from operator import itemgetter

# List of student records: (ID, First Name, Last Name, Age)
students = [('123', 'Derek', 'Smith', 7),
            ('124', 'Carrie', 'Brown', 7),
            ('125', 'Bob', 'Smith', 6),
            ('126', 'Aaron', 'Hewitt', 6)]

# 1. Sort by Age
"""Expected output: [('125', 'Bob', 'Smith', 6), ('126', 'Aaron', 'Hewitt', 6), ('123', 'Derek', 'Smith', 7), ('124', 
'Carrie', 'Brown', 7)]"""
sorted_by_age = sorted(students, key=itemgetter(3))
print("Sorted by Age:", sorted_by_age)

# 2. Sort by ID (Descending)
"""Expected output: [('126', 'Aaron', 'Hewitt', 6), ('125', 'Bob', 'Smith', 6), ('124', 'Carrie', 'Brown', 7), 
('123', 'Derek', 'Smith', 7)]"""
sorted_by_id_desc = sorted(students, key=itemgetter(0), reverse=True)
print("Sorted by ID (Descending):", sorted_by_id_desc)

# 3. Sort by Age and ID
"""Expected output: [('125', 'Bob', 'Smith', 6), ('126', 'Aaron', 'Hewitt', 6), ('123', 'Derek', 'Smith', 7), ('124', 
'Carrie', 'Brown', 7)]"""
sorted_by_age_and_id = sorted(students, key=itemgetter(3, 0))
print("Sorted by Age and ID:", sorted_by_age_and_id)
