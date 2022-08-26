# Method: 位运算
# 从1开始，向左移动N位，即变为2的n次方，右边补零；遍历2^32, 看hashmap结构是否和给定的n一样
# T: 0(logN)
# S: 0(logN)

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = collections.Counter(str(n))
        # print(count)
        
        # 从1开始，向左移动N位，即变为2的n次方，右边补零；遍历2^32, 看hashmap结构是否和给定的n一样
        # 左移动运算符：运算数的各二进位全部左移若干位，
        # 由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))
