"""
Integrantes del grupo:
    Juan Carlos Collao Mamani
    Denilson Rafael Flores Linneo
    Alejandra Gabriela Sandy Laura
"""

import flet as ft
normal_radius = 120
hover_radius = 140
normal_title_style = ft.TextStyle(
    size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
)
hover_title_style = ft.TextStyle(
    size=16,
    color=ft.colors.WHITE,
    weight=ft.FontWeight.BOLD,
    shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
)
normal_badge_size = 40
def badge(icon, size):
    return ft.Container(
        ft.Icon(icon),
        width=size,
        height=size,
        border=ft.border.all(1, ft.colors.BROWN),
        border_radius=size / 2,
        bgcolor=ft.colors.WHITE,
    )
def on_chart_event(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                section.title_style = hover_title_style
            else:
                section.radius = normal_radius
                section.title_style = normal_title_style
        chart.update()

chart = ft.PieChart(
        sections=[
            ft.PieChartSection(
                40,
                title="Transportes",
                title_style=normal_title_style,
                color=ft.colors.BLUE,
                radius=normal_radius,
                badge=badge(ft.icons.AC_UNIT, normal_badge_size),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                40,
                title="Comida",
                title_style=normal_title_style,
                color=ft.colors.ORANGE,
                radius=normal_radius,
                badge=badge(ft.icons.FOOD_BANK, normal_badge_size),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                5,
                title="Salud",
                title_style=normal_title_style,
                color=ft.colors.PURPLE,
                radius=normal_radius,
                badge=badge(ft.icons.HEALTH_AND_SAFETY, normal_badge_size),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                15,
                title="Hogar",
                title_style=normal_title_style,
                color=ft.colors.GREEN,
                radius=normal_radius,
                badge=badge(ft.icons.HOME, normal_badge_size),
                badge_position=0.98,
            ),
        ],
        sections_space=0,
        center_space_radius=0,
        on_chart_event=on_chart_event,
        expand=True,
    )

contenido = ft.Column(
    [
        ft.Text(
            value = "Gastos",
            text_align = ft.TextAlign.CENTER,
            size = 30,
            weight = ft.FontWeight.BOLD,
            italic = True
        ),
        chart
    ],
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
)
def mostrarPantalla3():
    return ft.Container(
        content = contenido,
        margin = ft.margin.Margin(10, 50, 10, 10),
        alignment = ft.alignment.center
    )