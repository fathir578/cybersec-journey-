# Cybersec Journey - Progres & Dokumentasi

Proyek ini berisi perjalanan pembelajaran keamanan siber, mulai dari dasar-dasar Python hingga alat bantu keamanan jaringan dan analisis log.

## 🚀 Progres Pengerjaan

### 1. Python Fundamental (Awal Maret 2026)
Fase ini berfokus pada pemahaman dasar sintaksis Python, fungsi, dan manipulasi string.

*   **`week0/week0.py`**
    *   **Apa yang dibuat:** Skrip dasar untuk input nama dan perulangan angka.
    *   **Cara Kerja:** Menerima input nama, membersihkan spasi (`strip`), mengubahnya menjadi huruf kapital (`upper`), lalu mencetaknya di dalam kotak bintang (`*`).
*   **`calculator-cli/calculator.py`**
    *   **Apa yang dibuat:** Kalkulator interaktif berbasis Command Line Interface (CLI).
    *   **Cara Kerja:** Menggunakan loop `while True` untuk terus meminta input angka dan operator. Memiliki penanganan error (`try-except`) untuk pembagian nol dan input tidak valid.

### 2. Security Labs - Network Scanning (3 Maret 2026)
Implementasi Python untuk pemindaian jaringan.

*   **`scanner-port/scanner.py`**
    *   **Apa yang dibuat:** Port Scanner sederhana.
    *   **Cara Kerja:** Menggunakan pustaka `socket` untuk mendeteksi port yang terbuka pada IP target, mengidentifikasi layanan (seperti HTTP/SSH), dan menyimpan hasilnya ke `hasil_scanner.txt`.

### 3. Security Labs - Log Analysis (5 Maret 2026)
Otomatisasi pemantauan keamanan melalui analisis file log.

*   **`log-parser/log_parser.py`**
    *   **Apa yang dibuat:** Alat penganalisis log otomatis.
    *   **Cara Kerja:** Membaca file log untuk mencari kata kunci "ERROR" dan "WARNING". Memicu alert jika mendeteksi "Failed login attempt" berulang kali dan merangkumnya di `report.txt`.

---

## 📚 Catatan Belajar (Materi Dasar)

### Functions and Variables
Mempelajari input dan manipulasi string dalam Python.

**Parameter Penting:**
1.  **`end=""`**: Digunakan di akhir `print` untuk melanjutkan perintah selanjutnya dalam satu baris. Sering dipakai dalam perulangan.
2.  **`sep=""`**: Digunakan untuk mengatur pemisah antar nilai yang dicetak dalam satu fungsi `print`.

**Contoh Kode:**
```python
# Parameter end="" dan sep=""
print("Hello, ", end="")
print(name)
print("hello", name, sep="---", end="!!!\n")
```

---
*Terakhir diperbarui: 5 Maret 2026*
