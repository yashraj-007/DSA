class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == " ":
            return 1
        sett = set()
        l , r = 0, 0
        longest = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            w = (r - l) + 1
            longest = max(longest, w)
            sett.add(s[r])

        return longest