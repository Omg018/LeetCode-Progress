class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        sorted_seen = dict(sorted(seen.items(), key=lambda x: x[1], reverse=True))
        arr = list(sorted_seen.keys())
        arrs = arr[0:k]
        return arrs
       
          
