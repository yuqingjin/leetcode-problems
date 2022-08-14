# Method: hashmap, linked list, left/right pointers
# T: O(N)
# S: O(N)/O(1) for slow/fast pointers method
# fast slow poiter method: first, find the middle of the list; second, reverse the second half; third, merge the two half

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        hashmap = []
        snipper = head
        
        while snipper != None:
            hashmap.append(snipper)
            snipper = snipper.next
        
        
        l, r = 0, len(hashmap) - 1
        dummy = ListNode()
        while l <= r:
            # print(l, r)
            dummy.next = hashmap[l]
            dummy = dummy.next
            # break the link firstly, so that there would be no cycle in list!
            dummy.next = None
            l += 1
            
            # print(l, r)  
            dummy.next = hashmap[r]
            dummy = dummy.next
            dummy.next = None
            r -= 1
