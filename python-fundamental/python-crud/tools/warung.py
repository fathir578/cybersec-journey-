from datetime import datetime
import services.db as db
import main

def add():
    print("\n=== Tambah Barang Baru ===")
    
    while True:
        nama_barang = input('nama barang  : ').strip()
        if nama_barang: break
        print('⚠️  nama barang tidak boleh kosong!')

    while True:
        try:
            harga_barang = int(input('harga barang : ').strip())
            if harga_barang > 0: break
            print('⚠️  harga barang harus lebih dari 0!')
        except ValueError:
            print('⚠️  harga barang harus berupa angka!')

    while True:
        try:
            stok_barang = int(input('stok barang  : ').strip())
            if stok_barang >= 0: break
            print('⚠️  stok tidak boleh negatif!')
        except ValueError:
            print('⚠️  stok barang harus berupa angka!')

    # Generate kode otomatis dari db
    kode_barang = db.generate_kode_barang()
    waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insert ke database
    db.insert_item(nama_barang, harga_barang, stok_barang)

    # Simpan ke file log
    with open('data_barang.txt', 'a') as file:
        file.write(f'{"-"*30}\n')
        file.write(f'waktu        : {waktu}\n')
        file.write(f'kode barang  : {kode_barang}\n') 
        file.write(f'nama barang  : {nama_barang}\n')
        file.write(f'harga barang : {harga_barang}\n')
        file.write(f'stok barang  : {stok_barang}\n')

    print(f"\n\033[92m Barang '{nama_barang}' berhasil ditambahkan dengan kode {kode_barang}!\033[0m")


def cek_barang():
    items = db.fetch_item()

    if not items: 
        print('\n\033[93m Belum ada barang tersimpan.\033[0m')
        return

    print(f"\n{'='*45}")
    print(f"{'KODE':<10} {'NAMA':<20} {'HARGA':>10} {'STOK':>4}")
    print(f"{'='*45}")
    for item in items:
        kode_barang  = item['kode_barang']
        nama_barang  = item['nama_barang']
        harga_barang = item['harga_barang']
        stok_barang  = item['stok_barang']
        print(f"{kode_barang:<10} {nama_barang:<20} Rp{harga_barang:>8,} {stok_barang:>4}")
    print(f"{'='*45}")
    print(f"Total: {len(items)} barang\n") 

def start():
    while True:
        print("\n====== WARUNG MINI ======")
        print("1. Tambah Barang")
        print("2. Cek Barang")
        print("3. Kembali")
        
        try:
            menu = int(input('\nSilahkan pilih: '))
        except ValueError:
            print('⚠️  Masukkan angka yang valid!')
            continue

        if menu == 1:
            add()
        elif menu == 2:
            cek_barang()
        elif menu == 3:
            main.menu()
        else:
            print('⚠️  Pilihan tidak tersedia!') 


if __name__ == '__main__':
    start()