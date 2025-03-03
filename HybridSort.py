#  ---------------------------------------------------------
#  - CSE 830 - AAFNAN MAHMOOD
#  - HOMEWORK 3
#  - Q5
#  ---------------------------------------------------------

import time, random

# -- Merge sort and Insertion sort algorithms were sourced from GeeksforGeeks:
# --    https://www.geeksforgeeks.org/python-program-for-merge-sort/
# --    https://www.geeksforgeeks.org/python-program-for-insertion-sort/

#  Merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0 
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

#  Insertion sort
def insertionSort(arr, l = 0, r = None):
    if r is None:
        r = len(arr) - 1
        
    for i in range(l + 1, r + 1):
        key = arr[i]
        j = i - 1
        while j >= l and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#  Hybrid sorting algorithm (Merge Sort + Insertion Sort for small subarrays)
def hybridSort(arr, l, r, k):
    if (r - l + 1) <= k:
        insertionSort(arr, l, r)
        return
    else:
        if l < r:
            m = l + (r - l) // 2
            hybridSort(arr, l, m, k)
            hybridSort(arr, m + 1, r, k)
            merge(arr, l, m, r)


#  Common test parameters
NUM_TESTS = 7   #  Number of tests to run
START_SIZE = 10  #  Starting array size
STEP_SIZE = 30  #  Increase in array size per test
K_VALUES = [50, 70, 90, 100, 110, 120, 150]  #  k-values to test

#  Function to time hybrid merge sort with different k values
def time_hybrid_sort():
    print("\n--- Hybrid Sort Timing ---")
    for k in K_VALUES:
        print(f"\nTesting with k = {k}")
        for i in range(NUM_TESTS):
            size = START_SIZE + i * STEP_SIZE
            arr = [random.randint(0, 10000) for _ in range(size)]
            start_time = time.perf_counter()
            hybridSort(arr, 0, len(arr) - 1, k)
            end_time = time.perf_counter()
            print(f"Array size: {size}, Hybrid Sort (k={k}) time: {end_time - start_time:.6f} sec")

# Run timing tests
time_hybrid_sort()

