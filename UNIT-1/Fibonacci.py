
# FIBONACCI COMPARISON (NORMAL vs OPTIMIZED)

# Idea:
# 1. Simple recursion → baar-baar same calculation (slow)
# 2. Memoization → ek baar calculate karke store (fast)

# ------------------ NORMAL RECURSION ------------------

def fib_basic(n, counter):

    counter[0] += 1   # har function call count kar rahe hain

    if n <= 1:
        return n

    return fib_basic(n-1, counter) + fib_basic(n-2, counter)


# ------------------ MEMOIZATION VERSION ------------------

def fib_fast(n, counter, memory):

    counter[0] += 1

    # agar already calculate ho chuka hai
    if n in memory:
        return memory[n]

    if n <= 1:
        memory[n] = n
        return n

    # calculate + store
    value = fib_fast(n-1, counter, memory) + fib_fast(n-2, counter, memory)
    memory[n] = value

    return value


# ------------------ TESTING ------------------

print("n | fib(n) | basic calls | optimized calls")
print("------------------------------------------")

test_values = [10, 20, 30]

for num in test_values:

    basic_count = [0]
    fast_count = [0]
    memory_store = {}

    ans1 = fib_basic(num, basic_count)
    ans2 = fib_fast(num, fast_count, memory_store)

    print(f"{num} | {ans1} | {basic_count[0]} | {fast_count[0]}")


# ------------------ SUMMARY ------------------

print("\n=== Observation ===")
print("Basic recursion → bahut zyada calls (exponential growth)")
print("Memoization → kaafi kam calls (almost linear)")
print("Reason: duplicate work avoid ho jata hai")
