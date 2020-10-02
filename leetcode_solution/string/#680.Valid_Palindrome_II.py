# [#680] Valid Palindrome II
#
#
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if self.validPalindrome2(s[i:j]) or self.validPalindrome2(s[(i+1):(j+1)]):
                    return True
                return False
        return True
        
        
    def validPalindrome2(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
                
        return True