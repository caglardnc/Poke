import unittest
import json
import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)
from scripts.constants import POKEMON_DATA_FILE  # noqa: E402


class TestPokemonData(unittest.TestCase):
    def test_all_pokemon_integrity(self):
        # İstisnasız tüm pokemonların verisini kontrol et
        try:
            with open(POKEMON_DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.fail("Veri dosyası kayıp!")

        for pkm in data:
            self.assertIn("name", pkm, "Pokemon ismi eksik!")
            self.assertIn("rarity_score", pkm, "Nadirlik puanı eksik!")
            self.assertTrue(
                pkm["rarity_score"] >= 0,
                "Nadirlik puanı negatif olamaz!"
            )


if __name__ == '__main__':
    unittest.main()
