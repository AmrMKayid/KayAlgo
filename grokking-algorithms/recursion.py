import random


def factorial(
    *,
    number: int,
) -> int:
  """Recursive Factorial Function

  Args:
      number (int): number

  Returns:
      int: factorial of the number
  """
  if number <= 1:
    return 1
  return number * factorial(number=number - 1)


def tail_factorial(
    number: int,
    accumulator: int = 1,
) -> int:
  """Tail Recursive Factorial Function

  Args:
      number (int): [description]
      accumulator (int, optional): [description]. Defaults to 1.

  Returns:
      int: factorial of the number
  """
  if number == 0:
    return accumulator

  return tail_factorial(
      number=number - 1,
      accumulator=accumulator * number,
  )


number = random.randint(0, 10)
print(f"Number: {number} => ({number}!) = {factorial(number=number)}")
print(f"Number: {number} => ({number}!) = {tail_factorial(number=number)}")
