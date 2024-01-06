class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit= limit
        self.items = items
        # self.Stack= [self.items]


    def isEmpty(self):
        return len(self.items)== 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop() 

    def peek(self):
        # if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i, item in enumerate(self.items):
            if item == target:
                return i
        return -1

items = Stack([1,2,3,4,5,6,8])
print(items.peek())
print(items.size())
print(items.search(5))