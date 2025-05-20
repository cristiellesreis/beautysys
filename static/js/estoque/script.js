function prepararNovoCadastroItemEstoque() {
    const form = document.querySelector('#modal-novo-item form');
    form.reset();
    const queryString = window.location.search;
    form.action = `/estoque/cadastrar/${queryString}`;
    document.getElementById('modal-title-7').textContent = 'Cadastro de Item de Estoque';
}

function carregarDadosItemEstoque(id) {
    fetch(`/estoque/obter/${id}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('id_nome').value = data.nome;
            document.getElementById('id_quantidade').value = data.quantidade;
            document.getElementById('id_preco_aquisicao').value = data.preco_aquisicao;
            document.getElementById('id_preco_venda').value = data.preco_venda;
            document.getElementById('id_data_validade').value = data.data_validade || '';
            document.getElementById('id_item_estoque').value = data.id;

            const queryString = window.location.search;
            const form = document.querySelector('#modal-novo-item form');
            form.action = `/estoque/editar/${data.id}/${queryString}`;

            document.getElementById('modal-title-7').textContent = 'Editar Item de Estoque';
        })
        .catch(error => {
            alert('Erro ao carregar dados do item de estoque.');
            console.error(error);
        });
}
