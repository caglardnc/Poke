import json
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

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
    data_file = "data/pokemon_data.json"

    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error(f"{data_file} not found.")
        return
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON from {data_file}.")
        return

    # Apply optimization to each pokemon (Bolt'un batch mantığıyla tek seferde yolluyoruz)
    updated_data = optimize_rarity(data)

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=4, ensure_ascii=False)

    logging.info("Optimization complete. Data saved to data/pokemon_data.json")

if __name__ == "__main__":
    main()