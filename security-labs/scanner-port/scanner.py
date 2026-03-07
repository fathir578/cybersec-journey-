import socket
import time

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            return True
        s.close()
    except socket.error: 
        return False


    
def main():
    target_ip = input("Enter target IP: ")
    print(f"Scanning {target_ip} for open ports...")
    start_time = time.time()
    nama_file = "hasil_scanner.txt"
    while True:
        try:           
            port_awal = int(input("Enter starting port (default 1): ") or "1")
            port_akhir = int(input("Enter ending port (default 1024): ") or "1024")

            if not (1 <= port_awal <= 65535) or not (1 <= port_akhir <= 65535): 
                print("\033[31mERROR: Invalid port range. Please enter valid port numbers between 1 and 65535, with starting port less than or equal to ending port.\033[0m")
                continue

            if port_awal > port_akhir:
                print("\033[31mERROR: Starting port must be less than or equal to ending port.\033[0m")
                continue
            break
        except ValueError:
            print("\033[31mERROR: Invalid input. Please enter numeric values for ports.\033[0m")
            
    with open(nama_file, 'a') as file:
        for port in range(port_awal, port_akhir + 1):
            if scan_port(target_ip, port):
                try:
                    service = socket.getservbyport(port, 'tcp')
                except (OSError, socket.error):
                    service = "Unknown"
                print(f"\033[32mPort {port} is open. Service: {service}\033[0m")

        file.write("" + "-"*30 + "\n")
        file.write(f"Scan results for {target_ip} (Ports {port_awal}-{port_akhir}):\n")
        elapsed_time = time.time() - start_time
        print(f"\nScan completed in {elapsed_time:.2f} seconds.")
        file.write(f"Port {port} is open. Service: {service}\n")
        file.write(f"Scan completed in {elapsed_time:.2f} seconds.\n")
        
main()
            