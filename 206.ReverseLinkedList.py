# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # method: 确定好pre, cur, nxt三个的情况
        cur = head
        pre = None
        
        while cur:
            # attention: store the former next node
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp
            
        return pre
            
        
        # method: without stack, S: O(1)
#         h = head
#         # basic idea: 是所有后一个节点的next指向前一个节点
#         while h:
#             nxt = h.next
#             nxt.next = h
#             h = h.next
        
#         head.next = None
        
#         return h
        
        
        # method: 搭配stack，T：O（N）， S：O（N）
#         if not head:
#             return None
        
#         dummy = ListNode(0, head)
#         d = dummy
#         stack = []
        
#         while d:
#             stack.append(d)
#             d = d.next
        
#         h = stack[-1]
#         for i in range(len(stack)-1):
#             prev = stack.pop()
#             prev.next = stack[-1]
        
#         prev.next = None
            
#         return h
