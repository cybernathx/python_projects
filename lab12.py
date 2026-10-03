# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative numbers aren't allowed. Try again.")
        continue
    elif num == 0:
        print("Goodbye!")
        break
    print(f"You entered {num}")


# A
while True:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Negative numbers aren't allowed. Try again.")
            continue
        elif num == 0:
            print("Goodbye!")
            break
        print(f"You entered {num}")
    except:
        print("Invalid input. Please enter a number.")

    