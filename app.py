import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# instanciando o Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
        html.H1(
            'Hello Dash',
            id='h1',
            # estilo do titulo
            style={
                'textAlign': 'center'
            }
        ),

        # subtitulo
        html.Div(
            'Dash um framework web para Python.',
            id='div1',
            # estilo do subtitulo
            style={
                'textAlign': 'center'
            }
        ),

        # grafico
        dcc.Graph(
            figure=fig,
            id='graph1',
            # estilo do grafico
            style={
                'align': 'center',
                'width': '50%',
                'height': '100%',
                'margin': 'auto',
            }
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
