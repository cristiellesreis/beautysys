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

//carrossel mobile

const slides = document.querySelector('.slides');
const indicatorsContainer = document.querySelector('.indicators');

document.querySelectorAll('.slide').forEach((slide, index) => {
  const indicator = document.createElement('div');
  indicator.classList.add('indicator');
  indicator.addEventListener('click', () => {
    goToSlide(index);
  });
  indicatorsContainer.appendChild(indicator);
});

let currentIndex = 0;

function goToSlide(index) {
  currentIndex = index;
  const translateValue = -index * 100 + '%';
  slides.style.transform = 'translateX(' + translateValue + ')';

  document.querySelectorAll('.indicator').forEach((indicator, i) => {
    if (i === index) {
      indicator.classList.add('active');
    } else {
      indicator.classList.remove('active');
    }
  });
}

goToSlide(0);

// validação no campo de email

document.getElementById('botao-go').addEventListener('click', function(event) {

  const emailInput = document.getElementById('campo-email');
  const errorMessage = document.getElementById('mensagem-erro');
  const email = emailInput.value;

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailPattern.test(email)) {
      emailInput.classList.add('email-error');
      errorMessage.style.display = 'block';
  } else {
      emailInput.classList.remove('email-error');
      errorMessage.style.display = 'none';
  }
});