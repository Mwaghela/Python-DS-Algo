class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.size = 1

LinkedList = LinkedList(10)

print("LinkedList initialized with head value:", LinkedList.head.value)