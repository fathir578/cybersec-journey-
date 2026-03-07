# 🛡️ Cybersecurity Learning Journey

> A personal repository documenting my hands-on journey into cybersecurity — built by a vocational student (RPL/Software Engineering) with a focus on practical tools, real code, and structured progress.

---

## 📌 About This Repository

This repo serves as a public portfolio and progress log for my 18-month self-directed cybersecurity learning roadmap. Every folder and file here represents something I've actually built, studied, or practiced. No copy-paste — everything is written and understood from scratch.

**Learning style:** Hands-on practice + text-based reading (~3 hours/day)  
**Goal:** Build a portfolio strong enough to enter the cybersecurity field professionally.

---

## 📂 Repository Structure
```
cybersec-journey-/
├── python-fundamental/
│   └── python-crud/        # CRUD app with MySQL + mini game
├── security-labs/          # Security tools built from scratch
├── hasil_scanner.txt       # Sample output from the Port Scanner tool
└── note.md                 # Personal study notes & learning reflections
```

---

## ✅ Progress Log — Phase 1

### 🐍 Python Fundamentals
Core Python scripting skills built as the foundation for all security tooling. Topics covered include data types, control flow, file I/O, functions, modules, string manipulation, and working with the terminal.

---

### 🔧 Projects Built

#### 1. Port Scanner
A command-line network port scanning tool built in Python.

**Features:**
- Custom port range input
- Service detection per open port
- Scan timing measurement
- Color-coded terminal output
- File output (results saved to `hasil_scanner.txt`)

**Skills demonstrated:** Socket programming, CLI argument handling, file I/O, terminal formatting with color codes.

---

#### 2. Log Parser
A Python-based log analysis tool for detecting suspicious activity.

**Features:**
- Brute force attack detection from log files
- Dual-file I/O (reads input log, writes output report)
- Automated report generation

**Skills demonstrated:** File parsing, pattern recognition logic, report automation, defensive security thinking.

---

#### 3. Python CRUD — Warung Mini & CUYPY Game
A modular Python application combining a database-backed inventory system with a terminal mini-game.

**Sub-projects:**

**Warung Mini (Inventory Management)**
- Add items with code, name, price, and stock
- View all stored items from the database
- MySQL integration via `mysql-connector-python`
- Persistent data storage using a structured `penyimpanan` table

**CUYPY Game**
- A terminal-based guessing game with randomized cave positions
- Option to replay or return to the main menu

**Project structure:**
```
python-crud/
├── main.py           # Main entry point
├── libs.py           # Utility functions (welcome/exit messages)
├── game/cuypy.py     # Guessing game logic
├── tools/warung.py   # Inventory management logic
├── services/db.py    # MySQL connection and queries
├── README.md
└── TODO.md           # Planned improvements
```

**Skills demonstrated:** OOP/modular design, MySQL database operations, multi-file project structure, separation of concerns (services/tools/game layers).

**Planned improvements (from TODO.md):**
- Fix circular imports between `main.py` and sub-modules
- Implement Update and Delete functionality for Warung Mini
- Enhance input validation and error handling

---

### 🗂️ Git & Version Control Workflow
Beyond just committing code, the following Git workflows have been practiced and applied directly in this repo:

- Rebasing commits for clean history
- Conflict resolution during merges
- `.gitignore` configuration to exclude sensitive/unnecessary files
- Maintaining a readable, professional commit history

---

## 🗺️ Roadmap Overview

| Phase | Focus | Status |
|-------|-------|--------|
| Phase 1 | Python fundamentals, security scripting basics, Git workflow | 🟡 In Progress |
| Phase 2 | Networking concepts, Linux, basic pentesting tools | ⏳ Upcoming |
| Phase 3 | Web security, CTF challenges, vulnerability labs | ⏳ Upcoming |
| Phase 4 | Advanced topics, certifications, real-world projects | ⏳ Upcoming |

---

## 🧠 Study Notes

Personal reflections, concept breakdowns, and key takeaways are logged in [`note.md`](./note.md). This is where ideas get processed — not just memorized.

---

## 📬 Contact

- **GitHub:** [github.com/fathir578](https://github.com/fathir578)
- Open to feedback, suggestions, or collaboration from others on the same path.

---

*"The best way to learn security is to build the tools yourself."*