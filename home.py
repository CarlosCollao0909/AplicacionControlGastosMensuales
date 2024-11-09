"""
Integrantes del grupo:
    Juan Carlos Collao Mamani
    Denilson Rafael Flores Linneo
    Alejandra Gabriela Sandy Laura
"""

import flet as ft
from opcion1 import mostrarPantalla1
from opcion2 import mostrarPantalla2
from opcion3 import mostrarPantalla3
from opcion4 import mostrarPantalla4

def homePage(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Home"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def cambiarContenido(index):
        if index == 0:
            contenido.controls = [mostrarPantalla1()]
        elif index == 1:
            contenido.controls = [mostrarPantalla2()]
        elif index == 2:
            contenido.controls = [mostrarPantalla3()]
        elif index == 3:
            contenido.controls = [mostrarPantalla4()]
        page.update()

    contenido = ft.Column(
        [],
        expand = True,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        alignment=ft.alignment.center
    )

    barraNavegacion = ft.NavigationBar(
        destinations = [
            ft.NavigationBarDestination(
                label = "Saldo",
                icon = ft.icons.MONEY,
            ),
            ft.NavigationBarDestination(
                label = "Gastos",
                icon = ft.icons.QUERY_STATS,
            ),
            ft.NavigationBarDestination(
                label = "Reportes",
                icon = ft.icons.BAR_CHART,
            ),
            ft.NavigationBarDestination(
                label = "Perfil",
                icon = ft.icons.PERSON,
            ),
        ],
        bgcolor = ft.colors.BLUE_900,
        indicator_color = ft.colors.BLUE_300,
        animation_duration = 600,
        on_change = lambda e: cambiarContenido(e.control.selected_index)
    )

    cambiarContenido(0)
    page.add(contenido, barraNavegacion)