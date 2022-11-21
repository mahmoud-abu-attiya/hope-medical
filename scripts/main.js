var swiper = new Swiper(".mySwiper", {
   spaceBetween: 30,
   effect: "fade",
   navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
   },
   loop: true,
   autoplay: true,
});

var swiperTwo = new Swiper(".mySwiper2", {
   spaceBetween: 30,
   autoplay:true,
   loop:true,
   pagination: {
      el: ".swiper-pagination",
   },
});

function setHeight() {
   let nav = document.querySelector("header");
   let header = document.querySelector(".header");
   let height = this.innerHeight - nav.offsetHeight;
   header.style.height = `${height}px`;
   header.style.marginTop = `${nav.offsetHeight}px`;
   console.log(nav.offsetHeight);
   console.log(this.innerHeight);
}
setHeight();
window.addEventListener("resize", setHeight());
