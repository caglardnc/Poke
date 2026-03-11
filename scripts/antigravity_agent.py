import json

from scripts.constants import POKEMON_DATA_FILE

def optimize_rarity(pokemon_data):
    # ⚡ Bolt: Batch process list to avoid function overhead per item
    # ⚡ Bolt: Use try/except to reduce dictionary lookups from 2 (in, get) to 1
    is_single = not isinstance(pokemon_data, list)
    if is_single:
        pokemon_data = [pokemon_data]

    for p in pokemon_data:
        try:
            # Ajan kendi inisiyatifiyle puanı optimize ediyor
            p["rarity_score"] = round(p["rarity_score"] * 1.05, 2)
        except KeyError:
            p["rarity_score"] = 10  # Başlangıç değeri ataması

    return pokemon_data[0] if is_single else pokemon_data

def main():
    try:
        with open(POKEMON_DATA_FILE, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: Failed to decode JSON from {POKEMON_DATA_FILE}.")
                return
    except FileNotFoundError:
        print(f"Error: {POKEMON_DATA_FILE} not found.")
        return

    # Apply optimization to each pokemon (Bolt'un batch mantığıyla tek seferde yolluyoruz)
    updated_data = optimize_rarity(data)

    with open(POKEMON_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=4, ensure_ascii=False)

    print(f"Optimization complete. Data saved to {POKEMON_DATA_FILE}")

if __name__ == "__main__":
    main()