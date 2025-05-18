document.addEventListener("DOMContentLoaded", () => {
  const chartDataScript = document.getElementById('dollar-chart-data');
  const historyData = JSON.parse(chartDataScript.textContent);

  const canvas = document.getElementById('dollarChart');
  const ctx = canvas.getContext('2d');

  // Crear degradados
  const gradientBuy = ctx.createLinearGradient(0, 0, 0, canvas.height);
  gradientBuy.addColorStop(0, 'rgba(33, 150, 243, 0.3)');
  gradientBuy.addColorStop(1, 'rgba(33, 150, 243, 0)');

  const gradientSell = ctx.createLinearGradient(0, 0, 0, canvas.height);
  gradientSell.addColorStop(0, 'rgba(244, 67, 54, 0.3)');
  gradientSell.addColorStop(1, 'rgba(244, 67, 54, 0)');

  const chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: historyData.dates,
      datasets: [
        {
          label: 'Compra',
          data: historyData.buy_rates,
          borderColor: 'rgba(33, 150, 243, 1)',
          backgroundColor: gradientBuy,  // 👈 Aplicar degradado
          borderWidth: 2,
          fill: true,                    // 👈 Rellenar debajo de la línea
          pointRadius: 0,
          tension: 0.4,
        },
        {
          label: 'Venta',
          data: historyData.sell_rates,
          borderColor: 'rgba(244, 67, 54, 1)',
          backgroundColor: gradientSell, // 👈 Aplicar degradado
          borderWidth: 2,
          fill: true,                    // 👈 Rellenar debajo de la línea
          pointRadius: 0,
          tension: 0.4,
        },
      ],
    },
    options: {
      responsive: true,
      animation: {
        duration: 1500,
        easing: 'easeOutQuart'
      },
      interaction: {
        mode: 'index',
        intersect: false,
        axis: 'x'
      },
      layout: {
        padding: {
          top: 10,
          bottom: 0,
        },
      },
      scales: {
        x: {
          grid: {
            display: false,
          },
          ticks: {
            display: false
          }
        },
        y: {
          beginAtZero: false,
          grid: {
            drawBorder: false,
            color: 'rgba(0, 0, 0, 0.05)',
          },
          ticks: {
            color: '#424242',
            font: {
              size: 10,
              family: "'Roboto', sans-serif",
            },
            maxTicksLimit: 5
          }
        },
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            color: '#424242',
            usePointStyle: true,
            pointStyle: 'line',
            font: {
              size: 10,
              family: "'Roboto', sans-serif",
            },
            padding: 10
          }
        },
        tooltip: {
          mode: 'index',
          intersect: true,
          position: 'nearest',
          backgroundColor: '#ffffff',
          titleColor: '#000000',
          bodyColor: '#333333',
          borderColor: '#e0e0e0',
          borderWidth: 1,
          titleFont: {
            size: 12,
            family: "'Roboto', sans-serif",
            weight: 'bold'
          },
          bodyFont: {
            size: 11,
            family: "'Roboto', sans-serif"
          },
          padding: 8,
          displayColors: false
        }
      }
    }
  });
});
