import time
import random
import unittest

from miller_rabin.miller_rabin import miller_rabin, miller_rabin_mutilprocess

DEFAULT_TEST_K = 4

prime_test_cases = [
    # Trivia case
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (13, True),
    (25, False),
    # Big number
    (1548587, True),
    (1551087, False),
    (15485867, True),  # 1000001 st prime
    (15488959, False),
]


class TestMillerRabin(unittest.TestCase):
    def setUp(self):
        random.seed(0)

    def test_default(self):
        for num, expect in prime_test_cases:
            print("Run test for", num)
            start = time.time()
            self.assertEqual(
                miller_rabin(num, DEFAULT_TEST_K), expect, f"{num} should be {expect}"
            )
            print("Time executed: {:.4f}s".format(time.time() - start))

    def test_multiprocess(self):
        for num, expect in prime_test_cases:
            print("Run test for", num)
            start = time.time()
            self.assertEqual(
                miller_rabin_mutilprocess(num, DEFAULT_TEST_K),
                expect,
                f"{num} should be {expect}",
            )
            print("Time executed: {:.4f}s".format(time.time() - start))
