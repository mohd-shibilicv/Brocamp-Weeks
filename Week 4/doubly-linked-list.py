class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def appendToLast(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
            self.tail = new_node

    def displayDoublyLinkedListInReverseOrder(self):
        if not self.head:
            print("List is empty")
            return

        current_node = self.tail

        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")
    
    def displayDoublyLinkedList(self):
        if not self.head:
            print("List is empty")
            return

        current_node = self.head

        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")


doubly_linked_list = DoublyLinkedList()

doubly_linked_list.appendToLast(100)
doubly_linked_list.appendToLast(400)
doubly_linked_list.appendToLast(500)
doubly_linked_list.appendToLast(600)
doubly_linked_list.appendToLast(700)
doubly_linked_list.displayDoublyLinkedList()
doubly_linked_list.displayDoublyLinkedListInReverseOrder()

def binarySearch(arr, item):
    first = 0
    last = len(arr)
    mid = (first + last) // 2

    for i in range(len(arr)):
        if arr[i] == item:
            return mid
        elif arr[i] > mid:
            first = mid + 1
        else:
            last = mid - 1
