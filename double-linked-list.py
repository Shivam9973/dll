class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        current_node = self.head.next
        length = 0
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length

    def display(self):
        elems = []
        current_node = self.head.next
        while current_node != None:
            elems.append(current_node.data)
            current_node = current_node.next
        print(f"Linked list: {elems}")

    def get(self, index):
        if index >= self.length() or index < 0:
            return "<ERROR: 'Get': Index out of range !!! >"
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def delete(self, index):
        if index >= self.length() or index < 0:
            print("\n<ERROR: 'Delete': Index out of range !!! >")
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

mylist = LinkedList()
mylist.display()  # prints "Linked list: []"
print(f"Length of list: {mylist.length()}")  # prints "Length of list: 0"

mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.display()  # prints "Linked list: [10, 20, 30]"
print(f"Length of list: {mylist.length()}")  # prints "Length of list: 3"

print(f"Data at index 1: {mylist.get(1)}")  # prints "Data at index 1: 20"

mylist.delete(1)
mylist.display()  # prints "Linked list: [10, 30]"
print(f"Length of list: {mylist.length()}")  # prints "Length of list: 2"