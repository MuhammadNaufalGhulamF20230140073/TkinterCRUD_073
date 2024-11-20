import sqlite3

# Membuka koneksi ke database SQLite
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Menjalankan perintah SELECT * untuk mengambil semua data dari tabel
try:
    cursor.execute("SELECT * FROM nilai_siswa")
    hasil = cursor.fetchall()  # Mengambil semua hasil query

    # Menampilkan data
    print("ID | Nama Siswa | Biologi | Fisika | Inggris | Prediksi Fakultas")
    print("-" * 60)
    for row in hasil:
        print(f"{row[0]:<3} | {row[1]:<12} | {row[2]:<7} | {row[3]:<6} | {row[4]:<7} | {row[5]:<17}")
except sqlite3.Error as e:
    print("Terjadi kesalahan:", e)

# Menutup koneksi
conn.close()
