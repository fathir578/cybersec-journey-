# Port Scanner

A simple TCP port scanner built with Python for educational purposes.

---

## Features
- Scan custom port range on any target IP
- Detect service name on each open port
- Display total scan duration
- Save results to txt file automatically
- Input validation with error messages
- Color-coded terminal output

---

## Built With
- Python 3
- socket — core scanning logic
- time — scan duration tracking
- ANSI escape codes — terminal colors

---

## How to Use
1. Run the script
   python port_scanner.py
2. Enter target IP
3. Enter port range (default 1-1024)

---

## Output Example
Scanning 127.0.0.1 for open ports...
Port 22 is open. Service: ssh
Port 80 is open. Service: http
Scan completed in 12.34 seconds.

---

## Disclaimer
For educational purposes only.
Only scan systems you own or have permission to test.

---

## What I Learned
- TCP connections at socket level
- Port ranges and service mappings
- Input validation and error handling
- File I/O for logging
- ANSI terminal formatting
```
