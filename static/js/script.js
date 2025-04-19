const darkModeToggle = document.getElementById('darkModeToggle');

darkModeToggle.addEventListener('click', function() {

    if (document.documentElement.getAttribute("data-bs-theme") == "dark") {
        document.documentElement.setAttribute("data-bs-theme", "light");

    } else {
        document.documentElement.setAttribute("data-bs-theme", "dark");
    }
});

/**
 * Exibe o modal de confirmação de remoção de um item (receita, despesa etc.).
 *
 * @param {string} nome - O nome do item que será exibido no texto do modal (ex: "Salário", "Aluguel").
 * @param {string} actionUrl - A URL para a qual o formulário de remoção será enviado (ex: "/financas/receitas/remover/3/").
 *
 * Funcionalidade:
 * - Atualiza o texto de confirmação no modal com o nome do item.
 * - Define a URL do formulário de remoção.
 * - Abre o modal utilizando a API do Bootstrap.
 */
function abrirModalRemocao(nome, actionUrl) {
    document.getElementById('nome-item').textContent = nome;
    const queryString = window.location.search;
    document.getElementById('form-remocao').action = actionUrl + queryString;
    const modalElement = document.getElementById('modal-remocao');
    const modalBootstrap = new bootstrap.Modal(modalElement);
    modalBootstrap.show();
}