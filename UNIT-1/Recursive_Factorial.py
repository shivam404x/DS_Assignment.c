
# RECURSIVE FACTORIAL :-

# Factorial ka matlab:
# n! = n × (n-1) × (n-2) × ... × 1

def fact(n):

    # invalid input check
    if n < 0:
        print("Negative number ka factorial define nahi hota ")
        return None

    # base case
    if n == 0 or n == 1:
        return 1

    # recursive step
    return n * fact(n - 1)


# ------------------ USER INPUT ------------------

print("=== Factorial Calculator ===")

num = int(input("Enter a number: "))

result = fact(num)

print("Result:", result)
