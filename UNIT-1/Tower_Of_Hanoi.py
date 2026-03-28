
# TOWER OF HANOI (RECURSION + MOVE COUNT)

# Basic idea:
# 3 rods → Source, Helper, Destination
# Har step me chhote disks ko move karke bada disk shift karte hain

# ------------------ MAIN FUNCTION ------------------

def solve_hanoi(n, source, helper, destination):

    # base case
    if n == 1:
        print(f"Disk 1: {source} → {destination}")
        return

    # step 1: n-1 disks helper par bhejo
    solve_hanoi(n-1, source, destination, helper)

    # step 2: sabse bada disk move karo
    print(f"Disk {n}: {source} → {destination}")

    # step 3: helper se destination par shift karo
    solve_hanoi(n-1, helper, source, destination)


# ------------------ DEMO ------------------

print("=== Hanoi Demo (n = 3) ===")
solve_hanoi(3, "A", "B", "C")


# ------------------ MOVE COUNT ------------------

def count_moves(n, counter):

    # base case
    if n == 1:
        counter[0] += 1
        return

    # recursion
    count_moves(n-1, counter)
    counter[0] += 1
    count_moves(n-1, counter)


print("\n=== Move Count (n = 4) ===")

moves = [0]
count_moves(4, moves)

print("Total moves:", moves[0])


# ------------------ COMPLEXITY ------------------

print("\n=== Complexity Info ===")
print("Time Complexity: O(2^n)")
print("Moves follow pattern → 1, 3, 7, 15, ...")
print("Formula: (2^n) - 1")
print("Reason: har step me problem 2 parts me break hoti hai")
