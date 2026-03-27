
# FIBONACCI (NATIVE V/S MEMORIZED)

# NATIVE : CALCULATOR WITHOUT MEMORY (RECOUNTS EVERYTHING)
# MEMORIZED : CALCULATOR WITH MEMORY BUTTON (STORES ANSWERS)

def fib_naive(n, calls=[0]): # function defination with a default value of calls=[0]

    calls[0] += 1  # counting each call

    if n <= 1:  # base case
        return n
    
    return fib_naive(n-1, calls) + fib_naive(n-2, calls)  # recursive case


# function defination with calls=[0] and cache={} - smart fibonacci
def fib_memo(n, calls=[0], cache={}):  

    calls[0] += 1  # counting each call

    if n in cache:   # running for loop and checking it cache already have the particular value - SUPER FAST CALCULATION
        return cache[n]  # returning that particular value 
    
    if n <= 1:  # base case + saving info in cache
        cache[n] = n
        return n
    
    # calculating the values and saving it to the cache + returning it
    cache[n] = fib_memo(n-1, calls, cache) + fib_memo(n-2, calls, cache)
    return cache[n]


print("n\tfib(n)\tNaive Calls\tMemo Calls")  # headings of the table
print("---------------------------------------------")

tests = [10, 20, 30]  # lab test case

for n in tests:
    # reseting all the values before every step and then comparing
    naive_calls = [0]
    memo_calls = [0]
    memo_cache = {}
    
    naive_result = fib_naive(n, naive_calls)  # calling the fib_naive function
    memo_result = fib_memo(n, memo_calls, memo_cache)  # calling the fib_memo function

   # to get result in tabular form 
    print(f"{n}\t{naive_result}\t{naive_calls[0]}\t\t{memo_calls[0]}")   


# explanation 
print("\nMemoization Analysis:")
print("Naive: Exponential calls (2^n growth)")
print("Memoized: Linear calls (2n growth only)") 
print("Savings: 99.99% fewer function calls!")

