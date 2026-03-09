count_error = 0
count_warning = 0
count_failed = 0
with open ('sample.log', 'r') as file, open('report.txt', 'a') as report:
    report.write("Log Analysis Report\n")
    report.write("===================\n")
    for line in file:
            if "ERROR" in line:
                count_error += 1
                print(line.strip())
                report.write(line.strip() + "\n")
            elif "WARNING" in line:
                count_warning += 1
                print(line.strip())
                report.write(line.strip() + "\n")
                if "Failed login attempt" in line:
                    count_failed += 1
                    report.write(line.strip() + "\n")

    report.write(f"Total errors: {count_error}\n")
    report.write(f"Total warnings: {count_warning}\n")
    report.write(f"Total failed login attempts: {count_failed}\n")
    print(f"Total errors: {count_error}")
    print(f"Total warnings: {count_warning}")
    print(f"Total failed login attempts: {count_failed}")

    if count_failed >= 3:
        alert = "Alert: Multiple failed login attempts detected!"
        print(f"\033[91m{alert}\033[0m")
        report.write(alert + "\n")
