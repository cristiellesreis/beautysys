document.addEventListener('DOMContentLoaded', function () {

    function criarGraficoFinanceiro() {
      Highcharts.chart('graficoFinanceiro', {
        chart: {
          type: 'line',
          backgroundColor: null,
          style: {
            fontFamily: 'inherit',
            color: '#5c6e8a',
            fontWeight: '600'
          }
        },
        title: { text: '' },
        xAxis: {
          categories: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
          labels: { style: { color: '#5c6e8a', fontWeight: '600' } },
          lineColor: '#5c6e8a',
          tickColor: '#5c6e8a'
        },
        yAxis: {
          title: { text: 'Valores (R$)', style: { color: '#5c6e8a', fontWeight: '600' } },
          labels: { style: { color: '#5c6e8a', fontWeight: '600' } },
          gridLineColor: '#e6e6e6',
          lineColor: '#5c6e8a',
          tickColor: '#5c6e8a'
        },
        legend: {
          itemStyle: { color: '#5c6e8a', fontWeight: '600' },
          itemHoverStyle: { color: '#3b4a61' }
        },
        tooltip: { style: { color: '#5c6e8a', fontWeight: '600' } },
        series: [
          { name: 'Receita', data: [5000, 7000, 8000, 6000, 9000], color: '#20C8A7' },
          { name: 'Despesas', data: [3000, 4000, 5000, 3500, 4500], color: '#FD7192' }
        ]
      });
    }
  
    function criarGraficoReceitaPorCategoria() {
      Highcharts.chart('graficoReceitaPorCategoria', {
        chart: {
          type: 'pie',
          backgroundColor: 'transparent',
          style: { fontFamily: 'inherit', color: '#5c6e8a', fontWeight: '600' }
        },
        title: { text: null },
        legend: {
          enabled: true,
          align: 'center',
          verticalAlign: 'bottom',
          layout: 'horizontal',
          itemStyle: { fontSize: '14px', color: '#5c6e8a', fontWeight: '600' }
        },
        plotOptions: {
          pie: {
            innerSize: '30%',
            dataLabels: { enabled: false },
            showInLegend: true
          }
        },
        series: [{
          name: 'Receita',
          data: [
            { name: 'Cortes', y: 40, color: '#1D8F4C' },
            { name: 'Finalização', y: 30, color: '#1FB5C5' },
            { name: 'Química', y: 20, color: '#2B6D85' },
            { name: 'Tratamento', y: 10, color: '#48A79E' },
            { name: 'Outros', y: 10, color: '#FBC02D' }
          ]
        }]
      });
    }
  
    function criarGraficoDespesasPorCategoria() {
      Highcharts.chart('graficoDespesasPorCategoria', {
        chart: {
          type: 'pie',
          backgroundColor: 'transparent',
          style: { fontFamily: 'inherit', color: '#5c6e8a', fontWeight: '600' }
        },
        title: { text: null },
        legend: {
          enabled: true,
          align: 'center',
          verticalAlign: 'bottom',
          layout: 'horizontal',
          itemStyle: { fontSize: '14px', color: '#5c6e8a', fontWeight: '600' }
        },
        plotOptions: {
          pie: {
            innerSize: '30%',
            dataLabels: { enabled: false },
            showInLegend: true
          }
        },
        series: [{
          name: 'Despesas',
          data: [
            { name: 'Custos fixos', y: 35, color: '#FF6F61' },
            { name: 'Produtos', y: 25, color: '#FF5722' },
            { name: 'Salário', y: 30, color: '#C2185B' },
            { name: 'Outros', y: 10, color: '#8E24AA' }
          ]
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
          backgroundColor: 'transparent',
          events: {
            load: function () {
              const chart = this;
              const total = chart.series[0].data.reduce((s, p) => s + p.y, 0);
              chart.customLabel = chart.renderer.text(
                'Total<br><span style="font-size:22px; font-weight:bold;">' + total + '</span>',
                0, 0, true
              ).css({
                color: '#5c6e8a',
                fontSize: '14px',
                fontWeight: '600',
                textAlign: 'center'
              }).add();
              positionCenterText(chart);
            },
            render: function () {
              if (this.customLabel) {
                positionCenterText(this);
              }
            }
          }
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
  
    function positionCenterText(chart) {
      const bbox = chart.customLabel.getBBox();
      const centerX = chart.plotLeft + chart.plotWidth / 2;
      const centerY = chart.plotTop + chart.plotHeight / 2;
      chart.customLabel.attr({
        x: centerX - bbox.width / 2,
        y: centerY - bbox.height / 4
      });
    }
  
    criarGraficoFinanceiro();
    criarGraficoReceitaPorCategoria();
    criarGraficoDespesasPorCategoria();
    criarGraficoStatusAgendamentos();
  });
  