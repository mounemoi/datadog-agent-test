import unittest
from mock import Mock

import sample_check

class TestSampleCheck(unittest.TestCase):
    def test_check(self):
        mock_gauge = Mock()
        sample_check.SampleCheck.__init__ = Mock(return_value = None)
        sample_check.SampleCheck.gauge    = mock_gauge

        sample = sample_check.SampleCheck()
        sample.check({})
        mock_gauge.assert_called_with(1)

class TestSampleClass(unittest.TestCase):
    def test_methods(self):
        sample = sample_check.SampleClass()
        self.assertEqual(sample._num, 0)

        value = sample.set(100)
        self.assertEqual(value, 100)
        self.assertEqual(sample._num, 100)

        value = sample.get()
        self.assertEqual(value, 100)
