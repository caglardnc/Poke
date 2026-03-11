document.addEventListener('DOMContentLoaded', () => {
    const loadingEl = document.getElementById('loading');
    const errorEl = document.getElementById('error');
    const gridEl = document.getElementById('dashboard-grid');

    async function fetchAndRenderData() {
        try {
            // Fetch the JSON data
            const response = await fetch('../data/pokemon_data.json');

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Sort by rarity_score descending (highest score at the top)
            data.sort((a, b) => b.rarity_score - a.rarity_score);

            // Clear loading state
            loadingEl.classList.add('hidden');
            gridEl.classList.remove('hidden');

            // Render cards
            data.forEach(pokemon => {
                const card = document.createElement('div');
                card.classList.add('card');

                const nameEl = document.createElement('h2');
                nameEl.classList.add('card-title');
                nameEl.textContent = pokemon.name;

                const valueContainer = document.createElement('div');
                valueContainer.classList.add('card-value-container');

                const labelEl = document.createElement('span');
                labelEl.classList.add('card-label');
                labelEl.textContent = 'Rarity Score';

                const valueEl = document.createElement('span');
                valueEl.classList.add('card-value');
                // Format the score to 2 decimal places if it's a number
                valueEl.textContent = typeof pokemon.rarity_score === 'number' ? pokemon.rarity_score.toFixed(2) : pokemon.rarity_score;

                valueContainer.appendChild(labelEl);
                valueContainer.appendChild(valueEl);

                card.appendChild(nameEl);
                card.appendChild(valueContainer);

                gridEl.appendChild(card);
            });

        } catch (error) {
            console.error("Failed to load Pokémon data:", error);
            loadingEl.classList.add('hidden');
            errorEl.classList.remove('hidden');
            errorEl.textContent = `Failed to load data: ${error.message}`;
        }
    }

    // Start fetching data
    fetchAndRenderData();
});