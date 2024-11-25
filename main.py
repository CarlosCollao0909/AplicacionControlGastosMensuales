"""
Integrantes del grupo:
    Juan Carlos Collao Mamani
    Denilson Rafael Flores Linneo
    Alejandra Gabriela Sandy Laura
"""

import flet as ft
from login import loginPage

def main(page: ft.Page):
    page.bgcolor = "#287094"
    def comenzar(e):
        page.clean()
        page.add(loginPage(page))

    page.add(
        ft.Container(
            expand = True,
            alignment = ft.alignment.center,
            content = ft.Column(
                alignment = "center",
                horizontal_alignment = "center",
                controls = [
                    ft.Text(
                        value = "Bienvenido",
                        size = 38,
                        weight = ft.FontWeight.BOLD,
                        italic = True,
                        color = ft.colors.WHITE
                    ),
                    ft.Image(
                        src = "https://res.cloudinary.com/dum4okaqx/image/upload/v1730132170/logo_fx2a7y.jpg",
                        width = 250,
                        height = 250,
                        border_radius = ft.border_radius.all(100)
                    ),
                    ft.ElevatedButton(
                        text = "Iniciar",
                        bgcolor = "#D4D4CE",
                        color = "#023246",
                        width=175,
                        height=45,
                        style = ft.ButtonStyle(
                            text_style = ft.TextStyle(
                                color = "#023246",
                                font_family = "Montserrat",
                                italic = True,
                                weight = ft.FontWeight.BOLD,
                                size = 24
                            ),
                        ), 
                        on_click=comenzar
                    )
                ]
            )
        )
    )

ft.app(main)