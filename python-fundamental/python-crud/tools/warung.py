import main
from datetime import datetime
from services import db

def add():
 waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 with open('data_barang.txt', 'a') as file:   

    while True:
        kode_barang = input('kode barang: ').strip()
        if kode_barang:
            break
        print('kode barang tidak boleh kosong, silahkan masukkan kode barang')
    while True:
        nama_barang = input('nama barang: ').strip()
        if nama_barang:
            break
        print('nama barang tidak boleh kosong, silahkan masukkan nama barang')
    while True:
        try:
            harga_barang = int(input('harga barang: '))
            break
        except ValueError:
            print('harga barang harus berupa angka, silahkan masukkan harga barang')
    while True:
        try:
            stok_barang = int(input('stok barang: '))
            break
        except ValueError:
            print('stok barang harus berupa angka, silahkan masukkan stok barang')

    file.write('------------------------------\n')
    file.write(f'waktu: {waktu}\n')
    file.write(f'kode barang: {kode_barang}\n')
    file.write(f'nama barang: {nama_barang}\n')
    file.write(f'harga barang: {harga_barang}\n')
    file.write(f'stok barang: {stok_barang}\n')

    save = db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    
def cek_barang():
    items = db.fetch_item()
    for item in items:
        kode_barang = item [0]
        nama_barang = item [1]
        harga_barang = item [2]
        stok_barang = item [3]
        print(f'''
kode barang: {kode_barang}
{nama_barang}| Rp {harga_barang}
stok barang: {stok_barang}
''')
    
def start():
    while True:
         try:
            menu = int(input('menu:\n1.Tambah Barang\n2.Cek Barang\n3.Kembali\n\nsilahkan pilih: '))
         except ValueError:
            print('please enter a valid number')
            continue
         if menu == 1:
             add()
         elif menu == 2:
             cek_barang()
         elif menu == 3:
              main.menu()
         print('ini warung')
    
if __name__ == '__main__':
    start()