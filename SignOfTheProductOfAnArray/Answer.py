import math as m 
class Solution(object):
    def arraySign(self, nums):
        product = m.prod(nums)
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
