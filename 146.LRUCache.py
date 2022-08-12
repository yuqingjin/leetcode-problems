# Method: hashmap + double linked list
# T: O(1) for put and get
# S: O(capacity)

# for double linked list 
class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # left is the least recently used
        # right is the most recently used
        self.left = self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        
        
    # need to update the most recently used as well
    # in order to do that, we need two more helper functions
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
    
    # remove the current node
    def remove(self, node):
        cur_prev = node.prev
        cur_next = node.next
        cur_prev.next, cur_next.prev = cur_next, cur_prev
        
    # insert node to right most
    # 注意这里的写法
    def insert(self, node):
        cur_node = self.right.prev
        cur_node.next = self.right.prev = node
        node.prev, node.next = cur_node, self.right
        
    
    # first, remove the node from double linked list;
    # second, insert the node to the rightmost of the linked list
    # third, remove the leftmost node from the list
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
