class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        charSet = set()
        while left < len(s) and right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                ans = max(ans, right-left+1)
                right += 1
            else:
                charSet.remove(s[left])
                left += 1
        return ans