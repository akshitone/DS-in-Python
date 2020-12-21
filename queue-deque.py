class Queue:
    def __init__(self):
        self.queue = list()
        self.count = 0

    def size(self):
        return self.count

    def insert_at_start(self, data):
        self.queue.insert(0, data)
        self.count += 1

    def insert_at_end(self, data):
        self.queue.append(data)
        self.count += 1

    def remove_at_start(self):
        if self.count <= 0:
            print("Queue is empty(underflow)")
        else:
            self.queue.pop(0)
            self.count -= 1

    def remove_at_end(self):
        if self.count <= 0:
            print("Queue is empty(underflow)")
        else:
            self.queue.pop()
            self.count -= 1


# in queue only use insert at start and remove at end
queue = Queue()
queue.insert_at_start(10)
queue.insert_at_start(20)
queue.insert_at_start(30)
queue.insert_at_end(40)
print(queue.queue)
queue.remove_at_end()
print(queue.queue)
queue.remove_at_start()
print(queue.queue)
