class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def can_form_pairs(max_diff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2  # skip both indices (no reuse)
                else:
                    i += 1
            return count >= p

        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                high = mid
            else:
                low = mid + 1

        return low

