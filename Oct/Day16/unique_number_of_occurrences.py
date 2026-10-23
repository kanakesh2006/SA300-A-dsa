class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
        seen_freq = set()
        for count in freq.values():
            if count in seen_freq:
                return False
            seen_freq.add(count)
            
        return True
