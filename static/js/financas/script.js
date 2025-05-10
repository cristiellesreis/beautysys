
function prepararNovoCadastroReceita() {
    const form = document.querySelector('#modal-nova-receita form');
    form.reset();
    const queryString = window.location.search;
    form.action = `/financas/receitas/cadastrar/${queryString}`;
    document.getElementById('modal-title-7').textContent = 'Cadastro de Receita';
}

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

function prepararNovoCadastroDespesa() {
    const form = document.querySelector('#modal-nova-despesa form');
    form.reset();
    const queryString = window.location.search;
    form.action = `/financas/despesas/cadastrar/${queryString}`;
    document.getElementById('modal-title-7').textContent = 'Cadastro de Despesa';
}

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
                    },
                    backgroundColor: null
                },
                title: { 
                    text: '',
                    style: {
                        color: '#5c6e8a',
                        fontSize: '20px',
                        fontWeight: 'bold'
                    }
                },
                subtitle: { 
                    text: '',
                    style: {
                        color: '#5c6e8a',
                        fontSize: '14px',
                        fontStyle: 'italic'
                    }
                },
                legend: {
                    enabled: true,
                    itemStyle: {
                        color: '#5c6e8a',
                        fontSize: '14px',
                        fontWeight: 'bold'
                    }
                },
                xAxis: {
                    type: 'category',
                    labels: {
                        style: {
                            color: '#5c6e8a', 
                            fontSize: '14px',
                            fontWeight: 'bold'
                        }
                    }
                },
                yAxis: [{
                    title: { text: null },
                    labels: { enabled: false },
                    tickAmount: 3,
                    gridLineColor:'#8a98b1',
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
                    color: '#FD7192',
                    borderColor: '#FD7192',
                    borderWidth: 1,
                    data: data.despesas
                }, {
                    name: 'Receitas',
                    color: '#20C8A7',
                    borderColor: '#20C8A7',
                    borderWidth: 1,
                    data: data.receitas
                }],
                exporting: { enabled: true 
                },
                responsive: {
                    rules: [{
                        condition: {
                            maxWidth: 500
                        },
                        chartOptions: {
                            legend: {
                                layout: 'horizontal',
                                align: 'center',
                                verticalAlign: 'bottom'
                            }
                        }
                    }]
                }
            });
        });
            
});

