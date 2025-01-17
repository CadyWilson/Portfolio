from weather_data import WeatherData
from weather_database import WeatherDatabase
from datetime import date

def main():
    # Create an instance of WeatherData for Salem, MA on October 31, 2023
    weather = WeatherData(42.5195, -70.8967, 10, 31, 2023)

    # Process the weather data
    weather.process_weather_data()


       # Create an instance of WeatherDatabase
    db = WeatherDatabase()

    # Add the weather record to the database
    db.add_record(weather)
  

    # Query and display the record
    query_date = date(2023, 10, 31)
    record = db.query_record(42.5195, -70.8967, query_date)
    db.display_record(record)

    # Call methods to get daily weather variables
    mean_temp_f = weather.get_mean_temperature_fahrenheit()
    max_wind_speed_mph = weather.get_max_wind_speed_mph()
    precipitation_sum_inches = weather.get_precipitation_sum_inches()

    # Print the results
    print(f"Five-year average temperature on Oct 31: {mean_temp_f:.2f}°F")
    print(f"Five-year maximum wind speed on Oct 31: {max_wind_speed_mph:.2f} mph")
    print(f"Five-year sum precipitation on Oct 31: {precipitation_sum_inches:.2f} inches")

# Query and display the record
    query_date = date(2023, 10, 31)
    record = db.query_record(42.5195, -70.8967, query_date)
    db.display_record(record)

    # Display daily weather variables
    print(f"\nDaily Weather Variables:")
    print(f"Mean Temperature: {weather.get_mean_temperature_fahrenheit():.2f}°F")
    print(f"Maximum Wind Speed: {weather.get_max_wind_speed_mph():.2f} mph")
    print(f"Precipitation Sum: {weather.get_precipitation_sum_inches():.2f} inches")

if __name__ == "__main__":
    main()