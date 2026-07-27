class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_ch = {}
        left = 0
        max_freq = 0
        best = 0
        whole_len = len(s)

        for right in range(len(s)):
            right_ch = s[right]
            count_ch[right_ch] = count_ch.get(right_ch, 0) + 1 

            max_freq = max(max_freq, count_ch[right_ch])

            print(max_freq)

            window_len = right - left + 1

            if window_len - max_freq > k:
                count_ch[s[left]] -= 1
                left += 1
           
            best = max(best, right-left+1)
            # elif whole_len == max_freq:
            #     best = max(best, window_len)
        return best
        
        # if right - left + 1         
