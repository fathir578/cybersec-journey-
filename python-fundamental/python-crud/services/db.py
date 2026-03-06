import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passwordbaru",
    database="market_mini"
)

def insert_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor() 
    cursor.execute("INSERT INTO penyimpanan (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang, stok_barang))
    db.commit()
    if cursor.rowcount > 0:
        print('\ndata berhasil dibuat\n')
    else:
        print('\ndata gagal di buat\n')
        
def fetch_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM penyimpanan")
    return cursor.fetchall()
    
    