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

    def prepend(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
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
    
    def popfirst(self):
        if self.size == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True

print("Creating Linked List and performing operations:")
LinkedList = LinkedList(10)
LinkedList.append(20)
LinkedList.append(30)
LinkedList.append(40)
LinkedList.append(50)
LinkedList.append(60)

print("Initial list:")
LinkedList.print_list()

print("List after popping elements:")
popValue = LinkedList.pop()
print("Popped value:", popValue)
LinkedList.print_list()

print("List after popping another element:")
popValue = LinkedList.pop()
print("Popped value:", popValue)
LinkedList.print_list()

print("List after prepending 5:")
LinkedList.prepend(5)
LinkedList.print_list()

print("List after popping first element:")
popValue=LinkedList.popfirst()
print("Popped value:", popValue)
LinkedList.print_list()

print("Value at index 2:",LinkedList.get(2))  # Should return the value at index 2

print("Setting value at index 2 to 99")
LinkedList.set_value(2, 99)
LinkedList.print_list()  # Should show the updated list with 99 at index 2