# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # method 2: stack, pop the end of the node for n times
        dummy = ListNode(0, head)
        d = dummy
        stack = []
        while d:
            stack.append(d)
            d = d.next
        
        for i in range(n+1):
            cur = stack.pop()
        cur.next = cur.next.next
        
        return dummy.next

        
        # method 1: 计算linked list长度
        # 设置dummy node
#         dummy = ListNode(val=0, next=head)
#         d = dummy
#         length = 0
#         while d.next:
#             d = d.next
#             length += 1
            
#         if n == length:
#             return head.next
        
#         h = head
#         for i in range(length-n-1):
#             h = h.next
        
#         h.next = h.next.next
        
#         return head
