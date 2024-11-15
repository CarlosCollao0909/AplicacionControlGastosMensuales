# registro.py
import flet as ft
from db import add_user

def registroPage(page: ft.Page):

    nombre = ft.TextField(
                expand = True,
                color = "white",
                border_color = "transparent",
                hint_text = "Nombre",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0
            )
    apellido = ft.TextField(
                expand = True,
                color = "white",
                border_color = "transparent",
                hint_text = "Apellido",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0
            )
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
                hint_text = "Contraseña",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0,
                password = True,
                can_reveal_password = True
            )

    def registrarUsuario(e):
        nombreVal = nombre.value
        apellidoVal = apellido.value
        emailVal = email.value
        passwordVal = password.value
        add_user(nombreVal, apellidoVal, emailVal, passwordVal)
        page.dialog = ft.AlertDialog(
            title = ft.Text("Registro exitoso"),
        )
        page.dialog.open = True
        page.update()

    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Registro"
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
                                "Crear Cuenta",
                                size = 38,
                                weight = ft.FontWeight.BOLD,
                                font_family = "Montserrat",
                            ),
                            ft.Text(
                                "Ingresa tus datos para registrarte",
                                size = 18,
                                color = "#b9babb",
                                font_family = "Montserrat",
                            )
                        ]
                    )
                ),
                # Los campos para ingresar los datos del usuario
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
                                ft.icons.PERSON,
                                color = "#b9babb"
                            ),
                            ft.VerticalDivider(width = 1, color = "#b9babb"),
                            nombre
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
                                ft.icons.PERSON,
                                color = "#b9babb"
                            ),
                            ft.VerticalDivider(width = 1, color = "#b9babb"),
                            apellido
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
                        text = "Registrarse",
                        bgcolor = "#4A90E2",
                        color = "white",
                        width = 250,
                        height = 45,
                        on_click = registrarUsuario,
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
