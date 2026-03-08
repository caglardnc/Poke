import unittest
import json
import os

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

if __name__ == '__main__':
    unittest.main()
