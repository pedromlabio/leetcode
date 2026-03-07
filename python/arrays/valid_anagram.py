class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #no python nooooo
        if len(s) != len(t): return False
        s1 = sorted(s)
        s2 = sorted(t)
        for i in range(len(s)):
            if s1[i] != s2[i]: return False

        #top 10 worst solutions ever
        #TODO make this better, make it faster, make it use less memory(don't use sort)

        return True