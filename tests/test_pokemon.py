import unittest
import json
import os
import sys

# Ensure scripts directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.antigravity_agent import optimize_rarity

class TestPokemonData(unittest.TestCase):
    def test_all_pokemon_integrity(self):
        # İstisnasız tüm pokemonların verisini kontrol et
        data_file = "data/pokemon_data.json"
        self.assertTrue(os.path.exists(data_file), "Veri dosyası kayıp!")
        
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for pkm in data:
            self.assertIn("name", pkm, "Pokemon ismi eksik!")
            self.assertIn("rarity_score", pkm, "Nadirlik puanı eksik!")
            self.assertTrue(pkm["rarity_score"] >= 0, "Nadirlik puanı negatif olamaz!")

    def test_optimize_rarity_single_object(self):
        # Test passing a single dictionary to optimize_rarity
        pokemon = {"name": "Pikachu", "rarity_score": 100}
        result = optimize_rarity(pokemon)

        # Verify it returns a single dictionary, not a list
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "Pikachu")
        # Verify rarity_score was updated (100 * 1.05 = 105.0)
        self.assertEqual(result["rarity_score"], 105.0)

    def test_optimize_rarity_single_object_missing_score(self):
        # Test passing a single dictionary with missing rarity_score
        pokemon = {"name": "Mew"}
        result = optimize_rarity(pokemon)

        # Verify it returns a single dictionary
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "Mew")
        # Verify missing score falls back to 10
        self.assertEqual(result["rarity_score"], 10)

if __name__ == '__main__':
    unittest.main()
