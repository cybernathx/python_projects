import json

with open("security_config.json", "r") as config_file:
    config = json.load(config_file)

    firewall_enabled = config.get("firewall_enabled")
    print(f"Firewall enabled: {firewall_enabled}")
    maximum_login_attempts = config.get("max_login_attempts")
    print(f"Maximum login attempts: {maximum_login_attempts}")
    allowed_ports = config.get("allowed_ports")
    print(f"Allowed ports: {allowed_ports}")
    admin_email = config.get("admin_email")
    print(f"Admin email: {admin_email}")

    change_max_attempts = input("Do you want to change the maximum login attempts? (yes/no): ").strip().lower()
    if change_max_attempts == "yes":
        new_max_attempts = input("Enter the new maximum login attempts: ")
        try:
            new_max_attempts = int(new_max_attempts)
            config["max_login_attempts"] = new_max_attempts
            with open("security_config.json", "w") as config_file_write:
                json.dump(config, config_file_write, indent=4)
            print(f"Maximum login attempts updated to: {new_max_attempts}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")