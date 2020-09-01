def power_set(set):
  all_subsets = []
  max = 1 << len(set)
  for i in range(max):
    subset = convert_int_to_set(i, set)
    all_subsets.append(subset)
  return all_subsets


def convert_int_to_set(i, set):
  subset = []
  index = 0
  k = i
  while k > 0:
    if (k & 1) == 1 and set[index] not in subset:
      subset.append(set[index])
    index += 1
    k >>= 1
  return subset


print(power_set([1, 2, 3]))
