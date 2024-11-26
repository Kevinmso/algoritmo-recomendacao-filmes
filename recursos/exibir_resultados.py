from flet import *


def voltar(pagina: Page):
    from main import main

    pagina.controls.clear()
    main(pagina)
    pagina.update()

def ExibirResultados(pagina: Page, resultados):
    pagina.controls.clear()

    pagina.theme_mode = ThemeMode.DARK
    pagina.title = "Sistema de Recomendação de Filmes"
    pagina.vertical_alignment = "start"
    pagina.horizontal_alignment = "center"
    pagina.padding = padding.symmetric(vertical=20, horizontal=50)

    pagina.add(
        Text(
            "🎥 Resultados da Recomendação",
            font_family="Consolas",
            size=24,
            color=colors.CYAN,
            weight="bold",
            text_align="center",
        ),
        Divider(color=colors.CYAN, thickness=2),
    )

    lista_resultados = Column(
        spacing=10,
        controls=[
            Container(
                content=Row(
                    controls=[
                        Text(
                            "Filme",
                            color=colors.WHITE,
                            weight="bold",
                            size=16,
                            expand=1,
                        ),
                        Text(
                            "Similaridade",
                            color=colors.WHITE,
                            weight="bold",
                            size=16,
                        ),
                    ],
                ),
                padding=padding.all(10),
                bgcolor=colors.BLUE_GREY_900,
                border_radius=6,
                margin=margin.only(bottom=10),
            ),
        ],
    )

    for filme, similaridade in resultados.items():
        lista_resultados.controls.append(
            Container(
                content=Row(
                    controls=[
                        Text(filme, color=colors.CYAN, expand=1),  
                        Text(f"{similaridade:.4f}", color=colors.ORANGE),  
                    ],
                ),
                padding=padding.all(10),
                bgcolor=colors.BLUE_GREY_800,
                border_radius=6,
                margin=margin.only(bottom=5),
            )
        )

    pagina.add(lista_resultados)

    pagina.add(
        ElevatedButton(
            text="Voltar",
            bgcolor=colors.CYAN,
            color=colors.BLACK,
            on_click=lambda e: voltar(pagina),  
        ),
    )
    
    pagina.update()