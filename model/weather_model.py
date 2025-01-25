class Weather:
    def __init__(self, city, country, continent, temperature, pressure, humidity, wind_speed, description, date_time):
        self.city = city
        self.country = country
        self.continent = continent
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.description = description
        self.date_time = date_time

def __str__(self):
    return f"{self.city}, {self.country}: {self.temperature}°C, {self.description}, Umidade: {self.humidity}%, Vento: {self.wind_speed} m/s"
