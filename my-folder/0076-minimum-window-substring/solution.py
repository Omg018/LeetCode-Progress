class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        left = 0
        start = 0

        min_length = float('inf')
        

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)
        formed = 0

        for right in range(len(s)):
            right_char = s[right]
            window[right_char] = window.get(right_char, 0) + 1

            if right_char in need and window[right_char] == need[right_char]:
                formed += 1

            while formed == required:

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        if min_length == float('inf'):
            return ""

        return s[start: start + min_length]
















        # need = {}
        # for ch in t:
        #     need[ch] = need.get(ch, 0) + 1

        # window = {}
        # left = 0

        # formed = 0
        # required = len(need)

        # min_len = float('inf')
        # start = 0

        # for right in range(len(s)):

        #     ch = s[right]
        #     window[ch] = window.get(ch, 0) + 1

        #     if ch in need and window[ch] == need[ch]:
        #         formed += 1

        #     while formed == required:

        #         if right - left + 1 < min_len:
        #             min_len = right - left + 1
        #             start = left

        #         left_char = s[left]
        #         window[left_char] -= 1

        #         if left_char in need and window[left_char] < need[left_char]:
        #             formed -= 1

        #         left += 1

        # if min_len == float("inf"):
        #     return ""

        # return s[start:start + min_len]
        

        # # need = {}
        # # window = {}
        # # left = 0
        # # required = len(need)
        # # formed = 0
        # # for sn in t:
        # #     need[sn] = need.get(sn,0) + 1
        # # for right in range(len(s)):
        # #     window[s[right]] = window.get(s[right], 0) + 1
        # #     while formed == required:

        #     # if window.items() >= need.items(): 


                 
        # # for sw in s:
        # #     window[sw] = window.get(sw,0) + 1
        # # print(need)
        # # print(window)


        # # seen = { }
        # # left = 0
        # # best = 0

        # # for right in range(len(s)):
        # #     if s[right] in seen:
        # #         if seen in t:
        # #             return

        # #         seen.remove(s[right])
        # #         left += 1


        # #     seen.add(s[right])
        # #     best = max(best, right - left + 1)    
