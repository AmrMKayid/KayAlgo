import random

from typing import Any
from typing import List


def sum_(*, array: List[Any]) -> int:

  if len(array) <= 0:
    return 0
  return array[0] + sum_(array=array[1:])


def count_(*, array: List[Any]) -> int:

  if len(array) <= 0:
    return 0
  return 1 + count_(array=array[1:])


def max_(*, array: List[Any]) -> int:

  if len(array) <= 0:
    return 0
  return max(array[0], max_(array=array[1:]))


def binary_search(*, array: List[Any], item: int) -> int:
  return recursive_binary_search(array=array, item=item, low=0, high=len(array))


def recursive_binary_search(*, array: List[Any], item: int, low: int,
                            high: int) -> int:
  if low > high:
    return None

  mid = int((low + high) / 2)
  if array[mid] == item:
    return mid
  elif array[mid] < item:
    return recursive_binary_search(array=array,
                                   item=item,
                                   low=mid + 1,
                                   high=high)
  else:
    return recursive_binary_search(array=array,
                                   item=item,
                                   low=low,
                                   high=mid - 1)


range_ = int(10)
array = random.sample(range(range_), range_)
print(f"Array: {array} | " + f"Sum = {sum_(array=array)} | " +
      f"Count = {count_(array=array)} | " + f"Max = {max_(array=array)}")

range_ = int(10e3)
array = range(range_)
item = random.randint(-range_, range_)
print(f"Array: {array}\n Item: {item}")

print(binary_search(
    array=array,
    item=item,
))
