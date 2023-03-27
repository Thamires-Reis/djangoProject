import unittest

from tests import test_views


# Define a test suite
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(test_views('test_successful_login'))
    suite.addTest(test_views('test_unsuccessful_login'))
    suite.addTest(test_views('test_logout'))
    return suite


if __name__ == '__main__':
    # Run the test suite
    runner = unittest.TextTestRunner()
    test_suite = test_suite()
    runner.run(test_suite)
