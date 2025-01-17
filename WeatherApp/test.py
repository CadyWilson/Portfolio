import unittest
from weather_data import WeatherData
from weather_database import WeatherDatabase
from datetime import date

class TestWeatherProject(unittest.TestCase):
    def setUp(self):
        self.weather = WeatherData(42.5195, -70.8967, 10, 31, 2023)
        self.weather.process_weather_data()
        self.db = WeatherDatabase('test.db')

    def test_weather_data_processing(self):
        self.assertIsNotNone(self.weather.five_year_avg_temp)
        self.assertIsNotNone(self.weather.five_year_avg_wind_speed)
        self.assertIsNotNone(self.weather.five_year_sum_precipitation)

    def test_database_insertion(self):
        self.db.add_record(self.weather)
        record = self.db.query_record(42.5195, -70.8967, date(2023, 10, 31))
        self.assertIsNotNone(record)

    def test_temperature_conversion(self):
        temp_f = self.weather.get_mean_temperature_fahrenheit()
        self.assertIsNotNone(temp_f)
        self.assertGreater(temp_f, -459.67)  # Temperature should be above absolute zero

if __name__ == '__main__':
    unittest.main()