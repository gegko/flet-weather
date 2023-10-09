import flet as ft
from weather import (
    HiddenWeatherContent,
    WeatherForecast,
    get_current_weather,
    get_geo_data,
)


def expand_container(e: ft.ControlEvent) -> None:
    top_container = e.control
    if e.data == 'true':
        top_container.height = 700
        top_container.update()
    else:
        top_container.height = 300
        top_container.update()


def weekly_content() -> ft.Row:
    weather = WeatherForecast()
    return ft.Row(
        controls=[
            weather.weekday,
            weather.weather_icon,
            weather.temperature
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )


def main_container() -> ft.Container:
    return ft.Container(
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLACK87,
        width=400,
        height=800,
        border_radius=40,
        content=weekly_content(),
        padding=ft.padding.only(top=300, left=25, right=25),
    )


def main_weather_content() -> ft.Row:
    main_weather = get_current_weather()
    return ft.Row(
        controls=[
            ft.Image(
                f'assets/weather_icons/set01/big/{main_weather["icon"]}.png',
                scale=1.33,
            ),
            ft.Column(
                controls=[
                    ft.Text('Today', color=ft.colors.WHITE, 
                            text_align=ft.TextAlign.CENTER),
                    ft.Text(
                        main_weather['temperature'],
                        size=65,
                        color=ft.colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        main_weather['summary'],
                        size=13, 
                        color=ft.colors.WHITE38,
                        text_align=ft.TextAlign.CENTER,
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=1,
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


def additional_weather_content() -> ft.Row:
    additional_weather = get_current_weather()
    icons_style = {
        "color": ft.colors.WHITE70,
        "width": 25,
        "height": 25,
    }
    text_style = {
        "color": ft.colors.WHITE70,
        "weight": ft.FontWeight.W_400,
    }
    sub_text_style = {
        "color": ft.colors.WHITE24,
        "size": 12,
    }
    column_style = {
        "spacing": 1,
        "horizontal_alignment": ft.CrossAxisAlignment.CENTER,
    }
    return ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Image('assets/winds.png', **icons_style),
                    ft.Text(additional_weather['wind_speed'], **text_style),
                    ft.Text('Wind', **sub_text_style)
                ],
                **column_style,
            ),
            ft.Column(
                controls=[
                    ft.Image('assets/humidity.png', **icons_style),
                    ft.Text(additional_weather['humidity'], **text_style),
                    ft.Text('Humidity', **sub_text_style)
                ],
                **column_style,
            ),
            ft.Column(
                controls=[
                    ft.Image('assets/thermometer.png', **icons_style),
                    ft.Text(additional_weather['feels_like'], **text_style),
                    ft.Text('Feels Like', **sub_text_style)
                ],
                **column_style,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )


def top_container_content() -> ft.Column:
    city = get_geo_data()
    return ft.Column(
        controls=[
            ft.Container(
                width=400,
                height=40,
                content=ft.Text(
                    f"{city['city']}, {city['country']}", 
                    weight=ft.FontWeight.W_400, 
                    size=18, 
                    color=ft.colors.WHITE, 
                    text_align=ft.TextAlign.CENTER
                ),
                alignment=ft.alignment.bottom_center,                
            ),
            ft.Container(
                alignment=ft.alignment.center,
                width=400,
                height=160,
                content=main_weather_content(),
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE24,
                width=350,
                height=.5,
                border_radius=1,
                margin=ft.margin.only(bottom=15)
            ),
            ft.Container(
                alignment=ft.alignment.center,
                width=400,
                height=100,
                content=additional_weather_content()
            ),
            ft.Container(
                width=400,
                height=400,
                content=HiddenWeatherContent(),
                padding=ft.padding.symmetric(horizontal=25),
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )


def top_container() -> ft.Container:
    return ft.Container(
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLUE_600,
        width=400,
        height=300,
        border_radius=40,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[
                ft.colors.LIGHT_BLUE_600,
                ft.colors.LIGHT_BLUE_900
            ],
        ),
        on_hover=expand_container,
        animate=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
        content=top_container_content(),
        
    )


def main_stack() -> ft.Stack:
    return ft.Stack(
        controls=[
            main_container(),
            top_container(),
        ]
    )


def main(page: ft.Page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(main_stack())

ft.app(main, view=ft.AppView.WEB_BROWSER, assets_dir='.')
