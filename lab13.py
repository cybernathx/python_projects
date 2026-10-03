print("================================\nSTUDENT SECURITY PROFILE\n================================")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
dept = input("Enter your department: ").upper()
cgpa = float(input("Enter your CGPA: "))
enrollment_status = input("Are you currently enrolled?: ")

if enrollment_status.lower() in ["yes", "y"]:
    enrollment_status = "Active"
elif enrollment_status.lower() in ["no", "n"]:
    enrollment_status = "Inactive"

student = {
    "Name": name,
    "Age": age,
    "Department": dept,
    "CGPA": cgpa,
    "Enrollment Status": enrollment_status
}

def view_profile():
    print("\n==========\nPROFILE\n==========")
    for key in student:
        print(f"{key}: {student[key]}")

def check_academic_status():
    if student["CGPA"] >= 4.5:
        print("Academic status: Excellent")
    elif student["CGPA"] >= 3.5:
        print("Academic status: Very Good")
    elif student["CGPA"] >= 2.5:
        print("Academic status: Good")
    elif student["CGPA"] >= 1.5:
        print("Academic status: Pass")
    else:
        print("Academic status: At Risk")

print("Profile created successfully!")
while True:
    print("==========\nMENU\n==========")
    print("1.View Profile\n2.Check Academic Status\n3.Exit\n")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        view_profile()
    elif choice == "2":
        check_academic_status()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
