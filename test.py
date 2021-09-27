import unittest

# Unittest requires organisation into classes
# An assertion is made that the resulf of this addition will equal 15


class testsum(unittest.TestCase):
    def test_list_int(self):

        num_list = [1, 2, 3, 4, 5]
        result = sum(num_list)
        self.assertEqual(result, 15)


# entry point
if __name__ == '__main__':
    unittest.main()
