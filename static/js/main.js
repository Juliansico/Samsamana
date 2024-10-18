// Prevenir la navegación hacia atrás
window.history.forward();
function noBack() {
    window.history.forward();
}

// Ajustar la posición del highlight según el botón activo
document.addEventListener('DOMContentLoaded', function() {
    const navButtons = document.querySelectorAll('.nav-button');
    const highlight = document.getElementById('nav-content-highlight');

    navButtons.forEach((button, index) => {
        button.addEventListener('mouseenter', () => {
            highlight.style.top = `${16 + 54 * index}px`;
        });
    });
});


