
# TOWER OF HANOI (N=3 TRACE + COMPLEXITY)

# Tower of Hanoi is a simple game:

# 3 rods (A, B, C) + some circles of different sizes (disks)

# START: All circles stacked on rod A (biggest at bottom, smallest at top)
# GOAL: Move ALL circles to rod C (same order)

# 3 SIMPLE rules:
# 1. Move only 1 circle at a time
# 2. NEVER put bigger circle on smaller circle
# 3. Can only move the topmost circle from any rod

# MINIMUN 2^N-1 MOVES ARE REQUIRED


def hanoi(n, src, aux, dst): # DEFINING THE MAIN FUNCTION
    # n = disks count
    # src = source rod
    # aux = helper rod
    # dst = destination rod

    if n == 1:  # BASE CASE : IF ONLY 1 DISK LEFT
        # DIRECT MOVE(NO RECURSSION NEEDED) - SINGLE FRAME ONLY
        print(f"Move disk 1 from {src} to {dst}")  # PRINT SINGLE DISK MOVE
        return   # EXIT BASE CASE, NO RECURSION NEEDED
    
    hanoi(n-1, src, dst, aux)  # FIRST RECURSSIVE CALL
    print(f"Move disk {n} from {src} to {dst}")  # LARGEST DISK MOVED
    hanoi(n-1, aux, src, dst)  # SECOND RECURSSIVE CALL 


print("=== TOWER OF HANOI n=3 (7 moves) ===")  # EXAMPLE
hanoi(3, 'A', 'B', 'C')  # MAIN FUNCTION CALL

move_count = [0]  # LIST : MUTABLE COUNTER 

def hanoi_count(n, src, aux, dst, count): # DEFINING HANOI COUNTER FUNCTION

    if n == 1:  # BASE CASE 
        count[0] += 1  # COUNT BASE CASE MOVES - INCREMENT MOVE COUNTER
        return  # EXIT BASE CASE
    
    hanoi_count(n-1, src, dst, aux, count)  # RECURSE : MOVE N-1 TO AUX
    hanoi_count(n-1, aux, src, dst, count)  # RECURSE : MOVE N-1 TO DEST


print("\n=== MOVE COUNT n=4 ===")  # PRINTING MESSAGE

move_count[0] = 0  # RESET COUNTER TO 0
hanoi_count(4, 'A', 'B', 'C', move_count)  # COUNT MOVES FOR N=4
print(f"n=4 needs {move_count[0]} moves")  # PRINTING RESULT


print("\n=== COMPLEXITY ===")

print("Time Complexity: O(2^n)")
print("n=1: 1 move, n=2: 3 moves, n=3: 7 moves, n=4: 15 moves")  # PATTERN PROOF
print("Pattern: 2^n - 1 = EXPONENTIAL GROWTH!")  # MATHEMATICAL FORMULA
