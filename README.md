# Predicción de Riesgo Epidemiológico de Dengue en Piura

Este proyecto implementa un pipeline de Machine Learning para predecir el nivel de riesgo semanal de brotes de dengue en la región de Piura, Perú. Integra series temporales meteorológicas y datos epidemiológicos para establecer un sistema de alerta temprana.

## Arquitectura de Datos (ETL)
*   **Fuentes:** Registros epidemiológicos del MINSA y datos climáticos de estaciones terrestres (SENAMHI) y satelitales (NASA POWER).
*   **Procesamiento:** Imputación de anomalías físicas, interpolación espacial para homogeneización regional y creación de rezagos temporales (lags $t-1, t-2$) para modelar el ciclo de vida del vector *Aedes aegypti*.

## Modelado y Evaluación
Se evaluaron tres algoritmos abordando el desbalance de clases epidemiológicas mediante pesos ponderados:
1.  Regresión Logística (Baseline Lineal)
2.  Support Vector Machine (Kernel RBF)
3.  **Random Forest Classifier** (Modelo Seleccionado)

El modelo Random Forest logró un **Recall del 1.00** para la clase de riesgo "Alto", demostrando ser la arquitectura óptima para priorizar la sensibilidad en alertas sanitarias, reduciendo a cero los falsos negativos en escenarios críticos.

## Estructura del Repositorio
*   `01_Exploracion_y_ETL.ipynb`: Extracción, limpieza y consolidación de la matriz climática-epidemiológica.
*   `02_Entrenamiento_y_Evaluacion.ipynb`: Hold-out cronológico, entrenamiento de modelos y generación de métricas de desempeño.
*   `data/`: Datasets crudos y procesados.
*   `models/`: Modelo exportado en formato `.pkl` y visualizaciones de importancia de características e inercia térmica.

## Tecnologías Utilizadas
*   Python 3
*   Pandas, NumPy
*   Scikit-Learn
*   Matplotlib