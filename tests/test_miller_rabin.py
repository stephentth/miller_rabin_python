import logging
import random
import unittest

from miller_rabin.miller_rabin import miller_rabin

DEFAULT_TEST_K = 1
logging.basicConfig(level=logging.DEBUG)

class TestMillerRabin(unittest.TestCase):
    def test_default(self):
        test_cases = [
            # Triva case
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (13, True),
            (25, False),

            # Big
            (1548587, True),
            (1551087, False),
            (15485867, True),  # 1'000'001 st prime
            (15488959, False),
        ]

        for num, expect in test_cases:
            # assert miller_rabin(num, DEFAULT_TEST_K) == expect
            self.assertEqual(miller_rabin(num, DEFAULT_TEST_K), expect, f"{num} should be {expect}")
