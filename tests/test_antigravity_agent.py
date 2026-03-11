import os
import sys
import unittest
from unittest.mock import patch, mock_open
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.antigravity_agent import main

class TestAntigravityAgent(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data='{invalid}')
    @patch('os.path.exists', return_value=True)
    def test_main_invalid_json(self, mock_exists, mock_file, mock_stdout):
        main()
        self.assertIn("Error: Failed to decode JSON from data/pokemon_data.json.", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
