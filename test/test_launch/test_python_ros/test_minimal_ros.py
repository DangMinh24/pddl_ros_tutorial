#!/usr/bin/python
import rostest
import unittest
                        # * 
                        # * 
class Test_A(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(3+5, 8)
                        # * 
                        # * 
if __name__ == "__main__":
    rostest.rosrun(<package_name>, <test_file_name>, Test_A)
