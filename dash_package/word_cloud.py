import plotly
import plotly.graph_objs as go
from plotly.offline import plot
import random

from dash_package.models import Artist, Year, Gene, ArtistGene


words = dir(go)[:30]
colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(30)]
weights = [random.randint(15, 35) for i in range(30)]


data = go.Scatter(x=[random.random() for i in range(30)],
                 y=[random.random() for i in range(30)],
                 mode='text',
                 text=words,
                 marker={'opacity': 0.3},
                 textfont={'size': weights,
                           'color': colors})
layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                    'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
fig = go.Figure(data=[data], layout=layout)

plot(fig)
