address = input("Enter an IP address: ")
cut_address = address.split(".")

if len(cut_address) != 4:
    print("Invalid IP address!")
    exit()
for segment in cut_address:
    if not segment.isdigit():
        print("There is a non digit value in the IP address!")
        exit()  
    value = int(segment)      
    if value < 0 or value > 255:
        print("Part of the IP address is greater than 255 or less than 0!")
        exit()
print("Valid IPv4 address")

        