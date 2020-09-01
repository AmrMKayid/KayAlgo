import math


def isPrime(n):
  if n == 2:
    return True
  elif n == 1 or (n & 1) == 0:
    return False

  for i in range(2, math.ceil(math.sqrt(n)) + 1):
    if (n % i) == 0:
      return False

  return True


p = int(input())
for i in range(0, p):
  print("Prime" if (isPrime(int(input()))) else "Not prime")
