# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        slow.next = None

        while second != None:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev
        
        first = head
        tail = dummy
        while second != None and first != None:
            tail.next = first
            first = first.next
            tail = tail.next
            tail.next = second
            second = second.next
            tail = tail.next
        
        tail.next = first if first else second
