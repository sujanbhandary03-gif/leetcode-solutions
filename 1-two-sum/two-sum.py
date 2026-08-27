class Solution:
    def twoSum(self, nums, target):
        seen={}
        for i,num in enumerate(nums):
            c=target-num
            if c in seen:
                return seen[c],i
            seen[num]=i

