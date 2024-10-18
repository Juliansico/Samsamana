document.addEventListener('DOMContentLoaded', () => {
    const darkModeButton = document.getElementById('dark-mode-button');

    // Aplicar el tema oscuro basado en el estado almacenado
    const isDarkModeEnabled = localStorage.getItem('dark-mode') === 'true';
    if (isDarkModeEnabled) {
        document.body.classList.add('dark-mode');
    }

    // Alternar el tema oscuro y guardarlo en el almacenamiento local
    darkModeButton.addEventListener('click', () => {
        const isDarkModeEnabled = document.body.classList.toggle('dark-mode');
        localStorage.setItem('dark-mode', isDarkModeEnabled);
    });
});