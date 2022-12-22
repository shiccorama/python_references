# unit testing can be done using test runner such as unittest or pytest modules
# test case is the smallest unit of testing
# test suite is a collection of test cases
# test report contains success and failures
import unittest

### let's try to use assert without using unittest and returns our own custom report:

# def test_case():
#     assert 5 * 10 == 50, "should be True"

# def test_case_two():
#     assert 5 * 10 == 70, "should be True"

# if __name__ == "__main__":
#     test_case()
#     test_case_two()

#     print(f"all tests finished")

# output:     assert 5 * 10 == 70, "should be True"
#             AssertionError: should be True

### now, let's use unitest module :

class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(50 != 60, "50 isn't equal to 60, so it hast to be True, if it fails, you should see this message")
    
    def test_two(self):
        self.assertEqual(50, 60, "something wrong,val1 should equal val2")

if __name__ == "__main__":
    unittest.main()


# AssertionError: 50 != 60 : something wrong,val1 should equal val2
#----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# FAILED (failures=1)