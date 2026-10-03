user = "Nathanael"
passwd = "yaks123"
attempts = 0

while attempts < 3:
    name = input("\nUsername: ")
    password = input("Password: ")

    if name == user and passwd == password:
        print("\n==== LOGIN SUCCESSFUL! ====")
        break
    else:
        print("\nIncorrect username or password!")
        attempts += 1

    if attempts == 3:
        print("\nAccount locked!")