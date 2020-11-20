import random

from typing import Any
from typing import List


def quicksort(
    *,
    array: List[Any],
) -> List[Any]:

  if len(array) < 2:
    return array

  index = random.randint(0, len(array) - 1)
  pivot = array[index]
  smaller = [
      item for i, item in enumerate(array) if item <= pivot and i != index
  ]
  larger = [item for item in array if item > pivot]

  return quicksort(array=smaller) + [pivot] + quicksort(array=larger)


range_ = int(1e2)
array = random.sample(range(range_), range_)
print(array)
print(quicksort(array=array))
