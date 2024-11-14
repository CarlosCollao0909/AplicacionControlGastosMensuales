import flet as ft
import sqlite3

def registerPage(page: ft.Page):
    
    conn = sqlite3.connect('gastos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    def volverLogin(e):
        page.dialog.open = False
        page.update()
        page.clean()
        from login import loginPage
        page.add(loginPage(page))
        page.update()
    def registrarUsuario(e):
        nameVal = name.value
        lastnameVal = lastname.value
        emailVal = mail.value
        pswdVal = pswd.value

        cursor.execute("INSERT INTO usuarios (nombre, apellido, email, password) VALUES (?, ?, ?, ?)", (nameVal, lastnameVal, emailVal, pswdVal))
        conn.commit()

        print(f"se registró: {nameVal}, {lastnameVal}, {emailVal}, {pswdVal}")

        page.dialog = ft.AlertDialog(
            title=ft.Text("Usuario registrado exitosamente!"),
            actions = [
                ft.TextButton("Aceptar", on_click = volverLogin)
            ]
        )
        page.dialog.open = True

        name.value = ""
        lastname.value = ""
        mail.value = ""
        pswd.value = ""
        page.update()

    page.title = "Registro de Usuario"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    name = ft.TextField(
                expand = True,
                color = "white",
                border_color = "transparent",
                hint_text = "Nombres",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0
            )

    lastname = ft.TextField(
                expand = True,
                color = "white",
                border_color = "transparent",
                hint_text = "Apellidos",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0
            )

    mail = ft.TextField(
                expand = True,
                color = "white",
                border_color = "transparent",
                hint_text = "Email",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0
            )
    pswd = ft.TextField(
                expand = True,
                color = "white",
                border_color = "transparent",
                hint_text = "Password",
                hint_style = ft.TextStyle(color = "#b9babb"),
                content_padding = 0,
                password = True,
                can_reveal_password = True
            )
    page.add(
        ft.Column(
            controls = [
                ft.Container(
                    width = 250,
                    height = 45,
                    border_radius = 10,
                    alignment = ft.alignment.center,
                    content = ft.Row(
                        alignment = ft.alignment.center,
                        controls = [
                            ft.Text(
                                value = "Nuevo Usuario",
                                size = 25,
                                color = ft.colors.WHITE,
                                weight = ft.FontWeight.BOLD,
                                text_align = "center"
                            ),
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
                                ft.icons.PERSON_ROUNDED,
                                color = "#b9babb"
                            ),
                            ft.VerticalDivider(width = 1, color = "#b9babb"),
                            name
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
                                        ft.icons.PERSON_ROUNDED,
                                        color = "#b9babb"
                                    ),
                                    ft.VerticalDivider(width = 1, color = "#b9babb"),
                                    lastname
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
                            mail
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
                            pswd
                        ]
                    )
                ),
                ft.Container(
                    width = 250,
                    height = 45,
                    alignment = ft.alignment.center,
                    content = ft.ElevatedButton(
                        text = "Registrarse",
                        color = "white",
                        bgcolor = "#4A90E2",
                        on_click = registrarUsuario
                    )
                )
            ]
        )
    )