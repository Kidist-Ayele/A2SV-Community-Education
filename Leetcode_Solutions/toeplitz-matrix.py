class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        traverse = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                diagonal = row - col
                if diagonal in traverse:
                    if matrix[row][col]!=traverse[diagonal]:
                        return False
                else:
                    traverse[diagonal] = matrix[row][col]
        return True
        