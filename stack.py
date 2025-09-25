class Stack():
    def __init__(self):
        self.stk=[]

    def length(self):
        return len(self.stk)
    
    def push(self,a):
        self.stk.append(a)
    
    def pop(self):
        if self.length()!=0:
            self.stk.pop()
    
    def peek(self):
        print(self.stk[-1])
    
    def show(self):
        print(self.stk)

s = Stack()
s.push(2)
s.push(3)
s.push(5)
s.pop()
s.peek()
s.show()
    

    