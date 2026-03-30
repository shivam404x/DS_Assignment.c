# QUEUE USING SINGLY LINKED LIST (O(1) OPERATIONS)

class Node:
    def __init__(self, val):
        self.data = val      # node ka value
        self.next = None     # next node ka link


class MyQueue:

    def __init__(self):
        self.head = None     # front pointer (yaha se remove hota hai)
        self.tail = None     # rear pointer (yaha add hota hai)
        self.count = 0       # total elements


    # ----------- ENQUEUE -----------

    def add(self, value):

        new_node = Node(value)   # naya node bana

        if self.tail is None:
            # agar queue empty hai
            self.head = self.tail = new_node
        else:
            # normal case → last node ke baad add karo
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        print(f"Added: {value}")


    # ----------- DEQUEUE -----------

    def remove(self):

        if self.head is None:
            print("Queue empty (Underflow)")
            return None

        removed_value = self.head.data   # front element

        self.head = self.head.next      # front ko aage shift karo

        # agar last element tha
        if self.head is None:
            self.tail = None

        self.count -= 1
        print(f"Removed: {removed_value}")

        return removed_value


    # ----------- FRONT -----------

    def peek(self):

        if self.head is None:
            return None

        return self.head.data


    # ----------- DISPLAY -----------

    def show(self):

        if self.head is None:
            print("Queue is empty")
            return

        temp = self.head
        items = []

        while temp:
            items.append(str(temp.data))
            temp = temp.next

        print("Queue:", " -> ".join(items), f"(size={self.count})")


# ------------------ DEMO ------------------

print("=== Queue using SLL Demo ===\n")

q = MyQueue()

print("Enqueue:")
q.add(10); q.show()
q.add(20); q.show()
q.add(30); q.show()

print("\nFront element:")
print(q.peek())

print("\nDequeue:")
q.remove(); q.show()

print("\nUnderflow test:")
q.remove(); q.remove(); q.remove()
q.remove()   # empty case

print("\nQueue usage example:")
q.add("A"); q.add("B"); q.add("C")
q.show()
