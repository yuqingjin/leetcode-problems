# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # method: recursion; T:O(N+M)
        if not list1:
            return list2
        
        elif not list2:
            return list1
        
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
            
        
        # method: iteration, T:O(N+M), S:O(1)
#         cur1, cur2 = list1, list2
#         dummy = ListNode(0)
#         d = dummy
        
#         while cur1 and cur2:
#             if cur1.val <= cur2.val:
#                 d.next = cur1
#                 cur1 = cur1.next
#                 d = d.next
#             else:
#                 d.next = cur2
#                 cur2 = cur2.next
#                 d = d.next

#         # finish the uncomplete portion in one of the list        
#         if not cur1 and cur2:
#             d.next = cur2
#         elif not cur2 and cur1:
#             d.next = cur1
            
#         return dummy.next
