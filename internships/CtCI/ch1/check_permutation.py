import unittest


def check_permutation(str1, str2):
  if len(str1) != len(str2):
    return False

  for c in str1:
    if c not in str2:
      return False
  return True


class Test(unittest.TestCase):
  dataT = [('abc', 'acb'), ('qwert', 'wertq'), ('', '')]
  dataF = [('acb', 'asd'), ('acv', '')]

  def test_check_permutation(self):
    # true check
    for test_strings in self.dataT:
      result = check_permutation(*test_strings)
      self.assertTrue(result)

    # false check
    for test_strings in self.dataF:
      result = check_permutation(*test_strings)
      self.assertFalse(result)


if __name__ == '__main__':
  unittest.main()
