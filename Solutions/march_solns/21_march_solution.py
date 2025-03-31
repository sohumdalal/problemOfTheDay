'''
Problem Of The Day - 3/21/2025

Part 1: Create a Node class and a LinkedList class.

Node Class: 
--- Stores value and next (pointer to next node).

LinkedList Class:
--- append(value): Adds node to the end.
--- prepend(value): Adds node to the beginning.
--- print_list(): Prints all values.

Part 2: Modify LinkedList to support the following:
- insert(value, index): Inserts value at index.
- delete(value): Removes the first occurrence of value.
- reverse(): Reverses the linked list in-place.

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> " if temp.next else "")
            temp = temp.next
        print()

    def insert(self, value, index):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        temp = self.head
        for _ in range(index - 1):
            if not temp:  # If index is out of bounds
                return
            temp = temp.next
        if temp:
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse pointer
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        self.head = prev  # Update head

# Example Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.insert(15, 2)
ll.print_list()  # Output: 5 -> 10 -> 15 -> 20 -> 30
ll.delete(10)
ll.print_list()  # Output: 5 -> 15 -> 20 -> 30
ll.reverse()
ll.print_list()  # Output: 30 -> 20 -> 15 -> 5
