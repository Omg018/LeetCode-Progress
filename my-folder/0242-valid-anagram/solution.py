class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        seen2 = {}
        for i in s:
            seen[i] = seen.get(i, 0) + 1
        for j in t:
            seen2[j] = seen2.get(j, 0) + 1
        if seen == seen2:
            return True
        else:
            return False
