import main
from services import db

def add():
    kode_barang = input('kode barang: ')
    nama_barang = input('nama barang: ')
    harga_barang = int(input('harga barang: '))
    stok_barang = int(input('stok barang: '))
    
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
         menu = int(input('menu:\n1.Tambah Barang\n2.Cek Barang\n3.Kembali\n\nsilahkan pilih: '))
         if menu == 1:
             add()
         elif menu == 2:
             cek_barang()
         elif menu == 3:
              main.menu()
         print('ini warung')
    
if __name__ == '__main__':
    start()