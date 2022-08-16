from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

#Carga dateset
df_happiness = pd.read_csv('./data/Happiness_final.csv')

#Ploteo en un mapa los paises y que el tamaño de su ubicacion varie segun el Score de la felicidad, y desplazarme segun los años
def plot_map():
    df_happiness["Score"] = pd.to_numeric(df_happiness["Score"])
    fig = px.scatter_geo(df_happiness,lat='latitud',lon='longitud',hover_name="Country",
                         color="Country",size = "Score"
                         ,animation_frame="Year",projection="natural earth",height=600)
    fig.update_layout(title = 'Happiness Map', title_x=0.5)
    return fig

app.layout = html.Div(children=[
    html.H1(children='DASHBOARD WORLD HAPPINESS'),

    html.Div(children='''
        Dashboard for Coderhouse project
    '''),

    dcc.Graph(
        id='map-graph',
        figure=plot_map()
    ),
    dcc.Dropdown(
        id="dropdown",
        options=df_happiness["Country"].unique(),
        value="Argentina"
    ),
    dcc.Graph(
        id='graph-lines'
    )
])

#Ploteo los distintos indices que me da el reporte a traves de los años y filtro por pais
@app.callback(
    Output("graph-lines", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(dims):
    fig = go.Figure()
    fig_tmp = px.line(
    df_happiness.loc[df_happiness["Country"].eq(dims)],
    x="Year",
    y=["Score","Economy","Family","Health","Freedom","Corruption","Generosity"],
    markers=True,
    ).update_traces(legendgroup=dims, legendgrouptitle_text=dims)
    fig.add_traces(fig_tmp.data)
    fig.update_layout(fig_tmp.layout)
    fig.update_layout(title = 'Lines Chart', title_x=0.5)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True,port=8051,host='0.0.0.0')