import unittest
from unittest.mock import patch, mock_open, MagicMock
import json

from scripts.antigravity_agent import optimize_rarity, main

class TestAntigravityAgent(unittest.TestCase):

    def test_optimize_rarity_single_dict(self):
        pokemon_data = {"name": "Pikachu", "rarity_score": 100}
        result = optimize_rarity(pokemon_data)
        self.assertEqual(result, {"name": "Pikachu", "rarity_score": 105.0})

    def test_optimize_rarity_single_dict_missing_score(self):
        pokemon_data = {"name": "Missingno"}
        result = optimize_rarity(pokemon_data)
        self.assertEqual(result, {"name": "Missingno", "rarity_score": 10})

    def test_optimize_rarity_list(self):
        pokemon_data = [
            {"name": "Pikachu", "rarity_score": 100},
            {"name": "Missingno"}
        ]
        result = optimize_rarity(pokemon_data)
        self.assertEqual(result, [
            {"name": "Pikachu", "rarity_score": 105.0},
            {"name": "Missingno", "rarity_score": 10}
        ])

    @patch('builtins.print')
    @patch('builtins.open')
    def test_main_file_not_found(self, mock_open_func, mock_print):
        mock_open_func.side_effect = FileNotFoundError()
        main()
        mock_print.assert_called_with("Error: data/pokemon_data.json not found.")

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open, read_data="invalid json")
    def test_main_json_decode_error(self, mock_file, mock_print):
        main()
        mock_print.assert_called_with("Error: Failed to decode JSON from data/pokemon_data.json.")

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "Pikachu", "rarity_score": 100}]')
    @patch('scripts.antigravity_agent.json.dump')
    def test_main_success(self, mock_json_dump, mock_file, mock_print):
        main()
        mock_json_dump.assert_called_once()
        mock_print.assert_called_with("Optimization complete. Data saved to data/pokemon_data.json")

if __name__ == '__main__':
    unittest.main()
