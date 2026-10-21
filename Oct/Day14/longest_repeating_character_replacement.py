class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_freq = 0
        max_len = 0
        
        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            if counts[ch] > max_freq:
                max_freq = counts[ch]
                
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len
