# DOUBLY LINKED LIST 

class Node:
    def __init__(self, data):
        self.data = data   # node ka actual value store hota hai
        self.next = None   # next node ka pointer (aage wala)
        self.prev = None   # previous node ka pointer (piche wala)


class DoublyLinkedList:
    def __init__(self):
        self.head = None   # list ka starting point (initially empty)


    def print_list(self):

        if not self.head:   # agar list empty hai
            print("Empty list")
            return
        
        temp = self.head   # traversal start head se

        forward = []  
        backward = []
        
        # FORWARD TRAVERSAL (head → last)
        while temp:
            forward.append(str(temp.data))  # current node ka data store
            temp = temp.next               # next node pe move
        
        # BACKWARD TRAVERSAL (last → head)
        temp = self.get_last()   # last node find kiya
        while temp:
            backward.append(str(temp.data))  # data store
            temp = temp.prev               # previous node pe move
        
        print("Forward:  " + " <-> ".join(forward))
        print("Backward: " + " <-> ".join(backward[::-1]))  
        # reverse kiya taaki forward se match kare
        print()


    def get_last(self):
        temp = self.head
        
        # last node tak jao (jiska next None ho)
        while temp and temp.next:
            temp = temp.next
        
        return temp   # last node return


    def find_target(self, target):
        temp = self.head
        
        # pura list traverse karo
        while temp:
            if temp.data == target:   # match mila
                return temp           # node return
            temp = temp.next
        
        return None   # agar nahi mila


    def insert_after(self, target, x):

        target_node = self.find_target(target)  # pehle target node find karo
        
        if not target_node:
            print(f"Target {target} not found")
            return False
        
        new_node = Node(x)  # new node create
        
        # pointer connections set kar rahe hain
        new_node.next = target_node.next   # new ka next = target ka next
        new_node.prev = target_node        # new ka prev = target
        
        # agar target ke baad koi node hai to uska prev update karo
        if target_node.next:
            target_node.next.prev = new_node
        
        # finally target ka next new node ban gaya
        target_node.next = new_node
        
        return True


    def delete_at_position(self, pos):

        if not self.head:
            print("Empty list")
            return False
        
        temp = self.head
        
        # given position tak pahuchne ke liye loop
        for i in range(pos):
            if not temp:
                print("Position out of range")
                return False
            temp = temp.next
        
        if not temp:
            print("Position out of range")
            return False
        
        # DELETE LOGIC (pointer update)

        if temp.prev:
            # middle node delete → prev ka next skip kare
            temp.prev.next = temp.next
        else:
            # head delete ho raha hai → head shift karo
            self.head = temp.next
        
        if temp.next:
            # next node ka prev update karo
            temp.next.prev = temp.prev
        
        print(f"Deleted: {temp.data}")
        return True


# ------------------ DEMO ------------------

dll = DoublyLinkedList()

print("=== Doubly Linked List Demo ===\n")

# manually list bana rahe hain: 10 <-> 20 <-> 30
dll.head = Node(10)

dll.head.next = Node(20)
dll.head.next.prev = dll.head   # backward link

dll.head.next.next = Node(30)
dll.head.next.next.prev = dll.head.next  # backward link


print("Initial list:")
dll.print_list()


print("1. Insert 15 after 10:")
dll.insert_after(10, 15)
dll.print_list()


print("2. Insert 25 after 20:")
dll.insert_after(20, 25)
dll.print_list()


print("3. Delete position 1 (15):")
dll.delete_at_position(1)
dll.print_list()


print("4. Delete position 0 (head 10):")
dll.delete_at_position(0)
dll.print_list()


print("5. Delete position 2 (last node):")
dll.delete_at_position(2)
dll.print_list()
