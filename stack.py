def isempty(stk):
    if(len(stk)==0):
        return True
    else:
        return False
def push(stk,ele):
    stk.append(ele)
    print("Element is successfully pushed into the stack!")
def pop(stk):
    if(isempty(stk)):
        print("Stack is empty an you cannot pop the element now!")
    else:
        print("Element is popped out successfully!")
        print("Popped out element is: ",stk.pop())
def peek(stk):
    if(isempty(stk)):
        print("Stack is empty and there is no element to display!")
    else:
        print("Displaying the top element in the stack!")
        print("Top element is: ",stk[-1])
def display(stk):
    if(isempty(stk)):
        print("Stack is empty and there is no element to display!")
    else:
        print("Displaying the stack!")
        print("Stack: ",stk[::-1])
stack=[]
while(True):
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter the operation you want to perform on the stack: "))
    if(choice==1):
        element=int(input("Enter the element you want to push into the stack: "))
        push(stack,element)
    if(choice==2):
        pop(stack)
    if(choice==3):
        peek(stack)
    if(choice==4):
        display(stack)
    elif(choice==5):
        print("You have successfully exited the program!")
        break