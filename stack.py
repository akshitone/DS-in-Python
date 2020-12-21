class Stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        if len(self.stack) <= 0:
            return True

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty(underflow)")
        else:
            self.stack.pop()


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.stack)
stack.pop()
print(stack.stack)
