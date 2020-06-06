"""
Model class for the Weather
"""
from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Declare a Base from which concrete classes should extend.
Base = declarative_base()


class Weather(Base):
    ''' the weather class

        Define a class that provides the OR/M - mapping
    '''
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

    def __repr__(self):
        return f'city={self.city}, date={self.date}'
