document.addEventListener('DOMContentLoaded', () => {
    // Intercepta clics en enlaces con clase "view-transition"
    document.querySelectorAll('a.view-transition').forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault(); // Evita la navegación inmediata
            const href = event.target.href;

            // Inicia la transición y navega al final
            document.startViewTransition(() => {
                window.location.href = href;
            });
        });
    });
});