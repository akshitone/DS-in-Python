class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # 0(1) --> Time Complexity
    def insert_at_start(self, data):
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # 0(1) --> Time Complexity
    def size_of_list(self):
        return self.size

    # 0(N) --> Time Complexity
    def size_another(self):
        current_node = self.head
        size = 0
        if current_node is not None:
            size += 1
            current_node = current_node.next_node
        return size

    # 0(N) --> Time Complexity
    def insert_at_end(self, data):
        self.size += 1
        new_node = Node(data)
        current_node = self.head

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def traverse_list(self):
        current_node = self.head

        while current_node is not None:
            print(str(current_node.data) + " --->", end=" ")
            current_node = current_node.next_node

    def remove(self, data):
        self.size -= 1
        current_node = self.head
        previous_node = None

        if self.head is None:
            return

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        # if we want to remove root node
        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node


linked_list = LinkedList()
linked_list.insert_at_start(10)
linked_list.insert_at_start(20)
linked_list.insert_at_start(30)
linked_list.insert_at_start(50)
linked_list.insert_at_end(40)
print()
linked_list.traverse_list()
print()
print("size of linked list: " + str(linked_list.size_of_list()))
linked_list.remove(10)
linked_list.traverse_list()
print()
print("size of linked list: " + str(linked_list.size_of_list()))
