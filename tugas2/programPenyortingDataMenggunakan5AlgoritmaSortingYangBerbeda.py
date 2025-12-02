import json
import os

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
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# ----------------------------------------------------
#  BAGIAN PENAMBAHAN: SAVE DATA KE data.json + INPUT
# ----------------------------------------------------
def save_data_to_json():
    n = int(input("Masukkan jumlah data: "))
    data = []

    for i in range(n):
        nilai = int(input(f"Data ke-{i+1}: "))
        data.append(nilai)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data berhasil disimpan ke data.json\n")


# ----------------------------------------------------
# PROGRAM UTAMA
# ----------------------------------------------------
def main():

    # Jika file tidak ada, minta user input data dulu
    if not os.path.exists("data.json"):
        print("File data.json tidak ditemukan. Membuat file baru...")
        save_data_to_json()

    # Baca file JSON
    with open('data.json', 'r') as file:
        data = json.load(file)

    print("Data asli dari data.json:", data)

    print("\n=== HASIL SORTING ===")
    print("Bubble Sort   :", bubble_sort(data.copy()))
    print("Selection Sort:", selection_sort(data.copy()))
    print("Insertion Sort:", insertion_sort(data.copy()))
    print("Merge Sort    :", merge_sort(data.copy()))
    print("Quick Sort    :", quick_sort(data.copy()))


if __name__ == "__main__":
    main()
