class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_dic and nums_dic[complement] != i:
                return [i, nums_dic[complement]]
            nums_dic[nums[i]] = i