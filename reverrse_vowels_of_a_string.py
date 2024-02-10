# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "hello"
# Output: "holle"

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('aeiouAEIOU')
        left = 0
        right = len(s) - 1
        while left < right:
            if ((s[left] in vowels) and (s[right] in vowels)):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if(s[right] not in vowels):
                right -= 1
            if(s[left] not in vowels):
                left += 1
            
        return ''.join(s)