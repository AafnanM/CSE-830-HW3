#  ---------------------------------------------------------
#  - CSE 830 - AAFNAN MAHMOOD
#  - HOMEWORK 3
#  - Q4
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

# Insertion sort
def insertionSort(arr):
    n = len(arr)
     
    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


#  Common test parameters
NUM_TESTS = 10   #  Number of tests to run
START_SIZE = 10  #  Starting array size
STEP_SIZE = 30  #  Increase in array size per test

#  Function to time merge sort separately
def time_merge_sort():
    print("\n--- Merge Sort Timing ---")
    for i in range(NUM_TESTS):
        size = START_SIZE + i * STEP_SIZE
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        start_time = time.perf_counter()
        mergeSort(arr, 0, len(arr) - 1)
        end_time = time.perf_counter()
        print(f"Array size: {size}, Merge Sort time: {end_time - start_time:.6f} sec")

#  Function to time insertion sort separately
def time_insertion_sort():
    print("\n--- Insertion Sort Timing ---")
    for i in range(NUM_TESTS):
        size = START_SIZE + i * STEP_SIZE
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        start_time = time.perf_counter()
        insertionSort(arr)
        end_time = time.perf_counter()
        print(f"Array size: {size}, Insertion Sort time: {end_time - start_time:.6f} sec")

# R un timing tests separately
time_merge_sort()
time_insertion_sort()


