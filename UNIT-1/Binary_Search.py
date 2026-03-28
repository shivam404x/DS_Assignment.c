# RECURSIVE BINARY SEARCH :-

# Binary Search ek efficient technique hai jo sorted array me
# kisi element ko dhoondhne ke liye use hoti hai.
# Yeh recursion ka use karke har step me search space ko half kar deta hai.

def binary_search(arr, target, start, end):

    # Base Case 1: agar range invalid ho gayi (element nahi mila)
    if start > end:
        print(f"{target} array me nahi mila ❌")
        return -1

    # Middle index nikalna (safe formula)
    mid = start + (end - start) // 2

    # Debug info (optional - samajhne ke liye useful)
    print(f"Range: [{start}, {end}] | Mid: {mid} | Value: {arr[mid]}")

    # Base Case 2: element mil gaya
    if arr[mid] == target:
        print(f"{target} mil gaya at index {mid} ✅")
        return mid

    # Agar target chhota hai → left side me search
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)

    # Agar target bada hai → right side me search
    else:
        return binary_search(arr, target, mid + 1, end)


# ================== TESTING ==================

print("==== Binary Search Test ====")

nums = [2, 4, 6, 8, 10, 12, 14]

print("\nCase 1: Element present")
result = binary_search(nums, 8, 0, len(nums)-1)
print("Result Index:", result)

print("\nCase 2: Element absent")
result = binary_search(nums, 5, 0, len(nums)-1)
print("Result Index:", result)

print("\nCase 3: Empty array")
empty = []
result = binary_search(empty, 3, 0, len(empty)-1)
print("Result Index:", result)


# ================== TIME COMPLEXITY ==================

print("\n==== Time Complexity ====")

print("""
Har step me:
- Sirf ek comparison hota hai → O(1)
- Aur problem size half ho jata hai → n/2

Isliye recurrence relation:
T(n) = T(n/2) + O(1)

Steps:
n → n/2 → n/4 → n/8 → ... → 1

Total steps ≈ log(n)

Final Time Complexity = O(log n)
""")
