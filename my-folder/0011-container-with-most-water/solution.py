class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            best = max(best, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return best
            
        # setcurr = set(currentlvl)
        # arr = list(setcurr)
        # rev = arr[::-1]
        # return rev[0]  
