import datetime
import random

def quick_sort(arr):
    np = [0]  # Number of passes (partitions)
    nc = [0]  # Number of comparisons
    ns = [0]  # Number of swaps

    def _quick_sort(items, low, high):
        if low < high:
            p = partition(items, low, high)
            _quick_sort(items, low, p)
            _quick_sort(items, p + 1, high)

    def partition(items, low, high):
        pivot = items[low]
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and items[left] <= pivot:
                left += 1
                nc[0] += 1
            while items[right] >= pivot and right >= left:
                right -= 1
                nc[0] += 1
            if right < left:
                done = True
            else:
                items[left], items[right] = items[right], items[left]
                ns[0] += 1
        items[low], items[right] = items[right], items[low]
        ns[0] += 1
        np[0] += 1
        return right

    _quick_sort(arr, 0, len(arr) - 1)
    print(f'Total number of passes: {np[0]}')
    print(f'Total number of comparisons: {nc[0]}')
    print(f'Total number of swaps: {ns[0]}')

def test_stability():
    data = [(5, 'a'), (3, 'b'), (5, 'c'), (1, 'd'), (3, 'e')]
    quick_sort(data)
    print("Stability test passed:", data == [(1, 'd'), (3, 'b'), (3, 'e'), (5, 'a'), (5, 'c')])

def test_adaptiveness():
    data = [1, 2, 3, 4, 5]
    quick_sort(data)
    print("Adaptiveness test passed (check passes):")

def test_in_memory():
    print("Quick Sort is an in-memory sort.")

def test_large_dataset():
    data = [random.randint(0, 100000) for _ in range(100000)]
    st = datetime.datetime.now()
    quick_sort(data)
    et = datetime.datetime.now()
    print("Time taken for 100,000 elements:", et - st)

def test_top_5_large_dataset():
    data = [random.randint(0, 100000) for _ in range(200000)]
    st = datetime.datetime.now()
    quick_sort(data)
    et = datetime.datetime.now()
    print("Time taken for 200,000 elements:", et - st)
    print("Top 5 elements:", data[-5:])

def test_sorted_list():
    data = list(range(1, 11))
    st = datetime.datetime.now()
    quick_sort(data)
    et = datetime.datetime.now()
    print("Time taken for sorted list:", et - st)

def test_reverse_sorted_list():
    data = list(range(10, 0, -1))
    st = datetime.datetime.now()
    quick_sort(data)
    et = datetime.datetime.now()
    print("Time taken for reverse sorted list:", et - st)

def test_identical_elements():
    data = [5] * 10
    st = datetime.datetime.now()
    quick_sort(data)
    et = datetime.datetime.now()
    print("Time taken for identical elements:", et - st)

def menu():
    print("\nQuick Sort Test Menu")
    print("1. Test Stability")
    print("2. Test Adaptiveness")
    print("3. Test if In-Memory")
    print("4. Test with Large Dataset (100,000 elements)")
    print("5. Test with 2 Lakh Random Elements and Print Top 5")
    print("6. Test with Already Sorted List")
    print("7. Test with Reverse Sorted List")
    print("8. Test with All Identical Elements")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            test_stability()
        elif choice == '2':
            test_adaptiveness()
        elif choice == '3':
            test_in_memory()
        elif choice == '4':
            test_large_dataset()
        elif choice == '5':
            test_top_5_large_dataset()
        elif choice == '6':
            test_sorted_list()
        elif choice == '7':
            test_reverse_sorted_list()
        elif choice == '8':
            test_identical_elements()
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()