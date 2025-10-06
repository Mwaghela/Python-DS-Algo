class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.size = 1

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1 

LinkedList = LinkedList(10)
LinkedList.append(20)
LinkedList.append(30)
LinkedList.append(40)
LinkedList.append(50)
LinkedList.append(60)

LinkedList.print_list()

popValue = LinkedList.pop()
print("Popped value:", popValue)
LinkedList.print_list()

popValue = LinkedList.pop()
print("Popped value:", popValue)
LinkedList.print_list()

LinkedList.prepend(5)
LinkedList.print_list()