# ADA Lab Assignment - Analysis & Design of Algorithms
# Author: Adarsh Rai

import time
import random
import matplotlib.pyplot as plt

# -------------------- TASK 1 --------------------
# Algorithm Growth Observation

def constant_time(n):
    return n * 5

def linear_time(n):
    total = 0
    for i in range(n):
        total += i
    return total

def quadratic_time(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total

def logarithmic_time(n):
    while n > 1:
        n = n // 2
    return n

def task1():
    input_sizes = [100, 500, 1000, 2000]

    constant_times, linear_times = [], []
    quadratic_times, logarithmic_times = [], []

    for n in input_sizes:
        start = time.perf_counter()
        constant_time(n)
        constant_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        linear_time(n)
        linear_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        logarithmic_time(n)
        logarithmic_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        quadratic_time(n)
        quadratic_times.append(time.perf_counter() - start)

    plt.plot(input_sizes, constant_times, label="O(1)")
    plt.plot(input_sizes, linear_times, label="O(n)")
    plt.plot(input_sizes, logarithmic_times, label="O(log n)")
    plt.plot(input_sizes, quadratic_times, label="O(n^2)")

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time")
    plt.title("Growth Comparison")
    plt.legend()
    plt.show()


# -------------------- TASK 2 --------------------
# Searching Algorithms

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def task2():
    input_sizes = [10, 100, 500, 1000]

    for n in input_sizes:
        arr = sorted(random.sample(range(1, n * 5), n))

        start = time.time()
        linear_search(arr, -1)
        print(f"Linear Search Worst Case for n={n}: {time.time() - start}")


# -------------------- TASK 3 --------------------
# Recursion

factorial_calls = 0

def factorial(n):
    global factorial_calls
    factorial_calls += 1
    if n == 0:
        return 1
    return n * factorial(n - 1)


# -------------------- TASK 4 --------------------
# Recurrence

count_T1 = 0

def T1(n):
    global count_T1
    count_T1 += 1
    if n <= 1:
        return 1
    return T1(n // 2) + n


# -------------------- MAIN --------------------

if __name__ == "__main__":
    print("Running Task 1...")
    task1()

    print("\nRunning Task 2...")
    task2()

    print("\nFactorial Example:", factorial(5))
