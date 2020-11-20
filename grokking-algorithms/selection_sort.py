import random
import time
from typing import Any
from typing import List


def timeit(f):

  def timed(*args, **kw):

    ts = time.time()
    result = f(*args, **kw)
    te = time.time()

    print(f'func:{f.__name__} args:[{args, kw}] took: {te - ts} sec')
    return result

  return timed


@timeit
def selection_sort(
    *,
    array: List[Any],
) -> List[Any]:
  """Selection sort algorithm.

  Args:
      array (List[Any]): Array to be sorted

  Returns:
      List[Any]: sorted array
  """

  def find_smallest(
      *,
      array: List[Any],
  ) -> List[Any]:
    smallest_index = 0
    smallest = array[smallest_index]
    for i in range(1, len(array)):
      if array[i] < smallest:
        smallest = array[i]
        smallest_index = i
    return smallest_index

  new_array = []
  for i in range(len(array)):
    smallest = find_smallest(array=array)
    new_array.append(array.pop(smallest))

  return new_array


@timeit
def selection_sort_inplace(
    *,
    array: List[Any],
) -> List[Any]:

  for i in range(len(array)):

    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j

    array[i], array[min_index] = array[min_index], array[i]

  return array


range_ = int(1e3)
array = random.sample(range(range_), range_)
print(array)
print(selection_sort(array=array))
print(selection_sort_inplace(array=array))
