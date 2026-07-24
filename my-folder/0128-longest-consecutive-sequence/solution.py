class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 in num_set:
                continue
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest,length)
        return longest

