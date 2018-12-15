import unittest


def URLify(string):
    return list(''.join(string).strip().replace(' ', '%20'))


class Test(unittest.TestCase):
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '),
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, expected] in self.data:
            actual = URLify(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
