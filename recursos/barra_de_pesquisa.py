import pandas as pd
import locale
from flet import *


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

df = pd.read_csv('./bases_de_dados/Filmes.csv')
filmes = df['title'].tolist()
filmes = [i for i in filmes if isinstance(i, str)]
filmes = sorted(filmes, key=locale.strxfrm)


class BarraDePesquisa(UserControl):
    def __init__(self):
        super().__init__()
        self.numero_itens = Text(size=9, italic=True, color="white")
        self.resultados_container = Column(scroll="auto", expand=True)
        self.filmes_selecionados = []
        self.lista_filmes_selecionados = Column()


    def build(self):
        return Container(
            width=450,
            bgcolor="white10",
            border_radius=6,
            padding=padding.all(15),
            clip_behavior=ClipBehavior.HARD_EDGE,
            animate=animation.Animation(400, "decelerate"),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.START,
                controls=[
                    Row(
                        spacing=10,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Icon(icons.SEARCH, size=15, opacity=0.7),
                            TextField(
                                border_color="transparent",
                                height=20,
                                content_padding=2,
                                text_style=TextStyle(size=14, font_family="Consolas"),
                                hint_style=TextStyle(size=13, font_family="Consolas"),
                                hint_text="Buscar um filme",
                                cursor_color="white",
                                cursor_width=1,
                                on_change=self.filtragem,
                            ),
                            self.numero_itens,
                        ],
                    ),
                    self.resultados_container,
                    Text("Filmes Selecionados:", weight="bold", color="white"),
                    self.lista_filmes_selecionados,
                ],
            ),
        )


    def filtragem(self, e):
        texto = e.control.value.strip().lower()

        self.resultados_container.controls.clear()

        if texto:
            resultados = [filme for filme in filmes if texto in filme.lower()]
            self.numero_itens.value = f"{len(resultados)} resultados encontrados"
            for filme in resultados:
                self.resultados_container.controls.append(
                    Container(
                        content=Text(filme, color="white"),
                        padding=10,
                        border_radius=5,
                        bgcolor="white10",
                        on_click=lambda e, f=filme: self.selecionar_filme(f),
                    )
                )
        else:
            self.numero_itens.value = ""

        if self.resultados_container.page:
            self.resultados_container.update()
        if self.numero_itens.page:
            self.numero_itens.update()


    def selecionar_filme(self, filme):
        if filme not in self.filmes_selecionados:
            self.filmes_selecionados.append(filme)
            self.lista_filmes_selecionados.controls.append(
                Container(
                    content=Row(
                        controls=[
                            Text(filme, color="white"),
                            IconButton(
                                icon=icons.DELETE,
                                icon_color="red",
                                on_click=lambda e, f=filme: self.remover_filme(f),
                            ),
                        ]
                    ),
                    padding=10,
                    border_radius=5,
                    bgcolor="white10",
                )
            )

        self.lista_filmes_selecionados.update()


    def remover_filme(self, filme):
        if filme in self.filmes_selecionados:
            self.filmes_selecionados.remove(filme)
            self.lista_filmes_selecionados.controls = [
                c
                for c in self.lista_filmes_selecionados.controls
                if c.content.controls[0].value != filme
            ]
        self.lista_filmes_selecionados.update()