# Python CRUD Project

This project is a collection of simple Python applications designed for learning fundamentals. It includes a mini-game and a basic inventory management system (Warung Mini) that interacts with a MySQL database.

## Features

### 1. CUYPY Game
A simple guessing game where the player tries to find "CUYPY" hidden in one of the caves.
- Randomized position for CUYPY.
- Interactive terminal-based gameplay.
- Option to play again or return to the main menu.

### 2. Warung Mini (Inventory Management)
A basic CRUD (Create, Read, Update, Delete) application for managing market inventory.
- **Add Items:** Register new items with code, name, price, and stock.
- **Check Items:** View all items currently stored in the database.
- **Database Integration:** Uses MySQL to persist data.

## Project Structure

```text
python-crud/
├── main.py            # Main entry point of the application
├── libs.py            # Utility functions (welcome/exit messages)
├── game/
│   └── cuypy.py       # Guessing game logic
├── tools/
│   └── warung.py      # Inventory management logic
├── services/
│   └── db.py          # MySQL database connection and operations
└── TODO.md            # List of planned improvements and bug fixes
```

## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` library

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Install dependencies:**
    ```bash
    pip install mysql-connector-python
    ```
3.  **Database Configuration:**
    Ensure you have a MySQL database named `market_mini` and a table named `penyimpanan` with the following structure:
    ```sql
    CREATE TABLE penyimpanan (
        id INT AUTO_INCREMENT PRIMARY KEY,
        kode_barang VARCHAR(50),
        nama_barang VARCHAR(100),
        harga_barang INT,
        stok_barang INT
    );
    ```
    Update the database credentials in `services/db.py` if necessary.

## How to Run

Execute the main script from the `python-crud` directory:

```bash
python main.py
```

## Future Improvements

- Fix circular imports between `main.py` and sub-modules.
- Implement Update and Delete functionality in Warung Mini.
- Enhance error handling and input validation.
