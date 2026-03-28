# STACK ADT IMPLEMENTATION USING LIST :-

# Stack = LIFO (Last In First Out)

class Stack:

    def __init__(self):
        self.items = []

    # push operation
    def push(self, value):
        self.items.append(value)

    # pop operation
    def pop(self):
        if self.empty():
            return None
        return self.items.pop()

    # top element dekhna
    def top(self):
        if self.empty():
            return None
        return self.items[-1]

    # stack empty hai ya nahi
    def empty(self):
        return len(self.items) == 0

    # total elements
    def length(self):
        return len(self.items)

    # pura stack print
    def show(self):
        return self.items


# ------------------ MENU DRIVER ------------------

def start():

    s = Stack()

    while True:

        print("\n====== STACK MENU ======")
        print("1. Push")
        print("2. Pop")
        print("3. Top")
        print("4. Check Empty")
        print("5. Show Stack")
        print("6. Size")
        print("7. Exit")

        ch = input("Choose option: ").strip()

        if ch == "1":
            val = input("Enter value: ")
            s.push(val)
            print("✔ Value added")

        elif ch == "2":
            removed = s.pop()
            if removed is None:
                print("❌ Stack is empty (Underflow)")
            else:
                print(f"✔ Removed: {removed}")

        elif ch == "3":
            t = s.top()
            if t is None:
                print("❌ Stack is empty")
            else:
                print(f"Top element: {t}")

        elif ch == "4":
            print("Empty hai kya?", s.empty())

        elif ch == "5":
            print("Stack content:", s.show())

        elif ch == "6":
            print("Total elements:", s.length())

        elif ch == "7":
            print("Program closed 👍")
            break

        else:
            print("⚠ Invalid option, try again")


# program start
if __name__ == "__main__":
    start()
