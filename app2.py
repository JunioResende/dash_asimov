import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# instanciando o Dash
app = dash.Dash(
    __name__,
)

# criacao do layout
app.layout = html.Div([
    # Dropdown
    html.H1('Dropdown'),
    dcc.Dropdown(
        id='dp1',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    # Checklist
    html.H1('Checklist'),
    dcc.Checklist(
        id='dp1',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
    ),

    # Radio Items
    html.H1('Radio Items'),
    dcc.RadioItems(
        id='dp1',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
    ),

    # Input
    html.H1('Input'),
    dcc.Input(
        id='dp1',
        placeholder='Enter a value...',
        type='text',
        value=''
    ),

    # Slider
    html.H1('Slider'),
    dcc.Slider(
        id='dp1',
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i)
               for i in range(1, 20)},
        value=5,
    ),

    # Range Slider
    html.H1('Range Slider'),
    dcc.RangeSlider(
        id='dp1',
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i)
               for i in range(1, 20)},
        value=[5, 7]
    ),

    # Textarea
    html.H1('Textarea'),
    dcc.Textarea(
        id='dp1',
        placeholder='Enter a value...',
        value='This is a TextArea component',
        style={'width': '100%'}
    ),

    # Button
    html.H1('Button'),
    html.Button('Button', id='dp1', n_clicks=0),

    # Upload
    html.H1('Upload'),
    dcc.Upload(
        id='dp1',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center'
        }
    ),

    # Date Picker Single
    html.H1('Date Picker Single'),
    dcc.DatePickerSingle(
        id='dp1',
        date='2017-06-21'
    ),

    # Date Picker Range
    html.H1('Date Picker Range'),
    dcc.DatePickerRange(
        id='dp1',
        start_date='2017-06-21',
        end_date_placeholder_text='Select a date!'
    ),

    # Markdown
    html.H1('Markdown'),
    dcc.Markdown('''
        # Dash and Markdown

        Dash supports [Markdown](http://commonmark.org/help).

        Markdown is a simple way to write and format text.
        It includes a syntax for things like **bold text** and *italics*,
        [links](http://commonmark.org/help), inline `code` snippets, lists,
        quotes, and more.
    '''),

    # HTML
    html.H1('HTML'),
    html.Label('This is a label'),
    html.Br(),
    html.Br(),
    html.Div('This is a div'),
    html.Br(),
    html.Br(),
    html.Span('This is a span'),
    html.Br(),
    html.Br(),
    html.Hr(),
    html.Br(),
    html.Br(),
    html.P('This is a paragraph'),
    html.Br(),
    html.Br(),
    html.Pre('''
        This is a preformatted text block.
        It can have multiple lines.
    '''),
    html.Br(),
    html.Br(),
    html.Blockquote('This is a blockquote'),
    html.Br(),
    html.Br(),
    html.Code('This is a code'),
    html.Br(),
    html.Br(),
    html.Em('This is a em'),
    html.Br(),
    html.Br(),
    html.I('This is a i'),
    html.Br(),
    html.Br(),
    html.B('This is a b'),
    html.Br(),
    html.Br(),
    html.Strong('This is a strong'),
    html.Br(),
    html.Br(),
    html.Small('This is a small'),
    html.Br(),
    html.Br(),
    html.Sub('This is a sub'),
    html.Br(),
    html.Br(),
    html.Sup('This is a sup'),
    html.Br(),
    html.Br(),
    html.U('This is a u'),
    html.Br(),
    html.Br(),
    html.Abbr('This is a abbr'),
    html.Br(),
    html.Br(),
    html.Address('This is a address'),
    html.Br(),
    html.Br(),
    html.Bdi('This is a bdi'),
    html.Br(),
    html.Br(),
    html.Bdo('This is a bdo'),
    html.Br(),
    html.Br(),
    html.Caption('This is a caption'),
    html.Br(),
    html.Br(),
    html.Cite('This is a cite'),
    html.Br(),
    html.Br(),
    html.Code('This is a code'),
    html.Br(),
    html.Br(),
    html.Del('This is a del'),
    html.Br(),
    html.Br(),
    html.Dfn('This is a dfn'),
])

# rodando o servidor web
app.run_server(
    debug=True,
    port=3000,
    use_reloader=True,
    dev_tools_hot_reload=True,
    threaded=True
)
