class Solution(object):
    def isAnagram(self, s, t):
        count = {}
        countt = {}
        for i in s:
            count[i] = count.get(i,0) + 1
        for j in t:
            countt[j] = countt.get(j,0) + 1
        if count == countt:
            return True
        else:
            return False