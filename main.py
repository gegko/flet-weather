import flet as ft


def hidden_content():
    return [
        ('assets/view.png', '10 Km', 'Visibility'),
        ('assets/barometer.png', '30.81 inHg', 'Pressure'),
        ('assets/sunset.png', '11:40 PM', 'Sunset'),
        ('assets/sunrise.png', '02:41 PM', 'Sunrise'),
    ]


def hidden_grid():
    return ft.GridView(
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE10,
                border_radius=5,
                content=ft.Column(
                    controls=[
                        ft.Image(
                            src=src,
                            color=ft.colors.WHITE70,
                            height=50,
                            width=50
                        ),
                        ft.Text(text, color=ft.colors.WHITE70, size=16),
                        ft.Text(sub_text, color=ft.colors.WHITE30, size=11)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=30,
            )
            for src, text, sub_text in hidden_content()
        ],
        expand=1,
        max_extent=320,
        spacing=5,
        run_spacing=5,
    )


def expand_container(e):
    top_container = e.control
    if e.data == 'true':
        top_container.height = 700
        top_container.update()
    else:
        top_container.height = 300
        top_container.update()


def weather_content():
    return [
        ('Tue', 'assets/sun.png', ft.colors.YELLOW_400, 'Clear', '0', '-3'),
        ('Wed', 'assets/cloud.png', ft.colors.LIGHT_BLUE_300, 'Clouds', '1', '-2'),
        ('Thu', 'assets/snow.png', ft.colors.LIGHT_BLUE_300, 'Snow', '1', '-1'),
        ('Fri', 'assets/snow.png', ft.colors.LIGHT_BLUE_300, 'Snow', '2', '1'),
        ('Sat', 'assets/snow.png', ft.colors.LIGHT_BLUE_300, 'Snow', '1', '0'),
        ('Sun', 'assets/cloud.png', ft.colors.LIGHT_BLUE_300, 'Clouds', '0', '-1'),
        ('Mon', 'assets/snow.png', ft.colors.LIGHT_BLUE_300, 'Snow', '0', '-6'),
    ]


def weekly_content():
    return ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(day, size=30, color=ft.colors.WHITE)
                    for day, *_ in weather_content()
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
            ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Image(icon, width=40, height=40),
                        ft.Text(weather, size=18, color=ft.colors.WHITE38),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER)
                    for _, icon, color, weather, *_ in weather_content()
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
            ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Text(
                            day_celc,
                            size=30,
                            weight=ft.FontWeight.W_100,
                            color=ft.colors.WHITE,
                        ),
                        ft.Text(
                            night_celc,
                            size=30,
                            weight=ft.FontWeight.W_100,
                            color=ft.colors.WHITE,
                        ),
                    ],
                    width=70,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                    for *_, day_celc, night_celc in weather_content()
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )


def main_container():
    return ft.Container(
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLACK87,
        width=400,
        height=800,
        border_radius=40,
        content=weekly_content(),
        padding=ft.padding.only(top=300, left=25, right=25),
    )


def main_weather_content():
    return ft.Row(
        controls=[
            ft.Image('assets/sun-cloud.png', scale=1.33),
            ft.Column(
                controls=[
                    ft.Text('Today', color=ft.colors.WHITE, 
                            text_align=ft.TextAlign.CENTER),
                    ft.Text('-3°', color=ft.colors.WHITE, size=65, 
                            text_align=ft.TextAlign.CENTER),
                    ft.Text('Clouds • Overcast', size=13, 
                            color=ft.colors.WHITE38, 
                            text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=1,
                
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )


def additional_weather_content():
    return ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Image(
                        'assets/winds.png',
                        color=ft.colors.WHITE70,
                        height=25,
                        width=25
                    ),
                    ft.Text(
                        '1 km/h',
                        color=ft.colors.WHITE70,
                        weight=ft.FontWeight.W_400
                    ),
                    ft.Text('Wind', color=ft.colors.WHITE24, size=12)
                ],
                spacing=1,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Column(
                controls=[
                    ft.Image(
                        'assets/humidity.png',
                        color=ft.colors.WHITE70,
                        height=25,
                        width=25
                    ),
                    ft.Text(
                        '85%',
                        color=ft.colors.WHITE70,
                        weight=ft.FontWeight.W_400
                    ),
                    ft.Text('Humidity', color=ft.colors.WHITE24, size=12)
                ],
                spacing=1,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Column(
                controls=[
                    ft.Image(
                        'assets/thermometer.png',
                        color=ft.colors.WHITE70,
                        height=25,
                        width=25
                    ),
                    ft.Text(
                        '-4°',
                        color=ft.colors.WHITE70,
                        weight=ft.FontWeight.W_400
                    ),
                    ft.Text('Feels Like', color=ft.colors.WHITE24, size=12)
                ],
                spacing=1,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )


def top_container_content():
    return ft.Column(
        controls=[
            ft.Container(
                height=40,
                width=400,
                content=ft.Text(
                    'Toronto, CA', 
                    weight=ft.FontWeight.W_400, 
                    size=18, 
                    color=ft.colors.WHITE, 
                    text_align=ft.TextAlign.CENTER
                ),
                alignment=ft.alignment.bottom_center,                
            ),
            ft.Container(
                alignment=ft.alignment.center,
                height=160,
                width=400,
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
                height=100,
                width=400,
                content=additional_weather_content()
            ),
            ft.Container(
                height=400,
                width=400,
                content=hidden_grid(),
                padding=ft.padding.symmetric(horizontal=25),
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )


def top_container():
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


def main_stack():
    return ft.Stack(
        controls=[
            main_container(),
            top_container(),
        ]
    )


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(main_stack())


ft.app(main, view=ft.AppView.WEB_BROWSER, assets_dir='.')