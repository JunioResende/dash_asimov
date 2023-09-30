import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# instanciando o Dash
app = dash.Dash(__name__)

# dataframe de exemplo para ser usado como grafico
df = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Orange'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
})

# montagem do grafico
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

# criacao do layout
app.layout = html.Div(
    children=[
        # titulo
        html.H1('Hello Dash', id='h1'),

        # subtitulo
        html.Div('Dash um framework web para Python.', id='div1'),

        # grafico
        dcc.Graph(
            figure=fig,
            id='graph1'
        )
    ]
)

# rodando o servidor web
app.run_server(
    debug=True,
    port=3000,
    use_reloader=True,
    dev_tools_hot_reload=True,
    threaded=True
)
