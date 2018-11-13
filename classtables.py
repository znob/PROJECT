from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    years = relationship('Auction', back_populates='auctions')
    genes = relationship('Gene', back_populates='artists')

class Auction(Base):
    __tablename__ = 'auctions'
    id = Column(Integer, primary_key=True)
    year = Column(Text)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    artist = relationship('Artist', back_populates='years')
    totalsold = Column(Integer)
    totallots =  Column(Integer)
    maxprice = Column(Integer)

class Gene(Base):
    __tablename__= 'genes'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    artists = relationship('Artist', back_populates='genes')


engine = create_engine('sqlite:///artists.db', echo=True)
Base.metadata.create_all(engine)
