# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # method 2: 快慢指针，思想：龟兔赛跑，套圈
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
        
        # method1: hashmap/set; T:O(N), S:O(N)
        visit = set()
        while head:
            if head in visit:
                return True
            visit.add(head)
            head = head.next
            
        return False
