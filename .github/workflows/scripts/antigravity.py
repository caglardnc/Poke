def optimize_rarity(pokemon_data):
    # Ajan burada tüm pokemonlar için nadirlik değerini otonom düzeltir
    if "rarity_score" not in pokemon_data:
        pokemon_data["rarity_score"] = 10  # Başlangıç değeri ataması
    else:
        # Ajan kendi inisiyatifiyle puanı optimize ediyor
        pokemon_data["rarity_score"] = round(pokemon_data["rarity_score"] * 1.05, 2)
    
    return pokemon_data
