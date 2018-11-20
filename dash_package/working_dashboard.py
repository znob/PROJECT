from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_package.models import Artist, Year, Gene, ArtistGene

def artist_turnover_2017():
    all_artists = Artist.query.join(Year).filter(Year.year == 2017).all()
    all_years = Year.query.filter(Year.year == 2017).all()
    x_list = [year.rank for year in all_years]
    y_list = [year.totalsold for year in all_years]
    text = [artist.name for artist in all_artists]
    return {'x': x_list, 'y': y_list, 'text': text, 'mode': 'markers'}

def artist_turnover_year(year):
    all_artists = Artist.query.join(Year).filter(Year.year == year).all()
    all_years = Year.query.filter(Year.year == year).all()
    x_list = [year.rank for year in all_years]
    y_list = [year.totalsold for year in all_years]
    text = [artist.name for artist in all_artists]
    return {'x': x_list, 'y': y_list, 'text': text, 'mode': 'markers'}

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
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(id='2017 turnover', label='2017 turnover',
            children=[
            dcc.Graph(figure=
            {'data': [artist_turnover_2017()],
            'layout': {'title': 'Artist turnover 2017'}})
            ]
        ),


        dcc.Tab(id='Yearly tab with input', label='Year turnover',
            children=[
            dcc.Graph(figure=
            {'data': [job_salaries()],
            'layout': {}})
            ]
        )

        ])
    ]
)
