from flask import render_template
# from ourpackage import db, app
from dash_package.models import Artist, Year, Gene, ArtistGene

from dash_package import server

@server.route('/')
def index():
    return '''<h3>Art Project</h3> <br>
    <h2><a href=/dashboard/>Dashboard</a></h2><br>
    <h2><a href=/artists/>All artists</a></h2><br>'''




# Returns complete list of artists for all years
@server.route('/artists/')
def artists_index():
    all_artists = Artist.query.all()
    return render_template('artists.html', artists=all_artists)

# Returns list of artist for A year
@server.route('/artists/<int:year>')
def artists_in_year(year):
    what_year = year
    all_artists = Artist.query.join(Year).filter(Year.year == what_year).all()
    return render_template('artists.html', artists=all_artists)

# Returns biographical data for an artist
@server.route('/artist/<name>/')
def artist_info(name):
    artists = Artist.query.filter(Artist.name.like('%'+name+'%')).all()
    if len(artists) == 1:
        artist = artists[0]
        return render_template('artist_info.html', artist=artist)
    else:
        return render_template('artists_info.html', artists=artists)

# Returns Data of an Artist for a given Year
@server.route('/artist/<name>/<int:year>/')
def artist_year(name, year):
    all_artists = Artist.query.filter(Artist.name.like('%'+name+'%')).all()
    first_id = all_artists[0].id
    yearly_info = Year.query.join(Artist).filter(Year.artist_id == first_id).filter(Year.year == year).first()
    return render_template('year_info.html', artist=all_artists[0], year=yearly_info)

@server.route('/artist/<name>/auction/')
def artist_auction(name):
    all_artists = Artist.query.filter(Artist.name.like('%'+name+'%')).all()
    first_id = all_artists[0].id
    yearly_info = Year.query.join(Artist).filter(Year.artist_id == first_id).all()
    return render_template('years_info.html', artist=all_artists[0], year=yearly_info)



# Artist.query.join(Year).filter(Year.year == year).all()

@server.route('/testings')
def testing():
    return render_template('artists.html', artists=[{'name': 'Vicente'}, {'name': 'Emilia'},
    {'name': 'Emiliaa'}, {'name': 'Emiliaaa'}])
