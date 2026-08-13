# Dictionary in Python
# Dictionaries are used to store data values in key:value pairs
# “key” : value
# They are unordered, mutable(changeable) & don’t allow duplicate keys

# 1.Topic 

# student = {
#     "name": "Sushil",
#     "age": 23,
#     "city": "Bilaspur"
# }

# print(student)
# print(student["city"])

# 2.Topic Access Value using get()

# student = {
#     "name": "Sushil",
#     "age": 23
# }

# print(student.get("name"))
# print(student.get("age", "Not Found"))

# 3.Topic Add New Item

# student = {
#     "name": "Sushil",
#     "age": 23
# }

# student["city"] = "Bilaspur"
# student["college"] = "CGIT" 


# print(student)

# 4.Topic Update Value

# student = {
#     "name": "Sushil",
#     "age": 23
# }

# student["age"] = 24

# print(student)

# 5.Topic Delete Item

# student = {
#     "name": "Sushil",
#     "age": 23,
#     "city": "Bilaspur",
#     "college" : "CGIT" 
# }

# del student["college"]

# print(student)

# 6. Loop Through Dictionary

# student = {
#     "name": "Sushil",
#     "age": 23,
#     "city": "Bilaspur"
# }

# for key, value in student.items():
#     print(key, ":", value)

# 7. Dictionary Length

# student = {
#     "name": "Sushil",
#     "age": 23,
#     "city": "Bilaspur"
# }

# print(len(student))

# 8. Nested Dictionary

# students = {
#     "student1": {
#         "name": "Sushil",
#         "age": 23
#     },
#     "student2": {
#         "name": "Rahul",
#         "age": 22
#     }
# }

# print(students ["student1"]["age"])