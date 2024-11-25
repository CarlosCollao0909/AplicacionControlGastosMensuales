import flet as ft
from db import get_user_id, add_saldo, get_saldo

# Variables globales
current_email = None
saldo_text = None
estado_imagen = None

def set_current_email(email: str):
    global current_email
    current_email = email

def get_current_email():
    global current_email
    return current_email

def get_estado_saldo(saldo):
    if saldo >= 3000:
        return {
            "icon": ft.icons.SENTIMENT_VERY_SATISFIED,
            "color": ft.colors.GREEN_500,
            "mensaje": "¡Excelente gestión financiera! 🌟\nEstás construyendo un futuro sólido"
        }
    elif saldo >= 1500:
        return {
            "icon": ft.icons.SENTIMENT_SATISFIED,
            "color": ft.colors.BLUE_500,
            "mensaje": "¡Buen trabajo! 💪\nMantén este ritmo de ahorro"
        }
    elif saldo >= 500:
        return {
            "icon": ft.icons.SENTIMENT_NEUTRAL,
            "color": ft.colors.ORANGE_500,
            "mensaje": "Tu saldo está en punto medio 📊\nEs buen momento para aumentar tus ahorros"
        }
    else:
        return {
            "icon": ft.icons.SENTIMENT_DISSATISFIED,
            "color": ft.colors.RED_500,
            "mensaje": "Tiempo de tomar acción 💡\nRevisa tus gastos y establece prioridades"
        }

def mostrarFormularioSaldo(e):
    monto_field = ft.TextField(
        label="Monto en Bs.",
        label_style=ft.TextStyle(color="#F6F6F6"),
        hint_text="Ingrese su saldo",
        hint_style=ft.TextStyle(color="#D4D4CE"),
        width=250,
        border_color="#D4D4CE",
        focused_border_color="#D4D4CE",
        cursor_color="#D4D4CE",
        text_style=ft.TextStyle(color="#F6F6F6"),
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
                    content=ft.Text("Saldo agregado exitosamente", color="#F6F6F6"),
                    bgcolor=ft.colors.BLUE_500
                )
                e.page.snack_bar.open = True
                e.page.update()
            except ValueError:
                e.page.snack_bar = ft.SnackBar(
                    content=ft.Text("Por favor ingrese un monto válido.", color="#F6F6F6"),
                    bgcolor=ft.colors.RED_600
                )
                e.page.snack_bar.open = True
                e.page.update()
        else:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text("El monto no puede estar vacío.", color="#F6F6F6"),
                bgcolor=ft.colors.RED_600
            )
            e.page.snack_bar.open = True
            e.page.update()

    formulario_dialog = ft.AlertDialog(
        title=ft.Text("Agregar Saldo", color="#F6F6F6", weight=ft.FontWeight.BOLD),
        content=ft.Container(
            width=300,
            height=180,
            bgcolor="#023246",
            border=ft.border.all(2, "#D4D4CE"),
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
                        color="#023246",
                        bgcolor="#D4D4CE"
                    )
                ),
                border_radius=8,
                margin=ft.margin.only(right=10)
            ),
            ft.Container(
                content=ft.TextButton(
                    "Añadir",
                    on_click=aceptarFormulario,
                    style=ft.ButtonStyle(
                        color="#023246",
                        bgcolor="#D4D4CE"
                    )
                ),
                border_radius=8,
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor="#023246",
    )
    
    e.page.dialog = formulario_dialog
    formulario_dialog.open = True
    e.page.update()

def cerrarFormulario(e):
    e.page.dialog.open = False
    e.page.update()

def actualizarSaldo(e):
    global saldo_text, estado_imagen
    if saldo_text and estado_imagen:
        usuario_id = get_user_id(get_current_email())
        saldo = get_saldo(usuario_id)
        saldo_text.value = f"Bs. {saldo:.2f}"
        
        # Actualizar el estado de la imagen y mensaje
        estado = get_estado_saldo(saldo)
        estado_imagen.content.controls[0].name = estado["icon"]
        estado_imagen.content.controls[0].color = estado["color"]
        estado_imagen.content.controls[1].value = estado["mensaje"]
        estado_imagen.content.controls[1].color = estado["color"]
        e.page.update()

def mostrarPantalla1(usuario_id):
    global saldo_text, estado_imagen
    
    # Obtener el saldo inicial
    saldo_inicial = get_saldo(usuario_id)
    estado_inicial = get_estado_saldo(saldo_inicial)
    
    # Crear el texto del saldo
    saldo_text = ft.Text(
        value=f"Bs. {saldo_inicial:.2f}",
        text_align=ft.TextAlign.CENTER,
        size=38,
        weight=ft.FontWeight.BOLD,
        font_family="Montserrat",
        italic=True,
        color="#F6F6F6"
    )
    
    # Crear el contenedor para la imagen y mensaje con fondo
    estado_imagen = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(
                    name=estado_inicial["icon"],
                    size=100,
                    color=estado_inicial["color"]
                ),
                ft.Text(
                    value=estado_inicial["mensaje"],
                    color=estado_inicial["color"],
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        margin=ft.margin.only(top=20, bottom=20),
        padding=20,  # Añadir padding interno
        bgcolor="#0E5675",  # Color de fondo más oscuro que el fondo principal
        border_radius=20,  # Bordes redondeados
        width=300,  # Ancho fijo para el contenedor
        alignment=ft.alignment.center,  # Centrar el contenido
        border=ft.border.all(1, "#D4D4CE"),  # Borde sutil
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.colors.with_opacity(0.3, "#000000"),
            offset=ft.Offset(0, 2)
        )
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
                            color="#F6F6F6"
                        ),
                        saldo_text
                    ],
                ),
            ),
            ft.Container(
                alignment=ft.alignment.bottom_right,
                content=ft.FloatingActionButton(
                    text="Agregar Saldo",
                    icon=ft.icons.ADD,
                    bgcolor="#D4D4CE",
                    foreground_color="#023246",
                    on_click=mostrarFormularioSaldo,
                ),
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.alignment.center,
                    controls=[
                        estado_imagen  # Contenedor con icono y mensaje
                    ]
                )
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    return ft.Container(
        content=contenido,
        margin=ft.margin.Margin(10, 65, 10, 10),
        alignment=ft.alignment.center,
    )