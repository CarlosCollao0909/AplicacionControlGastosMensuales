import flet as ft
from db import get_user_data

current_user_email = None

def set_current_user(email):
    global current_user_email
    current_user_email = email

class PerfilUsuario(ft.UserControl):
    def __init__(self, user_email):
        super().__init__()
        self.user_email = user_email
        # Obtener los datos del usuario inmediatamente
        user_data = get_user_data(self.user_email)
        if user_data:
            nombre, apellido, email = user_data
        else:
            nombre, apellido, email = "No disponible", "No disponible", self.user_email

        # Inicializar los textos con los datos del usuario
        self.nombre_texto = ft.Text(
            f"Nombre: {nombre}",
            size=20,
            color="#F6F6F6",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )
        self.apellido_texto = ft.Text(
            f"Apellido: {apellido}",
            size=20,
            color="#F6F6F6",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )
        self.email_texto = ft.Text(
            f"Email: {email}",
            size=20,
            color="#F6F6F6",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )

    def cerrar_sesion(self, e):
        page = e.page
        # Limpiar el almacenamiento del cliente
        page.client_storage.remove("user_email")
        page.clean()
        import login
        page.add(login.loginPage(page))

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    # Botón de cerrar sesión
                    ft.Container(
                        width=300,
                        content=ft.ElevatedButton(
                            width=63,
                            bgcolor="#e61a23",
                            style=ft.ButtonStyle(
                                color="#F6F6F6",
                            ),
                            content=ft.Icon(name=ft.icons.EXIT_TO_APP),
                            on_click=self.cerrar_sesion,
                        ),
                        margin=ft.margin.only(top=15),
                        alignment=ft.alignment.top_right,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors.BLACK12,
                            offset=ft.Offset(0, 5),
                        ),
                    ),
                    # Contenedor para la imagen de perfil
                    ft.Container(
                        content=ft.Image(
                            src="https://res.cloudinary.com/djletwbhg/image/upload/v1731563716/usuario_inb2mn.png",
                            width=150,
                            height=150,
                            border_radius=ft.border_radius.all(75),
                            fit=ft.ImageFit.COVER,
                        ),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(bottom=20),
                    ),
                    # Título del perfil
                    ft.Container(
                        content=ft.Text(
                            "Perfil de Usuario",
                            size=32,
                            color="#F6F6F6",
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(bottom=30),
                    ),
                    # Contenedor para la información del usuario
                    ft.Container(
                        content=ft.Column(
                            [
                                self.nombre_texto,
                                self.apellido_texto,
                                self.email_texto
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,
                        ),
                        padding=20,
                        border_radius=10,
                        bgcolor="#287094",
                        width=300,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            ),
            # Contenedor principal
            margin=ft.margin.Margin(10, 50, 10, 10),
            padding=20,
            alignment=ft.alignment.center,
            border_radius=10,
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.BLACK12,
                offset=ft.Offset(0, 5),
            ),
        )

def mostrarPantalla4(user_email):
    return PerfilUsuario(user_email)