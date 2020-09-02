class Solution:

  def validMountainArray(self, A: List[int]) -> bool:
    i, n = 0, len(A)
    while i + 1 < n and A[i] < A[i + 1]:
      i += 1
    if i == 0 or i == n - 1:
      return False

    while i + 1 < n and A[i + 1] < A[i]:
      i += 1

    return i + 1 == n
