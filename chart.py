import pandas as pd

order = "https://raw.githubusercontent.com/Data-Science-Research/edital_avaliacao/main/order.csv"
mainCategory = "https://raw.githubusercontent.com/Data-Science-Research/edital_avaliacao/main/mainCategory.csv"
order = pd.read_csv(order, sep=";", header=0)
mainCategory = pd.read_csv(mainCategory, sep=";", header=0)

df_merged =  order.merge(mainCategory, how='inner',
                      left_on=['page 1 (main category)'],
                      right_on=['id'])
roupas_distintas_por_categoria = df_merged.groupby('mainCategory')['page 2 (clothing model)'].nunique()
categorias = roupas_distintas_por_categoria.index.tolist()
num_modelos_distintos = roupas_distintas_por_categoria.tolist()

html_chart = f'''
<!DOCTYPE html>
<html>
<head>
  <title>Grafico de Barras</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
  <canvas id="barChart" width="800" height="400"></canvas>
  <script>
    var ctx = document.getElementById('barChart').getContext('2d');
    var myChart = new Chart(ctx, {{
      type: 'bar',
      data: {{
        labels: {categorias},
        datasets: [{{
          label: 'Numero de Modelos Distintos',
          data: {num_modelos_distintos},
          backgroundColor: 'rgba(54, 162, 235, 0.5)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }}]
      }},
      options: {{
        scales: {{
          y: {{
            beginAtZero: true
          }}
        }},
        responsive: true,
        maintainAspectRatio: false
      }}
    }});
  </script>
</body>
</html>
'''

with open('index.html', 'w') as file:
    file.write(html_chart)