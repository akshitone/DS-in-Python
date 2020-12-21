class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def size(self):
        return self.count

    def insert_at_start(self, data):
        new_node = Node(data)
        self.count += 1
        if self.head == None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        self.count += 1
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def insert_at_position(self, data, position):
        position -= 1
        if position < self.size():
            if position == 0:
                self.insert_at_start(data)
            else:
                cnt = 0
                new_node = Node(data)
                self.count += 1
                current_node = self.head
                while cnt < (position-1):
                    current_node = current_node.next_node
                    cnt += 1
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
        else:
            print("Wrong position")

    def traverse(self):
        current_node = self.head
        print()
        if self.head == None:
            print("Circular linked list is empty")
        else:
            while current_node is not None:
                print(str(current_node.data) + "-->", end="")
                current_node = current_node.next_node

    def remove_at_first(self):
        self.count -= 1
        current_node = self.head
        self.head = self.head.next_node
        del(current_node)

    def remove_at_end(self):
        self.count -= 1
        last_node = None
        current_node = self.head
        while current_node.next_node is not None:
            last_node = current_node
            current_node = current_node.next_node

        last_node.next_node = None
        del(current_node)

    def remove_at_position(self, position):
        position -= 1
        if position < self.size():
            if position == 0:
                self.remove_at_first()
            elif position == (self.size()-1):
                self.remove_at_end()
            else:
                cnt = 0
                last_node = None
                current_node = self.head
                while cnt < position:
                    last_node = current_node
                    current_node = current_node.next_node
                    cnt += 1
                last_node.next_node = current_node.next_node
                del(current_node)
        else:
            print("Wrong position")


linkedlist = LinkedList()
linkedlist.insert_at_start(10)
linkedlist.insert_at_start(20)
linkedlist.insert_at_start(30)
linkedlist.insert_at_start(15)
linkedlist.insert_at_end(40)
linkedlist.traverse()
linkedlist.insert_at_position(5, 4)
linkedlist.traverse()
linkedlist.remove_at_first()
linkedlist.remove_at_end()
linkedlist.remove_at_position(3)
linkedlist.traverse()
