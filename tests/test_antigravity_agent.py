import unittest
from unittest.mock import patch
import sys
import os
import io

# Add the root project directory to sys.path to allow imports from scripts
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.antigravity_agent import main

class TestAntigravityAgent(unittest.TestCase):

    @patch('scripts.antigravity_agent.os.path.exists')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_missing_data_file(self, mock_stdout, mock_exists):
        # Arrange
        mock_exists.return_value = False
        data_file = "data/pokemon_data.json"

        # Act
        main()

        # Assert
        mock_exists.assert_called_once_with(data_file)
        self.assertEqual(mock_stdout.getvalue().strip(), f"Error: {data_file} not found.")

if __name__ == '__main__':
    unittest.main()
