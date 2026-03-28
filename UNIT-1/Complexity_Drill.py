
# COMPLEXITY PRACTICE DRILL:-

# Ye program different loop patterns ko use karke
# time complexity samajhne me help karta hai.

# ------------------ 1. SIMPLE LOOP (O(n)) ------------------

def simple_loop(n):

    operations = 0

    for i in range(n):
        operations += 1

    print("\n[Simple Loop]")
    print("Operations:", operations)
    print("Time Complexity: O(n)")
    print(f"Reason: loop exactly {n} baar chala → linear growth")


# ------------------ 2. DOUBLE LOOP (O(n^2)) ------------------

def double_loop(n):

    operations = 0

    for i in range(n):
        for j in range(n):
            operations += 1

    print("\n[Double Loop]")
    print("Operations:", operations)
    print("Time Complexity: O(n^2)")
    print(f"Reason: {n} × {n} = {n*n} operations")


# ------------------ 3. TRIANGLE PATTERN LOOP ------------------

def triangle_loop(n):

    operations = 0

    for i in range(1, n + 1):
        for j in range(i):
            operations += 1

    print("\n[Triangle Loop]")
    print("Operations:", operations)
    print("Time Complexity: O(n^2)")
    print("Reason: total ≈ n(n+1)/2 → still quadratic")


# ------------------ 4. HALF REDUCTION LOOP ------------------

def log_loop(n):

    operations = 0
    value = n

    while value > 0:
        operations += 1
        value = value // 2   # har step me half

    print("\n[Halving Loop]")
    print("Operations:", operations)
    print("Time Complexity: O(log n)")
    print("Reason: har step me size half ho raha hai")


# ------------------ SEARCH CASES ------------------

def linear_search_info():

    print("\n[Linear Search Cases]")
    print("Best Case   → O(1)   (first element)")
    print("Average     → O(n)")
    print("Worst Case  → O(n)   (last ya absent)")


def binary_search_info():

    print("\n[Binary Search Cases] (sorted array needed)")
    print("Best Case   → O(1)   (middle element)")
    print("Average     → O(log n)")
    print("Worst Case  → O(log n)")


# ------------------ MAIN FUNCTION ------------------

def run():

    n = int(input("Enter n value: "))

    print("\n==== Complexity Analysis ====")

    simple_loop(n)
    double_loop(n)
    triangle_loop(n)
    log_loop(n)

    linear_search_info()
    binary_search_info()


# Program start point
if __name__ == "__main__":
    run()
