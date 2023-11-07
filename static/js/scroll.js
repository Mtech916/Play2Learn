// User Scroll For Navbar
function userScroll() {
  const navbar = document.querySelector('.navbar');
  const toTopBtn = document.querySelector('#to-top');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('navbar-sticky');
      navbar.classList.add('bg-light');
      navbar.classList.add('border-bottom');
      toTopBtn.classList.add('show');
    } else {
      navbar.classList.remove('navbar-sticky');
      navbar.classList.remove('bg-light');
      navbar.classList.remove('border-bottom');
      toTopBtn.classList.remove('show');
    }
  });
}

function scrollToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

document.addEventListener('DOMContentLoaded', userScroll);
document.querySelector('#to-top').addEventListener('click', scrollToTop);
