class Solution:
    def maxProduct(self, nums):
        currMax = nums[0]
        currMin = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                currMax, currMin = currMin, currMax

            currMax = max(num, currMax * num)
            currMin = min(num, currMin * num)

            result = max(result, currMax)

        return result