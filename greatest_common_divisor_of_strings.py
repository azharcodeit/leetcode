# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcdLength(a:int, b:int):
            if(a > b):
                return gcdLength(b, a)
            r = b % a
            if(r == 0):
                return a
            return gcdLength(r, a)
        if(str1 + str2 != str2 + str1):
            return ""
        return str1[0:gcdLength(len(str1), len(str2))]