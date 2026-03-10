def optimize_rarity(pokemon_data):
    # Ajan burada tüm pokemonlar için nadirlik değerini otonom düzeltir
    rarity = pokemon_data.get("rarity_score")
    if rarity is None:
        pokemon_data["rarity_score"] = 10  # Başlangıç değeri ataması
    else:
        # Ajan kendi inisiyatifiyle puanı optimize ediyor
        pokemon_data["rarity_score"] = round(rarity * 1.05, 2)

    return pokemon_data
