import flet as ft
from datetime import datetime
from db import registrar_gasto, get_user_id, get_gastos_usuario

# Variable global para almacenar el email del usuario actual
current_user_email = None

def set_current_user(email):
    global current_user_email
    current_user_email = email

def abrirFormulario(page):
    descripcion_input = ft.TextField(
        label="Descripción",
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_800,
        prefix_icon=ft.icons.DESCRIPTION
    )
    
    monto_input = ft.TextField(
        label="Monto",
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color=ft.colors.BLUE_400,
        focused_border_color=ft.colors.BLUE_800,
        prefix_icon=ft.icons.MONEY
    )
    
    # Usar DatePicker con botón para abrir
    def open_date_picker(e):
        def handle_change(e):
            page.selected_date = e.control.value.strftime('%Y-%m-%d')
            date_input.value = f"Fecha seleccionada: {page.selected_date}"
            page.update()

        page.open(
            ft.DatePicker(
                first_date=datetime(year=2023, month=1, day=1),
                last_date=datetime(year=2024, month=12, day=31),
                on_change=handle_change
            )
        )

    date_input = ft.Text(value="Selecciona la Fecha")
    select_date_button = ft.ElevatedButton("Selecciona la Fecha", on_click=open_date_picker)

    mensaje = ft.Text(
        color=ft.colors.RED_400,
        size=12,
        visible=False
    )

    def validar_fecha(fecha_str):
        try:
            return datetime.strptime(fecha_str, '%Y-%m-%d')
        except ValueError:
            return None

    def validar_monto(monto_str):
        try:
            monto = float(monto_str)
            return monto if monto > 0 else None
        except ValueError:
            return None

    def guardar_gasto(e):
        mensaje.visible = False
        page.update()

        if not descripcion_input.value or not monto_input.value or page.selected_date is None:
            mensaje.value = "Todos los campos son obligatorios"
            mensaje.visible = True
            page.update()
            return

        monto = validar_monto(monto_input.value)
        if monto is None:
            mensaje.value = "El monto debe ser un número positivo"
            mensaje.visible = True
            page.update()
            return

        global current_user_email
        usuario_id = get_user_id(current_user_email)
        if usuario_id is None:
            mensaje.value = f"Error: Usuario no encontrado para {current_user_email}"
            mensaje.visible = True
            page.update()
            return

        success, message = registrar_gasto(
            usuario_id,
            descripcion_input.value,
            monto,
            page.selected_date
        )

        if success:
            dialog.open = False
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Gasto registrado exitosamente"),
                    bgcolor=ft.colors.GREEN_700
                )
            )
            actualizar_historial(page)
        else:
            mensaje.value = message
            mensaje.color = ft.colors.RED_400
            mensaje.visible = True
        
        page.update()

    def cerrarFormulario(e):
        dialog.open = False
        page.update()

    dialog_content = ft.Column(
        [
            descripcion_input,
            monto_input,
            select_date_button,
            date_input,
            mensaje,
        ],
        spacing=20,
        width=300,
    )

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(
            "Registrar nuevo gasto",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE_900,
        ),
        content=ft.Container(
            dialog_content,
            padding=ft.padding.all(20),
        ),
        actions=[
            ft.TextButton(
                "Cancelar",
                style=ft.ButtonStyle(color=ft.colors.GREY_700),
                on_click=cerrarFormulario
            ),
            ft.TextButton(
                "Guardar",
                style=ft.ButtonStyle(color=ft.colors.BLUE_700),
                on_click=guardar_gasto
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.dialog = dialog
    dialog.open = True
    page.update()

# Función para cargar el historial de gastos
def cargar_historial():
    global current_user_email
    usuario_id = get_user_id(current_user_email)

    if usuario_id is None:
        return []

    return get_gastos_usuario(usuario_id)

# Función para actualizar el historial de gastos
def actualizar_historial(page):
    historial = cargar_historial()
    if not historial:
        tabla_historial.controls = [
            ft.Text(
                "Sin gastos registrados.",
                size=16,
                color=ft.colors.GREY_700,
                italic=True
            )
        ]
    else:
        filas = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(gasto[1], color=ft.colors.BLUE_900)),      # Descripción
                    ft.DataCell(ft.Text(f"{gasto[2]:.2f} Bs", color=ft.colors.BLUE_900)),  # Monto
                    ft.DataCell(ft.Text(gasto[3], color=ft.colors.BLUE_900))       # Fecha
                ]
            ) for gasto in historial
        ]
        tabla_historial.controls = [
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Descripción", color=ft.colors.BLUE_900)),
                    ft.DataColumn(ft.Text("Monto", color=ft.colors.BLUE_900)),
                    ft.DataColumn(ft.Text("Fecha", color=ft.colors.BLUE_900)),
                ],
                rows=filas
            )
        ]
    page.update()

tabla_historial = ft.Column([])

contenido = ft.Column(
    [
        ft.Container(
            ft.FloatingActionButton(
                text="Nuevo gasto",
                icon=ft.icons.ADD,
                on_click=lambda e: abrirFormulario(e.page),
                bgcolor=ft.colors.BLUE_700,
            ),
            alignment=ft.alignment.top_right,
            margin=ft.margin.only(right=20, top=20),
        ),
        ft.Container(
            ft.Text(
                value="Historial de gastos",
                size=35,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE_900,
            ),
            margin=ft.margin.only(top=20, bottom=20),
        ),
        ft.Divider(
            height=2,
            color=ft.colors.BLUE_200,
        ),
        tabla_historial,
    ],
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=10,
)

def mostrarPantalla2():
    return ft.Container(
        content=contenido,
        margin=ft.margin.Margin(10, 50, 10, 10),
        padding=ft.padding.all(20),
        border_radius=10,
        bgcolor=ft.colors.WHITE,
        border=ft.border.all(1, ft.colors.BLUE_200),
    )
