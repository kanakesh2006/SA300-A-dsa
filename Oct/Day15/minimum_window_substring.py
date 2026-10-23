class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
            
        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
            
        window = {}
        have = 0
        need = len(target)
        
        res_len = float('inf')
        res_range = (-1, -1)
        left = 0
        
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            
            if ch in target and window[ch] == target[ch]:
                have += 1
                
            while have == need:
                curr_len = right - left + 1
                if curr_len < res_len:
                    res_len = curr_len
                    res_range = (left, right)
                    
                left_char = s[left]
                window[left_char] -= 1
                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1
                left += 1
                
        start, end = res_range
        return s[start : end + 1] if res_len != float('inf') else ""
