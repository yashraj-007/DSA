class Solution(object):
    def isPalindrome(self, s):
        if s == " ":
            return True
        t = []
        for i in s.lower():
            if i.isalnum():
                t.append(i)
        
        l = 0
        n = len(t)
        r = n - 1

        while l < r:
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1
        return True