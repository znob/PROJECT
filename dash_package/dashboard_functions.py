from dash_package.models import Artist, Year, Gene, ArtistGene
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import random

def artist_comparison_years(value1, value2):
    artist1 = Artist.query.filter(Artist.name == value1).first()
    years1 = artist1.years
    artist2 = Artist.query.filter(Artist.name == value2).first()
    years2 = artist2.years
    years = [years1, years2]
    artists = [artist1, artist2]
    x_axis = [x.name for x in artists]
    y_years = [len(x) for x in years]
    y_ts = []
    y_tl = []
    y_max = []
    for year in years:
        tx = [x.totalsold for x in year]
        tl = [x.totallots for x in year if x.totallots]
        # max = [x.maxprice for x in year]
        y_ts.append(sum(tx)/len(tx)/1000000000)
        y_tl.append(sum(tl)/len(tl))
        # y_max.append(sum(max)/len(max))
    trace1 = go.Bar(x = x_axis, y =y_years, name = 'Years appeared')
    trace2 = go.Bar(x = x_axis, y =y_ts, name = 'Avg Sold in millions')
    trace3 = go.Bar(x = x_axis, y =y_tl, name = 'Avg Pieces Sold')
    # trace4 = go.Bar(x = x_axis, y =y_max, name = 'Max Price Achieved')

    layout = go.Layout(title= 'Artist Comparison', barmode='group', yaxis={'title': 'Years'})
    fig1 = go.Figure(data = [trace3, trace2], layout=layout)
    fig2 = go.Figure(data = [trace1], layout=layout)
    return fig2

def artist_comparison_ts(value1, value2):
    artist1 = Artist.query.filter(Artist.name == value1).first()
    years1 = artist1.years
    artist2 = Artist.query.filter(Artist.name == value2).first()
    years2 = artist2.years
    years = [years1, years2]
    artists = [artist1, artist2]
    x_axis = [x.name for x in artists]
    y_years = [len(x) for x in years]
    y_ts = []
    y_tl = []
    y_max = []
    for year in years:
        tx = [x.totalsold for x in year]
        tl = [x.totallots for x in year if x.totallots]
        # max = [x.maxprice for x in year]
        y_ts.append(sum(tx)/len(tx)/1000000)
        y_tl.append(sum(tl)/len(tl))
        # y_max.append(sum(max)/len(max))
    trace1 = go.Bar(x = x_axis, y =y_years, name = 'Years appeared')
    trace2 = go.Bar(x = x_axis, y =y_ts, name = 'Avg Sold in millions')
    trace3 = go.Bar(x = x_axis, y =y_tl, name = 'Avg Pieces Sold')
    # trace4 = go.Bar(x = x_axis, y =y_max, name = 'Max Price Achieved')

    layout = go.Layout(title= 'Artist Comparison', barmode='group', yaxis={'title': 'Millions'})
    fig1 = go.Figure(data = [trace2], layout=layout)
    fig2 = go.Figure(data = [trace1], layout=layout)
    return fig1




def artist_turnover_2017():
    all_artists = Artist.query.join(Year).filter(Year.year == 2017).all()
    all_years = Year.query.filter(Year.year == 2017).all()
    x_list = [year.rank for year in all_years]
    y_list = [year.totalsold for year in all_years]
    text = [artist.name for artist in all_artists]
    return {'x': x_list, 'y': y_list, 'text': text, 'mode': 'markers'}

def artist_turnover_year(value1, value2):
    year1 = value1
    year2 = value2
    all_artists = []
    artists1 = Artist.query.join(Year).filter(Year.year == year1).all()
    artists2 = Artist.query.join(Year).filter(Year.year == year2).all()
    all_artists = artists1
    all_artists += artists2
    all_artists = list(set(all_artists))
    x_list = []
    y_list = []
    for artist in all_artists:
        x = -50
        y = -50
        years = artist.years
        for year in years:
            if year.year == year1:
                x = year.rank
            elif year.year == year2:
                y = year.rank
        y_list.append(y)
        x_list.append(x)
    # print(x_list, y_list)
    text = [artist.name for artist in all_artists]
    return {'x': x_list, 'y': y_list, 'text': text, 'mode': 'markers'}

def all_genes_dropdown():
    all_genes = Gene.query.all()
    gene_list = []
    for gene in all_genes:
        gene_list.append({'label': gene.name, 'value':gene.name})
    return gene_list

def all_artists_dropdown():
    all_artists = Artist.query.all()
    artist_list = []
    for artist in all_artists:
        artist_list.append({'label': artist.name, 'value':artist.name})
    return artist_list

def artists_similar_genes(values):
    if len(values) == 0:
        return ["Please select some genes"]
    elif len(values) == 1:
        gene = Gene.query.filter(Gene.name == values[0]).first()
        artists = gene.artists
        print(values)
        return similar_genes_cloud(artists)
        # return [artist.name for artist in gene.artists]
    else:
        gene_artist_list = []
        for value in values:
            gene_artist_list.append(set(Gene.query.filter(Gene.name == value).first().artists))
        x = gene_artist_list[-1]
        result_set = x.intersection(*gene_artist_list[:-1])
        # figure out how to do multiple set intersections
        return similar_genes_cloud(list(result_set))
        # return [artist.name for artist in list(result_set)]

