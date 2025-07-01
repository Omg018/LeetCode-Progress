class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums_set = set(nums)

        # print(nums_set)

        for i in range( len(nums) + 1):
            # print(i)
            if i in nums_set:
                print(i)
            else:
                return i
