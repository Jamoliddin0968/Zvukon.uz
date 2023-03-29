document.addEventListener("DOMContentLoaded", function () {
    /* ==============================================
       HERO SLIDER
    ============================================== */
    var heroSlider = new Swiper("#hero-slider", {
        parallax: true,
        speed: 800,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        pagination: {
            el: ".swiper-pagination",
            type: "custom",
            renderCustom: function (swiper, current, total) {
                return (
                    ' <span class="h2">' +
                    ("0" + current).slice(-2) +
                    "</span> " +
                    ' <span class="swiper-divider">/</span> ' +
                    ' <span class="text-muted">' +
                    ("0" + total).slice(-2)
                );
                +"</span> ";
            },
        },
    });

    /* ==============================================
    NEW ARRIVALS SLIDER
  ============================================== */
    var newArrivals = new Swiper("#newArrivals", {
        loop: true,
        spaceBetween: 25,
        breakpoints: {
            640: {
                slidesPerView: 2,
            },
            768: {
                slidesPerView: 4,
            },
            1024: {
                slidesPerView: 5,
            },
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
    });

    /* ==============================================
        FEATURED PRODUCTS SLIDER
    ============================================== */
    var featuredProducts = new Swiper("#featuredProducts", {
        loop: true,
        breakpoints: {
            640: {
                slidesPerView: 2,
            },
            768: {
                slidesPerView: 4,
            },
            1024: {
                slidesPerView: 5,
            },
        },
        spaceBetween: 25,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
    });

    /* ==============================================
        SIMILAR PRODUCTS SLIDER
    ============================================== */
    var similarItemsSlider = new Swiper("#similarItemsSlider", {
        loop: true,
        breakpoints: {
            640: {
                slidesPerView: 2,
            },
            768: {
                slidesPerView: 3,
            },
            1024: {
                slidesPerView: 4,
            },
        },
        spaceBetween: 25,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
    });

    /* ==============================================
    DETAILS SLIDER THUMBNAILS
  ============================================== */
    var galleryThumbs = new Swiper("#detailSliderThumb", {
        direction: "horizontal",
        breakpoints: {
            768: {
                direction: "vertical",
            },
        },
        spaceBetween: 10,
        slidesPerView: 4,
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
    });

    /* ==============================================
        DETAILS SLIDER
      ============================================== */
    var detailSlider = new Swiper("#detailSlider", {
        spaceBetween: 10,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        thumbs: {
            swiper: galleryThumbs,
        },
    });

    /* ==============================================
    GLIGHTBOX
  ============================================== */
    const lightbox = GLightbox({
        touchNavigation: true,
        loop: true,
        autoplayVideos: true,
    });
});

/* ==============================================
        INC & DEC BUTTONS
    ============================================== */

function increase(x) {
    var inputVal = x.previousElementSibling;
    inputVal.value++;
}
function decrease(x) {
    var inputVal = x.nextElementSibling;
    if (inputVal.value > 1) {
        inputVal.value--;
    }
}
