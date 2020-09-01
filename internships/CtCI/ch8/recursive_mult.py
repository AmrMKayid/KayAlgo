def recursive_mult(n1, n2):
  bigger = n2 if n1 < n2 else n1
  smaller = n1 if n1 < n2 else n2
  return min_product(smaller, bigger)


def min_product(smaller, bigger):
  if smaller == 0:
    return 0
  elif smaller == 1:
    return bigger
  s = smaller >> 1
  half_prod = min_product(s, bigger)

  return half_prod + half_prod if smaller % 2 == 0 else half_prod + half_prod + bigger


print(recursive_mult(1 << 1024, 1 << 512))
