class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0 
        right = 0
        for i in range(len(nums)):

            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
            
        return left + 1
        # unique_nums = list(set(nums))
        # nums[:len(unique_nums)] = unique_nums

        # return len(unique_nums)
      
