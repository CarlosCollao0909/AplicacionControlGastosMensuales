import flet as ft
from db import get_gastos_por_fecha, get_user_id
from datetime import datetime
import calendar
import locale

# Establecer el locale en español
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')
    except:
        pass

normal_radius = 120
hover_radius = 140
normal_title_style = ft.TextStyle(
    size=12, color="#F6F6F6", weight=ft.FontWeight.BOLD
)
hover_title_style = ft.TextStyle(
    size=16,
    color="#F6F6F6",
    weight=ft.FontWeight.BOLD,
    shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
)
normal_badge_size = 40

def badge(icon, size):
    return ft.Container(
        ft.Icon(icon),
        width=size,
        height=size,
        border=ft.border.all(1, "#D4D4CE"),
        border_radius=size / 2,
        bgcolor="#287094",
    )

def get_monthly_expenses(usuario_id):
    # Obtener el año actual
    current_year = datetime.now().year
    
    # Crear un diccionario para almacenar los gastos por mes
    monthly_expenses = {}
    
    # Obtener el primer día del año y el último día del año actual
    start_date = f"{current_year}-01-01"
    end_date = f"{current_year}-12-31"
    
    # Obtener todos los gastos del año
    gastos = get_gastos_por_fecha(usuario_id, start_date, end_date)
    
    # Inicializar el diccionario con todos los meses
    for month_num in range(1, 13):
        try:
            month_name = calendar.month_name[month_num].capitalize()
        except:
            month_name = f"Mes {month_num}"
        monthly_expenses[month_name] = 0
    
    # Sumar los gastos por mes
    for gasto in gastos:
        fecha = datetime.strptime(gasto[3], '%Y-%m-%d')
        try:
            month_name = calendar.month_name[fecha.month].capitalize()
        except:
            month_name = f"Mes {fecha.month}"
        monthly_expenses[month_name] += gasto[2]  # gasto[2] es el monto
    
    # Filtrar solo los meses con gastos
    return {k: v for k, v in monthly_expenses.items() if v > 0}

def create_pie_chart(usuario_id):
    # Obtener los gastos mensuales del usuario
    monthly_expenses = get_monthly_expenses(usuario_id)
    
    # Si no hay gastos, mostrar un mensaje
    if not monthly_expenses:
        return ft.Text(
            "No hay gastos registrados este año",
            size=20,
            color="#F6F6F6",
            weight=ft.FontWeight.BOLD
        )
    
    # Colores para los meses
    colors = [
        ft.colors.DEEP_ORANGE, ft.colors.GREEN, ft.colors.PURPLE, 
        ft.colors.ORANGE, ft.colors.PINK, ft.colors.CYAN,
        ft.colors.AMBER, ft.colors.LIME, ft.colors.INDIGO,
        ft.colors.TEAL, ft.colors.BROWN, ft.colors.RED
    ]
    
    # Calcular el total de gastos
    total_expenses = sum(monthly_expenses.values())
    
    # Crear las secciones del gráfico
    sections = []
    for (month, amount), color in zip(monthly_expenses.items(), colors):
        percentage = (amount / total_expenses) * 100
        sections.append(
            ft.PieChartSection(
                percentage,
                title=f"{month}\n(BS. {amount:.2f})",
                title_style=normal_title_style,
                color=color,
                radius=normal_radius,
                badge=badge(ft.icons.CALENDAR_MONTH, normal_badge_size),
                badge_position=0.98,
            )
        )
    
    def on_chart_event(e: ft.PieChartEvent):
        for idx, section in enumerate(pie_chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                section.title_style = hover_title_style
            else:
                section.radius = normal_radius
                section.title_style = normal_title_style
        pie_chart.update()
    
    pie_chart = ft.PieChart(
        sections=sections,
        sections_space=0,
        center_space_radius=0,
        on_chart_event=on_chart_event,
        expand=True,
    )
    
    return pie_chart

class PantallaReportes(ft.UserControl):
    def __init__(self, usuario_id):
        super().__init__()
        self.usuario_id = usuario_id
        
    def build(self):
        # Crear el gráfico
        chart = create_pie_chart(self.usuario_id)
        
        # Obtener el total de gastos
        monthly_expenses = get_monthly_expenses(self.usuario_id)
        total_gastos = sum(monthly_expenses.values())
        
        # Crear el contenido
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        value="Gastos Mensuales",
                        text_align=ft.TextAlign.CENTER,
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        italic=True,
                        color="#F6F6F6",
                    ),
                    chart,
                    ft.Text(
                        value=f"Total de gastos: Bs. {total_gastos:.2f}",
                        text_align=ft.TextAlign.CENTER,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#F6F6F6",
                    ) if total_gastos > 0 else None
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            margin=ft.margin.Margin(10, 50, 10, 10),
            alignment=ft.alignment.center
        )

def mostrarPantalla3():
    # En lugar de tratar de obtener el email desde la página,
    # lo obtendremos desde el módulo opcion1 donde ya está guardado
    from opcion1 import get_current_email
    
    # Obtener el email actual
    user_email = get_current_email()
    
    # Obtener el ID del usuario
    usuario_id = get_user_id(user_email)
    
    # Retornar la pantalla de reportes
    return PantallaReportes(usuario_id)