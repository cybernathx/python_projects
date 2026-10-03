name = input("What is your name?: ")
course = input("What course do you study?: ")
level = int(input("What level are you?: "))
specialization = input("What's your specialization?: ")
cgpa = float(input("What is your CGPA?: "))
skills = input("What skills do you have?: ")

profile = {
    "Name": name,
    "Course": course,
    "Level": level,
    "Specialization": specialization,
    "CGPA": cgpa,
    "Cybersecurity Skills": skills
}

def display_profile():
    print("==== DETAILS ====")
    for key in profile: 
        print(f"{key}: {profile[key]}")

display_profile()