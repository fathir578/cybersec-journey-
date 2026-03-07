# 📋 Laporan Belajar — SSH & MITM Testing
**Nama:** [REDACTED]  
**OS:** Kali Linux (6.18.3 / kali-amd64)  
**Tanggal:** Februari 2026  

---

## 📚 Ringkasan Materi yang Dipelajari

### 1. Secure Shell (SSH)
SSH (Secure Shell Protocol) adalah protokol jaringan kriptografis untuk mengoperasikan layanan jaringan secara aman melalui jaringan yang tidak aman. SSH menggantikan protokol lama seperti Telnet, rsh, dan rlogin yang tidak aman.

**Poin penting yang dipahami:**
- SSH menggunakan kriptografi kunci publik untuk autentikasi
- SSH beroperasi di port 22 (TCP)
- Terdiri dari 3 lapisan: Transport Layer, User Authentication Layer, Connection Layer
- SSH-1 sudah obsolete, SSH-2 adalah standar aktif

---

### 2. SSH Key Pair
Sepasang kunci kriptografi (publik & privat) yang digunakan untuk autentikasi tanpa password.

| Komponen | Lokasi | Fungsi |
|---|---|---|
| Kunci Privat | `~/.ssh/id_ed25519` | Disimpan di laptop sendiri, tidak boleh dibagikan |
| Kunci Publik | `~/.ssh/id_ed25519.pub` | Disalin ke server target |
| Authorized Keys | `~/.ssh/authorized_keys` | Daftar kunci publik yang diizinkan masuk |
| Known Hosts | `~/.ssh/known_hosts` | Daftar server yang sudah diverifikasi |

---

### 3. Passphrase
Password tambahan untuk mengenkripsi file kunci privat di lokal. Berfungsi sebagai lapisan keamanan tambahan jika file kunci privat dicuri.

- **Dengan passphrase** → file kunci privat terenkripsi, lebih aman
- **Tanpa passphrase** → lebih praktis, cocok untuk belajar/automation

---

### 4. Konfigurasi Keamanan SSH Server
File konfigurasi: `/etc/ssh/sshd_config`

| Konfigurasi | Nilai | Fungsi |
|---|---|---|
| `PermitRootLogin` | `no` | Larang login langsung sebagai root |
| `PasswordAuthentication` | `no` | Larang login dengan password biasa |
| `PubkeyAuthentication` | `yes` | Izinkan login dengan SSH key |

---

### 5. MITM (Man-in-the-Middle)
Teknik serangan/testing di mana attacker menyisipkan diri di antara victim dan gateway sehingga bisa memonitor traffic yang lewat.

**Cara kerja:**
```
Normal:   Victim ──► Router ──► Internet
MITM:     Victim ──► Attacker ──► Router ──► Internet
```

**Teknik yang dipelajari:** ARP Spoofing — membohongi tabel ARP victim dan router agar traffic melewati attacker.

---

### 6. Docker Networking
Docker secara otomatis membuat interface virtual `docker0` yang berfungsi sebagai gateway untuk semua container. Karena laptop sudah menjadi gateway, ARP Spoof tidak diperlukan di lingkungan Docker.

---

### 7. Tools yang Dipelajari

| Tool | Fungsi |
|---|---|
| `ssh-keygen` | Membuat pasangan kunci publik-privat |
| `ssh-copy-id` | Menyalin kunci publik ke server tujuan |
| `ssh -vvv` | Koneksi SSH dengan debug verbose lengkap |
| `nmap` | Scan jaringan dan port terbuka |
| `docker` | Menjalankan container victim (DVWA) |
| `bettercap` | Tools MITM — ARP spoofing dan sniffing |
| `tcpdump` | Capture traffic jaringan via terminal |
| `tshark` | Analisis traffic jaringan (versi terminal Wireshark) |
| `wireshark` | Analisis traffic jaringan (versi GUI) |

---

## 🛠️ Praktik yang Dilakukan

### Praktik 1 — Generate SSH Key
```bash
ssh-keygen -t ed25519
```
**Hasil:** Berhasil membuat pasangan kunci ED25519 di `~/.ssh/`

---

### Praktik 2 — Copy SSH Key ke Server
```bash
ssh-copy-id <username>@localhost
```
**Hasil:** Kunci publik berhasil disalin ke `~/.ssh/authorized_keys`

---

### Praktik 3 — Koneksi SSH Tanpa Password
```bash
ssh <username>@localhost
```
**Hasil:** Berhasil login tanpa password menggunakan kunci ED25519

---

