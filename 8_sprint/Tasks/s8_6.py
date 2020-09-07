# Create function file_parser.
# If function called with 2 arguments program must count the number of occurrence string in a file,
# if 3 arguments program must replace string in a file to new string
#
# first argument - path to file
# second argument - find string
# third argument - replace string
#
# Example:
# file_parser("file.txt", 'x', 'o') -> Replaced 8 strings
# file_parser("file.txt", 'o') -> Find 8 strings
#
# Please, create class ParsesTest and write unittest for file_parser function uses mock object.

import unittest
from unittest.mock import Mock, patch, mock_open


def file_parser(file_name, a, b=None):
    if b is None:
        return f"Find {open(file_name).read().count(a)} strings"

    else:
        with open(file_name) as file:
            data = file.read()
            data = data.replace(a, b)
        with open(file_name, 'w') as file:
            file.write(data)
        return f"Replaced {open(file_name).read().count(a)} strings"


z = file_parser("file.txt", "4", "t")
print(z)


class ParsesTest(unittest.TestCase):

    def test_file_parser():
        open_mock = mock_open()
        with patch(open_mock, create=True):
            write_to_file("test-data")

        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_called_once_with("test-data")


parserTestSuite = unittest.TestSuite()
parserTestSuite.addTest(unittest.makeSuite(ParsesTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(parserTestSuite)