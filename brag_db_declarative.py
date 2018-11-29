import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from credentials import user, password
 
Base = declarative_base()
 
class Journal(Base):
    __tablename__ = 'journal'
    id = Column(Integer, Sequence('journal_id_seq'), primary_key=True)
    title = Column(String(250), nullable=False)
    impact_factor = Column(Numeric)
    def __repr__(self):
        return "<Journal(title='%s', impact_factor='%s')>" % (self.title, self.impact_factor)

engine = create_engine('postgresql+psycopg2://' + user + ':' + password + '@localhost:5432/brag')
Base.metadata.create_all(engine)