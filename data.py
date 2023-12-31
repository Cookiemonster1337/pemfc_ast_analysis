from dash import Dash, dcc, html, Input, Output, callback
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px
import os


def drawFigureTestbench():

    file = r'data\kcs#01_summary_60s.csv'

    palette = px.colors.qualitative.Alphabet

    test_data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    # test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)

    test_data_df['duration/h'] = test_data_df.index * (1 / 60)
    time = test_data_df['duration/h']

    # read in values of interest for plotting from dataframe
    # time = test_data_df['Time Stamp']
    voltage = test_data_df['voltage']
    current = test_data_df['current']

    compression = test_data_df['pressure_stack_compression']

    # CELL
    temp_cell_an = test_data_df['temp_anode_endplate']
    temp_cell_cat = test_data_df['temp_cathode_endplate']

    # COOLANT
    temp_coolant_inlet = test_data_df['temp_coolant_inlet']
    temp_coolant_outlet = test_data_df['temp_coolant_outlet']
    temp_coolant_diff = test_data_df['temp_coolant_in_out_diff']
    pressure_coolant_inlet = test_data_df['pressure_coolant_inlet']
    pressure_coolant_outlet = test_data_df['pressure_coolant_outlet']
    pressure_coolant_diff = test_data_df['pressure_coolant_in_out_diff']

    # ANODE
    temp_an_inlet = test_data_df['temp_anode_inlet']
    temp_an_outlet = test_data_df['temp_anode_outlet']
    temp_an_diff = test_data_df['temp_anode_in_out_diff']
    flow_an = test_data_df['total_anode_stack_flow']
    pressure_an_inlet = test_data_df['pressure_anode_inlet']
    pressure_an_outlet = test_data_df['pressure_anode_outlet']
    pressure_an_diff = test_data_df['pressure_anode_in_out_diff']

    # CATHODE
    temp_cat_inlet = test_data_df['temp_cathode_inlet']
    temp_cat_outlet = test_data_df['temp_cathode_outlet']
    temp_cat_diff = test_data_df['temp_cathode_in_out_diff']
    flow_cat = test_data_df['total_cathode_stack_flow']
    pressure_cat_inlet = test_data_df['pressure_cathode_inlet']
    pressure_cat_outlet = test_data_df['pressure_cathode_outlet']
    pressure_cat_diff = test_data_df['pressure_cathode_in_out_diff']

    # VARIABLES
    var01 = test_data_df['variable_01']
    var02 = test_data_df['variable_02']
    var03 = test_data_df['variable_03']
    var04 = test_data_df['variable_04']
    var05 = test_data_df['variable_05']
    var06 = test_data_df['variable_06']
    var07 = test_data_df['variable_07']
    var08 = test_data_df['variable_08']

    # create traces from values for plot
    fig_overview = make_subplots(specs=[[{"secondary_y": True}]])

    traces_y1 = []
    traces_y2 = []

    # GENERAL
    traces_y1.append(
        go.Scatter(x=time, y=voltage, mode="lines",
                   name='Cell Voltage [Y1]',
                   line=dict(color=palette[0]),
                   yaxis='y1',
                   visible=True
                   )

    )

    traces_y2.append(
        go.Scatter(x=time, y=current, mode="lines",
                   name='Current [Y2]',
                   line=dict(color=palette[1]),
                   yaxis='y2',
                   visible=True
                   )
    )

    # CELL
    traces_y2.append(
        go.Scatter(x=time, y=temp_cell_cat, mode="lines",
                   name='Cell Temperature (Cathode) [Y2]',
                   line=dict(color=palette[16]),
                   yaxis='y2',
                   visible=True
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=temp_cell_an, mode="lines",
                   name='Cell Temperature (Anode) [Y2]',
                   line=dict(color=palette[17]), yaxis='y2',
                   visible='legendonly'
                   )
    )

    # COOLANT
    traces_y1.append(
        go.Scatter(x=time, y=temp_coolant_inlet,
                   mode="lines",
                   name='Temperature Coolant Inlet [Y2]',
                   line=dict(color=palette[16]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_coolant_outlet,
                   mode="lines",
                   name='Temperature Coolant Outlet [Y2]',
                   line=dict(color=palette[17]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_coolant_diff,
                   mode="lines",
                   name='Temperature Coolant Diff [Y1]',
                   line=dict(color=palette[18]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=pressure_coolant_inlet,
                   mode="lines",
                   name='Pressure Coolant Inlet [Y2]',
                   line=dict(color=palette[19]),
                   yaxis='y2',
                   visible='legendonly')
    )

    traces_y1.append(
        go.Scatter(x=time, y=pressure_coolant_outlet,
                   mode="lines",
                   name='Pressure Coolant Outlet [Y2]',
                   line=dict(color=palette[20]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=pressure_coolant_diff,
                   mode="lines",
                   name='Pressure Coolant Diff [Y1]',
                   line=dict(color=palette[21]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    # ANODE
    traces_y1.append(
        go.Scatter(x=time, y=flow_an, mode="lines",
                   name='Flowrate Anode [Y1]',
                   line=dict(color=palette[2]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_an_inlet, mode="lines",
                   name='Temp Anode Inlet [Y2]',
                   line=dict(color=palette[3]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_an_outlet, mode="lines",
                   name='Temp Anode Outlet [Y2]',
                   line=dict(color=palette[4]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_an_diff, mode="lines",
                   name='Temp Anode Diff. [Y2]',
                   line=dict(color=palette[5]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_an_inlet, mode="lines",
                   name='Pressure Anode Inlet [Y2]',
                   line=dict(color=palette[6]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_an_outlet, mode="lines",
                   name='Pressure Anode Outlet [Y2]',
                   line=dict(color=palette[7]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_an_diff, mode="lines",
                   name='Pressure Anode Diff. [Y1]',
                   line=dict(color=palette[8]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    # CATHODE
    traces_y1.append(
        go.Scatter(x=time, y=flow_cat, mode="lines",
                   name='Flowrate Cathode [Y1]',
                   line=dict(color=palette[9]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_cat_inlet, mode="lines",
                   name='Temp Cathode Inlet [Y2]',
                   line=dict(color=palette[10]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_cat_outlet, mode="lines",
                   name='Temp Cathode Outlet [Y2]',
                   line=dict(color=palette[11]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y1.append(
        go.Scatter(x=time, y=temp_cat_diff, mode="lines",
                   name='Temp Cathode Diff. [Y2]',
                   line=dict(color=palette[12]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_cat_inlet, mode="lines",
                   name='Pressure Cathode Inlet [Y2]',
                   line=dict(color=palette[13]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_cat_outlet, mode="lines",
                   name='Pressure Cathode Outlet [Y2]',
                   line=dict(color=palette[14]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=pressure_cat_diff, mode="lines",
                   name='Pressure Cathode Diff. [Y1]',
                   line=dict(color=palette[15]),
                   yaxis='y1',
                   visible='legendonly'
                   )
    )

    # VARIABLES
    traces_y2.append(
        go.Scatter(x=time, y=var01, mode="lines",
                   name='Load Cycle Count [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=var02, mode="lines",
                   name='AST Cycle Count Pt.1 [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=var03, mode="lines",
                   name='CHAR Cycle Count Pt.1 [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=var04, mode="lines",
                   name='AST Cycle Count Pt.2 [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    traces_y2.append(
        go.Scatter(x=time, y=var08, mode="lines",
                   name='CHAR Cycle Count Pt.2 [Y2]',
                   line=dict(color=palette[15]),
                   yaxis='y2',
                   visible='legendonly'
                   )
    )

    # gather traces in a list which is given to dash-layout-function (drawTestFigureRig)
    traces = traces_y1 + traces_y2

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(

        title='Testbench Parameter',
        title_font=dict(size=30, color='black'),
        title_x=0.5,

        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',

        xaxis=dict(title='duration [h]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   gridcolor='lightgrey',
                   griddash='dash',
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',

                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,
                   ),

        yaxis=dict(title='arbitrary unit',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   gridcolor='lightgrey',
                   griddash='dash',
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,
                   range=[0, 1.2]),

        yaxis2=dict(title='arbitrary unit',
                    overlaying='y',
                    side='right',
                    title_font=dict(size=24, color='black'),
                    tickfont=dict(size=20, color='black'),
                    minor=dict(ticks="inside", ticklen=5, showgrid=False),
                    ticks='inside',
                    ticklen=10,
                    tickwidth=2,

                    linewidth=2,
                    linecolor='black',
                    range=[-10, 120]
                    ),

        legend_font=dict(size=16),
        legend=dict(
            x=1.3,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
        ),
        plot_bgcolor='white',
    )
    return figure

def drawFigurePOLDec():

    file = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\KCS#01\python\dataframes\kcs#01_pol.csv'

    palette = px.colors.qualitative.Bold

    test_data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)

    mask = ()

    test_data_df = test_data_df[
        # test_data_df['File Mark'].str.contains('polcurve_inc', na=False)
        # |
        test_data_df['File Mark'].str.contains('polcurve_dec', na=False)
        ]

    test_data_df['current rounded'] = round(test_data_df['current'], 2)

    char_cycles = test_data_df['variable_20'].unique()

    traces = []

    c = 0
    for i in char_cycles:

        cycle_df = test_data_df[test_data_df['variable_20'] == i].reset_index(drop=True)

        currents = cycle_df['current_set'].unique()

        u = []
        j = []
        erry = []

        for current in currents:
            if current < 46:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'].tail(60).mean())
                j.append(current / 25)
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'].tail(60).std())

        name = cycle_df['Time Stamp'][0]

        traces.append(
            go.Scatter(x=j, y=u, mode="markers+lines", marker=dict(size=10, color=palette[c]), error_y=dict(array=erry),
                       name=name, )
        )
        c += 1

    # AVERAGE POL

    currents = test_data_df['current_set'].unique()

    u = []
    j = []
    erry = []
    errx = []

    for current in currents:
        if current < 46:
            u.append(test_data_df[test_data_df['current_set'] == current]['voltage'].mean())
            j.append(current / 25)
            erry.append(test_data_df[test_data_df['current_set'] == current]['voltage'].std())
            errx.append(0)
    #
    # u.append(test_data_df[test_data_df['current_set'] > 45]['voltage'].tail(60).mean())
    # j.append(test_data_df[test_data_df['current_set'] > 45]['current'].tail(60).mean() / 25)
    # erry.append(test_data_df[test_data_df['current_set'] > 45]['voltage'].tail(60).std())
    # errx.append(test_data_df[test_data_df['current_set'] > 45]['current'].tail(60).std() / 25)

    traces.append(
        go.Scatter(x=j, y=u, mode="markers+lines",
                   marker=dict(size=10, color='black'),
                   error_y=dict(array=erry, thickness=1),
                   error_x=dict(array=errx, thickness=1),
                   name='POL Average')
    )

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(
        # TITLE
        title='POL (decreasing j)',
        title_font=dict(size=30, color='black'),
        title_x=0.4,

        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',

        # XAXIS
        xaxis=dict(title='current density [A/cm²]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   gridcolor='lightgrey',
                   griddash='dash',
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',

                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,
                   range=[0, 2]),

        # YAXIS
        yaxis=dict(title='voltage [V]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   gridcolor='lightgrey',
                   griddash='dash',
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,
                   range=[0, 1.2]),

        # LEGEND
        legend_font=dict(size=16),
        legend=dict(
            x=1.3,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
        ),

        # # ANNOTATIONS
        # annotations=[
        #     {
        #         'x': 1.5,  # x-coordinate of the textbox
        #         'y': 1,  # y-coordinate of the textbox
        #         'xref': 'x',
        #         'yref': 'y',
        #         'text': '''
        #         Temperature:\t80°C
        #         <br>rH (Anode):\t50%
        #         <br>rh (Cathode):\t30%
        #         <br>Flow (H2):\t2l/min
        #         <br>Flow (Air):\t 2S
        #         ''',
        #         'bgcolor': 'lightgray'
        #     }
        # ],

        plot_bgcolor='white',
    )
    return figure

def drawFigurePOLInc():

    file = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\KCS#01\python\dataframes\kcs#01_pol.csv'

    palette = px.colors.qualitative.Bold

    test_data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    test_data_df = test_data_df.sort_values(by='Time Stamp', ascending=True)

    test_data_df = test_data_df[
        test_data_df['File Mark'].str.contains('polcurve_inc', na=False)
        # |
        # test_data_df['File Mark'].str.contains('polcurve_dec', na=False)
        ]

    test_data_df['current rounded'] = round(test_data_df['current'], 2)

    char_cycles = test_data_df['variable_20'].unique()

    traces = []

    c = 0
    for i in char_cycles:

        cycle_df = test_data_df[test_data_df['variable_20'] == i].reset_index(drop=True)

        currents = cycle_df['current_set'].unique()

        u = []
        j = []
        erry = []

        for current in currents:
            if current < 46:
                u.append(cycle_df[cycle_df['current_set'] == current]['voltage'].tail(60).mean())
                j.append(current / 25)
                erry.append(cycle_df[cycle_df['current_set'] == current]['voltage'].tail(60).std())

        name = cycle_df['Time Stamp'][0]

        traces.append(
            go.Scatter(x=j, y=u, mode="markers+lines", marker=dict(size=10, color=palette[c]), error_y=dict(array=erry),
                       name=name, )
        )
        c += 1

    # AVERAGE POL

    currents = test_data_df['current_set'].unique()

    u = []
    j = []
    erry = []
    errx = []

    for current in currents:
        if current < 46:
            u.append(test_data_df[test_data_df['current_set'] == current]['voltage'].mean())
            j.append(current / 25)
            erry.append(test_data_df[test_data_df['current_set'] == current]['voltage'].std())
            errx.append(0)
    #
    # u.append(test_data_df[test_data_df['current_set'] > 45]['voltage'].tail(60).mean())
    # j.append(test_data_df[test_data_df['current_set'] > 45]['current'].tail(60).mean() / 25)
    # erry.append(test_data_df[test_data_df['current_set'] > 45]['voltage'].tail(60).std())
    # errx.append(test_data_df[test_data_df['current_set'] > 45]['current'].tail(60).std() / 25)

    traces.append(
        go.Scatter(x=j, y=u, mode="markers+lines",
                   marker=dict(size=10, color='black'),
                   error_y=dict(array=erry, thickness=1),
                   error_x=dict(array=errx, thickness=1),
                   name='POL Average')
    )

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(
        # TITLE
        title='POL (increasing j)',
        title_font=dict(size=30, color='black'),
        title_x=0.4,
        hoverlabel=dict(bgcolor='white', font_size=14),
        hovermode='x unified',
        # XAXIS
        xaxis=dict(title='current density [A/cm²]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   gridcolor='lightgrey',
                   griddash='dash',
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',

                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,
                   range=[0, 2]),

        # YAXIS
        yaxis=dict(title='voltage [V]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   gridcolor='lightgrey',
                   griddash='dash',
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,
                   range=[0, 1.2]),

        legend_font=dict(size=16),
        legend=dict(
            x=1.3,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
        ),
        plot_bgcolor='white',
    )
    return figure

def drawFigureEIS025a():

    file_025a = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\KCS#01\python\dataframes\eis_025a.csv'

    palette = px.colors.qualitative.Bold

    fig = go.Figure()

    # DATAFRAMES
    data_df_025a = pd.read_csv(file_025a, encoding='cp1252', low_memory=False)

    data_df_025a = data_df_025a.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df_025a['#'].unique())

    c = 0
    for i in count:
        cycle_df_025a = data_df_025a[data_df_025a['#'] == i].reset_index(drop=True)


        name_025a = '#' + str(i) + '_' + cycle_df_025a['date'][0] + ' ' + cycle_df_025a['time'][0]

        z_real_025a = cycle_df_025a['ohm'] * 1000 * 25
        z_imag_025a = cycle_df_025a['ohm.1'] * -1000 * 25

        fig.add_trace(go.Scatter(x=z_real_025a, y=z_imag_025a, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_025a))

        c += 1

    fig.update_layout(
        # TITLE
        title='EIS @0.1A/cm²',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   gridcolor='lightgrey',
                   griddash='dash',
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,
                   linewidth=2,
                   linecolor='black',
                   mirror=True,

                   range=[0, 650]

                   )
        # YAXIS
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   gridcolor='lightgrey',
                   griddash='dash',
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,
                   linewidth=2,
                   linecolor='black',
                   mirror=True,

                   range=[-20, 250]
                   )


    return fig

def drawFigureEIS20a():

    file_20a = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\KCS#01\python\dataframes\eis_20a.csv'

    palette = px.colors.qualitative.Bold

    # create traces from values for plot
    fig = go.Figure()

    # DATAFRAMES
    data_df_20a = pd.read_csv(file_20a, encoding='cp1252', low_memory=False)

    data_df_20a = data_df_20a.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df_20a['#'].unique())

    c = 0
    for i in count:
        cycle_df_20a = data_df_20a[data_df_20a['#'] == i].reset_index(drop=True)

        name_20a = '#' + str(i) + '_' + cycle_df_20a['date'][0] + ' ' + cycle_df_20a['time'][0]

        z_real_20a = cycle_df_20a['ohm'] * 1000
        z_imag_20a = cycle_df_20a['ohm.1'] * -1000

        fig.add_trace(go.Scatter(x=z_real_20a, y=z_imag_20a, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_20a))

        c += 1

    fig.update_layout(
        # TITLE
        title='EIS (Nyquist) @0.8A/cm²',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   gridcolor='lightgrey',
                   griddash='dash',
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',

                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,

                   range=[0, 180]

                    )

        # YAXIS
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   gridcolor='lightgrey',
                   griddash='dash',
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,

                   range=[0, 120]
                   )
    return fig

def drawFigureEIS45a():

    file_45a = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\KCS#01\python\dataframes\eis_45a.csv'

    palette = px.colors.qualitative.Bold

    fig = go.Figure()

    # DATAFRAMES
    data_df_45a = pd.read_csv(file_45a, encoding='cp1252', low_memory=False)

    data_df_45a = data_df_45a.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df_45a['#'].unique())

    c = 0
    for i in count:
        cycle_df_045a = data_df_45a[data_df_45a['#'] == i].reset_index(drop=True)


        name_45a = '#' + str(i) + '_' + cycle_df_045a['date'][0] + ' ' + cycle_df_045a['time'][0]

        z_real_45a = cycle_df_045a['ohm'] * 1000 * 25
        z_imag_45a = cycle_df_045a['ohm.1'] * -1000 * 25

        fig.add_trace(go.Scatter(x=z_real_45a, y=z_imag_45a, mode="markers", marker=dict(size=10, color=palette[c]),
                                 name=name_45a))

        c += 1

    fig.update_layout(
        # TITLE
        title='EIS (Nyquist) @1.8A/cm²',
        title_font=dict(size=30, color='black'),
        title_x=0.5,
        legend_font = dict(size=16),
        legend = dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
    ),
    plot_bgcolor = 'white',
    )
    fig.update_xaxes(title='real [mOhm*cm²]',
                     title_font=dict(size=24, color='black'),
                     tickfont=dict(size=20, color='black'),
                     minor=dict(ticks="inside", ticklen=5, showgrid=False),
                     gridcolor='lightgrey',
                     griddash='dash',
                     showline=True,
                     zeroline=True,
                     zerolinewidth=2,
                     zerolinecolor='black',
                     ticks='inside',
                     ticklen=10,
                     tickwidth=2,
                     linewidth=2,
                     linecolor='black',
                     mirror=True,

                     range=[0, 1000]
                     )
        # YAXIS
    fig.update_yaxes(title='-imag. [mOhm*cm²]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   gridcolor='lightgrey',
                   griddash='dash',
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,
                   linewidth=2,
                   linecolor='black',
                   mirror=True,

                   range=[-20, 600]
                   )


    return fig

def drawFigureCV():
    # -*- coding: utf-8 -*-
    """
    Created on Fri Aug  4 10:42:24 2023

    @author: j.kapp
    """

    from plotly.offline import download_plotlyjs, init_notebook_mode, plot
    from plotly.subplots import make_subplots
    import plotly.graph_objs as go
    import pandas as pd
    import plotly.express as px
    import os

    file = r'W:\Arbeitsgruppe\Abteilung NMT\Gruppe-Materialanalyse\BP Charakterisierung\in-situ\GTS\KCS#01\python\dataframes\gamry_cv01.csv'

    palette = px.colors.qualitative.Bold

    data_df = pd.read_csv(file, encoding='cp1252', low_memory=False)

    data_df = data_df.sort_values(by=['date', 'time'], ascending=[True, True])

    count = sorted(data_df['#'].unique())

    traces = []

    c = 0
    for i in count:
        print(i)
        cycle_df = data_df[data_df['#'] == i]
        cycle_df = cycle_df[cycle_df['#.2'] == 5].reset_index(drop=True)

        try:
            name = '#' + str(i) + '_' + cycle_df['date'][0] + ' ' + cycle_df['time'][0]
        except KeyError:
            name = 'x'
            print(cycle_df['date'])

        u = cycle_df['V vs. Ref.'] * 1000
        j = cycle_df['A'] * 1000 / 25

        traces.append(
            go.Scatter(x=u, y=j, mode="lines", marker=dict(size=10, color=palette[c]), line=dict(color=palette[c]),
                       name=name))
        c += 1

    fig_data = traces

    figure = go.Figure(fig_data).update_layout(
        # TITLE
        title='CV-Analysis (@100 mV/s)',
        title_font=dict(size=30, color='black'),
        title_x=0.5,

        # XAXIS
        xaxis=dict(title='voltage [mV]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   gridcolor='lightgrey',
                   griddash='dash',
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='black',

                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,

                   range=[0, -1000],
                   # autorange='reversed',
                   ),

        # YAXIS
        yaxis=dict(title='current [mA]',
                   title_font=dict(size=24, color='black'),
                   tickfont=dict(size=20, color='black'),
                   gridcolor='lightgrey',
                   griddash='dash',
                   minor=dict(ticks="inside", ticklen=5, showgrid=False),
                   showline=True,
                   zeroline=True,
                   zerolinewidth=2,
                   zerolinecolor='darkgrey',
                   ticks='inside',
                   ticklen=10,
                   tickwidth=2,

                   linewidth=2,
                   linecolor='black',

                   mirror=True,
                   autorange='reversed'
                   ),

        legend_font=dict(size=16),
        legend=dict(
            x=1.2,
            y=1,
            xanchor='right',  # Set the x anchor to 'right'
            yanchor='top',  # Set the y anchor to 'top'
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
        ),
        plot_bgcolor='white',
    )

    return figure