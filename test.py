import unittest

import rust_pyo3

class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(rust_pyo3.sum(1, 2), 3)

    def test_raises(self):
        with self.assertRaises(TypeError):
            rust_pyo3.sum(1, '2')

