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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def zipper_merge(head1, head2):
    if not head1: return head2
    if not head2: return head1

    p1, p2 = head1, head2
    while p1 and p2:
        p1_next, p2_next = p1.next, p2.next  
        p1.next = p2  # Link first list node to second list node
        if p1_next is None:
            break
        p2.next = p1_next  # Link second list node to first list node
        p1, p2 = p1_next, p2_next  

    return head1  # Head of merged list


# Example Usage:
list1 = LinkedList()
list2 = LinkedList()

for val in [1, 3, 5]:
    list1.append(val)

for val in [2, 4, 6, 8, 10]:
    list2.append(val)

merged_head = zipper_merge(list1.head, list2.head)

# Print merged list
current = merged_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

