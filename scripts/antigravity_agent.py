import json
import os

def optimize_rarity(pokemon_data):
    # Ajan burada tüm pokemonlar için nadirlik değerini otonom düzeltir
    if "rarity_score" not in pokemon_data:
        pokemon_data["rarity_score"] = 10  # Başlangıç değeri ataması
    else:
        # Ajan kendi inisiyatifiyle puanı optimize ediyor
        pokemon_data["rarity_score"] = round(pokemon_data["rarity_score"] * 1.05, 2)
    
    return pokemon_data

def main():
    data_file = "data/pokemon_data.json"

    if not os.path.exists(data_file):
        print(f"Error: {data_file} not found.")
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from {data_file}.")
            return

    # Apply optimization to each pokemon
    updated_data = [optimize_rarity(pkm) for pkm in data]

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=4, ensure_ascii=False)

    print("Optimization complete. Data saved to data/pokemon_data.json")

if __name__ == "__main__":
    main()
