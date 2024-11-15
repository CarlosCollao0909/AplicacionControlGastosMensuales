import flet as ft
from home import homePage
from db import verify_user, create_db, add_user
import time

create_db()

# Función para mostrar la página de inicio de sesión
def loginPage(page: ft.Page):
    email = ft.TextField(
        expand=True,
        color="white",
        border_color="transparent",
        hint_text="Email",
        hint_style=ft.TextStyle(color="#b9babb"),
        content_padding=0
    )
    password = ft.TextField(
        expand=True,
        color="white",
        border_color="transparent",
        hint_text="Password",
        hint_style=ft.TextStyle(color="#b9babb"),
        content_padding=0,
        password=True,
        can_reveal_password=True
    )

    def mostrarInicio(e):
        emailVal = email.value
        passwordVal = password.value
        if verify_user(emailVal, passwordVal):
            page.clean()
            page.add(
                ft.Lottie(
                    src="https://lottie.host/2d82e44c-9a3a-4f3d-baf2-3c7e5ac14cd8/UllxeRPqGP.json",
                    repeat=True,
                )
            )
            page.update()
            time.sleep(2.5)
            page.clean()
            print(verify_user(emailVal, passwordVal))
            homePage(page, emailVal)  # Pasamos el email del usuario

        else:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Usuario o contraseña incorrectos"),
            )
            page.dialog.open = True
            page.update()

    def irARegistro(e):
        page.clean()
        page.add(registroPage(page))  # Llamar a la página de registro

    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    return ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment="center",
            alignment="center",
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        horizontal_alignment="center",
                        alignment="center",
                        controls=[
                            ft.Text(
                                "Iniciar Sesión",
                                size=38,
                                weight=ft.FontWeight.BOLD,
                                font_family="Montserrat",
                            ),
                            ft.Text(
                                "Ingresa tus credenciales",
                                size=18,
                                color="#b9babb",
                                font_family="Montserrat",
                            )
                        ]
                    )
                ),
                ft.Container(
                    width=250,
                    height=45,
                    bgcolor="#272b30",
                    border_radius=10,
                    padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                    content=ft.Row(
                        alignment=ft.alignment.center_left,
                        controls=[
                            ft.Icon(
                                ft.icons.EMAIL,
                                color="#b9babb"
                            ),
                            ft.VerticalDivider(width=1, color="#b9babb"),
                            email
                        ]
                    )
                ),
                ft.Container(
                    width=250,
                    height=45,
                    bgcolor="#272b30",
                    border_radius=10,
                    padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                    content=ft.Row(
                        alignment=ft.alignment.center_left,
                        controls=[
                            ft.Icon(
                                ft.icons.LOCK,
                                color="#b9babb"
                            ),
                            ft.VerticalDivider(width=1, color="#b9babb"),
                            password
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=15),
                    content=ft.ElevatedButton(
                        text="Ingresar",
                        bgcolor="#4A90E2",
                        color="white",
                        width=250,
                        height=45,
                        on_click=mostrarInicio,
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                color="white",
                                font_family="Montserrat",
                                weight=ft.FontWeight.BOLD,
                                size=18
                            ),
                        )
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(top=15),
                    content=ft.CupertinoButton(
                        text="¿No tienes cuenta? Regístrate",
                        color="white",
                        width=250,
                        on_click=irARegistro,  # Función para ir a la página de registro
                    ),
                )
            ]
        )
    )


