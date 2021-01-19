import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))

import unittest


class Test_A(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(3+5, 8)


if __name__ == '__main__':
    unittest.main()
