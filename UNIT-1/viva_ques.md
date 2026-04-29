# VIVA QUESTIONS 

=============================
STACK (ADT)
=============================

1. What is an ADT?
An Abstract Data Type (ADT) is a model that describes data and the operations that can be performed on it, without explaining how they are implemented.
In a stack:
Data → collection of elements  
Operations → push(), pop(), peek(), isEmpty(), size()

2. Why are push and pop O(1)?
Push and pop are constant time operations because they work only at the top of the stack.
They do not require scanning or shifting elements, so the number of steps remains fixed.

3. One real-world use of a stack
A common example is the browser back feature.
Each visited page is stored, and when you press back, the most recent page is removed first (LIFO behavior).

=============================
COMPLEXITY BASICS
=============================

1. Big-O vs Big-Theta
Big-O represents the upper bound (worst-case limit) of an algorithm.  
Big-Theta represents the exact growth rate (tight bound).  
If an algorithm is Θ(f(n)), it is also O(f(n)), but not always the reverse.

2. What does worst-case represent?
Worst-case means the maximum time or space an algorithm may require for any possible input.
For example, in linear search, if the element is at the end or not present, all elements must be checked → O(n).

3. Why complexity matters in real systems
Complexity decides whether a system can handle large inputs efficiently.
For large data:
O(n²) → extremely slow  
O(n log n) → manageable  
Efficient algorithms are necessary for scalable applications.

=============================
RECURSIVE FACTORIAL
=============================

1. What is recursion depth?
Recursion depth is the number of function calls stacked before reaching the base case.
Example: factorial(5) creates 5 calls before stopping.

2. Why does recursion use stack memory?
Each recursive call creates a new stack frame containing variables and return information.
These frames follow the LIFO order (last call finishes first).

3. When is iteration better than recursion?
Iteration is preferred when:
- Input size is large
- Memory usage must be low
- Performance is critical  
Loops avoid stack overflow and reduce overhead.

=============================
FIBONACCI
=============================

1. Why is naive Fibonacci slow?
Because it repeatedly calculates the same values, leading to a large number of duplicate computations.
This results in exponential time complexity.

2. How is memoization related to DP?
Memoization is a Dynamic Programming technique (top-down approach).
It stores results of subproblems so they can be reused instead of recalculated.

3. Space impact of memoization
Memoization requires extra memory of O(n) to store computed results.
It also uses recursion stack space.

=============================
TOWER OF HANOI
=============================

1. Why are moves equal to (2^n - 1)?
The recurrence relation is:
T(n) = 2T(n-1) + 1  
Solving this gives:
T(n) = 2^n - 1

2. What is the recursion tree idea?
At each step, the problem is divided into two smaller subproblems.
This creates a tree structure where the number of calls grows exponentially.

3. Practical risk of exponential algorithms
Exponential algorithms become impractical very quickly.
Even a small increase in input size leads to a huge increase in time and memory usage.

=============================
RECURSIVE BINARY SEARCH
=============================

1. Why is sorted data required?
Binary search works by eliminating half of the search space at each step.
This is only possible when the data is sorted.

2. Best, average, and worst case
Best case → element found immediately (O(1))  
Average case → O(log n)  
Worst case → O(log n)

3. What is Divide and Conquer?
It is a technique where:
- The problem is divided into smaller parts
- Each part is solved recursively
- The results are combined to form the final solution

=============================
FINAL NOTE
=============================
The main goal of studying algorithms is to choose solutions that perform efficiently and scale well with increasing input size.
