count_error = 0
count_warning = 0
count_failed = 0
with open ('sample.log', 'r') as file:
    for line in file:
            if "ERROR" in line:
                count_error += 1
                print(line.strip())
            elif "WARNING" in line:
                count_warning += 1
                print(line.strip())
                if "Failed login attempt" in line:
                    count_failed += 1
    print(f"Total errors: {count_error}")
    print(f"Total warnings: {count_warning}")
    print(f"Total failed login attempts: {count_failed}")
    if count_failed >= 3:
        print("\033[91mAlert: Multiple failed login attempts detected!\033[0m")
with open('report.txt', 'a') as report:
    report.write(f"Total errors: {count_error}\n")
    report.write(f"Total warnings: {count_warning}\n")
    report.write(f"Total failed login attempts: {count_failed}\n")
    if count_failed >= 3:
        report.write("Alert: Multiple failed login attempts detected!\n")