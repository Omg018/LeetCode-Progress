class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        nums_set = set(nums)
        missing_arr = []

        for i  in range(1,len(nums) + 1):
            if i not in nums_set:
                missing_arr.append(i)
     
        return missing_arr
