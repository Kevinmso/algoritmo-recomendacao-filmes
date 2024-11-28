import pandas as pd
import numpy as np
import sklearn.metrics.pairwise as pw


def recomendacao(filmes_de_interesse):

    # lendo arquvivos .csv
    filmes = pd.read_csv('./bases_de_dados/Filmes.csv', sep = ',')
    avaliacoes = pd.read_csv('./bases_de_dados/Ratings.csv', sep = ';') 
    

    # unindo os dois dataframes em um só.
    df = filmes.merge(avaliacoes, on = 'movieId') 
    

    # transformando os id's do usuário em colunas
    tabela_df = pd.pivot_table(df, columns = 'userId', index = 'title', values = 'rating') 
    # removendo espaços em branco
    tabela_df.fillna(0, inplace = True) 
    

    # traçando similaridade
    recomendacao = pw.cosine_similarity(tabela_df)
    recomendacao_df = pd.DataFrame(recomendacao, columns = tabela_df.index, index = tabela_df.index) 

    # calcular a média entre as similaridades dos filmes
    cosseno_filme = 0
    for filme in filmes_de_interesse:
        cosseno_filme += recomendacao_df[filme]
        media_similaridade = cosseno_filme / len(filmes_de_interesse)

    # retirar itens que estejam na lista de interesses
    media_similaridade = media_similaridade[~media_similaridade.index.isin(filmes_de_interesse)]
 
    # ordenar as recomendações com base na média
    media_similaridade_ordenada = media_similaridade.sort_values(ascending=False).head(10)


    # retornar valores
    return media_similaridade_ordenada 








