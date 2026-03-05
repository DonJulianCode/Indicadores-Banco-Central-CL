"""
Extractor de Indicadores Banco Central de Chile (BCCH)
Versión: Script independiente para GitHub Actions
"""

import os
import sys
import bcchapi
import pandas as pd
from datetime import date, timedelta
import holidays


# 1. Configuración de Fechas
def obtener_ultimo_dia_habil():
    hoy = date.today()
    feriados = holidays.Chile(years=[hoy.year - 1, hoy.year])
    for anio in [hoy.year - 1, hoy.year]:
        feriados[date(anio, 12, 31)] = "Feriado Bancario"

    fecha = hoy - timedelta(days=1)
    while fecha.weekday() >= 5 or fecha in feriados:
        fecha -= timedelta(days=1)
    return fecha


fecha_consulta = obtener_ultimo_dia_habil() + timedelta(days=1)


# 2. Conexión Segura via Variables de Entorno (GitHub Secrets)
credenciales_crudas = os.environ.get("BCCH_AUTH")

if not credenciales_crudas:
    print("❌ Error: La variable de entorno BCCH_AUTH no está definida.")
    print("   Configura el secreto en: Settings > Secrets > Actions > New repository secret")
    sys.exit(1)

try:
    usuario, clave = credenciales_crudas.split("@@")
except ValueError:
    print("❌ Error: El formato de BCCH_AUTH es incorrecto.")
    print("   Formato esperado: tu_correo@email.cl@@Tu_Contrasena_123")
    sys.exit(1)

siete = bcchapi.Siete(usuario, clave)


# 3. Diccionario de Series del BCCH
series = {
    "USD": "F073.TCO.PRE.Z.D",    # Dólar observado
    "EUR": "F072.CLP.EUR.N.O.D",  # Euro
    "UF":  "F073.UFF.PRE.Z.D",    # Unidad de Fomento
    "JPY": "F072.CLP.JPY.N.O.D",  # Yen Japonés
    "GBP": "F072.CLP.GBP.N.O.D"   # Libra Esterlina
}


# 4. Extracción de Indicadores
indicadores_hoy = {}
for nombre, codigo in series.items():
    try:
        df = siete.cuadro(
            series=[codigo],
            nombres=[nombre],
            desde=fecha_consulta.strftime("%Y-%m-%d"),
            hasta=fecha_consulta.strftime("%Y-%m-%d"),
            frecuencia="D",
            observado={nombre: "last"}
        )
        valor = float(df.iloc[0, 0])
        indicadores_hoy[nombre] = valor
    except Exception as e:
        print(f"⚠️  Advertencia: No se pudo obtener {nombre}. Detalle: {e}")
        indicadores_hoy[nombre] = None


# 5. Panel Final
df_panel = pd.DataFrame(list(indicadores_hoy.items()), columns=["Indicador", "Valor"])
df_panel["Fecha"] = fecha_consulta.strftime("%d-%m-%Y")

print("\n" + "=" * 35)
print(f" PANEL DE INDICADORES AL {fecha_consulta.strftime('%d-%m-%Y')} ")
print("=" * 35)
print(df_panel.to_string(index=False))
print("=" * 35)


# 6. Exportar a Excel en carpeta output/
os.makedirs("output", exist_ok=True)
nombre_archivo = f"output/Indicadores_BCCH_{fecha_consulta.strftime('%Y%m%d')}.xlsx"
df_panel.to_excel(nombre_archivo, index=False)
print(f"\n✅ Archivo '{nombre_archivo}' generado con éxito!")
