class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
        return row