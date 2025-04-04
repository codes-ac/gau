document.addEventListener("DOMContentLoaded", function () {
    let slides = document.querySelectorAll(".banner img");
    let dots = document.querySelectorAll(".dot");
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.remove("active");
            dots[i].classList.remove("active");
            if (i === index) {
                slide.classList.add("active");
                dots[i].classList.add("active");
            }
        });
    }

    // Click event for dots
    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            currentIndex = index;
            showSlide(currentIndex);
        });
    });

    // Auto-slide every 5 seconds
    setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }, 5000);
});

