from dash_package import db

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    gender = db.Column(db.Text)
    birthday = db.Column(db.Integer)
    deathday = db.Column(db.Integer)
#     hometown = db.Column(db.Text)
    location = db.Column(db.Text)
    nationality = db.Column(db.Text)
    years = db.relationship('Year', back_populates='artist')
    genes = db.relationship('Gene', secondary='artists_genes')

class Year(db.Model):
    __tablename__ = 'years'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist', back_populates='years')
    totalsold = db.Column(db.Integer)
    totallots =  db.Column(db.Integer)
    maxprice = db.Column(db.Integer)

#if no display_name, name
class Gene(db.Model):
    __tablename__= 'genes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    artists = db.relationship('Artist', secondary='artists_genes')

class ArtistGene(db.Model):
    __tablename__ = 'artists_genes'
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), primary_key=True)
    gene_id = db.Column(db.Integer, db.ForeignKey('genes.id'), primary_key=True)

# engine = create_engine('sqlite:///artsy.db')
