import unittest


def containsDuplicate(nums):
    return len(set(nums)) != len(nums)


class Test(unittest.TestCase):
    def test_contains_duplicate(self):
        for arr, expected in [
            ([], False),
            ([0], False),
            ([0, 1], False),
            ([0, 3, -5, 3], True),
        ]:
            self.assertEqual(containsDuplicate(arr), expected)


if __name__ == "__main__":
    unittest.main()