### Praktik 4 — Debug SSH Verbose
```bash
ssh -vvv <username>@localhost
```
**Hasil:** Berhasil melihat seluruh proses koneksi SSH secara detail, mulai dari TCP handshake, key exchange, hingga autentikasi kunci publik

**Alur yang terlihat dari output debug:**
1. Baca konfigurasi SSH
2. Koneksi ke port 22
3. Negosiasi algoritma enkripsi (chacha20-poly1305)
4. Verifikasi server via `known_hosts`
5. Autentikasi menggunakan kunci ED25519
6. Sesi shell dibuka

---

### Praktik 5 — Konfigurasi SSH Server
```bash
sudo nano /etc/ssh/sshd_config
```
**Perubahan yang dilakukan:**
- `PermitRootLogin no`
- `PasswordAuthentication no`
- `PubkeyAuthentication yes`

---

### Praktik 6 — Setup Lab Docker untuk MITM
```bash
# Install Docker
sudo apt install docker.io

# Jalankan container DVWA sebagai victim
docker run -d --name victim -p 8080:80 vulnerables/web-dvwa

# Cek container berjalan
docker ps

# Cek IP container
docker inspect victim | grep IPAddress
```
**Hasil:** Container DVWA berhasil berjalan di IP `172.17.0.2`, dapat diakses di `http://localhost:8080`

---

### Praktik 7 — Reconnaissance dengan Nmap
```bash
sudo nmap -sV 172.17.0.2
```
**Hasil:** Port 80/tcp terbuka, menjalankan Apache httpd di container DVWA

---

### Praktik 8 — Capture Traffic dengan TCPDump
```bash
sudo tcpdump -i docker0 -A port 80
```
**Hasil:** Berhasil capture traffic HTTP termasuk credentials login DVWA:
```
POST /login.php HTTP/1.1
username=<REDACTED>&password=<REDACTED>  ← terlihat dalam plaintext!
```

---

### Praktik 9 — Analisis Traffic dengan TShark
```bash
sudo tshark -i docker0 -Y "http" -T fields \
  -e frame.time \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.request.uri \
  -e urlencoded-form.key \
  -e urlencoded-form.value
```
**Hasil:** Berhasil menampilkan traffic HTTP secara terstruktur per field, termasuk username dan password yang dikirim victim

---

## 💡 Pemahaman Penting yang Didapat

### Kenapa HTTP Berbahaya?
```
HTTP  → data dikirim plaintext → username & password terlihat jelas ❌
HTTPS → data dienkripsi        → tidak bisa dibaca tanpa kunci      ✅
```

### Kenapa ARP Spoof Tidak Bisa di Docker?
Docker menjadikan laptop sebagai gateway otomatis untuk semua container. Artinya traffic victim sudah otomatis melewati laptop tanpa perlu teknik ARP spoofing.

### Perbedaan Bettercap vs TCPDump vs TShark
| Tool | Fungsi Utama | Cocok Untuk |
|---|---|---|
| Bettercap | ARP Spoof + Sniff | Jaringan LAN nyata |
| TCPDump | Capture raw traffic | Quick capture via terminal |
| TShark | Analisis traffic detail | Analisis terstruktur via terminal |
| Wireshark | Analisis traffic detail | Analisis via GUI (butuh desktop) |

---

## ⚠️ Kendala yang Ditemukan

| Kendala | Penyebab | Solusi |
|---|---|---|
| Permission denied Docker | User belum di group docker | `sudo usermod -aG docker <username>` |
| ARP Spoof gagal di Docker | Docker sudah jadi gateway otomatis | Gunakan TCPDump/TShark langsung |
| Wireshark GUI tidak muncul | Berjalan di mode TTY tanpa desktop | Gunakan TShark sebagai alternatif |
| `startx` gagal | Xorg tidak izinkan non-console user | Edit `/etc/X11/Xwrapper.config` |

---

## 📌 Langkah Selanjutnya

- [ ] Fix Wireshark GUI (selesaikan masalah display/Xorg)
- [ ] Belajar SSL Stripping (downgrade HTTPS ke HTTP)
- [ ] Explore fitur DVWA (SQL Injection, XSS, dll)
- [ ] Coba MITM di jaringan WiFi nyata (dengan perangkat sendiri)
- [ ] Belajar di platform TryHackMe / HackTheBox

---

## 🔐 Catatan Etika

> Semua praktik di atas dilakukan di **lingkungan lab lokal milik sendiri** menggunakan Docker container sebagai target. Melakukan MITM, sniffing, atau serangan apapun di jaringan orang lain tanpa izin adalah **ilegal** dan melanggar hukum.

---

*Laporan dibuat otomatis — Februari 2026*
