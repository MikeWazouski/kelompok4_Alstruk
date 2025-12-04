# FUNGSI–FUNGSI SORTING
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# PROGRAM UTAMA
def print_header(title):
    print("\n" + "="*50)
    print(title.center(50))
    print("="*50 + "\n")


def main():

    print_header("PROGRAM SORTING PYTHON")

    # Input jumlah data
    n = int(input("Masukkan jumlah data: "))
    data = []

    # Input nilai data
    for i in range(n):
        nilai = int(input(f"Data ke-{i+1}: "))
        data.append(nilai)

    print_header("DATA ASLI")
    print("List Data :", data)
    print()

    print_header("PILIH METODE SORTING")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    pilihan = input("\nMasukkan pilihan (1-5): ")

    print_header("HASIL SORTING")

    # Hanya menjalankan metode yang dipilih user
    if pilihan == "1":
        print("Metode : Bubble Sort\n")
        hasil = bubble_sort(data.copy())
    elif pilihan == "2":
        print("Metode : Selection Sort\n")
        hasil = selection_sort(data.copy())
    elif pilihan == "3":
        print("Metode : Insertion Sort\n")
        hasil = insertion_sort(data.copy())
    elif pilihan == "4":
        print("Metode : Merge Sort\n")
        hasil = merge_sort(data.copy())
    elif pilihan == "5":
        print("Metode : Quick Sort\n")
        hasil = quick_sort(data.copy())
    else:
        print("Pilihan tidak valid!")
        return

    print(f"Data sebelum sorting : {data}")
    print(f"Data setelah sorting : {hasil}")
    print("\n" + "="*50)


if __name__ == "__main__":
    main()
