import unittest
from modelmatcher import RateMatrix

import numpy as np

class TestModels(unittest.TestCase):

    def test_sampling(self):
        wag = RateMatrix.instantiate('WAG')
        n = 100
        N = wag.sample_count_matrix(n, [1.0])
        self.assertEqual(int(np.sum(N)), n)
