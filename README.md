# Extractor de Indicadores Banco Central de Chile (BCCH) 🇨🇱📊

> Script en Python que automatiza la extracción de los principales indicadores económicos diarios conectándose directamente a la API oficial del Banco Central de Chile.

---

## 📌 Descripción

Este proyecto obtiene en tiempo real los valores del **Dólar (USD), UF, Euro (EUR), Yen (JPY) y Libra (GBP)** desde la API del BCCH. Está diseñado con un enfoque especial en la **seguridad de credenciales**, optimizado para ejecutarse en **Google Colab** mediante el uso de variables secretas (Secrets).

---

## 🚀 Características

| Característica | Descripción |
|---|---|
| 📅 **Días Hábiles** | Usa la librería `holidays` para saltar fines de semana y feriados bancarios chilenos automáticamente |
| 📈 **Extracción Dinámica** | Obtiene el valor observado de USD, EUR, UF, JPY y GBP en tiempo real |
| 🔐 **Seguridad Avanzada** | Lee credenciales desde un único secreto (`BCCH_AUTH`) dividiéndolas en memoria con el separador `@@` |
| 📊 **Exportación Automatizada** | Genera un panel de lectura en consola y exporta un archivo `.xlsx` listo para reportes |

---

## 📋 Requisitos Previos

1. Necesitas una **cuenta de acceso a la API del Banco Central de Chile**. Puedes registrarte en su [portal oficial](https://si3.bcentral.cl/estadisticas/Principal1/Web/BcchbddxpServicioAcceso/).

2. Instala las dependencias necesarias en tu entorno Python:

```bash
pip install bcchapi pandas holidays
```

---

## ⚙️ Configuración en Google Colab

Para mantener tus credenciales seguras sin exponerlas en el código fuente, este script utiliza la herramienta de **Secrets** de Google Colab.

### Paso a paso:

**1.** Abre el panel lateral izquierdo de Colab y haz clic en el ícono de la 🔑 **llave (Secrets)**.

**2.** Crea un nuevo secreto con el nombre **exactamente** como:
```
BCCH_AUTH
```

**3.** En el campo de valor, ingresa tu correo y contraseña separados **únicamente** por `@@`:
```
tu_correo@email.cl@@Tu_Contrasena_123
```

**4.** Activa el interruptor para **permitir que el cuaderno acceda** a este secreto.

> ⚠️ **Importante:** El separador `@@` es obligatorio y no debe aparecer en tu correo ni contraseña.

---

## 💻 Uso

Simplemente ejecuta el script. El código se encargará de manera automática de:

1. 🔑 Leer tu secreto de forma invisible desde Colab Secrets
2. ✂️ Separar las credenciales y conectarse a la API del BCCH
3. 📅 Consultar las series configuradas para el **último día hábil disponible**
4. 🖨️ Imprimir un resumen formateado en pantalla
5. 💾 Descargar un archivo Excel con el formato:

```
Indicadores_BCCH_AAAAMMDD.xlsx
```

---

## 🛠️ Modificar Indicadores

Si deseas agregar o quitar indicadores, modifica el diccionario `series` en la **sección 3** del código con el código de serie correspondiente del BCCH:

```python
series = {
    "USD": "F073.TCO.PRE.Z.D",    # Dólar observado
    "UF":  "F073.UFF.PRE.Z.D",    # Unidad de Fomento
    "EUR": "F073.TCE.PRE.Z.D",    # Euro
    "JPY": "F073.TCJ.PRE.Z.D",    # Yen japonés
    "GBP": "F073.TCL.PRE.Z.D",    # Libra esterlina
    # Agrega tus nuevas series aquí
}
```

> 💡 Puedes encontrar los códigos de otras series en el [catálogo de la API del BCCH](https://si3.bcentral.cl/estadisticas/Principal1/Web/BcchbddxpServicioAcceso/).

---

## 📁 Estructura del Proyecto

```
bcch-extractor/
│
├── extractor_bcch.ipynb    # Notebook principal (Google Colab)
├── README.md               # Este archivo
└── output/
    └── Indicadores_BCCH_AAAAMMDD.xlsx   # Archivo generado
```

---

## 🔒 Seguridad

Este proyecto **nunca expone credenciales en el código fuente**. El mecanismo de seguridad funciona así:

```
[Google Colab Secrets]
        │
        ▼
  BCCH_AUTH = "usuario@@contraseña"
        │
        ▼
  Split por "@@" en memoria RAM
        │
   ┌────┴────┐
   ▼         ▼
usuario  contraseña
   └────┬────┘
        ▼
  Conexión API BCCH
```

---

## 📦 Dependencias

| Librería | Versión recomendada | Uso |
|---|---|---|
| `bcchapi` | latest | Conexión con la API oficial del BCCH |
| `pandas` | ≥ 1.5 | Procesamiento y exportación de datos |
| `holidays` | ≥ 0.25 | Cálculo de días hábiles chilenos |
| `openpyxl` | ≥ 3.0 | Generación de archivos `.xlsx` |

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes una mejora:

1. Haz un **fork** del repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit: `git commit -m 'Agrega nueva funcionalidad'`
4. Haz push a la rama: `git push origin feature/nueva-funcionalidad`
5. Abre un **Pull Request**

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

<div align="center">
  Desarrollado para automatizar y facilitar el acceso a datos económicos de Chile 🇨🇱
</div>
