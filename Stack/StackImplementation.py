#Stack implementation through list first using the functions then with class

List1 = [1,2,3,4,5]

''' it is a stack here we will do operations like 
->push 
->pop
->top 
->isempty
->isfull
->size
'''

List1.append(6)         #PUSHING ELEMENTS TO THE STACK AS IT FOLLOWS THE PRINCIPLE OF LAST IN FIRST OUT 
print(List1)

List1.pop()             #REMOVING ELEMENT FROM STACK 
print(List1)

print(List1[-1])        #getting the top element of the stack 

# if 



#second method of implementing stack through class

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        return f"yourn updated stack is {self.stack}"
    
    def pop(self):
        if len(self.stack) == 0:
            return "stack is empty"
        else:
            self.stack.pop()
            return f'yourn updated stack is {self.stack}'
        
    def top(self):
        if len(self.stack) == 0:
            return "stack is empty"
        else:
            return self.stack[-1]
        
    def isempty(self):
        return len(self.stack) == 0
    
    def isfull(self):
        return False
    
    def size(self):
        return len(self.stack)
    
stack1 = Stack()
print(stack1.push(1))
print(stack1.push(2))
print(stack1.push(3))
print(stack1.pop())
print(stack1.top())
print(stack1.isempty())
print(stack1.isfull())
print(stack1.size())

