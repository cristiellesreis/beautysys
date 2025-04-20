
function prepararNovoAgendamento() {
    const form = document.querySelector('#modal-novo-agendamento form');
    form.reset();
    const queryString = window.location.search;
    form.action = `/agenda/cadastrar/${queryString}`;
    document.getElementById('modal-title-7').textContent = 'Cadastrar Agendamento';
}

function carregarDadosAgendamento(id) {
    fetch(`/agenda/obter/${id}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('id_cliente').value = data.cliente.id;
            document.getElementById('id_servico').value = data.servico;

            const formatarData = (dateString) => {
                const date = new Date(dateString);
                return date.toISOString().slice(0, 16);
            };

            document.getElementById('id_data_hora_inicio').value = formatarData(data.data_hora_inicio);
            document.getElementById('id_data_hora_fim').value = formatarData(data.data_hora_fim);
            document.getElementById('id_observacoes').value = data.observacoes || '';
            document.getElementById('id_status').value = data.status;
            document.getElementById('id_agendamento').value = data.id;

            const queryString = window.location.search;
            const form = document.querySelector('#modal-novo-agendamento form');
            form.action = `/agenda/editar/${data.id}/${queryString}`;

            document.getElementById('modal-title-7').textContent = 'Editar Agendamento';
        })
        .catch(error => {
            console.error('Erro ao carregar agendamento:', error);
            alert('Falha ao carregar os dados do agendamento. Tente novamente.');

            const modalEl = document.getElementById('modal-novo-agendamento');
            if (modalEl) {
                const modal = bootstrap.Modal.getInstance(modalEl);
                modal?.hide();
            }
        });
}