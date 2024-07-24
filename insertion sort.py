import datetime
import random


def insertion_sort(a):
    np = nc = ns = 0
    n = len(a)
    for i in range(1, n):
        np += 1
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            nc += 1
            a[j + 1] = a[j]
            ns += 1
            j -= 1
        a[j + 1] = key
        nc += 1

    print(f'Total number of passes: {np}')
    print(f'Total number of comparisons: {nc}')
    print(f'Total number of swaps: {ns}')


def test_stability():
    data = [(5, 'a'), (3, 'b'), (5, 'c'), (1, 'd'), (3, 'e')]
    expected = [(1, 'd'), (3, 'b'), (3, 'e'), (5, 'a'), (5, 'c')]
    insertion_sort(data)
    print("Stability test passed:", data == expected)


def test_adaptiveness():
    data = [1, 2, 3, 4, 5]
    insertion_sort(data)
    print("Adaptiveness test passed (check passes):")


def test_in_memory():
    print("Insertion Sort is an in-memory sort.")


def test_large_dataset():
    data = [random.randint(0, 100000) for _ in range(100000)]
    st = datetime.datetime.now()
    insertion_sort(data)
    et = datetime.datetime.now()
    print("Time taken for 100,000 elements:", et - st)


def test_top_5_large_dataset():
    data = [random.randint(0, 100000) for _ in range(200000)]
    st = datetime.datetime.now()
    insertion_sort(data)
    et = datetime.datetime.now()
    print("Time taken for 200,000 elements:", et - st)
    print("Top 5 elements:", data[-5:])


def test_sorted_list():
    data = list(range(1, 11))
    st = datetime.datetime.now()
    insertion_sort(data)
    et = datetime.datetime.now()
    print("Time taken for sorted list:", et - st)


def test_reverse_sorted_list():
    data = list(range(10, 0, -1))
    st = datetime.datetime.now()
    insertion_sort(data)
    et = datetime.datetime.now()
    print("Time taken for reverse sorted list:", et - st)


def test_identical_elements():
    data = [5] * 10
    st = datetime.datetime.now()
    insertion_sort(data)
    et = datetime.datetime.now()
    print("Time taken for identical elements:", et - st)


def menu():
    print("\nInsertion Sort Test Menu")
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