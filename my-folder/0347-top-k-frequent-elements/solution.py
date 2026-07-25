class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in seen.items():
            bucket[freq].append(num)
        
        ans = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                ans.append(num)

                if len(ans) == k:
                    return ans
