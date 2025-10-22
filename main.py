class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def __str__(self):
        if self.isEmpty():
            return 'Empty list'
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' -> '.join(elements) + ' -> None'

    def getSize(self):
        return self.size

    def addFistr(self, data):
        new_node = Node(data)
        new_node.next =self.head
        self.head = new_node
        self.size += 1

    def add_Fistr(self, data):
        new_node = Node(data)
        #self.head = new_node
        #self.size += 1
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            return 'This list is already empthy'
        remomeData = self.head.data
        self.head = self.head.next
        self.head -= 1
        return remomeData
    def searcheElement(self, value):
        count = 0
        current = self.head
        if self.isEmpty():
            return 'This lis is aredly empthy'
        else:
            while current:
                if current.data == value:
                    count += 1
                    print(f'{count}: {value}')
                current = current.next
    def searcheMaxElement(self):
        if self.isEmpty():
            return 'This lis is aredly empthy'
        current = self.head
        maxValue = current.data
        while current:
            if current.data > maxValue:
                maxValue = current.data
            current = current.next
        print(maxValue)
list0 = LinkedList()
list0.addFistr(11)
list0.addFistr(12)
list0.addFistr(2)
list0.addFistr(67)
list0.searcheElement(2)
list0.searcheElement(67)
list0.searcheElement(12)
list0.searcheMaxElement()