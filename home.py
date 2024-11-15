import flet as ft
from opcion1 import mostrarPantalla1, set_current_email
from opcion2 import mostrarPantalla2, set_current_user, actualizar_historial  # Importa actualizar_historial
from opcion3 import mostrarPantalla3
from opcion4 import mostrarPantalla4
from db import get_user_id

class HomePage:
    def __init__(self, page: ft.Page, user_email: str):
        self.page = page
        self.user_email = user_email
        self.setup_page()
        
    def setup_page(self):
        # Establecer el email del usuario actual en los módulos
        set_current_user(self.user_email)
        set_current_email(self.user_email)
        
        # Guardar el email en el almacenamiento del cliente
        self.page.client_storage.set("user_email", self.user_email)
        
        self.page.bgcolor = ft.colors.BLUE_GREY_800
        self.page.title = "Home"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.contenido = ft.Column(
            [],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center
        )

        self.barraNavegacion = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    label="Saldo",
                    icon=ft.icons.MONEY,
                ),
                ft.NavigationBarDestination(
                    label="Gastos",
                    icon=ft.icons.QUERY_STATS,
                ),
                ft.NavigationBarDestination(
                    label="Reportes",
                    icon=ft.icons.BAR_CHART,
                ),
                ft.NavigationBarDestination(
                    label="Perfil",
                    icon=ft.icons.PERSON,
                ),
            ],
            bgcolor=ft.colors.BLUE_900,
            indicator_color=ft.colors.BLUE_300,
            animation_duration=600,
            on_change=lambda e: self.cambiarContenido(e.control.selected_index)
        )

        self.cambiarContenido(0)
        self.page.add(self.contenido, self.barraNavegacion)

    def cambiarContenido(self, index):
        if index == 0:
            usuario_id = get_user_id(self.user_email)
            self.contenido.controls = [mostrarPantalla1(usuario_id)]
        elif index == 1:
            self.contenido.controls = [mostrarPantalla2()]
            # Actualizar el historial de gastos cuando se selecciona la opción 2
            actualizar_historial(self.page)  # Ahora esta función está definida
        elif index == 2:
            self.contenido.controls = [mostrarPantalla3()]
        elif index == 3:
            self.contenido.controls = [mostrarPantalla4(self.user_email)]
        self.page.update()

def homePage(page: ft.Page, user_email: str):
    return HomePage(page, user_email)
