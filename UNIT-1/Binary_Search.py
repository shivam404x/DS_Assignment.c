
# RECURSSIvE BINARY SEARCH

# IMPLEMENTING THE BINARY SEARCH RECURSSIVELY 
# AND EXPLAINING ITS TIME COMPLEXITY - O(LOG(N))

# RECURSIVE BINARY SEARCH IS AN ALGORITHM THAT FINDS A TARGET ELEMENT FROM A SORTED
#  ARRAY BY REPEATEDLY DIVIDING THE SEARCH INTERVAL IN HALF USING RECURSSION.

def binarySearch(arr, key, low, high):  # DEFINING THE MAIN RECURSSIVE BINARY SEARCH FUNCTION

    # arr - sorted array
    # key - value to find
    # low - starting index
    # high - ending index

    if low > high:  # base case - 1
        # if low > high - means empty range
        print(f"Key {key} NOT FOUND")
        return -1  # give -1 i.e. standard convention
    
    mid = low + (high - low) // 2  # finding the middle index
    # if we find it like (low + high)//2 - overflow risk
    # safe method is low + (high-low)//2 - overflow avoided
    
    print(f"low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}") 
     # debug trance - shows every steps including current range + mid value
    
    if arr[mid] == key:  # base case -2 
        # found the key no more recurssion will return the index where it is found
        return mid
    
    elif arr[mid] > key:  
# key is smaller - left half search and size is halfed, new smaller range - (low,mid-1)
        return binarySearch(arr, key, low, mid-1)
    
    else:
# key is larger - right half search and again size is halfed (i.e. logarithmic reduction) , 
# new smaller range - (mid+1, high)
        return binarySearch(arr, key, mid+1, high)


# testing 

print("=== BINARY SEARCH DEMO ===")
arr = [1, 3, 5, 7, 9, 11, 13, 15]  # testing the code with this sorted and even length array
 
 
print("\n1. FOUND case:")  # if key exists give at index 3
print("Index:", binarySearch(arr, 7, 0, len(arr)-1))


print("\n2. NOT FOUND case:")  # if key missing is return -1 (handles missing key correctly)
print("Index:", binarySearch(arr, 8, 0, len(arr)-1))


print("\n3. EMPTY array:")  # if empty array 
empty_arr = []  
print("Index:", binarySearch(empty_arr, 5, 0, len(empty_arr)-1))


print("\n=== RECURRENCE EXPLANATION ===")  # explanation of time complesity

print('''T(n) = Time to solve array size n
Each step:
1. O(1) work (mid calculate + compare)
2. T(n/2) recursive call (half size)
T(n) = T(n/2) + O(1)     <- RECURRENCE RELATION
''')

print("T(n) = T(n/2) + O(1)")
print("n=8 → 4 → 2 → 1 → O(log n)")

