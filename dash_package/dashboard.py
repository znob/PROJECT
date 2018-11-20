from dash_package import app, dash
from flask import render_template
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_package.dashboard_functions import *

def job_salaries():
    listing_titles = ['engineer', 'data scientist', 'product manager']
    listing_prices = [4, 55, 6]
    return {'x': listing_titles, 'y': listing_prices}


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div(
    children=[
    dcc.Tabs(id="tabs",
        children=[
            dcc.Tab(id='Yearly-tot-sales', label='Sales per Year',
                children=[
                html.Div(
                    dcc.Graph(figure=
                    total_yearly_sales()))

                    ]
                ),
            dcc.Tab(id='genders-in-art', label='Gender',
                children=[
                html.Div([
                    html.Div(
                        dcc.Graph(id = 'male-to-female',figure= male_to_female()),
                        style={'width': '48%', 'display': 'inline-block'}),
                    html.Div(
                        dcc.Graph(id='female-timeseries', figure= female_timeseries()),
                        style={'width': '48%', 'float': 'right', 'display': 'inline-block'})

                        ]
                    )]),
            dcc.Tab(id='Gene-Artist-Recommendation', label='Gene Recommendation',
                children=[
                dcc.Dropdown(
                    id ='gene-dropdown',
                    options=all_genes_dropdown(),
                    value=['Modern'],
                    multi=True),
                dcc.Graph(id='recommendations-output')
                    ]
                ),
            dcc.Tab(id='artist-comparison', label='Artist Comparison',
                children=[
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id ='artist1-dropdown',
                            options=all_artists_dropdown(),
                            value='Pablo Picasso',
                            multi=False)
                            ],
                            style={'width': '48%', 'display': 'inline-block'}),
                    html.Div([
                        dcc.Dropdown(
                            id ='artist2-dropdown',
                            options=all_artists_dropdown(),
                            value='Andy Warhol',
                            multi=False)
                            ],
                            style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
                            ]),
                    # html.Div(id='artists-comparison')
                dcc.Graph(id='artists-comparison-years')
                            , dcc.Graph(id='artists-comparison-ts')
                            ])
                    ,
            dcc.Tab(id='rank-over-years', label='Rank over Years',
                children=[
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id ='year1-dropdown',
                            options=[{'label': str(x), 'value': x} for x in list(range(2007,2018))],
                            value=2017,
                            multi=False)
                            ],
                            style={'width': '48%', 'display': 'inline-block'}),
                    html.Div([
                        dcc.Dropdown(
                            id ='year2-dropdown',
                            options=[{'label': str(x), 'value': x} for x in list(range(2007,2018))],
                            value=2016,
                            multi=False)

                    ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
                ]),
                dcc.Graph(id='rank-year-output')

                        ]
                    )
                ]
            )

                    ]
                )

@app.callback(
    dash.dependencies.Output('artists-comparison-years', 'figure'),
    [dash.dependencies.Input('artist1-dropdown', 'value'),
     dash.dependencies.Input('artist2-dropdown', 'value')])
def update_output(value1, value2):
    return artist_comparison_years(value1, value2)

@app.callback(
    dash.dependencies.Output('artists-comparison-ts', 'figure'),
    [dash.dependencies.Input('artist1-dropdown', 'value'),
     dash.dependencies.Input('artist2-dropdown', 'value')])
def update_output(value1, value2):
    return artist_comparison_ts(value1, value2)
    # return {'data': [artist_turnover_year(value1, value2)],
    #     'layout': {'title': f'Rank comparison in {value1} and {value2}',
    #     'autosize': False, 'width': 1000, 'height': 1000,
    #     'xaxis' : {'title': f'rank {value1}'},
    #     'yaxis' : {'title' : f'rank {value2}'}
    #             }}



@app.callback(
    dash.dependencies.Output('rank-year-output', 'figure'),
    [dash.dependencies.Input('year1-dropdown', 'value'),
     dash.dependencies.Input('year2-dropdown', 'value')])
def update_output(value1, value2):
    return {'data': [artist_turnover_year(value1, value2)],
        'layout': {'title': f'Rank comparison in {value1} and {value2}',
        'autosize': False, 'width': 1000, 'height': 1000,
        'xaxis' : {'title': f'rank {value1}'},
        'yaxis' : {'title' : f'rank {value2}'}
                }}


@app.callback(
    dash.dependencies.Output('recommendations-output', 'figure'),
    [dash.dependencies.Input('gene-dropdown', 'value')])
def update_output(gene_names):
    return artists_similar_genes(gene_names) if gene_names != [] else artists_similar_genes('Modern')
