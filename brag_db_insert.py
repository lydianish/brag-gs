from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from brag_db_declarative import Journal, Base
from credentials import user, password

engine = create_engine('postgresql+psycopg2://' + user + ':' + password + '@localhost:5432/brag')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

import csv
with open('journals.csv', newline='') as csvfile:
    journals = csv.DictReader(csvfile, delimiter=';')
    for row in journals:
        session.add(Journal(title=row['Title'], impact_factor=row['ImpactFactor']))

session.commit()