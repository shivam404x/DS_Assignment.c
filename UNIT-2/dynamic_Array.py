# DYNAMIC ARRAY (RESIZE + POP) 

class DynArray:

    def __init__(self):
        self.count = 0              # current elements count
        self.cap = 4                # starting capacity
        self.data = [None] * self.cap   # initial storage


    def show(self):
        # sirf filled part print karega (unused ignore)
        current = " ".join(str(x) for x in self.data[:self.count])
        print(f"Count: {self.count}, Capacity: {self.cap}, Data: {current}")


    def push(self, val):

        # agar array full ho gaya
        if self.count == self.cap:

            old_data = self.data
            self.cap = self.cap * 2   # capacity double

            self.data = [None] * self.cap   # new bigger array

            # old elements copy karna
            for i in range(self.count):
                self.data[i] = old_data[i]

            print(f"Resized from {self.cap//2} to {self.cap}")

        # next empty index pe value daalna
        self.data[self.count] = val
        self.count += 1


    def remove(self):

        # empty check
        if self.count == 0:
            print("Array empty hai")
            return None

        self.count -= 1
        val = self.data[self.count]   # last element
        self.data[self.count] = None  # slot clear

        print(f"Removed: {val}")
        return val


# ------------------ DEMO ------------------

print("Dynamic Array Demo")

arr = DynArray()

print("\n--- ADD OPERATIONS ---")
arr.push(10); arr.show()
arr.push(20); arr.show()
arr.push(30); arr.show()
arr.push(40); arr.show()   # resize yaha hoga (4 → 8)
arr.push(50); arr.show()

print("\n--- REMOVE OPERATIONS ---")
arr.remove(); arr.show()
arr.remove(); arr.show()
