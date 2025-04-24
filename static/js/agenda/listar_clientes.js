
function prepararNovoCadastroCliente() {
    const form = document.querySelector('#modal-novo-cliente form');
    form.reset();
    const queryString = window.location.search;
    form.action = `/agenda/clientes/cadastrar/${queryString}`;
    document.getElementById('modal-title-7').textContent = 'Cadastrar Cliente';
}

function carregarDadosCliente(id) {
    fetch(`/agenda/clientes/obter/${id}/`)
        .then(response => response.json())
        .then(data => {

            document.getElementById('id_nome').value = data.nome;
            document.getElementById('id_telefone').value = data.telefone;
            document.getElementById('id_email').value = data.email;
            document.getElementById('id_cliente').value = data.id;

            const queryString = window.location.search;
            const form = document.querySelector('#modal-novo-cliente form');
            form.action = `/agenda/clientes/editar/${data.id}/${queryString}`;

            document.getElementById('modal-title-7').textContent = 'Editar Cliente';
        })
        .catch(error => {
            console.error('Erro ao carregar cliente:', error);
            alert('Erro ao carregar dados do cliente.');

            const modalEl = document.getElementById('modal-novo-cliente');
            if (modalEl) {
                const modal = bootstrap.Modal.getInstance(modalEl);
                modal?.hide();
            }
        });
}
