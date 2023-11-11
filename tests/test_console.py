#!/usr/bin/python3
"""
Unittest for HBNBCommand class
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for HBNBCommand class"""

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        """Assert the output to stdout"""
        with self.subTest():
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_show_command(self):
        """Test the show command in HBNBCommand class"""
        with patch('sys.stdin', StringIO('show BaseModel\n')):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    def test_destroy_command(self):
        """Test the destroy command in HBNBCommand class"""
        with patch('sys.stdin', StringIO('destroy BaseModel\n')):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    def test_update_command(self):
        """Test the update command in HBNBCommand class"""
        with patch('sys.stdin', StringIO('update BaseModel\n')):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                HBNBCommand().cmdloop()
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    def test_do_destroy(self):
        """Test the do_destroy method in HBNBCommand class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().do_destroy("BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    def test_do_update(self):
        """Test the do_update method in HBNBCommand class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().do_update("BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
