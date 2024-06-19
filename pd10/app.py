# Importação de bibliotecas
from shiny import App, render, ui
from shinywidgets import render_plotly, output_widget, _render_widget
import pandas as pd
import plotly.express as px
from itables.shiny import DT


# Importação de dados ----
dados = (
    pd.read_csv(
        filepath_or_buffer = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=csv",
        sep = ";",
        decimal = ",",
        converters = {"data": lambda x: pd.to_datetime(x, format = "%d/%m/%Y")}
        )
    .query("data > = '2005-01-01'")
    .assign(variacao_pct = lambda x: ((x.valor / x.valor.shift(1)) - 1) * 100)
)

#Interface do usuário ----
app_ui = ui.page_navbar(
    ui.nav(
        "Gráficos",
        ui.layout_sidebar(
            ui.panel_sidebar("Barra lateral", width = 2),
            ui.panel_main(
            ui.row(ui.column(12, ui.output_plot("grafico_estatico"))),
            ui.row(ui.column(12, output_widget("grafico_interativo")))
                )
        )
    ),
    ui.nav(
        "Tabelas",
        ui.layout_sidebar(
            ui.panel_sidebar("Barra lateral", width = 2),
            ui.panel_main(
            ui.row(ui.column(12, ui.output_table("tabela_estatico"))),
            ui.row(ui.column(12, ui.HTML(DT(dados.tail(15)))))
                )
        )
    ),
    title =  "Visualizações de dados",
    bg = " #F6EFE2",
    inverse= False
)

# Lógica do Servidor ----
def server(input, output, session):
   @output
   @render.plot
   def grafico_estatico():
      return dados.plot(y = "valor", x = "data", kind = "line")
   
   @output
   @render_plotly
   def grafico_interativo():
      return px.line(data_frame = dados, x = "data", y = "valor")
   
   @output
   @render.table
   def tabela_estatico():
      return dados.tail(15)
      

# Dashboard Shiny App ----
app = App(app_ui, server)
