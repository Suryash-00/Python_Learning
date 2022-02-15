class Stack:
    def __init__(self):
        self.items=[]

    def push(self, e):
        self.items= [e]+self.items

    def pop(self):
        return self.items.pop()

s= Stack()
s.push(5)
s.push(7)
print(s.pop())