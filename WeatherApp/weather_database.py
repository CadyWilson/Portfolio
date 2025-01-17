from sqlalchemy import create_engine, Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = sqlalchemy.orm.declarative_base()

class WeatherRecord(Base):
    __tablename__ = 'weather_records'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)
    five_year_avg_temp = Column(Float)
    five_year_min_temp = Column(Float)
    five_year_max_temp = Column(Float)
    five_year_avg_wind_speed = Column(Float)
    five_year_min_wind_speed = Column(Float)
    five_year_max_wind_speed = Column(Float)
    five_year_sum_precipitation = Column(Float)
    five_year_min_precipitation = Column(Float)
    five_year_max_precipitation = Column(Float)

class WeatherDatabase:
    def __init__(self, db_name='weather.db'):
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_record(self, weather_data):
        session = self.Session()
        record = WeatherRecord(
            latitude=weather_data.latitude,
            longitude=weather_data.longitude,
            month=weather_data.month,
            day=weather_data.day,
            year=weather_data.year,
            five_year_avg_temp=weather_data.five_year_avg_temp,
            five_year_min_temp=weather_data.five_year_min_temp,
            five_year_max_temp=weather_data.five_year_max_temp,
            five_year_avg_wind_speed=weather_data.five_year_avg_wind_speed,
            five_year_min_wind_speed=weather_data.five_year_min_wind_speed,
            five_year_max_wind_speed=weather_data.five_year_max_wind_speed,
            five_year_sum_precipitation=weather_data.five_year_sum_precipitation,
            five_year_min_precipitation=weather_data.five_year_min_precipitation,
            five_year_max_precipitation=weather_data.five_year_max_precipitation
        )
        session.add(record)
        session.commit()
        session.close()

    def query_record(self, latitude, longitude, query_date):
        session = self.Session()
        record = session.query(WeatherRecord).filter_by(
            latitude=latitude,
            longitude=longitude,
            month=query_date.month,
            day=query_date.day,
            year=query_date.year
        ).first()
        session.close()
        return record

    def display_record(self, record):
        if record:
            print("\nWeather Record:")
            print(f"Location: {record.latitude}°N, {record.longitude}°E")
            print(f"Date: {record.year}-{record.month:02d}-{record.day:02d}")
            print(f"5-Year Avg Temperature: {record.five_year_avg_temp:.2f}°C")
            print(f"5-Year Min Temperature: {record.five_year_min_temp:.2f}°C")
            print(f"5-Year Max Temperature: {record.five_year_max_temp:.2f}°C")
            print(f"5-Year Avg Wind Speed: {record.five_year_avg_wind_speed:.2f} m/s")
            print(f"5-Year Min Wind Speed: {record.five_year_min_wind_speed:.2f} m/s")
            print(f"5-Year Max Wind Speed: {record.five_year_max_wind_speed:.2f} m/s")
            print(f"5-Year Sum Precipitation: {record.five_year_sum_precipitation:.2f} mm")
            print(f"5-Year Min Precipitation: {record.five_year_min_precipitation:.2f} mm")
            print(f"5-Year Max Precipitation: {record.five_year_max_precipitation:.2f} mm")
        else:
            print("No record found for the given location and date.")

    def show_all_records(self):
        session = self.Session()
        records = session.query(WeatherRecord).all()
        session.close()

        if records:
            print("\nAll Weather Records:")
            print("-" * 100)
            print(f"{'ID':<5}{'Latitude':<10}{'Longitude':<11}{'Date':<12}{'Avg Temp':<10}{'Min Temp':<10}{'Max Temp':<10}{'Avg Wind':<10}{'Min Wind':<10}{'Max Wind':<10}{'Sum Precip':<12}")
            print("-" * 100)
            for record in records:
                print(f"{record.id:<5}{record.latitude:<10.2f}{record.longitude:<11.2f}{f'{record.year}-{record.month:02d}-{record.day:02d}':<12}{record.five_year_avg_temp:<10.2f}{record.five_year_min_temp:<10.2f}{record.five_year_max_temp:<10.2f}{record.five_year_avg_wind_speed:<10.2f}{record.five_year_min_wind_speed:<10.2f}{record.five_year_max_wind_speed:<10.2f}{record.five_year_sum_precipitation:<12.2f}")
        else:
            print("No records found in the database.")