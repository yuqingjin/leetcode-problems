# Method 2: hashmap + ordered dict
from collections import OrderedDict, defaultdict
class LFUCache:

    def __init__(self, capacity: int):
        
        # key:key, value:freq
        self.key_to_freq = {}
        
        # key:freq, value:LRU cache
        self.frequency = defaultdict(OrderedDict)
        self.minfreq = 0
        self.cap = capacity
    
    # update both the LRU and LFU
    # 1. remove from the old frequency d-linked list
    # 2. append to frequency + 1 d-linked list
    # 3. update the min-frequency
    def get(self, key: int) -> int:
        if key in self.key_to_freq:
            freq = self.key_to_freq[key]
            
            # remove from the old frequency d-linked list
            # return the value of this key
            value = self.frequency[freq].pop(key)
            
            # update min frequency
            if self.minfreq == freq and not self.frequency[freq]:
                self.minfreq += 1 
            
            # append to (frequency + 1) d-linked list
            self.frequency[freq + 1][key] = value
            self.key_to_freq[key] += 1
            return value
        
        return -1
    
    # two cases: 1.key alredy in dict; 2.key not in dict yet
    # for case 2, should evict the LFU if equal the capacity
    # Attention: evict first, then append new key to dict (according to the LFU cache rule)
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        # Case1: key alredy in dict
        # update both LRU and LFU cache and update the value
        if key in self.key_to_freq:
            freq = self.key_to_freq[key]
            # pop out the original node from LRU cache
            self.frequency[freq].pop(key)
            
            # update the min frequency
            if self.minfreq == freq and not self.frequency[freq]:
                self.minfreq += 1 
            
            # update the original node
            self.frequency[freq + 1][key] = value
            self.key_to_freq[key] += 1
                
        else:
            if len(self.key_to_freq) == self.cap:
                k, v = self.frequency[self.minfreq].popitem(last=False)
                self.key_to_freq.pop(k)
            
            self.key_to_freq[key] = 1
            self.frequency[1][key] = value
            # bcs the new append node has never appeared before
            self.minfreq = 1

            
# Method 1: hashmap + double linked list
# from collections import defaultdict
# class Node:
#     def __init__(self, key= None, value=None):
#         self.key = key
#         self.value = value
#         self.prev = self.next = None
#         self.freq = 1

# # 单独建出来double linked list的data structure是为了直接放在frequency的defaultdict中，因为frequency字典对应的value应该是double linked list 而不是node
# class DLinkedList:
#     def __init__(self):
#         self.left = self.right = Node()
#         self.left.next, self.right.prev = self.right, self.left
#         self.size = 0
        
#     # remove node from LRU
#     def remove(self, node: Node = None):
#         if self.size == 0:
#             return
#         if node is None:
#             node = self.left.next
#         pre, nxt = node.prev, node.next
#         pre.next, nxt.prev = nxt, pre
#         self.size -= 1
#         return node
        
#     # append node to the most right of LRU
#     def append(self, node):
#         cur = self.right.prev
#         cur.next = self.right.prev = node
#         node.prev, node.next = cur, self.right
#         self.size += 1
        
# class LFUCache:

#     def __init__(self, capacity: int):
#         self.key_to_node = {}
#         self.frequency = defaultdict(DLinkedList)
#         self.minfreq = 0
#         self.cap = capacity
    
#     # update both the LRU and LFU
#     # 1. remove from the old frequency d-linked list
#     # 2. append to frequency + 1 d-linked list
#     # 3. update the min-frequency
#     def get(self, key: int) -> int:
#         if key in self.key_to_node:
#             node = self.key_to_node[key]
#             freq = node.freq
            
#             # remove from the old frequency d-linked list
#             self.frequency[freq].remove(node)
            
#             # update min frequency
#             if self.minfreq == freq and self.frequency[freq].size == 0:
#                 self.minfreq += 1 
            
#             # 更新node自己的freq
#             node.freq += 1
#             # append to (frequency + 1) d-linked list
#             self.frequency[freq + 1].append(node)
#             return node.value
        
#         return -1
    
#     # two cases: 1.key alredy in dict; 2.key not in dict yet
#     # for case 2, should evict the LFU if equal the capacity
#     # Attention: evict first, then append new key to dict (according to the LFU cache rule)
#     def put(self, key: int, value: int) -> None:
#         if self.cap == 0:
#             return
        
#         # Case1: key alredy in dict
#         # update both LRU and LFU cache and update the value
#         if key in self.key_to_node:
#             node = self.key_to_node[key]
#             freq = node.freq
#             self.frequency[freq].remove(node)
            
#             # update the min frequency
#             if self.minfreq == freq and self.frequency[freq].size == 0:
#                 self.minfreq += 1 
            
#             node.freq += 1
#             node.value = value
#             self.frequency[freq + 1].append(node)
                
#         else:
#             if len(self.key_to_node) == self.cap:
#                 dlist = self.frequency[self.minfreq]
#                 delete_node = dlist.left.next
#                 dlist.remove(delete_node)
#                 # print(self.key_to_node.keys())
                
#                 del self.key_to_node[delete_node.key]
            
#             node = Node(key, value)
#             self.key_to_node[key] = node
#             self.frequency[1].append(node)
#             # bcs the new append node has never appeared before
#             self.minfreq = 1

                
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
