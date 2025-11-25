barang = {
    "Pensil": {"harga": 5000, "stok": 10},
    "Buku": {"harga": 7500, "stok": 5},
    "Penggaris": {"harga": 12000, "stok": 4},
    "Pulpen": {"harga": 5500, "stok": 10},
    "Buku Gambar": {"harga": 4000, "stok": 7},
    "Pensil Warna": {"harga": 15000, "stok": 5}
}

while True:
    print("\n===== Diwan Tools Store =====")
    for nama, data in barang.items():
        print(f"{nama} - Harga: Rp {data['harga']} - Stok: {data['stok']}")

    print()
    nama_barang = input("Masukkan nama barang yang ingin dibeli: ")

    if nama_barang not in barang:
        print("Barang tidak ditemukan!")
        continue

    jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))

    if jumlah > barang[nama_barang]["stok"]:
        print("Stok barang habis")
    else:
        total = jumlah * barang[nama_barang]["harga"]
        barang[nama_barang]["stok"] -= jumlah

        print("\n===== Transaksi Berhasil =====")
        print(f"Barang      : {nama_barang}")
        print(f"Jumlah      : {jumlah}")
        print(f"Total Harga : Rp {total}")
        print(f"Sisa Stok   : {barang[nama_barang]['stok']}")

    lagi = input("\nIngin bertransaksi lagi? (y/n): ").lower()
    
    if lagi != "y":
        print("\nTerimakasih sudah berkunjung ke Diwan Tools Store!")
        break
