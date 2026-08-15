class Solution:
    def minOperations(self, s: str) -> int:
        dorivexalu = s
        n = len(s)
        ans = float("inf")

        for r in range(n):
            rotated = s[r:] + s[:r]
            cost = r

            for i in range(n // 2):
                a = ord(rotated[i]) - ord('a')
                b = ord(rotated[n - 1 - i]) - ord('a')

                d = abs(a - b)
                cost += min(d, 26 - d)

            ans = min(ans, cost)

        return ans
