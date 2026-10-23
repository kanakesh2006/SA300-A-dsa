class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
            
        for ch in t:
            if ch not in counts or counts[ch] == 0:
                return ch
            counts[ch] -= 1
            
        return ""
