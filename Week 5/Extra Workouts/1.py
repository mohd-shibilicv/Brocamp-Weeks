class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        new_node = Node(item)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
            self.tail = new_node

    def displayDoublyLinkedList(self):
        if not self.head:
            print("List is empty")
            return
        
        current_node = self.head

        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def removeAdjascentDuplicates(self): # O(1) Space, O(n) Time
        if not self.head:
            return
        
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

            if current_node.data == current_node.prev.data:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev


doubly_linked_list = DoublyLinkedList()

doubly_linked_list.append(100)
doubly_linked_list.append(300)
doubly_linked_list.append(300)
doubly_linked_list.append(500)
doubly_linked_list.append(500)
doubly_linked_list.append(56)
doubly_linked_list.append(500)
doubly_linked_list.append(500)
doubly_linked_list.append(500)
doubly_linked_list.append(500)
doubly_linked_list.append(500)
doubly_linked_list.append(1000)
doubly_linked_list.append(1000)
doubly_linked_list.append(1000)
doubly_linked_list.append(50)

doubly_linked_list.displayDoublyLinkedList()

doubly_linked_list.removeAdjascentDuplicates()

doubly_linked_list.displayDoublyLinkedList()

print(doubly_linked_list.tail.data)
