import unittest


def is_unique(string):
    if len(string) > 128:
        return False

    letters = [False] * 128
    for char in string:
        val = ord(char)
        if letters[val]:
            return False
        letters[val] = True

    return True


class Test(unittest.TestCase):
    dataT = ['abcd', 's4fad', '']
    dataF = ['abbcc', '23ds2', 'hb 627jh=j ()']

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
