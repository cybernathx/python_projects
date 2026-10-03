# names = ["Israel", "Nath", "Samuel", "Manasseh", "David"]

# print(names)
# print(names[0])
# print(names[4])

# names.append("Yakubu")
# print(names)

# for names in names:
#     print(names)

# user_input = input("Enter a name: ")
# if user_input in names:
#     print(f"{user_input} is on the list")
# else:
#     print(f"{user_input} is not on the list")


# numbers = [2, 5, 2, 8, 2, 10, 5, 3]
# user_input = int(input("Enter a number: "))

# count = numbers.count(user_input)
# print(f"{user_input} appears {count} times")

# student = {
#     "name": "Nathanael",
#     "age": 19,
#     "dept": "Cyber Security"
# }

# print(student)
# print(student["name"])
# print(student["dept"])

# student["age"] = 20
# print(student["age"])

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# dept = input("Enter your department: ")
# level = int(input("Enter your level: "))

# student = {
#     "name": "",
#     "age": "",
#     "dept": "",
#     "level": ""
# }

# student["name"] = name
# student["age"] = age
# student["dept"] = dept
# student["level"] = level

# print(student)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
dept = input("Enter your department: ")
level = int(input("Enter your level: "))

student = {
    "name": name,
    "age": age,
    "dept": dept,
    "level": level
}

for key in student:
    print(f"{key}: {student[key]}")