from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    gender = Column(Text)
    birthday = Column(Integer)
    deathday = Column(Integer)
#     hometown = Column(Text)
    location = Column(Text)
    nationality = Column(Text)
    years = relationship('Year', back_populates='artist')
    genes = relationship('Gene', secondary='artists_genes')

class Year(Base):
    __tablename__ = 'years'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    rank = Column(Integer)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    artist = relationship('Artist', back_populates='years')
    totalsold = Column(Integer)
    totallots =  Column(Integer)
    maxprice = Column(Integer)

#if no display_name, name
class Gene(Base):
    __tablename__= 'genes'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    artists = relationship('Artist', secondary='artists_genes')

class ArtistGene(Base):
    __tablename__ = 'artists_genes'
    artist_id = Column(Integer, ForeignKey('artists.id'), primary_key=True)
    gene_id = Column(Integer, ForeignKey('genes.id'), primary_key=True)

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
