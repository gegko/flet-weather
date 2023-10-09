import os
import flet as ft
import geocoder
import requests
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()
meteosource = os.getenv('METEOSOURCE_KEY')
openweather = os.getenv('OPENWEATHER_KEY')


def get_geo_data() -> dict:
    g = geocoder.ip('me')
    return {
        'city': g.city,
        'country': g.country,
        'lat': g.latlng[0],
        'lon': g.latlng[1],
    }


def get_forecast_weather() -> dict:
    location = get_geo_data()
    lat, lon = location['lat'], location['lon']
    base_url = 'https://www.meteosource.com/api/v1/free/point'
    params = {
        'lat': lat,
        'lon': lon,
        'sections': 'daily-parts',
        'units': 'metric',
        'key': meteosource
    }
    r = requests.get(base_url, params=params)
    data = [
        {
            'day': weather['day'],
            'weekday': datetime.strptime(weather['day'], '%Y-%m-%d').strftime('%a'),
            'icon': weather['all_day']['icon'],
            'temperature_min': round(weather['all_day']['temperature_min']),
            'temperature_max': round(weather['all_day']['temperature_max']),
            'weather': weather['summary'],
        }
        for weather in r.json()['daily']['data']
    ]
    return data


def get_current_weather() -> dict:
    location = get_geo_data()
    lat, lon = location['lat'], location['lon']
    base_url = 'https://api.openweathermap.org/data/3.0/onecall'
    params = {
        'lat': lat,
        'lon': lon,
        'units': 'metric',
        'appid': openweather,
        'exclude': 'daily,hourly,minutely'
    }
    r = requests.get(base_url, params=params)
    weather = r.json()
    sunrise = datetime.fromtimestamp(weather['current']['sunrise']).time()
    sunset = datetime.fromtimestamp(weather['current']['sunset']).time()
    data = {
        'temperature': f"{round(weather['current']['temp'])}°",
        'wind_speed': f"{weather['current']['wind_speed']} km/h",
        'pressure': f"{weather['current']['pressure']} hPa",
        'feels_like': f"{round(weather['current']['feels_like'])}°",
        'visibility': f"{round(weather['current']['visibility'] / 1000, 1)} km",
        'humidity': f"{weather['current']['humidity']}%",
        'uvi': weather['current']['uvi'],
        'sunrise': f"{sunrise.hour}:{sunrise.minute}",
        'sunset': f"{sunset.hour}:{sunset.minute}",
        'summary': weather['current']['weather'][0]['main'],
    }
    base_url = 'https://www.meteosource.com/api/v1/free/point'
    params = {
        'lat': lat,
        'lon': lon,
        'sections': 'current',
        'units': 'metric',
        'key': meteosource
    }
    r = requests.get(base_url, params=params)
    data['icon'] = r.json()['current']['icon_num']

    return data

    
pprint(get_current_weather())


def temperature_text_style() -> dict:
    return {
        "size": 30,
        "weight": ft.FontWeight.W_100,
        "color": ft.colors.WHITE,
    }


class WeatherForecast:
    def __init__(self, __weather_data=get_forecast_weather()) -> None:
        self.__weather_data = __weather_data
        self.weekday = ft.Column(
            controls=[
                ft.Text(weather['weekday'], size=30, color=ft.colors.WHITE)
                for weather in self.__weather_data
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        self.weather_icon = ft.Column(
            controls=[
                ft.Row(controls=[
                    ft.Image(
                        f"assets/weather_icons/set06/small/{weather['icon']}.png",
                        width=40,
                        height=40,
                        tooltip=weather['weather'],
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER)
                for weather in self.__weather_data
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        self.temperature = ft.Column(
            controls=[
                ft.Row(controls=[
                    ft.Text(
                        weather['temperature_max'],
                        **temperature_text_style(),
                    ),
                    ft.Text(
                        weather['temperature_min'],
                        **temperature_text_style(),
                    ),
                ],
                width=70,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                for weather in self.__weather_data
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
    
    def update(self):
        self.__weather_data = get_forecast_weather()
        self.weekday.page.update()


class HiddenWeatherContent(ft.UserControl):
    def __init__(self, __weather_data=get_current_weather()) -> None:
        super().__init__()
        self.__weather_data = __weather_data
        self.__image_style = {
            "color": ft.colors.WHITE70,
            "height": 50,
            "width": 50,
        }
        self.__container_style = {
            "alignment": ft.alignment.center,
            "bgcolor": ft.colors.WHITE10,
            "border_radius": 5,
            "padding": 30,
        }
        self.visibility_text = self.__weather_data['visibility']
        self.pressure_text = self.__weather_data['pressure']
        self.sunset_text = self.__weather_data['sunset']
        self.sunrise_text = self.__weather_data['sunrise']
        self.visibility = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src="assets/view.png",
                        **self.__image_style,
                    ),
                    ft.Text(self.visibility_text, color=ft.colors.WHITE70, size=16),
                    ft.Text("Visibility", color=ft.colors.WHITE30, size=11)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            **self.__container_style,
        )
        self.pressure = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src="assets/barometer.png",
                        **self.__image_style,
                    ),
                    ft.Text(self.pressure_text, color=ft.colors.WHITE70, size=16),
                    ft.Text("Pressure", color=ft.colors.WHITE30, size=11)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            **self.__container_style,
        )
        self.sunset = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src="assets/sunset.png",
                        **self.__image_style,
                    ),
                    ft.Text(self.sunset_text, color=ft.colors.WHITE70, size=16),
                    ft.Text("Sunset", color=ft.colors.WHITE30, size=11)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            **self.__container_style,
        )
        self.sunrise = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src="assets/sunrise.png",
                        **self.__image_style,
                    ),
                    ft.Text(self.sunrise_text, color=ft.colors.WHITE70, size=16),
                    ft.Text("Sunrise", color=ft.colors.WHITE30, size=11)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            **self.__container_style,
        )

    def build(self) -> ft.GridView:
        return ft.GridView(
            controls=[
                self.visibility,
                self.pressure,
                self.sunrise,
                self.sunset,
            ],
            expand=1,
            max_extent=320,
            spacing=5,
            run_spacing=5,
        )
