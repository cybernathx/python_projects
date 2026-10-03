failed_attempts = {} 

with open("security.log" , "r") as file:
    for address in file:
        strip_address = address.strip("\n")
        split_address = strip_address.split(" ")  

        if "FAILED" in strip_address:
            if split_address[0] in failed_attempts:
                failed_attempts[split_address[0]] += 1
            else:
                failed_attempts[split_address[0]] = 1

    for ip_address, count in failed_attempts.items():
        print("\n==== FAILED ATTEMPTS ====\n")
        print(f"{split_address[0]}: {count}")