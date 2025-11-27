import json   # Mengimpor modul json untuk membaca/menulis file JSON


# Fungsi untuk menambah pengeluaran baru
def add_expense(expenses, description, amount):
    # Tambahkan pengeluaran ke list
    expenses.append({'description': description, 'amount': amount})
    # Tampilkan notifikasi
    print(f"pengeluaran ditambahkan: {description}, jumlah: {amount}")


# Fungsi untuk menghitung total seluruh pengeluaran
def get_total_expenses(expenses):
    sum = 0
    # Loop setiap item di expenses
    for expense in expenses:
        sum += expense["amount"]   # Tambahkan nilai amount ke total
    return sum   # Kembalikan total pengeluaran


# Fungsi menghitung sisa anggaran
def get_balance(budget, expenses):
    # Sisa anggaran = budget awal - total pengeluaran
    return budget - get_total_expenses(expenses)


# Fungsi menampilkan semua detail anggaran
def show_budget_details(budget, expenses):
    print(f"total anggaran: {budget}")
    print("pengeluaran: ")

    # Tampilkan setiap pengeluaran
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")

    # Tampilkan total digunakan dan sisa anggaran
    print(f"total digunakan: {get_total_expenses(expenses)}")
    print(f"anggaran tersisa: {get_balance(budget, expenses)}")


# Fungsi memuat data dari file JSON
def load_budget_data(filepath):
    try:
        # Coba buka file JSON
        with open(filepath, 'r') as file:
            data = json.load(file)  # Baca file JSON
            # Kembalikan data anggaran dan daftar pengeluaran
            return data["initial_budget"], data["expenses"]

    # Jika file tidak ada atau rusak → gunakan nilai default
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []


# Fungsi menyimpan data ke file JSON
def save_budget_detail(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }

    # Tulis data ke file JSON
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


# Program utama
def main():
    print("Selamat datang di program penghitung anggaran!")

    filepath = 'budget_data.json'   # Nama file untuk menyimpan data

    # Muat data dari file jika ada
    initial_budget, expenses = load_budget_data(filepath)

    # Jika file kosong / belum ada, minta user masukkan anggaran awal
    if initial_budget == 0 and not expenses:
        initial_budget = float(input("Enter your initial budget: "))
        # Simpan anggaran awal ke file
        save_budget_detail(filepath, initial_budget, expenses)

    budget = initial_budget   # Set budget aktif

    # Loop menu utama
    while True:
        print("\nMau ngapain hari ini?")
        print("1. Tambah pengeluaran")
        print("2. Tununjukkan rincian anggaran")
        print("3. Keluar")
        choice = input("Masukkan pilihan anda (1/2/3): ")

        # Tambah pengeluaran
        if choice == '1':
            description = input("Masukkan deskripsi pengeluaran: ")
            amount = float(input("Masukkan jumlah pengeluaran: "))
            add_expense(expenses, description, amount)

        # Tampilkan rincian anggaran
        elif choice == '2':
            show_budget_details(budget, expenses)

        # Keluar program
        elif choice == '3':
            # Simpan data sebelum keluar
            save_budget_detail(filepath, initial_budget, expenses)
            print("Keluar dari aplikasi...")
            break

        # Jika input salah
        else:
            print("Pilihan tidak valid. silahkan coba lagi.")


# Menjalankan program jika file ini dijalankan langsung
if __name__ == "__main__":
    main()
