class Stack:  
    def __init__(self): 
        self.stck = [] 
    def push(self, data): 
        self.stck.append(data) 
    def pop(self): 
        self.stck.pop()
    def traverse(self): 
        for i in self.stck: 
            print(str(i)+' ')
        print('\n')

s1 = Stack()
print('Pushing elements into the stack')
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)

print('Traversing the stack')
s1.traverse()

print('Popping elements from the stack')
s1.pop()
s1.pop()

print('Traversing the stack')
s1.traverse()

        
