document.addEventListener('DOMContentLoaded', function() {
    const emojiContainer = document.querySelector('.emoji-container');
    const emojis = ['😂', '🤣', '😁', '🤭', '😈', '👻', '💀', '👀', '🐼', '🐸', '🐣', '🐳', '🦀', '🌝', '🌟', '🌈', '🌞', '🥑', '🌽', '🍔', '🍟', '🍺', '🍕', '🍿', '🗿', '💎',
    '🍀', '🚀', '🗽', '🗼', '🏯'];

    // Determine the number of emoji lines based on the viewport width
    const numberOfLines = Math.floor(window.innerWidth / 40);

    for (let i = 0; i < numberOfLines; i++) {
        const line = document.createElement('div');
        line.classList.add('emoji-line');

        const emojiDiv = document.createElement('div');

        // Generate a new set of 30 emojis for each line
        for (let j = 0; j < 30; j++) { // Increased number of emojis to ensure continuous loop
            const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
            const emojiElement = document.createElement('div');
            emojiElement.classList.add('emoji');
            emojiElement.textContent = randomEmoji;
            emojiDiv.appendChild(emojiElement);
        }

        line.appendChild(emojiDiv);
        line.appendChild(emojiDiv.cloneNode(true)); // Clone the emoji div to create a seamless loop
        emojiContainer.appendChild(line);
    }

    const placeholders = document.querySelectorAll('.placeholder');
    const submitButton = document.querySelector('.submit-button');

    // Event listener for input in placeholders
    placeholders.forEach(placeholder => {
        placeholder.addEventListener('input', function() {
            // Check if any placeholder has text
            const anyPlaceholderHasText = Array.from(placeholders).some(input => input.value.trim() !== '');
            
            if (anyPlaceholderHasText) {
                // Apply additional styles when input has text
                submitButton.style.backgroundColor = '#ffffff';
                submitButton.style.color = '#000000'; // Change arrow color
                submitButton.style.boxShadow = '0 0 10px rgba(255, 255, 255, 0.8)'; // Double glow effect
            } else {
                // Revert to default styles
                submitButton.style.backgroundColor = '#2c2c2c';
                submitButton.style.color = 'white'; // Arrow color back to white
                submitButton.style.boxShadow = '0 0 4px rgba(95, 95, 95, 0.5)'; // Default box shadow
            }
        });
    });
});
