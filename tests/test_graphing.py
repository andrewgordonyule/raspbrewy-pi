import unittest
from time import time

from raspbrewypi import graphing


class TestGraphing(unittest.TestCase):
    def test_graph_plotting(self):
        current_time = time()
        graphing.plot_graph(20, current_time)
        self.assertEqual([20], graphing.y)
        self.assertEqual([current_time], graphing.x)


if __name__ == '__main__':
    unittest.main()
