while True:
    print("=== ALAKADAR PHONE CELL ===")
    print("1. iPhone 11")
    print("2. iPhone 12")
    print("3. iPhone 13")
    print("4. iPhone 14")
    print("5. iPhone 15")

    pilihan = int(input("Pilih nomor iPhone yang ingin dilihat harganya: "))

    harga = 0
    ram_valid = True

    match pilihan:
        case 1:
            print("\niPhone 11")
            print("Pilih varian RAM:")
            print("1. 4GB (Rp 7.500.000)")
            print("2. 6GB (Rp 8.000.000)")
            ram = int(input("Masukkan pilihan RAM: "))
            match ram:
                case 1:
                    harga = 7500000
                    print("Kamu memilih iPhone 11 RAM 4GB seharga Rp 7.500.000")
                case 2:
                    harga = 8000000
                    print("Kamu memilih iPhone 11 RAM 6GB seharga Rp 8.000.000")
                case _:
                    print("RAM tidak tersedia!")
                    ram_valid = False
        case 2:
            print("\niPhone 12")
            print("Pilih varian RAM:")
            print("1. 4GB (Rp 9.000.000)")
            print("2. 6GB (Rp 9.800.000)")
            ram = int(input("Masukkan pilihan RAM: "))
            match ram:
                case 1:
                    harga = 9000000
                    print("Kamu memilih iPhone 12 RAM 4GB seharga Rp 9.000.000")
                case 2:
                    harga = 9800000
                    print("Kamu memilih iPhone 12 RAM 6GB seharga Rp 9.800.000")
                case _:
                    print("RAM tidak tersedia!")
                    ram_valid = False
        case 3:
            print("\niPhone 13")
            print("Pilih varian RAM:")
            print("1. 4GB (Rp 10.500.000)")
            print("2. 6GB (Rp 11.200.000)")
            ram = int(input("Masukkan pilihan RAM: "))
            match ram:
                case 1:
                    harga = 10500000
                    print("Kamu memilih iPhone 13 RAM 4GB seharga Rp 10.500.000")
                case 2:
                    harga = 11200000
                    print("Kamu memilih iPhone 13 RAM 6GB seharga Rp 11.200.000")
                case _:
                    print("RAM tidak tersedia!")
                    ram_valid = False
        case 4:
            print("\niPhone 14")
            print("Pilih varian RAM:")
            print("1. 6GB (Rp 12.000.000)")
            print("2. 8GB (Rp 13.000.000)")
            ram = int(input("Masukkan pilihan RAM: "))
            match ram:
                case 1:
                    harga = 12000000
                    print("Kamu memilih iPhone 14 RAM 6GB seharga Rp 12.000.000")
                case 2:
                    harga = 13000000
                    print("Kamu memilih iPhone 14 RAM 8GB seharga Rp 13.000.000")
                case _:
                    print("RAM tidak tersedia!")
                    ram_valid = False
        case 5:
            print("\niPhone 15")
            print("Pilih varian RAM:")
            print("1. 6GB (Rp 15.000.000)")
            print("2. 8GB (Rp 16.000.000)")
            print("3. 12GB (Rp 17.500.000)")
            ram = int(input("Masukkan pilihan RAM: "))
            match ram:
                case 1:
                    harga = 15000000
                    print("Kamu memilih iPhone 15 RAM 6GB seharga Rp 15.000.000")
                case 2:
                    harga = 16000000
                    print("Kamu memilih iPhone 15 RAM 8GB seharga Rp 16.000.000")
                case 3:
                    harga = 17500000
                    print("Kamu memilih iPhone 15 RAM 12GB seharga Rp 17.500.000")
                case _:
                    print("RAM tidak tersedia!")
                    ram_valid = False
        case _:
            print("\nPilihan iPhone tidak tersedia!")
            continue  # balik ke awal

    # kalau RAM tidak valid, tanya mau ulang
    if not ram_valid:
        ulang = input("\nApakah ingin memesan yang lain? (Y/N): ").upper()
        if ulang == "Y":
            continue
        else:
            print("\nTerima kasih sudah berkunjung ke ALAKADAR PHONE CELL!")
            break

    beli_aksesoris = input("\nApakah kamu ingin membeli aksesoris juga? (Y/N): ").upper()
    total = harga

    if beli_aksesoris == "Y":
        print("\n=== PRICE LIST AKSESORIS ===")
        print("1. Headset   - Rp 250.000")
        print("2. Earphone  - Rp 150.000")
        print("3. Casing    - Rp 100.000")
        print("4. Charger   - Rp 300.000")
        print("5. Tempered Glass - Rp 75.000")

        aks = int(input("Pilih nomor aksesoris yang ingin dibeli: "))

        match aks:
            case 1:
                print("Kamu menambah Headset seharga Rp 250.000")
                total += 250000
            case 2:
                print("Kamu menambah Earphone seharga Rp 150.000")
                total += 150000
            case 3:
                print("Kamu menambah Casing seharga Rp 100.000")
                total += 100000
            case 4:
                print("Kamu menambah Charger seharga Rp 300.000")
                total += 300000
            case 5:
                print("Kamu menambah Tempered Glass seharga Rp 75.000")
                total += 75000
            case _:
                print("Pilihan aksesoris tidak tersedia!")

    print("\n===================================")
    print(f" Total belanja kamu: Rp {total:,}")
    print("Terima kasih sudah berbelanja di ALAKADAR PHONE CELL!")
    print("===================================")

    # tanya lagi mau pesan ulang atau tidak
    ulang = input("\nApakah ingin memesan lagi? (Y/N): ").upper()
    if ulang != "Y":
        print("\nTerima kasih sudah berkunjung! Sampai jumpa lagi ")
        break