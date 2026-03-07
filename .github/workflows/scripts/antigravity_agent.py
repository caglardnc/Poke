import json
import os
import antigravity # Otonom kodlama ve analiz motorumuz

def process_all_pokemon():
    print("Antigravity Ajanı Başlatıldı: Tüm Pokémonlar taranıyor...")

    # Verilerinin durduğu dosya yolu (kendi yapına göre burayı güncelleyebilirsin)
    data_file = "data/pokemon_data.json"

    if not os.path.exists(data_file):
        print(f"Hata: {data_file} bulunamadı. Ajan beklemede.")
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        pokemon_list = json.load(f)

    updated_data = []
    
    # Döngü tüm pokemonları istisnasız tarayacak şekilde ayarlandı
    for pkm in pokemon_list:
        # Ajan her bir pokemonun verisini inceliyor ve gerekli düzeltmeleri kendi yapıyor
        optimized_pkm = antigravity.optimize_rarity(pkm)
        updated_data.append(optimized_pkm)

    # Değişiklikler tek seferde tüm pokemonlar için kaydediliyor
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=4)

    print("İşlem Tamam: Tüm Pokémon verileri Antigravity ile otonom olarak güncellendi.")

if __name__ == "__main__":
    process_all_pokemon()
