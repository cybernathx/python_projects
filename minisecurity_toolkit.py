def main():
    while True:
        print("=====================\nMINI SECURITY TOOLKIT\n=====================")
        print("1. Password Strength Checker\n2. IPv4 Validator\n3. Login Simulator\n4. Log Analyzer\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            check_password()
        elif choice == "2":
            validate_ip()
        elif choice == "3":
            login()
        elif choice == "4":
            analyze_logs()
        elif choice == "5":
            return
        else:
            print("Invalid choice, try again!")

def check_password():
    password = input("Input Password: ")
    score = 0
    special = "!@#$%"
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in special for char in password):
        score += 1

    if score <= 2:
        remark = "Weak"
    elif score <= 4:
        remark = "Medium"
    elif score == 5:
        remark = "Strong"
    print(f"====PASSWORD STRENGTH====\nPassword Strength: {score} [{remark}]")

def validate_ip():
    ip_address = input("Input IP address: ")
    ip_split = ip_address.split(".")
    if len(ip_split) != 4:
        print("An IPv4 address only contains 4 sections (e.g 192.168.1.10)")  
        print("Invalid IPv4 address")
        return    
    for section in ip_split:
        if not section.isdigit():
            print("Each IPv4 section must be a digit")
            print("Invalid IPv4 address")
            return  
        convert = int(section)
        if convert < 0 or convert > 255:
            print("Each section of the IPv4 address cannot be less than 0 or greater than 255")
            print("Invalid IPv4 address")  
            return
    print("Valid IPv4 address")

def login():
    real_user = "admin"
    real_password = "admin123"
    attempts = 0

    while attempts < 3:
        user = input("Username: ")
        password = input("Password: ")

        if user == real_user and password == real_password:
            print("Successful login")
            return
        else:
            print("Incorrect credentials")
            attempts += 1

        if attempts == 3:
            print("Account locked")

def analyze_logs():
    with open("security.log", "r") as file:
        ip_dictionary = {}

        for line in file:
            ip_strip = line.strip("\n")
            ip_split = ip_strip.split(" ")
            if "FAIL" in ip_strip:
                if ip_split[0] in ip_dictionary:
                    ip_dictionary[ip_split[0]] += 1
                else:
                    ip_dictionary[ip_split[0]] = 1

        for ip_address, count in ip_dictionary.items():
            print(f"{ip_address}: {count}")
            if count >= 3:
                print(f"WARNING: Suspicious activity detected from {ip_address}")               
            
main()

        
