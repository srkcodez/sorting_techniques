import datetime
import random
import tkinter as tk
from tkinter import messagebox, ttk


# Sorting algorithms
def bubble_sort(a):
    n = len(a)
    np = nc = ns = 0
    for i in range(n - 1):
        np += 1
        flag = 0
        for j in range(n - 1 - i):
            nc += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ns += 1
                flag = 1
        if flag == 0:
            break
    return np, nc, ns


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
    return np, nc, ns


def selection_sort(a):
    n = len(a)
    np = nc = ns = 0
    for i in range(n):
        np += 1
        min_idx = i
        for j in range(i + 1, n):
            nc += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            ns += 1
    return np, nc, ns


def quick_sort(arr):
    np = [0]
    nc = [0]
    ns = [0]

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
    return np[0], nc[0], ns[0]


def merge_sort(arr):
    np = [0]
    nc = [0]

    def _merge_sort(items):
        if len(items) > 1:
            mid = len(items) // 2
            left_half = items[:mid]
            right_half = items[mid:]

            _merge_sort(left_half)
            _merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                nc[0] += 1
                if left_half[i] < right_half[j]:
                    items[k] = left_half[i]
                    i += 1
                else:
                    items[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                items[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                items[k] = right_half[j]
                j += 1
                k += 1

            np[0] += 1

    _merge_sort(arr)
    return np[0], nc[0]


# Helper functions for tests
def perform_test(sort_func, data):
    st = datetime.datetime.now()
    result = sort_func(data)
    et = datetime.datetime.now()
    time_taken = et - st
    return result, time_taken


def run_test(sort_func, test_name, data_gen):
    data = data_gen()
    result, time_taken = perform_test(sort_func, data)
    return f"{test_name}:\nResult: {result}\nTime taken: {time_taken}\n"


# GUI
class SortingAnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sorting Algorithm Analysis")
        self.geometry("600x600")
        self.create_widgets()

    def create_widgets(self):
        self.algo_label = tk.Label(self, text="Select Sorting Algorithm")
        self.algo_label.pack(pady=10)

        self.algo_combobox = ttk.Combobox(self, values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort",
                                                        "Merge Sort"])
        self.algo_combobox.pack(pady=10)

        self.test_label = tk.Label(self, text="Select Test")
        self.test_label.pack(pady=10)

        self.test_combobox = ttk.Combobox(self, values=[
            "Stability Test", "Adaptiveness Test", "In-Memory Test",
            "Large Dataset Test (100,000 elements)", "2 Lakh Random Elements and Top 5",
            "Sorted List Test", "Reverse Sorted List Test", "Identical Elements Test"
        ])
        self.test_combobox.pack(pady=10)

        self.run_button = tk.Button(self, text="Run Test", command=self.run_selected_test)
        self.run_button.pack(pady=20)

        self.result_text = tk.Text(self, wrap=tk.WORD, height=20, width=70)
        self.result_text.pack(pady=10)

    def run_selected_test(self):
        algo = self.algo_combobox.get()
        test = self.test_combobox.get()

        if not algo or not test:
            messagebox.showerror("Input Error", "Please select both sorting algorithm and test.")
            return

        if algo == "Bubble Sort":
            sort_func = bubble_sort
        elif algo == "Insertion Sort":
            sort_func = insertion_sort
        elif algo == "Selection Sort":
            sort_func = selection_sort
        elif algo == "Quick Sort":
            sort_func = quick_sort
        elif algo == "Merge Sort":
            sort_func = merge_sort
        else:
            messagebox.showerror("Algorithm Error", "Unknown sorting algorithm selected.")
            return

        if test == "Stability Test":
            data_gen = lambda: [(5, 'a'), (3, 'b'), (5, 'c'), (1, 'd'), (3, 'e')]
        elif test == "Adaptiveness Test":
            data_gen = lambda: [1, 2, 3, 4, 5]
        elif test == "In-Memory Test":
            messagebox.showinfo("In-Memory Test",
                                f"{algo} is an in-memory sort." if algo != "Merge Sort" else f"{algo} is not purely in-memory as it requires additional space for merging.")
            return
        elif test == "Large Dataset Test (100,000 elements)":
            data_gen = lambda: [random.randint(0, 100000) for _ in range(100000)]
        elif test == "2 Lakh Random Elements and Top 5":
            data_gen = lambda: [random.randint(0, 100000) for _ in range(200000)]
        elif test == "Sorted List Test":
            data_gen = lambda: list(range(1, 11))
        elif test == "Reverse Sorted List Test":
            data_gen = lambda: list(range(10, 0, -1))
        elif test == "Identical Elements Test":
            data_gen = lambda: [5] * 10
        else:
            messagebox.showerror("Test Error", "Unknown test selected.")
            return

        test_name = f"{algo} - {test}"
        result = run_test(sort_func, test_name, data_gen)
        self.result_text.insert(tk.END, result + "\n")
        self.result_text.see(tk.END)


if __name__ == "__main__":
    app = SortingAnalysisApp()
    app.mainloop()