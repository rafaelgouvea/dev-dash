from shiny import App, render, ui

#Interface do usuário ----
app_ui = ui.page_navbar(
    ui.nav(
        "Página 1",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.markdown(
                    """
                    Um testo em **negrito** ou em *itálico*

                    Um parágrafo com um [link](https://www.afirainvestimentos.com/)

                    - Item 1
                    - Item 2
                    - Item 3

                    ![](https://static.wixstatic.com/media/761fe6_9a3b9a5f05d946b7951017dfed5fac4a~mv2.png/v1/fill/w_160,h_68,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Logo_Completo_Chumbo.png)
                    """
                ),
                width = 3
            ),
            ui.panel_main(
                "Painel de Conteúdo Principal",
                style = "background-color: #B7B7A5"
                )
        )
    ),
    ui.nav("Página 2"),
    ui.nav_control(ui.a("ÁFIRA INVESTIMENTOS", href = "https://www.afirainvestimentos.com/")),
    ui.nav_menu(
        "Mais",
        ui.nav_control(ui.a("ÁFIRA FUNDOS", href = "https://www.afirainvestimentos.com/afira-fundos")),
        ui.nav_control(ui.a("ÁFIRA GESTÃO", href = "https://www.afirainvestimentos.com/wealth-management"))
        ),
    title = ui.row(
        ui.column(3, ui.img(src = "https://static.wixstatic.com/media/761fe6_9a3b9a5f05d946b7951017dfed5fac4a~mv2.png/v1/fill/w_160,h_68,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Logo_Completo_Chumbo.png",
                            width = 70)),
        ui.column(9, "Título da Dashboard")
    ),
    bg = " #F6EFE2",
    inverse= False
)


# Servidor ----
def server(input, output, session):
    ...

# Dashboard Shiny App ----
app = App(app_ui, server)
