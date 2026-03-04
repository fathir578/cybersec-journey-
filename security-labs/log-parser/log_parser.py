count_error = 0
count_warning = 0
with open ('sample.log', 'r') as file:
    for line in file:
            if "ERROR" in line:
                count_error += 1
                print(line.strip())
            elif "WARNING" in line:
                count_warning += 1
                print(line.strip())

    print(f"Total errors: {count_error}")
    print(f"Total warnings: {count_warning}")