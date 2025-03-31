'''
Problem Of The Day - 3/24/2025

Doubly Linked List

Implement a Doubly Linked List (DLL) in Python. Your DLL should have the following features:

Class: Node – please include the following attributes:
--- data: The value stored in the node.
--- prev: A reference to the previous node.
--- next: A reference to the next node.

Class: DoublyLinkedList – please include and test the following methods:
--- append(data): Adds a node with the given data to the end of the list.
--- prepend(data): Adds a node with the given data to the beginning of the list.
--- delete(data): Removes the first occurrence of a node with the given data.
--- search(data): Returns True if the data is found, otherwise False.
--- display_forward(): Prints the elements from head to tail.
--- display_backward(): Prints the elements from tail to head.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Keep track of tail for easy backward traversal

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Empty list
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # Empty list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if not self.head:  # Empty list
            return
        
        temp = self.head
        while temp:
            if temp.data == data:
                if temp == self.head:  # Deleting head
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                elif temp == self.tail:  # Deleting tail
                    self.tail = temp.prev
                    self.tail.next = None
                else:  # Deleting middle node
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

    def display_backward(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" <-> " if temp.prev else "")
            temp = temp.prev
        print()

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return  # No need to sort if empty or single node

        current = self.head.next  # Start from the second node

        while current:
            key = current
            move = current.prev

            while move and move.value > key.value:
                # Swap values instead of re-linking nodes
                move.value, key.value = key.value, move.value
                key = move  # Move key pointer left
                move = move.prev  # Keep moving left

            current = current.next  # Move to the next node to sort


# Example Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)
dll.delete(10)
dll.display_forward()  # Output: 5 <-> 20 <-> 30
dll.display_backward()  # Output: 30 <-> 20 <-> 5
print(dll.search(20))  # Output: True
print(dll.search(100))  # Output: False

print("Before Sorting:")
dll.print_list()

dll.insertion_sort()

print("After Sorting:")
dll.print_list()
