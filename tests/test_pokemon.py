import unittest
import json
import os


class TestPokemonData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # İstisnasız tüm pokemonların verisini kontrol et
        data_file = "data/pokemon_data.json"
        if not os.path.exists(data_file):
            raise FileNotFoundError("Veri dosyası kayıp!")

        with open(data_file, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)

    def test_all_pokemon_integrity(self):
        self.assertTrue(len(self.data) > 0, "Veri dosyası boş olamaz!")
        for pkm in self.data:
            self.assertIn("name", pkm, "Pokemon ismi eksik!")
            self.assertIn("rarity_score", pkm, "Nadirlik puanı eksik!")
            self.assertTrue(pkm["rarity_score"] >= 0,
                            "Nadirlik puanı negatif olamaz!")


if __name__ == '__main__':
    unittest.main()
