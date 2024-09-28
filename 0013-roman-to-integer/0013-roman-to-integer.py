class Solution(object):
    def romanToInt(self, s):
        arrayOfEquivalents = [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]
        total = 0
        prev_value = 0

        for char in reversed(s):
            for symbol, value in arrayOfEquivalents:
                if char == symbol:
                    if value < prev_value:
                        total -= value
                    else:
                        total += value
                    prev_value = value
                    break
        
        return total

a = Solution()
test = "III"
print(a.romanToInt(test))
test = "LVIII"
print(a.romanToInt(test))
test = "MCMXCIV"
print(a.romanToInt(test))