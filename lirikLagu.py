import sys
from time import sleep

def print_lyrics():
    # Ini daftar lirik lagu sama 'delay' (jeda) buat efek ngetiknya
    # Formatnya: ("Teks Lirik", Kecepatan Muncul Huruf)
    # Catatan: Semakin kecil angkanya (misal 0.04), ngetiknya makin ngebut
    lines = [
        ("I wanna da-", 0.08),
        ("I wanna dance in the lights", 0.06),
        ("I wanna ro-", 0.09),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.07),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("Come on, come on", 0.05),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.04),
        ("Rock that body", 0.05),
        ("Come on, come on", 0.05)
    ]

    # Loop luar: Ini buat ngambil satu per satu baris lirik dari daftar di atas
    for line, delay in lines:
        # Loop dalam: Ini buat mecah kalimat jadi huruf per huruf
        for char in line:
            sys.stdout.write(char) # Cetak huruf ke samping (gak langsung enter ke bawah)
            sys.stdout.flush()     # Paksa hurufnya langsung nongol di layar (biar gak nunggu numpuk)
            sleep(delay)           # Tahan bentar sebelum nyetak huruf berikutnya (ini yang bikin efek kayak ngetik)
        
        print()    # Nah, kalo satu kalimat udah beres, baru kita kasih 'Enter' (garis baru)
        sleep(0.1) # Kasih napas dikit sebelum lanjut ke baris lirik berikutnya

# Panggil fungsi ini biar kodenya jalan
print_lyrics()
