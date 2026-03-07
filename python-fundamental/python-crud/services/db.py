import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="passwordbaru",
    database="market_mini"
)

def insert_item(nama_barang, harga_barang, stok_barang): 
    kode_barang = generate_kode_barang()                 
    cursor = db.cursor()
    cursor.execute("INSERT INTO penyimpanan (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang, stok_barang))
    db.commit()
    if cursor.rowcount > 0:
        print(f'\ndata berhasil dibuat dengan kode: {kode_barang}\n')
    else:
        print('\ndata gagal dibuat\n')
        
def fetch_item():
    cursor = db.cursor(dictionary=True)  # ← tambah ini
    cursor.execute("SELECT * FROM penyimpanan")
    return cursor.fetchall()

def generate_kode_barang():
    cursor = db.cursor()
    cursor.execute("SELECT IFNULL(MAX(CAST(SUBSTRING(kode_barang, 4) AS UNSIGNED)), 0) + 1 FROM penyimpanan")
    result = cursor.fetchone()[0]
    return f"BRG{str(result).zfill(3)}"
    