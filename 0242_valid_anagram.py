import unittest


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t


class Test(unittest.TestCase):
    def test_isAnagram(self):
        for a, b, expected in [
            ("a", "b", False),
            ("aba", "aab", True),
            ("aabb", "abbb", False),
            ("anagram", "nagaramm", False),
            ("anagram", "nagaram", True),
            ("aanagram", "nagaram", False),
        ]:
            self.assertEqual(isAnagram(a, b), expected)


if __name__ == "__main__":
    unittest.main()
