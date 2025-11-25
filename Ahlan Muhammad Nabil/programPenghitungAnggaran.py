import json


def add_expense(expenses, description, amount):
    expenses.append({'description': description, 'amount': amount})
    print(f"pengeluaran ditambahkan: {description}, jumlah: {amount}")

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"total anggaran: {budget}")
    print("pengeluaran: ")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"total digunakan: {get_total_expenses(expenses)}")
    print(f"anggaran tersisa: {get_balance(budget, expenses)}")
    
def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data ["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []
    
def save_budget_detail(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Selamat datang di program penghitung anggaran!")
    filepath = 'budget_data.json'
    initial_budget, expenses = load_budget_data(filepath)
    
    # Jika file tidak ada atau kosong, minta input dari user
    if initial_budget == 0 and not expenses:
        initial_budget = float(input("Enter your initial budget: "))
        save_budget_detail(filepath, initial_budget, expenses)
    
    budget = initial_budget

    while True:
        print("\nMau ngapain hari ini?")
        print("1. Tambah pengeluaran")
        print("2. Tununjukkan rincian anggaran")
        print("3. Keluar")
        choice = input("Masukkan pilihan anda (1/2/3): ")

        if choice == '1':
            description = input("Masukkan deskripsi pengeluaran: ")
            amount = float(input("Masukkan jumlah pengeluaran: "))
            add_expense(expenses, description, amount)
        elif choice == '2':
            show_budget_details(budget, expenses)
        elif choice == '3':
            save_budget_detail(filepath, initial_budget, expenses)
            print("Keluar dari aplikasi...")
            break
        else:
            print("Pilihan tidak valid. silahkan coba lagi.")

if __name__ == "__main__":
    main()
