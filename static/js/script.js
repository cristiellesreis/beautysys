const darkModeToggle = document.getElementById('darkModeToggle');

if (darkModeToggle) {
    darkModeToggle.addEventListener('click', toggleTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute("data-bs-theme");
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    applyTheme(newTheme);
    localStorage.setItem('theme', newTheme);
}

function applyTheme(theme) {
    document.documentElement.setAttribute("data-bs-theme", theme);
    if (darkModeToggle) {
        darkModeToggle.checked = (theme === 'dark');
    }
}

document.addEventListener('DOMContentLoaded', loadTheme);

function loadTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);
}

function abrirModalRemocao(nome, actionUrl) {
    document.getElementById('nome-item').textContent = nome;
    const queryString = window.location.search;
    document.getElementById('form-remocao').action = actionUrl + queryString;
    const modalElement = document.getElementById('modal-remocao');
    const modalBootstrap = new bootstrap.Modal(modalElement);
    modalBootstrap.show();
}

(function () {
    'use strict';
    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  })();