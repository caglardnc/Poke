import unittest
from scripts.antigravity_agent import optimize_rarity

class TestOptimizeRarity(unittest.TestCase):
    def test_valid_dict(self):
        data = {"name": "Pikachu", "rarity_score": 100}
        result = optimize_rarity(data)
        self.assertEqual(result["rarity_score"], 105.0)

    def test_valid_list(self):
        data = [{"name": "A", "rarity_score": 10}, {"name": "B", "rarity_score": 20}]
        result = optimize_rarity(data)
        self.assertEqual(result[0]["rarity_score"], 10.5)
        self.assertEqual(result[1]["rarity_score"], 21.0)

    def test_missing_key(self):
        data = {"name": "Missing"}
        result = optimize_rarity(data)
        self.assertEqual(result["rarity_score"], 10)

    def test_invalid_type_string(self):
        data = {"name": "BadString", "rarity_score": "high"}
        result = optimize_rarity(data)
        self.assertEqual(result["rarity_score"], 10)

    def test_invalid_type_boolean(self):
        data = {"name": "BadBool", "rarity_score": True}
        result = optimize_rarity(data)
        self.assertEqual(result["rarity_score"], 10)

    def test_invalid_element_in_list(self):
        # A list containing a string and a valid dictionary
        data = ["not a dict", {"name": "Valid", "rarity_score": 10}]
        result = optimize_rarity(data)
        self.assertEqual(result[0], "not a dict")  # Should be unchanged
        self.assertEqual(result[1]["rarity_score"], 10.5)

if __name__ == '__main__':
    unittest.main()
