"""
Integrantes del grupo:
    Juan Carlos Collao Mamani
    Denilson Rafael Flores Linneo
    Alejandra Gabriela Sandy Laura
"""

import flet as ft

contenido = ft.Column(
    [
        ft.Container(
            alignment = ft.alignment.center,
            content = ft.Column(
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                alignment = ft.alignment.center,
                controls = [
                    ft.Text(
                        value = "Tu saldo actual es de:",
                        text_align = ft.TextAlign.CENTER,
                        size = 38,
                        weight = ft.FontWeight.BOLD,
                        font_family = "Montserrat",
                    ),
                    ft.Text(
                        value = "Bs. 0.00",
                        text_align = ft.TextAlign.CENTER,
                        size = 38,
                        weight = ft.FontWeight.BOLD,
                        font_family = "Montserrat",
                        italic = True
                    ),
                ]
            )
        ),
        ft.Container(
            alignment = ft.alignment.bottom_right,
            content = ft.FloatingActionButton(
                        text = "Nuevo mes",
                        icon = ft.icons.ADD,
                        bgcolor = "#4A90E2",
                    )
        )
    ],
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
)
def mostrarPantalla1():
    return ft.Container(
        content = contenido,
        margin = ft.margin.Margin(10, 50, 10, 10),
        alignment = ft.alignment.center
    )