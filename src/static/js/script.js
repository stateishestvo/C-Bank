document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('section');

    sections.forEach(section => {
        section.addEventListener('mouseenter', () => {
            section.classList.add('hover');
        });

        section.addEventListener('mouseleave', () => {
            section.classList.remove('hover');
        });
    });
});
