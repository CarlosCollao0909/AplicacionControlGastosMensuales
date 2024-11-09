"""
Integrantes del grupo:
    Juan Carlos Collao Mamani
    Denilson Rafael Flores Linneo
    Alejandra Gabriela Sandy Laura
"""

import flet as ft

contenido = ft.Column(
    [
        
    ],
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
)
def mostrarPantalla4():
    return ft.Container(
        content = contenido,
        margin = ft.margin.Margin(10, 50, 10, 10),
        alignment = ft.alignment.center
    )