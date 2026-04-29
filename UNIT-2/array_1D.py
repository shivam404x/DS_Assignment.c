
# 1D ARRAY OPERATIONS (INSERT / DELETE + SHIFT COST)

# Idea:
# Array me insert/delete karte time elements shift hote hain,
# aur wahi time complexity ko affect karta hai.

# ------------------ PRINT FUNCTION ------------------

def show_array(arr):
    print(" ".join(str(x) for x in arr))


# ------------------ INSERT FUNCTION ------------------

def insert_element(arr, index, value, capacity):

    length = len(arr)

    # invalid cases
    if length >= capacity or index < 0 or index > length:
        print("Insert failed")
        return arr, 0

    # number of shifts required
    shift_count = length - index

    # new array create karke insert karna
    updated = arr[:index] + [value] + arr[index:]

    return updated, shift_count


# ------------------ DELETE FUNCTION ------------------

def delete_element(arr, index):

    length = len(arr)

    # invalid cases
    if length == 0 or index < 0 or index >= length:
        print("Delete failed")
        return arr, 0

    # shifts = elements after index move left
    shift_count = length - index - 1

    updated = arr[:index] + arr[index + 1:]

    return updated, shift_count


# ------------------ COMPLEXITY DISPLAY ------------------

def complexity_info(index, length, inserting):

    if inserting:
        if index == length:
            print("Time Complexity: O(1)")
        else:
            print("Time Complexity: O(n) due to shifting")

    else:
        if index == length - 1:
            print("Time Complexity: O(1)")
        else:
            print("Time Complexity: O(n) due to shifting")


# ------------------ DEMO ------------------

arr = [10, 20, 30, 40, 50]
capacity = 100

print("Initial Array:")
show_array(arr)


# Insert at beginning
print("\nInsert at beginning:")
arr, moves = insert_element(arr, 0, 5, capacity)
print("Array:", end=" ")
show_array(arr)
print("Shifts:", moves)
complexity_info(0, 5, True)


# Insert in middle
print("\nInsert in middle:")
mid = len(arr) // 2
arr, moves = insert_element(arr, mid, 99, capacity)
print("Array:", end=" ")
show_array(arr)
print("Shifts:", moves)
complexity_info(mid, 6, True)


# Insert at end
print("\nInsert at end:")
arr, moves = insert_element(arr, len(arr), 999, capacity)
print("Array:", end=" ")
show_array(arr)
print("Shifts:", moves)
complexity_info(len(arr)-1, 7, True)


# Delete from beginning
print("\nDelete from beginning:")
arr, moves = delete_element(arr, 0)
print("Array:", end=" ")
show_array(arr)
print("Shifts:", moves)
complexity_info(0, 7, False)


# Delete from end
print("\nDelete from end:")
arr, moves = delete_element(arr, len(arr)-1)
print("Array:", end=" ")
show_array(arr)
print("Shifts:", moves)
complexity_info(len(arr)-1, 6, False)
