# Sales Explorer — Actividades 1 y 2

Dashboard de ventas desarrollado con Streamlit y Plotly.

- **App desplegada:** https://sales-explorer-act1-g3tiaadm3pyanumaat5d83.streamlit.app/
- **Actividad 1 (copia de respaldo):** `session1/activity1_starter/app_before_refactor.py`
- **Actividad 2 (app modular desplegada):** `session1/activity1_starter/app.py`

## Estructura de la versión desplegada

```text
session1/activity1_starter/
├── app.py                   # Interfaz, filtros, KPIs y ensamblaje
├── app_before_refactor.py   # Copia de respaldo de Actividad 1
├── data/
│   ├── __init__.py
│   └── loaders.py           # clean_sales, load_sales y @st.cache_data
└── components/
    ├── __init__.py
    └── charts.py            # daily_units_chart, top_skus_chart
```

Los datos siguen en `sales_daily.csv` en la raíz del repositorio. La limpieza descarta duplicados y registros con unidades negativas, y recalcula ingresos a partir de unidades y precio. Los filtros tienen claves independientes; si no quedan filas, se muestra `st.warning` y se ejecuta `st.stop`.

## Ejecución local

```powershell
python -m pip install -r requirements.txt
python -m streamlit run session1/activity1_starter/app.py
```

La configuración de Streamlit Cloud debe seguir apuntando al archivo
`session1/activity1_starter/app.py`.

## Comparación con `session1/activity2_solution` del kit

**Diferencia 1 — Ubicación del CSV:** La solución del kit espera
`data/sales_daily.csv`, mientras que nuestro loader usa `sales_daily.csv`
en la raíz. Se mantuvo esta ruta para respetar el proyecto y el despliegue
existentes sin duplicar el dataset. A diferencia del kit, tampoco usamos el
fallback de entorno `SALES_CSV`, ya que trabajamos con una única fuente pública.

**Diferencia 2 — Preservación de la visualización original:** El kit presenta
el gráfico de los mejores SKU en barras verticales. Conservamos las barras
**horizontales**, la ordenación y los textos de la Actividad 1; además,
conservamos la tabla completa de filas filtradas en lugar de limitarla a 500.
Esto permite comparar la app antes y después de la refactorización sin cambiar
su comportamiento de usuario.

## Comprobación de equivalencia

Compara la copia `app_before_refactor.py` con la app actual usando las mismas
regiones y categorías: deben coincidir unidades, ingreso, cantidad de SKU,
ventas diarias, ranking de 10 SKU y filas filtradas. Con todos los filtros
vacíos, la versión nueva muestra una advertencia amigable, en lugar de
visualizaciones vacías.

## Seguridad

El archivo `.gitignore` excluye `.venv/`, `__pycache__/` y
`.streamlit/secrets.toml`. Nunca guardar credenciales en el repositorio.
