class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.dipinjam = False

    def info(self):
        status = "Dipinjam" if self.dipinjam else "Tersedia"
        return f"{self.judul} oleh {self.penulis} ({status})"


class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_pinjaman = []

    def pinjam_buku(self, buku):
        if not buku.dipinjam:
            buku.dipinjam = True
            self.buku_pinjaman.append(buku)
            print(f"{self.nama} meminjam {buku.judul}")
        else:
            print(f"Buku {buku.judul} sedang dipinjam")

    def kembalikan_buku(self, buku):
        if buku in self.buku_pinjaman:
            buku.dipinjam = False
            self.buku_pinjaman.remove(buku)
            print(f"{self.nama} mengembalikan {buku.judul}")
        else:
            print("Buku tidak ditemukan di daftar pinjaman")


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []
        self.daftar_anggota = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)

    def tampilkan_buku(self):
        print("\nDaftar Buku:")
        for buku in self.daftar_buku:
            print("-", buku.info())


# ===== Program Utama =====
perpus = Perpustakaan()

buku1 = Buku("Python Dasar", "Andi")
buku2 = Buku("OOP Python", "Budi")

anggota1 = Anggota("Raka", "A001")

perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_anggota(anggota1)

perpus.tampilkan_buku()

anggota1.pinjam_buku(buku1)
perpus.tampilkan_buku()

anggota1.kembalikan_buku(buku1)
perpus.tampilkan_buku()