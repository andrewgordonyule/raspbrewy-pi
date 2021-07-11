import unittest
from unittest.mock import MagicMock, Mock

from raspbrewy_pi import thermometer


class TestThermometer(unittest.TestCase):

    def test_base_dir(self):
        self.assertEqual('/sys/bus/w1/devices/', thermometer.base_dir)

    def test_read_temp(self):
        thermometer.read_temp_raw = Mock(return_value=['YES', 't=21000'])
        #raw_temp_mock = Mock(thermometer.read_temp_raw=Mock(return_value=['YES', 21000]))
        result = thermometer.read_temp()
        self.assertEqual(21, result)


if __name__ == '__main__':
    unittest.main()
