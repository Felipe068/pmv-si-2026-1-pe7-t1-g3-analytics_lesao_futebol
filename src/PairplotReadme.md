Gráfico Pairplot:

Comandos em python para gerar o gráfico:

  df_pair = df[["player_age", "days", "games_missed"]]

  sns.pairplot(df_pair)

  plt.show()

Gráfico gerado:

<img width="994" height="500" alt="pairplot1" src="https://github.com/user-attachments/assets/393eb669-422a-42d5-99d6-2076cccfb22b" />

Análise:

O pairplot evidencia uma distribuição aproximadamente normal para a idade dos jogadores, enquanto a variável de jogos perdidos apresenta forte assimetria positiva. A análise de dispersão não indica uma relação linear clara entre idade e severidade da lesão, sugerindo que a idade, isoladamente, possui baixo poder explicativo. No entanto, a presença de outliers e a concentração de dados em faixas específicas indicam a necessidade de transformações e análise multivariada mais aprofundada.
