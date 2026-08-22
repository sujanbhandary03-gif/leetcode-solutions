class Solution:
    def maxArea(self,height):
        maxArea=0
        left=0
        right=len(height)-1
        while left<right:
                width=right-left
                h=min(height[left],height[right])
                curArea=width*h
                maxArea=max(maxArea,curArea)
                if height[left]<height[right]:
                    left+=1
                else:
                    right-=1
        return maxArea