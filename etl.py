""" a simple ETL modulle """

from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Create the engine --> echo=True utiizes the integration with Python logging to display SQL
# To make the output more brief set ```echo=False```.
# conn_string = 'sqlite:///:memory:'
conn_string = 'sqlite:///etl.db'
engine = create_engine(conn_string, echo=False)

# Declare a Base from which concrete classes should extend.
Base = declarative_base()

# Define a class that provides the OR/M - mapping
class Weather(Base):
    ''' the weather class '''
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)

    city = Column(String)
    date = Column(Date)
    actual_mean_temp = Column(Integer)
    actual_min_temp = Column(Integer)
    actual_max_temp = Column(Integer)

    actual_precipitation = Column(Float)
    average_precipitation = Column(Float)
    record_precipitation = Column(Float)

    reserved2 = Column(String)

## We do not want to do this in production - it creates the tables ...
Base.metadata.create_all(engine)

# Make a session
Session = sessionmaker(bind=engine)
session = Session()

# Populate from file
df_with_reserved = pd.read_table('KPHX_with_reserved.dat', sep='|', header=0,
                                 usecols=[
                                     'id', 'city', 'date', 'actual_mean_temp', 'actual_min_temp', 'actual_max_temp', 'actual_precipitation', 'average_precipitation', 'record_precipitation', 'reserved2'
                                 ],
                                 dtype={
                                     'id': 'int', 'city': 'string',
                                     # 'date': '?', # let parser handle the converion - see https://stackoverflow.com/questions/21269399/datetime-dtypes-in-pandas-read-csv
                                     'actual_mean_temp': 'int8', 'actual_min_temp': 'int8', 'actual_max_temp': 'int8',
                                     # 'actual_precipitation','average_precipitation','record_precipitation',
                                     'reserved2': 'string'
                                 },
                                 # These next three are needed to parse and optimize datetime input handling
                                 parse_dates=[2],
                                 infer_datetime_format=True,
                                 date_parser=pd.to_datetime
                                 )

for index, row in df_with_reserved.iterrows():
    w = Weather(**row)
    session.add(w)

session.commit()
