import pandas as pd
from flet import *
from recursos import *
from recursos.exibir_resultados import ExibirResultados


def main(pagina: Page):

    pagina.theme_mode = ThemeMode.DARK
    pagina.title = 'Sistema de recomendação de filmes'
    pagina.vertical_alignment = 'start'
    pagina.horizontal_alignment = 'center'
    pagina.padding = padding.only(top = 50)

    pagina.add(Text('Bem-vindo ao Sistema de Recomendação de Filmes!', font_family = 'Consolas', size = 20))

    barra_de_pesquisa = BarraDePesquisa()
    pagina.add(barra_de_pesquisa)
    
    pagina.add(Container(
        content=ElevatedButton(
            text="Enviar",
            bgcolor=colors.BLUE,
            color=colors.WHITE,
            on_click=lambda e: ExibirResultados(pagina, recomendacao(barra_de_pesquisa.filmes_selecionados)), 
        ),
        alignment=alignment.bottom_right,  
        margin=padding.only(right=20, bottom=20),  
    )
)



if __name__ == '__main__':
    app(target = main)


