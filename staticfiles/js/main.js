// Prevenir la navegación hacia atrás
window.history.forward();
function noBack() {
    window.history.forward();
}

// Funcionalidad de la barra lateral y highlight
document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const navButtons = document.querySelectorAll('.nav-button');
    const highlight = document.getElementById('nav-content-highlight');
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    const sidebarToggle = document.getElementById('sidebarToggle');
    const overlay = document.querySelector('.sidebar-overlay');

    // Funcionalidad del highlight
    navButtons.forEach((button, index) => {
        // Highlight al hover
        button.addEventListener('mouseenter', () => {
            highlight.style.top = `${16 + 54 * index}px`;
        });

        // Mantener highlight en la página actual
        if (button.href === window.location.href) {
            highlight.style.top = `${16 + 54 * index}px`;
        }
    });

    // Funcionalidad de la barra lateral
    function toggleSidebar() {
        const isMobile = window.innerWidth <= 767.98;
        
        if (isMobile) {
            sidebar.classList.toggle('expanded');
            overlay.classList.toggle('active');
            
            // Ajustar la posición del highlight cuando la barra lateral está expandida
            if (sidebar.classList.contains('expanded')) {
                highlight.style.opacity = '1';
            } else {
                highlight.style.opacity = '0';
            }
        } else {
            sidebar.classList.toggle('collapsed');
            mainContent.classList.toggle('expanded');
            
            // Ajustar la visibilidad del highlight en modo tablet/desktop
            if (sidebar.classList.contains('collapsed')) {
                highlight.style.opacity = '0';
            } else {
                highlight.style.opacity = '1';
            }
        }
    }

    // Event listeners para la barra lateral
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', toggleSidebar);
    }
    if (overlay) {
        overlay.addEventListener('click', toggleSidebar);
    }

    // Manejar cambios de tamaño de ventana
    window.addEventListener('resize', function() {
        const isMobile = window.innerWidth <= 767.98;
        
        if (!isMobile) {
            overlay.classList.remove('active');
            highlight.style.opacity = sidebar.classList.contains('collapsed') ? '0' : '1';
        }
    });

    // Mantener el highlight visible inicialmente
    if (window.innerWidth > 767.98) {
        highlight.style.opacity = '1';
    }
});