num = int(input("Enter a number: "))
total = 0

for i in range(1, num + 1):
    # print(i)

    # if i % 2 == 0:
    #     print(i)

    total += i
print(f"The sum is {total}")