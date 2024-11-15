import flet as ft
from db import get_user_id, add_saldo, get_saldo

# Variable global para almacenar el email del usuario actual
current_email = None
saldo_text = None  # Variable global para mantener referencia al texto del saldo

def set_current_email(email: str):
    global current_email
    current_email = email

def get_current_email():
    global current_email
    return current_email

def mostrarFormularioSaldo(e):
    monto_field = ft.TextField(
        label="Monto en Bs.",
        label_style=ft.TextStyle(color=ft.colors.WHITE),
        hint_text="Ingrese su saldo",
        hint_style=ft.TextStyle(color=ft.colors.WHITE70),
        width=250,
        border_color=ft.colors.WHITE,
        focused_border_color=ft.colors.WHITE,
        cursor_color=ft.colors.WHITE,
        text_style=ft.TextStyle(color=ft.colors.WHITE),
    )
    
    def aceptarFormulario(e):
        monto = monto_field.value
        
        if monto:
            try:
                usuario_id = get_user_id(get_current_email())
                monto = float(monto)
                add_saldo(usuario_id, monto)
                cerrarFormulario(e)
                actualizarSaldo(e)
                
                # Mostrar mensaje de éxito
                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text("Saldo agregado exitosamente", color=ft.colors.WHITE),
                    bgcolor=ft.colors.BLUE_500
                )
                e.page.snack_bar.open = True
                e.page.update()
            except ValueError:
                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text("Por favor ingrese un monto válido.", color=ft.colors.WHITE),
                    bgcolor=ft.colors.RED_600
                )
                e.page.snack_bar.open = True
                e.page.update()
        else:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text("El monto no puede estar vacío.", color=ft.colors.WHITE),
                bgcolor=ft.colors.RED_600
            )
            e.page.snack_bar.open = True
            e.page.update()

    formulario_dialog = ft.AlertDialog(
        title=ft.Text("Agregar Saldo", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
        content=ft.Container(
            width=300,
            height=180,
            bgcolor=ft.colors.BLUE_900,
            border=ft.border.all(2, ft.colors.WHITE),
            border_radius=10,
            padding=20,
            content=ft.Column(
                controls=[monto_field],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
        actions=[
            ft.Container(
                content=ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: cerrarFormulario(e),
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE_500  # Color del botón "Cancelar"
                    )
                ),
                border=ft.border.all(1, ft.colors.BLUE_900),
                border_radius=8,
                margin=ft.margin.only(right=10)
            ),
            ft.Container(
                content=ft.TextButton(
                    "Añadir",
                    on_click=aceptarFormulario,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE_500  # Color del botón "Aceptar"
                    )
                ),
                border=ft.border.all(1, ft.colors.BLUE_900),
                border_radius=8,
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor=ft.colors.BLUE_900,
    )
    
    e.page.dialog = formulario_dialog
    formulario_dialog.open = True
    e.page.update()

def cerrarFormulario(e):
    e.page.dialog.open = False
    e.page.update()

def actualizarSaldo(e):
    global saldo_text
    if saldo_text:
        usuario_id = get_user_id(get_current_email())
        saldo = get_saldo(usuario_id)
        saldo_text.value = f"Bs. {saldo:.2f}"
        e.page.update()

def mostrarPantalla1(usuario_id):
    global saldo_text
    # Obtener el saldo inicial
    saldo_inicial = get_saldo(usuario_id)
    
    # Crear el texto del saldo y guardar la referencia
    saldo_text = ft.Text(
        value=f"Bs. {saldo_inicial:.2f}",
        text_align=ft.TextAlign.CENTER,
        size=38,
        weight=ft.FontWeight.BOLD,
        font_family="Montserrat",
        italic=True,
    )
    
    contenido = ft.Column(
        [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.alignment.center,
                    controls=[
                        ft.Text(
                            value="Tu saldo actual es de:",
                            text_align=ft.TextAlign.CENTER,
                            size=38,
                            weight=ft.FontWeight.BOLD,
                            font_family="Montserrat",
                        ),
                        saldo_text,  # Usar la referencia al texto del saldo
                    ],
                ),
            ),
            ft.Container(
                alignment=ft.alignment.bottom_right,
                content=ft.FloatingActionButton(
                    text="Agregar Saldo",
                    icon=ft.icons.ADD,
                    bgcolor="#4A90E2",
                    on_click=mostrarFormularioSaldo,
                ),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return ft.Container(
        content=contenido,
        margin=ft.margin.Margin(10, 50, 10, 10),
        alignment=ft.alignment.center,
    )
