
# STACK ADT IMPLEMENTATION :

# This is a program implementing the StackADT operations as mentioned.

class StackADT:  # defining the class

    def __init__(self):  # defining the init method
        self.data=[]

    def push(self,x):   # defining the push operation
        self.data.append(x)

    def pop(self):  # defining the pop operation
        if self.isEmpty():   # checking the stack underflow condition   
            return None  
        else:
            return self.data.pop()
        
    def peek(self):  # defining the peek operation
        if self.isEmpty():  # checking the stack underflow condition
            return None  
        else:
            return self.data[-1]
        
    def size(self):   # defining the size function
        return len(self.data)
    
    def isEmpty(self):   # defining the isEmpty function
        return len(self.data)==0
    
    def display(self):   # defining the display function
        return self.data
     

def main():  # defining the main function

    stk=StackADT()  # creating an object of the class

    while True:  # running the while loop till the conditions are True

        # printing the stack ADT menu
        print("-----------------------------------")
        print("StackADT Menu ...")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Display")
        print("6. Size")
        print("7. Exit")
        print("-----------------------------------")

        choice=input("Enter your choice :").strip() # taking the choice as an input from the user

        if choice=="1":   # push operation if choice is 1
            value=input("Enter your value :")
            stk.push(value)
            print(value, " Pushed Successfully !")

        elif choice=="2":   # pop operation if choice is 2
            if stk.isEmpty():
                print("Stack Underflow !")
            else:
                print(stk.pop()," Popped Successfully !")

        elif choice=="3":  # peek operation if choice is 3
            if stk.isEmpty():
                print("Stack Underflow !")
            else:
                print(stk.peek()," Is the TOP of the Stack !")

        elif choice=="4":  # checking the stack is empty or not
            print("Is the Stack Empty ? : \n",stk.isEmpty())

        elif choice=="5":  # displaying the stack if choice is 5
            print("The Stack is :", stk.display())

        elif choice=="6":  # displaying the length of the stack is choice is 6
            print("The length of the stack is : \n",stk.size())

        elif choice=="7":  # exiting the loop if choice is 7
            print("Exiting .... Thanks FOr visiting 🙏 !!!")
            break

        else: # else condition for managing some invalid inputs
            print("Invalid Input !!")
            print("Please enter a valid choice !")


if __name__=="__main__":
    main()    # calling the main function
