def main():
    try:
        # Meminta nama file dari pengguna
        nama_file = input("Masukkan nama file: ")

        # Membuka file dengan nama yang diberikan pengguna
        with open(nama_file, 'r') as file:
            print(f"File {nama_file} berhasil dibuka.\n")

            # Meminta nama mahasiswa yang ingin dicari
            nama_mahasiswa = input("Masukkan nama mahasiswa yang ingin dicari: ").strip()

            # Variabel penanda jika nama mahasiswa ditemukan
            found = False

            # Membaca setiap baris dalam file
            lines = file.readlines()

            # Memeriksa setiap pasangan nama dan nilai
            for i in range(0, len(lines), 2):
                nama = lines[i].strip()  # Ambil nama dari baris genap (index 0, 2, 4,...)
                if i + 1 < len(lines):
                    nilai = lines[i + 1].strip()  # Ambil nilai dari baris ganjil (index 1, 3, 5,...)

                # Membandingkan nama mahasiswa
                if nama.lower() == nama_mahasiswa.lower():  # Tidak sensitif terhadap huruf besar/kecil
                    print(f"Nama Mahasiswa: {nama}")
                    print(f"Nilai: {float(nilai):.2f}")
                    found = True
                    break

            # Jika mahasiswa tidak ditemukan
            if not found:
                print(f"Nama {nama_mahasiswa} tidak ditemukan.")

    # Menangani kesalahan jika file tidak ditemukan
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

# Panggil fungsi main
main()
