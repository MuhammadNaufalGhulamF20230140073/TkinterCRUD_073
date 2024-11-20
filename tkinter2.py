import sqlite3  # untuk mengelola database SQLite
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox  
# Membuat atau membuka database SQLite
conn = sqlite3.connect('nilai_siswa.db')  # Membuka (atau membuat) file database 'nilai_siswa.db'
cursor = conn.cursor()  

# Membuat tabel nilai_siswa
cursor.execute('''
CREATE TABLE nilai_siswa (  -- Membuat tabel bernama 'nilai_siswa' hanya jika belum ada
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Membuat atribut ID sebagai primary key, auto increment
    nama_siswa TEXT,  -- Membuat atribut untuk menyimpan Nama Mahasiswa
    biologi INTEGER,  -- Membuat atribut untuk menyimpan nilai biologi
    fisika INTEGER,  -- Membuat atribut untuk menyimpan nilai fisika
    inggris INTEGER,  -- Membuat atribut untuk menyimpan nilai Inggris
    prediksi_fakultas TEXT  -- Membuat atribut untuk menyimpan prediksi fakultas
)
''')
conn.commit()  # Menyimpan perubahan ke database

# Fungsi untuk menyimpan data ke database
def submit_data():
    nama = nama_var.get()  # Mengambil data Nama Mahasiswa dari input
    biologi = biologi_var.get()  # Mengambil nilai biologi dari input
    fisika = fisika_var.get()  # Mengambil nilai fisika dari input
    inggris = inggris_var.get()  # Mengambil nilai Inggris dari input

    # Validasi input: memastikan semua data diisi dan nilai adalah angka
    if not (nama and biologi.isdigit() and fisika.isdigit() and inggris.isdigit()):
        messagebox.showerror("Error", "Masukkan data dengan benar!")  # Tampilkan pesan error jika input salah
        return

    # Menentukan prediksi fakultas berdasarkan nilai tertinggi
    biologi, fisika, inggris = int(biologi), int(fisika), int(inggris)  # Mengubah nilai ke tipe integer
    if biologi > fisika and biologi > inggris:  # Jika nilai biologi paling tinggi
        prediksi = "Kedokteran"
    elif fisika > biologi and fisika > inggris:  # Jika nilai fisika paling tinggi
        prediksi = "Teknik"
    else:  # Jika nilai Inggris paling tinggi
        prediksi = "Bahasa"

    # Menyimpan data ke tabel database
    cursor.execute('''
    INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
    VALUES (?, ?, ?, ?, ?)
    ''', (nama, biologi, fisika, inggris, prediksi))  # Masukkan data ke tabel
    conn.commit()  # Menyimpan perubahan ke database

    # Tampilkan pesan sukses
    messagebox.showinfo("Sukses", f"Data berhasil disimpan!\nPrediksi Fakultas: {prediksi}")

    # Mengosongkan input setelah data disimpan
    nama_var.set("")
    biologi_var.set("")
    fisika_var.set("")
    inggris_var.set("")

# Membuat antarmuka Tkinter
root = Tk()  # Membuat jendela utama aplikasi
root.title("Input Nilai Siswa")  # Judul aplikasi

# Menambahkan judul besar di atas
Label(root, text="Tabel Prediksi Fakultas", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=20)  # Judul besar

# Label dan Entry untuk Nama Mahasiswa
Label(root, text="Nama Mahasiswa").grid(row=1, column=0, padx=10, pady=5)  # Label untuk Nama Mahasiswa
nama_var = StringVar()  # Variabel untuk menyimpan input Nama Mahasiswa
Entry(root, textvariable=nama_var).grid(row=1, column=1, padx=10, pady=5)  # Input field untuk Nama Mahasiswa

# Label dan Entry untuk nilai Biologi
Label(root, text="Nilai Biologi").grid(row=2, column=0, padx=10, pady=5)  # Label untuk nilai biologi
biologi_var = StringVar()  # Variabel untuk menyimpan input nilai biologi
Entry(root, textvariable=biologi_var).grid(row=2, column=1, padx=10, pady=5)  # Input field untuk nilai biologi

# Label dan Entry untuk nilai Fisika
Label(root, text="Nilai Fisika").grid(row=3, column=0, padx=10, pady=5)  # Label untuk nilai fisika
fisika_var = StringVar()  # Variabel untuk menyimpan input nilai fisika
Entry(root, textvariable=fisika_var).grid(row=3, column=1, padx=10, pady=5)  # Input field untuk nilai fisika

# Label dan Entry untuk nilai Inggris
Label(root, text="Nilai Inggris").grid(row=4, column=0, padx=10, pady=5)  # Label untuk nilai Inggris
inggris_var = StringVar()  # Variabel untuk menyimpan input nilai Inggris
Entry(root, textvariable=inggris_var).grid(row=4, column=1, padx=10, pady=5)  # Input field untuk nilai Inggris

# Button untuk menyimpan data
Button(root, text="Submit", command=submit_data).grid(row=5, column=0, columnspan=2, pady=10)  # Tombol submit data

# Menjalankan aplikasi
root.mainloop()  # Menjalankan aplikasi Tkinter

# Menutup koneksi database saat program berakhir
conn.close()  # Menutup koneksi ke database
