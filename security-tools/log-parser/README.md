# Log Parser

A simple security log analyzer built with Python as part of my cybersecurity learning journey.

---

## Features

- Parse and filter log files by severity level (WARNING, ERROR)
- Count total occurrences of each log level
- Detect potential brute force attacks via failed login tracking
- Trigger alert if failed login attempts exceed threshold
- Save full analysis report to txt file automatically
- Color-coded terminal output for better readability

---

## Built With

- Python 3
- File I/O — reading log files and writing reports
- String matching with `in` keyword
- ANSI escape codes — terminal color output

---

## How to Use

1. Place your log file in the same directory as `log_parser.py`

2. Run the parser
```bash
python log_parser.py
```

3. Results will be printed to terminal and saved to `report.txt`

---

## Output Example

```
2024-01-01 10:00:45 WARNING Failed login attempt for user admin
2024-01-01 10:01:02 WARNING Failed login attempt for user admin
2024-01-01 10:02:00 ERROR Too many failed attempts - IP blocked

Total errors: 1
Total warnings: 3
Total failed login attempts: 3
Alert: Multiple failed login attempts detected!
```

Full report saved to report.txt automatically.

---

## Log Format Supported

```
YYYY-MM-DD HH:MM:SS LEVEL Message
```

Example:
```
2024-01-01 10:00:01 INFO User admin logged in
2024-01-01 10:00:45 WARNING Failed login attempt for user admin
2024-01-01 10:02:00 ERROR Too many failed attempts - IP 192.168.1.10 blocked
```

---

## Brute Force Detection

If `Failed login attempt` appears 3 or more times in the log, the parser will automatically trigger an alert in both the terminal and the report file.

---

## Disclaimer

This tool is built for educational purposes only.
Only analyze log files from systems you own or have explicit permission to access.

---

## What I Learned

- File I/O for reading and writing simultaneously
- String filtering and pattern matching
- Counter logic for security event tracking
- Brute force detection concept
- Writing structured analysis reports programmatically

---

## Author

- GitHub: [@fathir578](https://github.com/fathir578)
