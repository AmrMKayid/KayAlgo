import random
from typing import Any
from typing import List


def binary_search(
    *,
    array: List[Any],
    item: Any,
) -> int:
  """Binary search algorithm.

  Runtime: O(log(n))

  Args:
      array (List[Any]): Sorted array
      item (Any): item to be searcher

  Returns:
      int: index of the item if exist
  """

  low = 0
  high = len(array) - 1

  while low <= high:
    middle = int((low + high) / 2)
    guess = array[middle]

    if guess == item:
      return middle

    if guess < item:  ## Too low
      low = middle + 1
    else:  ## Too high
      high = middle - 1

  return None


range_ = int(10e9)
array = range(range_)
item = random.randint(-range_, range_)
print(f"Array: {array}\n Item: {item}")

print(binary_search(
    array=array,
    item=item,
))
