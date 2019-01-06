class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p, n = 1, len(nums)
        out = []
        for i in range(n):
            out.append(p)
            p *= nums[i]
        
        p = 1
        for i in range(n-1, -1, -1):
            out[i] *= p
            p *= nums[i]
            
        return out
            
        