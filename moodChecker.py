print("=== CEK MOOD HARI INI ===")
print("1. Senang")
print("2. Sedih")
print("3. Marah")
print("4. Jatuh Cinta")

pilih = int(input("Bagaimana keadaan kamu hari ini? (1-4): "))

if pilih == 1:
    alasan = input("Kenapa kamu senang hari ini? : ")
    print(f"\nWahh ikut senang juga dengernya! 😄")
    print("Tetap jaga mood baikmu yaa 💗")

elif pilih == 2:
    alasan = input("Kenapa kamu sedih hari ini? : ")
    print(f"\nAduhh sabar ya sayang 😢")
    print("Kamu kuat kok… aku di sini kalau kamu butuh cerita 💗")

elif pilih == 3:
    alasan = input("Kenapa kamu marah hari ini? : ")
    print(f"\nHmmm jangan marah-marah terus yaa 😠👉👈")
    print("Tarik nafas dulu… kamu pasti bisa tenang lagi, oke? ✨")

elif pilih == 4:
    alasan = input("Kenapa kamu jatuh cinta hari ini? : ")
    print(f"\nIhhh so cuteee 😳💗")
    print("Semoga perasaan kamu dibalas yaa, semangat cintanya! 💕")

else:
    print("Pilihan tidak tersedia!")
