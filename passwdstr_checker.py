passwd = input("Enter a password: ")
strength = 0
special = "!@#$%^&*()_-=+/?.>,<';:[]}{`~"

if len(passwd) >= 8:
    strength += 1
if any(char.isupper() for char in passwd):
    strength += 1
if any(char.islower() for char in passwd):
    strength += 1
if any(char.isdigit() for char in passwd):
    strength += 1
if any(char in special for char in passwd):
    strength += 1

print("\n==== PASSWORD STRENGTH CHECK ====\n            ")
if strength <= 2:
    print("Weak")
elif strength <= 4:
    print("Moderate")
elif strength > 4:
    print("Strong")