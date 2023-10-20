from dash import Dash, dcc, html, Input, Output, callback
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from data import drawFigureTestbench, drawFigurePOLInc, drawFigurePOLDec, drawFigureCV, drawFigureEIS025a, \
    drawFigureEIS20a, drawFigureEIS45a


app = Dash(__name__)

app = Dash()

app.layout = dbc.Container([

    # # ROW1 #############################################################################################################
    # dbc.Row([
    #     html.H1('Testbench Parameter Monitoring'),
    #     dcc.Markdown('''
    #     Testbench Paramaeter Monitoring during operation of entire ST-Protocol \n
    #     Including Load Cycling, Shutdown, Startup and electrochemical Cahracterization Procedures
    #     '''),
    # ]),

    # ROW1 #############################################################################################################
    dbc.Row([
            dcc.Graph(id='graph-tb', figure=drawFigureTestbench(), style={'height': '800px'}),
    ]),

    # ROW2 #############################################################################################################
    dbc.Row([
            dcc.Graph(id='graph-pol-dec', figure=drawFigurePOLDec(), style={'height': '800px'})
    ]),

    # ROW3 #############################################################################################################
    dbc.Row([
        dcc.Graph(id='graph-pol-inc', figure=drawFigurePOLInc(), style={'height': '800px'})
    ]),

    # ROW4 #############################################################################################################
    dbc.Row([
            dcc.Graph(id='graph-eis-025a', figure=drawFigureEIS025a(), style={'height': '800px'}),
    ]),

    # ROW5 #############################################################################################################
    dbc.Row([
        dcc.Graph(id='graph-eis-20a', figure=drawFigureEIS20a(), style={'height': '800px'}),
    ]),

    # ROW6 #############################################################################################################
    dbc.Row([
        dcc.Graph(id='graph-eis-25a', figure=drawFigureEIS45a(), style={'height': '800px'}),
    ]),

    # ROW7 #############################################################################################################
    dbc.Row([
            dcc.Graph(id='graph-cv', figure=drawFigureCV(), style={'height': '800px'}),
    ]),

    ])

app.run_server(debug=True, port=8080)
