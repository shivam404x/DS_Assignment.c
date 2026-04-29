# SINGLY LINKED LIST (CORE OPERATIONS)

class Node:
    def __init__(self, val):
        self.data = val        # node ka value
        self.next = None       # next node ka link


class LinkedList:

    def __init__(self):
        self.head = None       # starting node (initially empty)


    # ----------- DISPLAY -----------

    def show(self):

        if self.head is None:
            print("List empty hai")
            return

        temp = self.head
        items = []

        # head se end tak traversal
        while temp:
            items.append(str(temp.data))   # data collect
            temp = temp.next              # next node pe move

        print("List:", " -> ".join(items))


    # ----------- INSERT AT START -----------

    def add_first(self, value):

        new_node = Node(value)     # naya node bana

        new_node.next = self.head  # new ka next = current head
        self.head = new_node       # head update

        print(f"{value} inserted at start")


    # ----------- INSERT AT END -----------

    def add_last(self, value):

        new_node = Node(value)

        # agar list empty hai
        if self.head is None:
            self.head = new_node
            print(f"{value} inserted at end")
            return

        temp = self.head

        # last node tak jao
        while temp.next:
            temp = temp.next

        temp.next = new_node   # last ke baad new node

        print(f"{value} inserted at end")


    # ----------- DELETE BY VALUE -----------

    def delete(self, key):

        if self.head is None:
            print("List empty hai")
            return False

        # case 1: head delete
        if self.head.data == key:
            self.head = self.head.next
            print(f"{key} deleted (head)")
            return True

        temp = self.head

        # case 2: middle / tail
        while temp.next:

            if temp.next.data == key:
                temp.next = temp.next.next   # skip node
                print(f"{key} deleted")
                return True

            temp = temp.next

        print(f"{key} not found")
        return False


# ------------------ DEMO ------------------

ll = LinkedList()

print("=== Singly Linked List Demo ===\n")

print("Insert at beginning:")
ll.add_first(30)
ll.add_first(20)
ll.add_first(10)
ll.show()

print("\nInsert at end:")
ll.add_last(40)
ll.add_last(50)
ll.show()

print("\nDelete head (10):")
ll.delete(10)
ll.show()

print("\nDelete middle (30):")
ll.delete(30)
ll.show()

print("\nDelete tail (50):")
ll.delete(50)
ll.show()

print("\nDelete non-existing (99):")
ll.delete(99)
ll.show()
