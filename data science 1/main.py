import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_detail = [('James', 5, 48.5), ('nail', 6, 52.5), ('paul', 5, 42.10),('pit', 5, 40.11)]

# Create a structured array
students = np.array(students_detail, dtype=data_type)
print("original array:")
print(students)
print("sort by height")
print(np.sort(students, order='height'))
