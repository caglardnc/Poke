import unittest
import json
import os
import sys

# Add root directory to sys.path so scripts can be imported
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

    def test_optimize_rarity_missing_score(self):
        pokemon = {"name": "MissingNo"}
        optimized_pokemon = optimize_rarity(pokemon)
        self.assertEqual(optimized_pokemon["rarity_score"], 10, "Varsayılan nadirlik puanı 10 atanmalı!")

if __name__ == '__main__':
    unittest.main()
