import unittest


def palindrome_permutation(string):
  hash_table = {}
  string = string.lower().replace(" ", "")
  for c in string:
    hash_table[c] = 0
  for c in string:
    hash_table[c] += 1
  one_odd = 0
  # print(hash_table)
  for value in hash_table.values():
    if value % 2 == 1:
      one_odd += 1
  return one_odd <= 1


class Test(unittest.TestCase):
  '''Test Cases'''
  data = [('Tact Coa', True), ('jhsabckuj ahjsbckj', True),
          ('Able was I ere I saw Elba', True),
          ('So patient a nurse to nurse a patient so', False),
          ('Random Words', False), ('Not a Palindrome', False),
          ('no x in nixon', True), ('azAZ', True)]

  def test_pal_perm(self):
    for [test_string, expected] in self.data:
      actual = palindrome_permutation(test_string)
      self.assertEqual(actual, expected)


if __name__ == "__main__":
  unittest.main()
