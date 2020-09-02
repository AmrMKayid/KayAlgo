class Solution:

  def checkIfExist(self, arr: List[int]) -> bool:
    for i, num in enumerate(arr):
      for j in range(i, len(arr)):
        if i != j and (num == arr[j] * 2 or arr[j] == num * 2):
          return True
    return False
