"""
Integrantes del grupo:
    Juan Carlos Collao Mamani
    Denilson Rafael Flores Linneo
    Alejandra Gabriela Sandy Laura
"""

import flet as ft

""" def addGasto():
    ft.AlertDialog(
        title = ft.Text("Añadir nuevo gasto"),
        content = ft.Column(
            [
                ft.TextField(label = "Monto gastado"),
                ft.TextField(label = "Categoría"),
                ft.TextField(label = "Fecha")
            ]
        ),
        
    ) """


contenido = ft.Column(
    [
        ft.Container(
            ft.FloatingActionButton(
                text = "Nuevo gasto",
                icon = ft.icons.ADD,
                #on_click = lambda e: addGasto()
            ),
            alignment = ft.alignment.top_right
        ),
        ft.Container(
            ft.Text(
                value = "Historial de gastos",
                size = 35,
                weight = ft.FontWeight.BOLD
            )
        ),
        ft.Container(
            alignment = ft.alignment.center,
            content = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Monto gastado")),
                ft.DataColumn(ft.Text("Categoría")),
                ft.DataColumn(ft.Text("Fecha")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("100")),
                        ft.DataCell(ft.Text("Salud")),
                        ft.DataCell(ft.Text("10/10/2024")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("100")),
                        ft.DataCell(ft.Text("Comida")),
                        ft.DataCell(ft.Text("10/10/2024")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("100")),
                        ft.DataCell(ft.Text("Hogar")),
                        ft.DataCell(ft.Text("10/10/2024")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("100")),
                        ft.DataCell(ft.Text("Hogar")),
                        ft.DataCell(ft.Text("10/10/2024")),
                    ],
                ),
            ],
        ),
        )
    ],
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
)
def mostrarPantalla2():
    return ft.Container(
        content = contenido,
        margin = ft.margin.Margin(10, 50, 10, 10),
        alignment = ft.alignment.center
    )