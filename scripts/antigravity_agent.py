def optimize_rarity(pokemon_data):
    # Ajan burada tüm pokemonlar için nadirlik değerini otonom düzeltir
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
