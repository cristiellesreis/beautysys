// menu mobile
function menuShow() {
  let menuMobile = document.querySelector('.menu-mobile');
  let overlay = document.querySelector('.overlay');

  if (menuMobile.classList.contains('open')) {
      menuMobile.classList.remove('open');
      overlay.classList.remove('show');

      document.querySelector('.icon').classList.add('fa-bars');
      document.querySelector('.icon').classList.remove('fa-x');
  } else {
      menuMobile.classList.add('open');
      overlay.classList.add('show');

      document.querySelector('.icon').classList.add('fa-x');
      document.querySelector('.icon').classList.remove('fa-bars');
  }
}

document.querySelector('.overlay').addEventListener('click', () => {
  const menuMobile = document.querySelector('.menu-mobile');
  const overlay = document.querySelector('.overlay');

  menuMobile.classList.remove('open');
  overlay.classList.remove('show');

  document.querySelector('.icon').classList.add('fa-bars');
  document.querySelector('.icon').classList.remove('fa-x');
});
