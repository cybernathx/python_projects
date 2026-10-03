num = int(input("Enter a number: "))

# def square(num):
#     return num * num

# result = square(num)
# print(f"The square of {num} is {result}")


# value_1 = int(input("Enter the first number: "))
# value_2 = int(input("Enter the second number: "))

# def multiply(value_1, value_2):
#     return value_1 * value_2

# ans = multiply(value_1, value_2)
# print(f"The answer is {ans}")

def check_even(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

display = check_even(num)
print(display)
 