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
            color="white",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )
        self.apellido_texto = ft.Text(
            f"Apellido: {apellido}",
            size=20,
            color="white",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )
        self.email_texto = ft.Text(
            f"Email: {email}",
            size=20,
            color="white",
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
                            color="white",
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
                        bgcolor="#272b30",
                        width=300,
                    ),
                    # Botón de cerrar sesión
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="Cerrar Sesión",
                            bgcolor="#4A90E2",
                            color="white",
                            width=250,
                            height=45,
                            on_click=self.cerrar_sesion,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                elevation=5,
                                animation_duration=300,
                                color=ft.colors.WHITE,
                                bgcolor={
                                    ft.MaterialState.DEFAULT: "#4A90E2",
                                    ft.MaterialState.HOVERED: "#357ABD",
                                    ft.MaterialState.PRESSED: "#2C6AAC",
                                },
                                text_style=ft.TextStyle(
                                    color="white",
                                    font_family="Montserrat",
                                    weight=ft.FontWeight.BOLD,
                                    size=18
                                ),
                            )
                        ),
                        margin=ft.margin.only(top=30),
                        alignment=ft.alignment.center,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors.BLACK12,
                            offset=ft.Offset(0, 5),
                        ),
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