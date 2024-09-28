class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filteredChars = [char.lower() for char in s if char.isalnum()]
        return filteredChars == filteredChars[::-1]
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  
print(solution.isPalindrome("race a car"))                       
print(solution.isPalindrome(" "))                                 
