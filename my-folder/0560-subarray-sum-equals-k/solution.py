class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0  
        count = 0
        seen = {0: 1}
        for i, num in enumerate(nums):
            curr_sum += num
            needed = curr_sum - k
            if needed in seen:
                count += seen[needed]
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
        return count
            
            
        # count = 0
        # for start in range(len(nums)):
        #     total = 0
        #     for end in range(start, len(nums)):
        #         total += nums[end]
        #         if total == k:
        #             count += 1
        # return count

      
