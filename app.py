# import dash
# from dash import html, dcc
# from dash.dependencies import Input, Output
# import plotly.graph_objs as go
# import plotly.express as px
# import pandas as pd
# import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components


# app = dash.Dash(__name__)

# colors = {
#     'background': '#FFFFFF',
#     'text': '#61CA21'
# }

# songs = pd.read_csv("List of most-streamed songs on Spotify.csv")

# fig = px.bar(songs, x="Song", y="Streams (Billions)", barmode="group")

# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#     html.H1(
#         children='Top 100 spotify songs',
#         style={
#             'textAlign': 'center',
#             'color': colors['text'],
#             'fontSize': '40px'
#         }
#     ),

#     html.Div(children='Project DASH by Indira Patricio Laura', style={
#         'textAlign': 'center',
#         'color': 'gray',
#         'fontSize': '25px'
#     }),

#     dcc.Graph(
#         id='example-graph-2',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


#=========================================================================
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('top50MusicFrom2010-2019.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="Beats.Per.Minute -The tempo of the song", y="Popularity- The higher the value the more popular the song is",
                     size="Popularity- The higher the value the more popular the song is", color="the genre of the track", hover_name="artist",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

# =========================================================================
# from dash import Dash, html, dcc
# import plotly.express as px
# import pandas as pd

# app = Dash(__name__)

# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#      app.run_server(debug=True)
       
    
# =========================================================================
# from dash import Dash, dcc, Output, Input  # pip install dash
# import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
# import plotly.express as px
# import pandas as pd                        # pip install pandas

# # incorporate data into app
# # Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
# df = pd.read_csv("social_capital.csv")
# print(df.head())

# # Build your components
# app = Dash(__name__, external_stylesheets=[dbc.themes.LUX]) # a nice theme
# mytitle = dcc.Markdown(children='')
# mygraph = dcc.Graph(figure={})
# dropdown = dcc.Dropdown(options=df.columns.values[2:], # means I take only from the third column Cesarian and on
#                         value='Cesarean Delivery Rate',  # initial value displayed when page first loads
#                         clearable=False)

# # Customize your own Layout
# app.layout = dbc.Container([
#     dbc.Row([
#         dbc.Col([mytitle], width=6)
#     ], justify='center'),
#     dbc.Row([
#         dbc.Col([mygraph], width=12)
#     ]),
#     dbc.Row([
#         dbc.Col([dropdown], width=6)
#     ], justify='center'),

# ], fluid=True)

# # Callback allows components to interact
# @app.callback(
#     Output(mygraph, 'figure'),
#     Output(mytitle, 'children'),
#     Input(dropdown, 'value')
# )
# def update_graph(column_name):  # function arguments come from the component property of the Input

#     print(column_name)
#     print(type(column_name))
#     # https://plotly.com/python/choropleth-maps/
#     fig = px.choropleth(data_frame=df,
#                         locations='STATE',
#                         locationmode="USA-states",
#                         scope="usa",
#                         height=600,
#                         color=column_name,
#                         animation_frame='YEAR')

#     return fig, '# '+column_name  # returned objects are assigned to the component property of the Output

# if __name__ == '__main__':
#      app.run_server(debug=True)
        
# =========================================================================