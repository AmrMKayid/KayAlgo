import unittest


def string_compression(string):
  count = 1
  n = len(string)
  new_string = ''
  for i in range(n):
    if not (i + 1 < n and string[i] == string[i + 1]):
      new_string += string[i] + str(count)
      count = 0
    count += 1

  return min(string, new_string, key=len)


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [('aabcccccaaa', 'a2b1c5a3'), ('abcdef', 'abcdef')]

  def test_string_compression(self):
    for [test_string, expected] in self.data:
      actual = string_compression(test_string)
      self.assertEqual(actual, expected)


if __name__ == "__main__":
  unittest.main()
