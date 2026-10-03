import os

path = input("Enter the path to the log file: ")
if not os.path.exists(path):
    print("File not found.")
else:
    with open(path, "r") as file:

        total_events = 0
        successful_logins = 0
        failed_logins = 0
        failed_attempts = {}
        unique_ips = set()

        for line in file:
            total_events += 1
            line_strip = line.strip("\n")
            ip_split = line_strip.split(" ")
            ip_address = ip_split[0]
            unique_ips.add(ip_address)
            if "SUCCESS" in line:
                successful_logins += 1
            elif "FAILED" in line:
                failed_logins += 1
                if ip_address in failed_attempts:
                    failed_attempts[ip_address] += 1
                else:
                    failed_attempts[ip_address] = 1


        heading = "\n==== SECURITY LOG REPORT ====\n"
        events = f"Total events: {total_events}"
        succ_logins = f"Successful logins: {successful_logins}"
        failed = f"Failed logins: {failed_logins}"
        unique = f"Unique IP addresses: {len(unique_ips)}"
        failed_heading = "\nFailed login attempts by IP:"
        for ip, count in failed_attempts.items():
            ip_count = f"  {ip}: {count}"

        report = f"{heading}\n{events}\n{succ_logins}\n{failed}\n{unique}\n{failed_heading}"

        with open("security_report.txt", "w") as report_file:
            report_file.write(report)
            for ip, count in failed_attempts.items():
                report_file.write(f"\n  {ip}: {count}")
        print("Report saved successfully to 'security_report.txt'.")