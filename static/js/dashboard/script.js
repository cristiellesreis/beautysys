document.addEventListener('DOMContentLoaded', function () {

  function criarGraficoReceitaPorCategoria(dadosReceita) {
    const coresPorCategoria = {
      'cortes': '#1D8F4C',
      'finalizacao': '#1FB5C5',
      'quimica': '#2B6D85',
      'tratamento': '#48A79E',
      'outros': '#FBC02D'
    };

    const el = document.getElementById('graficoReceitaPorCategoria');

    const dadosFormatados = dadosReceita.map(item => ({
      name: item.categoria,
      y: item.total,
      color: coresPorCategoria[item.categoria] || '#CCCCCC'
    }));

    Highcharts.chart('graficoReceitaPorCategoria', {
      chart: {
        type: 'pie',
        backgroundColor: 'transparent'
      },
      title: { text: null },
      tooltip: {
        pointFormat: '<b>R$ {point.y:.2f}</b> ({point.percentage:.1f}%)',
        style: { color: '#5c6e8a', fontWeight: '600' }
      },
      legend: {
        enabled: true,
        align: 'center',
        verticalAlign: 'bottom',
        layout: 'horizontal',
        itemStyle: { fontSize: '14px', color: '#5c6e8a', fontWeight: '600' }
      },
      plotOptions: {
        pie: {
          innerSize: '60%',
          dataLabels: { enabled: false },
          showInLegend: true,
          borderWidth: 0,
          animation: { duration: 800 }
        }
      },
      series: [{
        name: 'Receita',
        data: dadosFormatados
      }]
    });
  }

  function criarGraficoDespesasPorCategoria(dadosDespesa) {
    const coresPorCategoria = {
      'custos fixos': '#FF6F61',
      'produtos': '#FF5722',
      'salario': '#C2185B',
      'outros': '#8E24AA',
    };

    const dadosFormatados = dadosDespesa.map(item => ({
      name: item.categoria,
      y: item.total,
      color: coresPorCategoria[item.categoria] || '#CCCCCC'
    }));

    Highcharts.chart('graficoDespesasPorCategoria', {
      chart: {
        type: 'pie',
        backgroundColor: 'transparent'
      },
      title: { text: null },
      tooltip: {
        pointFormat: '<b>R$ {point.y:.2f}</b> ({point.percentage:.1f}%)',
        style: { color: '#5c6e8a', fontWeight: '600' }
      },
      legend: {
        enabled: true,
        align: 'center',
        verticalAlign: 'bottom',
        layout: 'horizontal',
        itemStyle: { fontSize: '14px', color: '#5c6e8a', fontWeight: '600' }
      },
      plotOptions: {
        pie: {
          innerSize: '60%',
          dataLabels: { enabled: false },
          showInLegend: true,
          borderWidth: 0,
          animation: { duration: 800 }
        }
      },
      series: [{
        name: 'Despesas',
        data: dadosFormatados
      }]
    });
  }

  function criarGraficoStatusAgendamentos() {
    const el = document.getElementById('graficoStatusAgendamentos');
    const concluido = parseInt(el.dataset.concluido || 0);
    const agendado = parseInt(el.dataset.agendado || 0);
    const cancelado = parseInt(el.dataset.cancelado || 0);

    Highcharts.chart('graficoStatusAgendamentos', {
      chart: {
        type: 'pie',
        backgroundColor: 'transparent'
      },
      title: { text: null },
      tooltip: {
        pointFormat: '<b>{point.y}</b> ({point.percentage:.1f}%)',
        style: { color: '#5c6e8a', fontWeight: '600' }
      },
      legend: {
        enabled: true,
        align: 'center',
        verticalAlign: 'bottom',
        layout: 'horizontal',
        itemStyle: { fontSize: '14px', color: '#5c6e8a', fontWeight: '600' }
      },
      plotOptions: {
        pie: {
          innerSize: '60%',
          dataLabels: { enabled: false },
          showInLegend: true,
          borderWidth: 0,
          animation: { duration: 800 }
        }
      },
      series: [{
        name: 'Agendamentos',
        data: [
          { name: 'Concluídos', y: concluido, color: '#20C8A7' },
          { name: 'Pendentes', y: agendado, color: '#fcd771' },
          { name: 'Cancelados', y: cancelado, color: '#fd7192' }
        ]
      }]
    });
  }

  const dadosReceita = JSON.parse(document.getElementById('dados-receita').textContent);
  const dadosDespesa = JSON.parse(document.getElementById('dados-despesa').textContent);

  criarGraficoReceitaPorCategoria(dadosReceita);
  criarGraficoDespesasPorCategoria(dadosDespesa);
  criarGraficoStatusAgendamentos();

  fetch('/financas/grafico-dados-mensal/')
    .then(response => response.json())
    .then(data => {
        Highcharts.chart('graficoFinanceiro', {
            chart: {
                type: 'line',
                animation: {
                    duration: 1000,
                    easing: 'easeOutBounce'
                },
                backgroundColor: null,
                style: {
                  fontFamily: 'inherit',
                  color: '#5c6e8a',
                  fontWeight: '600'
                },
            },
            title: { 
                text: '',
            },
            legend: {
              itemStyle: { color: '#5c6e8a', fontWeight: '600' },
              itemHoverStyle: { color: '#3b4a61' }
            },
            xAxis: {
                type: 'category',
                labels: { 
                    style: { 
                        color: '#5c6e8a', 
                        fontWeight: '600' 
                    } 
                },
                lineColor: '#5c6e8a',
                tickColor: '#5c6e8a'
            },
            yAxis: [{
                title: { text: 'Valores (R$)', style: { color: '#5c6e8a', fontWeight: '600' } },
                labels: { style: { color: '#5c6e8a', fontWeight: '600' } },
                gridLineColor: '#e6e6e6',
                lineColor: '#5c6e8a',
                tickColor: '#5c6e8a'

            }],
            tooltip: { style: { color: '#5c6e8a', fontWeight: '600' } },
            series: [{
                name: 'Despesas',
                color: '#FD7192',
                data: data.despesas
            }, {
                name: 'Receitas',
                color: '#20C8A7',
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
