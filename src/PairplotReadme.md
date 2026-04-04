##Gráfico Pairplot:

Comandos em python para gerar o gráfico:

  df_pair = df[["player_age", "days", "games_missed"]]

  sns.pairplot(df_pair)

  plt.show()

Gráfico gerado:

<img width="994" height="500" alt="pairplot1" src="https://github.com/user-attachments/assets/393eb669-422a-42d5-99d6-2076cccfb22b" />

Análise:

1. Distribuição etária dos jogadores

A variável player_age apresenta uma distribuição aproximadamente normal, com maior concentração entre 22 e 28 anos, faixa que corresponde ao pico de desempenho físico dos atletas. A baixa presença de jogadores em idades mais avançadas pode influenciar a análise, reduzindo a representatividade de atletas mais experientes no conjunto de dados.

2. Assimetria na severidade das lesões

A variável games_missed evidencia forte assimetria positiva, com grande concentração de casos de baixa severidade (até 10 jogos perdidos) e presença de poucos casos extremos. Esse comportamento reforça a existência de uma cauda longa, indicando alta variabilidade na severidade das lesões.

3. Ausência de relação linear clara entre idade e severidade

A análise de dispersão entre player_age e games_missed não revela uma relação linear evidente. Jogadores de diferentes idades apresentam padrões semelhantes de jogos perdidos, sugerindo que a idade, isoladamente, não é um fator determinante para a severidade das lesões.

4. Concentração de eventos em baixa severidade

Observa-se uma alta densidade de pontos concentrados em baixos valores de jogos perdidos, o que indica que a maioria das lesões no futebol profissional resulta em afastamentos curtos. Esse padrão é consistente com o comportamento observado nas análises anteriores (histograma e boxplot).

5. Presença de outliers relevantes

O gráfico evidencia a existência de valores extremos, com alguns jogadores apresentando números significativamente elevados de jogos perdidos. Esses casos representam lesões graves e têm impacto direto na distribuição dos dados, podendo influenciar análises estatísticas e modelos preditivos.

6. Possível limitação amostral

A menor densidade de observações em idades mais elevadas sugere um possível viés amostral, já que jogadores mais velhos são menos representados. Isso pode limitar a capacidade de generalização dos resultados para esse grupo específico.

Conclusão

A análise por meio do pairplot confirma que, embora a idade dos jogadores apresente uma distribuição relativamente equilibrada, a severidade das lesões é caracterizada por alta assimetria e forte presença de outliers. A ausência de uma relação linear clara entre idade e jogos perdidos indica que a idade, de forma isolada, possui baixo poder explicativo sobre a gravidade das lesões.

Esses resultados reforçam a necessidade de abordagens mais robustas e multivariadas para modelagem preditiva, incorporando outras variáveis relevantes, como posição em campo, tipo de lesão e contexto competitivo. Além disso, a presença de outliers e a distribuição não normal dos dados indicam a importância do uso de técnicas de transformação e métodos estatísticos robustos nas etapas seguintes da análise.
