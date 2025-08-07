class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket.values():
                stack.append(char)
            elif char in bracket:
                if not stack or stack[-1] != bracket[char]:
                    return False
                stack.pop()
            else:
                return False
        return not stack