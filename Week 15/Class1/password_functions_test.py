import unittest

from .password_functions import *

class Test_PW_Functions(unittest.TestCase):

    def test_pw_long_enough_min(self):

        sample_pass = "abcd"
        expected_result = False

        result = validate_password_length(sample_pass)

        self.assertEqual(expected_result, result)