def similar_genes_cloud(artists):
    weight_name = [(artist.years, artist.name) for artist in artists]

    x_list = [len(x[0]) for x in weight_name]
    y_values = []
    total_sold = []
    for t in weight_name:
        years = t[0]
        avg_rank = sum([x.rank for x in years])/len(years)
        sum_total = round(sum([x.totalsold for x in years])/1000000,2)
        y_values.append(avg_rank)
        total_sold.append(sum_total)

    name = [x[1] for x in weight_name]
    name_total = zip(name, total_sold)

    text = [f'{x[0]} {x[1]} million' for x in name_total]

##########TEST########


    words = name
    colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(len(x_list))]
    weights = [len(x[0])*8 for x in weight_name]

    data = go.Scatter(x=[random.random() for i in range(len(words))],
                     y=random.choices(range(len(words)), k=len(words)),
                     mode='text',
                     text=words,
                     hoverinfo= 'text' ,
                     marker={'opacity': 0.3},
                     textfont={'size': weights,
                               'color': colors})
    layout = go.Layout({'autosize': False, 'height':800, 'width': 1800,
                        'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
    fig = go.Figure(data=[data], layout=layout)
    return fig
#########TEST##ENDS############
    # return {'x': x_list, 'y': y_values, 'mode': 'text', 'text': text, 'mode': 'markers'}

def total_yearly_sales():
    years = list(range(2007,2018))
    all_artists = [Year.query.filter(Year.year == year).all()for year in years]
    x_list = years
    y_list = []
    modern_gene = Gene.query.filter(Gene.name == 'Modern').first()
    modern_list = []
    for year in all_artists:
        y_list.append(sum([artist.totalsold for artist in year if modern_gene not in artist.artist.genes]))
        modern_list.append(sum([artist.totalsold for artist in year if modern_gene in artist.artist.genes]))


    trace1 = go.Bar(x = x_list, y =y_list, name = 'Non-Modern Art')
    trace2 = go.Bar(x = x_list, y =modern_list, name = 'Modern Art')
    data = [trace1, trace2]
    layout = go.Layout({'autosize':False, 'height': 800, 'width': 1800 }, barmode= 'stack', xaxis = {'title' : 'Years', 'showticklabels': True, 'dtick': 1})
    return go.Figure(data=data, layout=layout)

def artists_similar_artists(values):
    if len(values) == 0:
        return ["Please select some Artists"]
    elif len(values) == 1:
        artist = Artist.query.filter(Artist.name == values[0]).first()
        return artists_similar_genes([x.name for x in artist.genes])
    else:
        artists_list = []
        for value in values:
            artists_list.append(Artist.query.filter(Artist.name == value).first().genes)
        genes_list = [*artists_list]
        gene = list(set([x.name for x in genes_list]))
        return artists_similar_genes(gene)

def male_to_female():
    male = Artist.query.filter(Artist.gender == 'male').all()
    female = Artist.query.filter(Artist.gender == 'female').all()
    unknown = len(Artist.query.all()) - len(male) - len(female)
    labels = ['Male', 'Female', 'Unknown']
    values = [len(male), len(female), unknown]
    trace = go.Pie(labels = labels, values = values, hoverinfo = 'label+percent')
    layout = go.Layout(title = '% Presence by gender')
    return go.Figure(data=[trace], layout=layout)

def female_timeseries():
    female = Artist.query.filter(Artist.gender == 'female').all()
    male = Artist.query.filter(Artist.gender == 'male').all()
    x_list =list(range(2007,2018))

    all_female_artists = counting_years(female)
    all_male_artists = counting_years(male)

    y_list1 = counting_items(x_list, all_female_artists)
    y_list2 = counting_items(x_list, all_male_artists)

    y_list3 = [(500 -y[0]-y[1]) for y in zip(y_list1,y_list2)]

    trace1 = go.Bar(x = x_list, y =y_list1, name = '# of Female artists')
    trace2 = go.Bar(x = x_list, y =y_list2, name = '# of Male artists')
    trace3 = go.Bar(x = x_list, y =y_list3, name = '# Unknown')
    layout = go.Layout(title= 'Number of artists by Gender', barmode= 'stack', xaxis = {'title' : 'Years', 'showticklabels': True, 'dtick': 1})
    return go.Figure(data = [trace3, trace2, trace1], layout=layout)

def counting_years(artists):
    listy = [artist.years for artist in artists]
    larger_listy =  []
    for artist in listy:
        larger_listy += artist
    return larger_listy

def counting_items(years, artists):
    y_list = []
    for x in years:
        i = 0
        for year in artists:
            if year.year == x:
                i += 1
        y_list.append(i)
    return y_list
