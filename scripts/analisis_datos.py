import os
import pandas as pd

def cargar_datos(ruta_csv: str) -> pd.DataFrame:
    """
    Carga el archivo CSV de ventas y devuelve un DataFrame de pandas.
    """
    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")
    df = pd.read_csv(ruta_csv)
    return df


def preparar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convierte la fecha a tipo datetime y calcula el monto de venta por registro.
    """
    # Asegurar tipo datetime en la columna de fecha
    df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])

    # Crear columna con el monto de cada venta
    df["monto_venta"] = df["cantidad_vendida"] * df["precio"]

    # Crear columna año-mes (por ejemplo 2026-01)
    df["anio_mes"] = df["fecha_venta"].dt.to_period("M").astype(str)

    return df


def calcular_metricas(df: pd.DataFrame) -> dict:
    """
    Calcula métricas principales del escenario B:
    - ventas_totales
    - producto_mas_vendido
    - unidades_producto_mas_vendido
    - ventas_por_mes (DataFrame)
    """
    # Ventas totales
    ventas_totales = df["monto_venta"].sum()

    # Producto más vendido por cantidad de unidades
    unidades_por_producto = df.groupby("producto")["cantidad_vendida"].sum()
    producto_mas_vendido = unidades_por_producto.idxmax()
    unidades_producto_mas_vendido = unidades_por_producto.max()

    # Ventas por mes (sumando monto_venta)
    ventas_por_mes = (
        df.groupby("anio_mes")["monto_venta"]
        .sum()
        .reset_index()
        .sort_values("anio_mes")
    )

    metricas = {
        "ventas_totales": ventas_totales,
        "producto_mas_vendido": producto_mas_vendido,
        "unidades_producto_mas_vendido": unidades_producto_mas_vendido,
        "ventas_por_mes": ventas_por_mes,
    }

    return metricas


def mostrar_resumen_en_consola(metricas: dict) -> None:
    """
    Imprime un resumen de las métricas principales por consola.
    """
    print("===== Resumen del análisis de ventas =====")
    print(f"Ventas totales: {metricas['ventas_totales']:.2f}")
    print(
        "Producto más vendido: "
        f"{metricas['producto_mas_vendido']} "
        f"({metricas['unidades_producto_mas_vendido']} unidades)"
    )
    print("Ventas por mes:")
    print(metricas["ventas_por_mes"])



# Rutas relativas según la estructura sugerida del repositorio
ruta_csv = os.path.join("datos", "data_ventas.csv")
ruta_grafico = os.path.join("resultados", "ventas_por_mes.png")

# 1) Cargar datos
df = cargar_datos(ruta_csv)

# 2) Preparar datos (fechas, monto_venta, año-mes)
df = preparar_datos(df)

# 3) Calcular métricas principales
metricas = calcular_metricas(df)

# 5) Mostrar un resumen por consola
mostrar_resumen_en_consola(metricas)