# Función para mostrar la página de registro
def registroPage(page: ft.Page):
    nombre = ft.TextField(
        expand=True,
        color="white",
        border_color="transparent",
        hint_text="Nombre",
        hint_style=ft.TextStyle(color="#b9babb"),
        content_padding=0
    )
    apellido = ft.TextField(
        expand=True,
        color="white",
        border_color="transparent",
        hint_text="Apellido",
        hint_style=ft.TextStyle(color="#b9babb"),
        content_padding=0
    )
    email = ft.TextField(
        expand=True,
        color="white",
        border_color="transparent",
        hint_text="Email",
        hint_style=ft.TextStyle(color="#b9babb"),
        content_padding=0
    )
    password = ft.TextField(
        expand=True,
        color="white",
        border_color="transparent",
        hint_text="Password",
        hint_style=ft.TextStyle(color="#b9babb"),
        content_padding=0,
        password=True,
        can_reveal_password=True
    )

    def registrarUsuario(e):
        nombreVal = nombre.value
        apellidoVal = apellido.value
        emailVal = email.value
        passwordVal = password.value
        
        if not nombreVal or not apellidoVal or not emailVal or not passwordVal:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Por favor, complete todos los campos"),
            )
            page.dialog.open = True
            page.update()
            return
            
        add_user(nombreVal, apellidoVal, emailVal, passwordVal)
        page.dialog = ft.AlertDialog(
            title=ft.Text("¡Registro exitoso!"),
        )
        page.dialog.open = True
        page.update()
        time.sleep(1.5)
        page.clean()
        page.add(loginPage(page))  # Regresar a la página de inicio de sesión

    def regresarALogin(e):
        page.clean()
        page.add(loginPage(page))  # Limpiar y mostrar la página de inicio de sesión

    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Registro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    return ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment="center",
            alignment="center",
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        horizontal_alignment="center",
                        alignment="center",
                        controls=[
                            ft.Text(
                                "Registro de usuario",
                                size=38,
                                weight=ft.FontWeight.BOLD,
                                font_family="Montserrat",
                            ),
                            ft.Text(
                                "Crea una cuenta nueva",
                                size=18,
                                color="#b9babb",
                                font_family="Montserrat",
                            )
                        ]
                    )
                ),
                ft.Container(
                    width=250,
                    height=45,
                    bgcolor="#272b30",
                    border_radius=10,
                    padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                    content=ft.Row(
                        alignment=ft.alignment.center_left,
                        controls=[
                            ft.Icon(
                                ft.icons.PERSON,
                                color="#b9babb"
                            ),
                            ft.VerticalDivider(width=1, color="#b9babb"),
                            nombre
                        ]
                    )
                ),
                ft.Container(
                    width=250,
                    height=45,
                    bgcolor="#272b30",
                    border_radius=10,
                    padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                    content=ft.Row(
                        alignment=ft.alignment.center_left,
                        controls=[
                            ft.Icon(
                                ft.icons.PERSON,
                                color="#b9babb"
                            ),
                            ft.VerticalDivider(width=1, color="#b9babb"),
                            apellido
                        ]
                    )
                ),
                ft.Container(
                    width=250,
                    height=45,
                    bgcolor="#272b30",
                    border_radius=10,
                    padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                    content=ft.Row(
                        alignment=ft.alignment.center_left,
                        controls=[
                            ft.Icon(
                                ft.icons.EMAIL,
                                color="#b9babb"
                            ),
                            ft.VerticalDivider(width=1, color="#b9babb"),
                            email
                        ]
                    )
                ),
                ft.Container(
                    width=250,
                    height=45,
                    bgcolor="#272b30",
                    border_radius=10,
                    padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                    content=ft.Row(
                        alignment=ft.alignment.center_left,
                        controls=[
                            ft.Icon(
                                ft.icons.LOCK,
                                color="#b9babb"
                            ),
                            ft.VerticalDivider(width=1, color="#b9babb"),
                            password
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=15),
                    content=ft.ElevatedButton(
                        text="Registrar",
                        bgcolor="#4A90E2",
                        color="white",
                        width=250,
                        height=45,
                        on_click=registrarUsuario,
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                color="white",
                                font_family="Montserrat",
                                weight=ft.FontWeight.BOLD,
                                size=18
                            ),
                        )
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(top=15),
                    content=ft.CupertinoButton(
                        text="¿Ya tienes cuenta? Inicia sesión",
                        color="white",
                        width=250,
                        on_click=regresarALogin,
                    ),
                )
            ]
        )
    )