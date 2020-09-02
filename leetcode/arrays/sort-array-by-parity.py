class Solution:

  def sortArrayByParity(self, A: List[int]) -> List[int]:
    even = 0
    for i in range(len(A)):
      if A[i] % 2 == 0:
        A[even], A[i] = A[i], A[even]
        even += 1
    return A
