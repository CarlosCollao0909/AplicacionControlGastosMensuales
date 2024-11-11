"""
Integrantes del grupo:
    Juan Carlos Collao Mamani
    Denilson Rafael Flores Linneo
    Alejandra Gabriela Sandy Laura
"""

import flet as ft
import time
from home import homePage
from db import verify_user, create_db

create_db()
def loginPage(page: ft.Page):

    email = ft.TextField(
                expand = True,
                color = "white",
                border_color = "transparent",
                hint_text = "Email",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0
            )
    password = ft.TextField(
                expand = True,
                color = "white",
                border_color = "transparent",
                hint_text = "Password",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0,
                password = True,
                can_reveal_password = True
            )
    def mostrarInicio(e):
        emailVal = email.value
        passwordVal = password.value
        if verify_user(emailVal, passwordVal):
            page.clean()
            page.add(
                ft.Lottie(
                    src = "https://lottie.host/2d82e44c-9a3a-4f3d-baf2-3c7e5ac14cd8/UllxeRPqGP.json",
                    repeat = True,
                )
            )
            page.update()
            time.sleep(2.5)
            page.clean()
            homePage(page)
        else:
            page.dialog = ft.AlertDialog(
                title = ft.Text("Usuario o contraseña incorrectos"),
            )
            page.dialog.open = True
            page.update()
    
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    return ft.Container(
        expand = True,
        alignment = ft.alignment.center,
        content = ft.Column(
            horizontal_alignment = "center",
            alignment = "center",
            controls = [
                ft.Container(
                    alignment = ft.alignment.center,
                    content = ft.Column(
                        horizontal_alignment = "center",
                        alignment = "center",
                        controls = [
                            ft.Text(
                                "Iniciar Sesión",
                                size = 38,
                                weight = ft.FontWeight.BOLD,
                                font_family = "Montserrat",
                            ),
                            ft.Text(
                                "Ingresa tus credenciales",
                                size = 18,
                                color = "#b9babb",
                                font_family = "Montserrat",
                            )
                        ]
                    )
                ),
                ft.Container(
                    width = 250,
                    height = 45,
                    bgcolor = "#272b30",
                    border_radius = 10,
                    padding = ft.padding.only(left = 10, right = 10, top = 5, bottom = 5),
                    content = ft.Row(
                        alignment = ft.alignment.center_left,
                        controls = [
                            ft.Icon(
                                ft.icons.EMAIL,
                                color = "#b9babb"
                            ),
                            ft.VerticalDivider(width = 1, color = "#b9babb"),
                            email
                        ]
                    )
                ),
                ft.Container(
                    width = 250,
                    height = 45,
                    bgcolor = "#272b30",
                    border_radius = 10,
                    padding = ft.padding.only(left = 10, right = 10, top = 5, bottom = 5),
                    content = ft.Row(
                        alignment = ft.alignment.center_left,
                        controls = [
                            ft.Icon(
                                ft.icons.LOCK,
                                color = "#b9babb"
                            ),
                            ft.VerticalDivider(width = 1, color = "#b9babb"),
                            password
                        ]
                    )
                ),
                ft.Container(
                    padding = ft.padding.only(top = 15),
                    content = ft.ElevatedButton(
                        text = "Ingresar",
                        bgcolor = "#4A90E2",
                        color = "white",
                        width = 250,
                        height = 45,
                        on_click = mostrarInicio,
                        style = ft.ButtonStyle(
                            text_style = ft.TextStyle(
                                color = "white",
                                font_family = "Montserrat",
                                weight = ft.FontWeight.BOLD,
                                size = 18
                            ),
                        )
                    ),
                )
            ]
        )
    )