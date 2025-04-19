/**
 * Função responsável por preparar o formulário de cadastro de uma nova receita.
 * Limpa os campos do formulário, ajusta a URL de ação com base na query string da URL atual,
 * e atualiza o título do modal para "Cadastro Receita".
 *
 * Esta função é chamada quando o modal de cadastro de receita é aberto, garantindo que
 * o formulário esteja pronto para receber um novo cadastro de receita.
 *
 * Passos executados:
 * 1. Limpa os campos do formulário.
 * 2. Atualiza a URL de ação do formulário com os parâmetros da query string.
 * 3. Atualiza o título do modal para "Cadastro Receita".
 *
 * Não possui parâmetros nem retorna nenhum valor.
 */
function prepararNovoCadastroReceita() {
    const form = document.querySelector('#modal-nova-receita form');
    form.reset();
    const queryString = window.location.search;
    form.action = `/financas/receitas/cadastrar/${queryString}`;
    document.getElementById('modal-title-7').textContent = 'Cadastro Receita';
}

/**
 * Função responsável por carregar os dados de uma receita existente e preenchê-los nos campos do formulário.
 *
 * A função faz uma requisição para obter os dados de uma receita pelo seu ID e, uma vez os dados recebidos,
 * preenche os campos do formulário com as informações da receita, além de ajustar a URL de ação para edição da receita
 * com base no ID da receita e na query string da URL.
 *
 * Passos executados:
 * 1. Faz uma requisição fetch para obter os dados da receita com o ID fornecido.
 * 2. Preenche os campos do formulário com os dados da receita (descrição, valor, data, ID).
 * 3. Atualiza a URL de ação do formulário para a edição da receita, incluindo o ID da receita e a query string da URL atual.
 * 4. Altera o título do modal para "Editar Receita".
 *
 * Parâmetros:
 * - `id` (Integer): ID da receita que será carregada.
 *
 * Retorno:
 * Não retorna nenhum valor. O preenchimento dos campos do formulário e a alteração do título do modal são feitos de forma direta.
 */
function carregarDadosReceita(id) {
    fetch(`/financas/receitas/obter/${id}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('id_descricao').value = data.descricao;
            document.getElementById('id_valor').value = data.valor;
            document.getElementById('id_data').value = data.data;
            document.getElementById('id_receita').value = data.id;

            const queryString = window.location.search;
            const form = document.querySelector('#modal-nova-receita form');
            form.action = `/financas/receitas/editar/${data.id}/${queryString}`;

            document.getElementById('modal-title-7').textContent = 'Editar Receita';
        })
        .catch(error => {
            alert('Erro ao carregar dados da receita.');
            console.error(error);
        });
}

/**
 * Função responsável por preparar o formulário de cadastro de uma nova despesa.
 * Limpa os campos do formulário, ajusta a URL de ação com base na query string da URL atual,
 * e atualiza o título do modal para "Cadastro Despesa".
 *
 * Esta função é chamada quando o modal de cadastro de despesa é aberto, garantindo que
 * o formulário esteja pronto para receber um novo cadastro de despesa.
 *
 * Passos executados:
 * 1. Limpa os campos do formulário.
 * 2. Atualiza a URL de ação do formulário com os parâmetros da query string.
 * 3. Atualiza o título do modal para "Cadastro Despesa".
 *
 * Não possui parâmetros nem retorna nenhum valor.
 */
function prepararNovoCadastroDespesa() {
    const form = document.querySelector('#modal-nova-despesa form');
    form.reset();
    const queryString = window.location.search;
    form.action = `/financas/despesas/cadastrar/${queryString}`;
    document.getElementById('modal-title-7').textContent = 'Cadastro Despesa';
}

/**
 * Função responsável por carregar os dados de uma despesa existente e preenchê-los nos campos do formulário.
 *
 * A função faz uma requisição para obter os dados de uma despesa pelo seu ID e, uma vez os dados recebidos,
 * preenche os campos do formulário com as informações da despesa, além de ajustar a URL de ação para edição da despesa
 * com base no ID da despesa e na query string da URL.
 *
 * Passos executados:
 * 1. Faz uma requisição fetch para obter os dados da despesa com o ID fornecido.
 * 2. Preenche os campos do formulário com os dados da despesa (descrição, valor, data, ID).
 * 3. Atualiza a URL de ação do formulário para a edição da despesa, incluindo o ID da despesa e a query string da URL atual.
 * 4. Altera o título do modal para "Editar Despesa".
 *
 * Parâmetros:
 * - `id` (Integer): ID da despesa que será carregada.
 *
 * Retorno:
 * Não retorna nenhum valor. O preenchimento dos campos do formulário e a alteração do título do modal são feitos de forma direta.
 */
function carregarDadosDespesa(id) {
    fetch(`/financas/despesas/obter/${id}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('id_descricao').value = data.descricao;
            document.getElementById('id_valor').value = data.valor;
            document.getElementById('id_data').value = data.data;
            document.getElementById('id_despesa').value = data.id;

            const queryString = window.location.search;
            const form = document.querySelector('#modal-nova-despesa form');
            form.action = `/financas/despesas/editar/${data.id}/${queryString}`;

            document.getElementById('modal-title-7').textContent = 'Editar Despesa';
        })
        .catch(error => {
            alert('Erro ao carregar dados da despesa.');
            console.error(error);
        });
}

document.addEventListener('DOMContentLoaded', function () {
    fetch('/financas/grafico-dados-mensal/')
    .then(response => response.json())
    .then(data => {
        Highcharts.chart('graficoFinanceiro', {
            chart: {
                type: 'column',
                animation: {
                    duration: 1000,
                    easing: 'easeOutBounce'
                }
            },
            title: { text: null },
            subtitle: { text: null },
            legend: { enabled: true },
            xAxis: {
                type: 'category'
            },
            yAxis: [{
                title: { text: null },
                labels: { enabled: false }
            }],
            tooltip: {
                shared: true,
                headerFormat: '<span style="font-size: 15px">{point.key}</span><br/>',
                pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name}: <b>R$ {point.y:,.2f}</b><br/>'
            },
            plotOptions: {
                column: {
                    borderRadius: 3,
                    grouping: true,
                },
                series: {
                    grouping: false,
                    borderWidth: 0
                }
            },
            series: [{
                name: 'Despesas',
                color: 'rgba(239, 68, 68, 0.6)',
                borderColor: '#B91C1C',
                borderWidth: 1,
                data: data.despesas
            }, {
                name: 'Receitas',
                color: 'rgba(59, 130, 246, 0.6)',
                borderColor: '#1D4ED8',
                borderWidth: 1,
                data: data.receitas
            }],
            exporting: { enabled: false }
        });
    });
});