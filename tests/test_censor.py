import unittest

from profanity import censor_profanity


class TestCensor(unittest.TestCase):

    def test_censor_false_small(self):
        self.assertEqual(censor_profanity("hello"), "hello", "Program censored unnecesarily")


if __name__ == '__main__':
    unittest.main()
