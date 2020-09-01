class Solution:

  def setZeroes(self, matrix):
    """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
    rows = len(matrix)
    cols = len(matrix[0])
    zeros = []
    for row in range(rows):
      for col in range(cols):
        if matrix[row][col] == 0:
          zeros.append([row, col])

    for zero in zeros:
      row = zero[0]
      for i in range(cols):
        matrix[row][i] = 0
      col = zero[1]
      for i in range(rows):
        matrix[i][col] = 0
