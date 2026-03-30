# 2D ARRAY (MATRIX OPERATIONS + TRAVERSAL)

# A 2D array represents data in rows and columns.
# Access format: matrix[row][column]

# ------------------ DISPLAY FUNCTION ------------------

def display_matrix(mat):
    for r in mat:
        print(" ".join(str(val) for val in r))


# ------------------ ROW SUM FUNCTION ------------------

def calculate_row_sums(mat):
    print("\nRow Sums:")

    for index, r in enumerate(mat):
        total = sum(r)
        print(f"Row {index}: {total}")


# ------------------ COLUMN SUM FUNCTION ------------------

def calculate_column_sums(mat):

    if not mat or not mat[0]:
        print("Matrix is empty")
        return

    print("\nColumn Sums:")

    num_cols = len(mat[0])

    for c in range(num_cols):
        total = 0
        for r in range(len(mat)):
            total += mat[r][c]

        print(f"Column {c}: {total}")


# ------------------ SEARCH FUNCTION ------------------

def find_value(mat, key):
    print(f"\nSearching for {key}:")

    for i in range(len(mat)):
        for j in range(len(mat[0])):

            if mat[i][j] == key:
                print(f"Value found at ({i}, {j})")
                return

    print("Value not found")


# ------------------ TRANSPOSE FUNCTION ------------------

def transpose_matrix(mat):

    if not mat or not mat[0]:
        print("Empty matrix")
        return

    rows = len(mat)
    cols = len(mat[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = mat[i][j]

    print("\nTranspose Matrix:")
    display_matrix(result)


# ------------------ DEMO ------------------

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Original Matrix:")
display_matrix(matrix)

calculate_row_sums(matrix)
calculate_column_sums(matrix)
find_value(matrix, 7)
transpose_matrix(matrix)
