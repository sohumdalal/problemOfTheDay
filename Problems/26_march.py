'''
Problem Of The Day - 3/26/2025

Zipper List

Given two singly linked lists, merge them in a zipper-like fashion. 
The first node should come from the first list, the second from the second list, 
the third from the first list, and so on. If one list is longer, attach the remaining nodes 
at the end.

Input:  
--- List1: 1 -> 3 -> 5  
--- List2: 2 -> 4 -> 6 -> 8 -> 10  

Output:  
--- 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 8 -> 10

Constraints:
--- Solve it in-place (modify the existing lists, do not create a new list).
--- The function should return the head of the new merged list.
--- Handle edge cases where one or both lists are empty.

Hint:
---- Use two pointers to traverse both lists and adjust the .next pointers to achieve the zipper effect.

'''

#attempt 1
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return
        self.tail.next = Node(data)
        self.tail = self.tail.next 

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        

myLL = LinkedList()
numList = [1,2,3,4,5]
for val in numList:
    myLL.append(val)
myLL.display()