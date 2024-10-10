import pandas as pd
import numpy as np
from IPython.display import display
import sklearn.metrics.pairwise as pw

# importando bibliotecas.

filmes = pd.read_csv('Filmes.csv', sep = ',')
avaliacoes = pd.read_csv('ratings.csv', sep = ';')

# lendo arquvivos .csv.

display(filmes.head(2))

display(avaliacoes.head(2))

display(filmes.shape)

display(avaliacoes.shape)

df = filmes.merge(avaliacoes, on = 'movieId')
display(df)

# unindo os dois dataframes em um só.

tabela_df = pd.pivot_table(df, columns = 'userId', index = 'title', values = 'rating')
tabela_df.fillna(0, inplace = True)
display(tabela_df)

recomendacao = pw.cosine_similarity(tabela_df)
recomendacao_df = pd.DataFrame(recomendacao, columns = tabela_df.index, index = tabela_df.index)
display(recomendacao_df)

filmes_de_interesse = ['Inception', 'Godfather, The', 'Interstellar', 'Back to the Future', 'Shawshank Redemption, The']

# Pegar as similaridades para cada filme de interesse

cosseno_filme_1 = recomendacao_df[filmes_de_interesse[0]]
cosseno_filme_2 = recomendacao_df[filmes_de_interesse[1]]
cosseno_filme_3 = recomendacao_df[filmes_de_interesse[2]]
cosseno_filme_4 = recomendacao_df[filmes_de_interesse[3]]
cosseno_filme_5 = recomendacao_df[filmes_de_interesse[4]]

# Calcular a média entre as similaridades dos filmes

media_similaridade = (cosseno_filme_1 + cosseno_filme_2 + cosseno_filme_3 + cosseno_filme_4 + cosseno_filme_5) / 5

# Ordenar as recomendações com base na média
media_similaridade_ordenada = media_similaridade.sort_values(ascending=False)

# Exibir os 20 filmes mais similares com base na média
print(media_similaridade_ordenada.head(20))



