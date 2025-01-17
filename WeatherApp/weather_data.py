
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import numpy as np

class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.five_year_avg_temp = None
        self.five_year_min_temp = None
        self.five_year_max_temp = None
        self.five_year_avg_wind_speed = None
        self.five_year_min_wind_speed = None
        self.five_year_max_wind_speed = None
        self.five_year_sum_precipitation = None
        self.five_year_min_precipitation = None
        self.five_year_max_precipitation = None

    def fetch_weather_data(self):
        cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session=retry_session)

        end_date = f"{self.year}-{self.month:02d}-{self.day:02d}"
        start_date = f"{self.year - 5}-{self.month:02d}-{self.day:02d}"

        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": start_date,
            "end_date": end_date,
            "daily": ["temperature_2m_mean", "wind_speed_10m_max", "precipitation_sum"],
            "timezone": "America/New_York"
        }

        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        daily = response.Daily()

        daily_data = {
            "date": pd.date_range(
                start=pd.to_datetime(daily.Time(), unit="s", utc=True),
                end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=daily.Interval()),
                inclusive="left"
            ),
            "temperature_2m_mean": daily.Variables(0).ValuesAsNumpy(),
            "wind_speed_10m_max": daily.Variables(1).ValuesAsNumpy(),
            "precipitation_sum": daily.Variables(2).ValuesAsNumpy()
        }

        return pd.DataFrame(data=daily_data)

    def process_weather_data(self):
        df = self.fetch_weather_data()
        target_date = pd.to_datetime(f"{self.year}-{self.month:02d}-{self.day:02d}")
        df['date'] = pd.to_datetime(df['date'])
        df = df[df['date'].dt.month == self.month]
        df = df[df['date'].dt.day == self.day]

        self.five_year_avg_temp = np.mean(df['temperature_2m_mean'])
        self.five_year_min_temp = np.min(df['temperature_2m_mean'])
        self.five_year_max_temp = np.max(df['temperature_2m_mean'])
        self.five_year_avg_wind_speed = np.mean(df['wind_speed_10m_max'])
        self.five_year_min_wind_speed = np.min(df['wind_speed_10m_max'])
        self.five_year_max_wind_speed = np.max(df['wind_speed_10m_max'])
        self.five_year_sum_precipitation = np.sum(df['precipitation_sum'])
        self.five_year_min_precipitation = np.min(df['precipitation_sum'])
        self.five_year_max_precipitation = np.max(df['precipitation_sum'])

    def get_mean_temperature_fahrenheit(self):
        return (self.five_year_avg_temp * 9/5) + 32

    def get_max_wind_speed_mph(self):
        return self.five_year_max_wind_speed * 2.23694  # Convert m/s to mph

    def get_precipitation_sum_inches(self):
        return self.five_year_sum_precipitation * 0.0393701  # Convert mm to inches

