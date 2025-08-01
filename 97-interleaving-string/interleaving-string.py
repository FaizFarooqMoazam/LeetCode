class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        l = [[False] * (n + 1) for _ in range(m + 1)]
        l[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and l[i-1][j] and s1[i-1] == s3[i+j-1]:
                    l[i][j] = True
                if j > 0 and l[i][j-1] and s2[j-1] == s3[i+j-1]:
                    l[i][j] = True

        return l[m][n]