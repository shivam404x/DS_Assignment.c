# STACK USING SLL + PARENTHESES VALIDATION

class Node:
    def __init__(self, val):
        self.data = val        # node ka value
        self.next = None       # next node ka link


class LinkedStack:

    def __init__(self):
        self.head = None       # stack ka top (head hi top hai)


    # ----------- PUSH -----------

    def push(self, value):

        new_node = Node(value)       # naya node bana

        new_node.next = self.head    # new ka next = current top
        self.head = new_node         # top update

    
    # ----------- POP -----------

    def pop(self):

        if self.head is None:
            return None              # stack empty

        removed = self.head.data     # top value store
        self.head = self.head.next   # top shift

        return removed


    # ----------- PEEK -----------

    def peek(self):

        if self.head is None:
            return None

        return self.head.data        # current top


    # ----------- EMPTY CHECK -----------

    def empty(self):
        return self.head is None


# ----------- PARENTHESES CHECK -----------

def check_parentheses(exp):

    st = LinkedStack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in exp:

        # closing bracket mila
        if ch in pairs:

            top = st.pop()   # last opening nikalo

            # agar mismatch ya empty
            if top != pairs[ch]:
                return False

        else:
            # opening bracket push karo
            st.push(ch)

    # agar end me stack empty hai → valid
    return st.empty()


# ------------------ DEMO ------------------

print("=== Stack using SLL Demo ===\n")

stk = LinkedStack()

print("Push operations:")
stk.push(10); print("Pushed 10")
stk.push(20); print("Pushed 20")
stk.push(30); print("Pushed 30")

print("Top:", stk.peek())

print("Pop:", stk.pop())
print("Top after pop:", stk.peek())


print("\nParentheses Check:")

tests = [
    "()", "(())", "({[]})",
    ")(", "(()", "([)]",
    "", "abc", "((()))"
]

for t in tests:
    print(f"{t} -> {check_parentheses(t)}")
