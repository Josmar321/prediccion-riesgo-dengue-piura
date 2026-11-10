import os
import re

DIRECTORIO_RAIZ = "."
MODO_PRUEBA = False

# Busca el año (4 dígitos) y el mes (2 dígitos)
patron_fecha = re.compile(r'(\d{4})[-_]?(\d{2})')

for raiz, carpetas, archivos in os.walk(DIRECTORIO_RAIZ):
    nombre_carpeta = os.path.basename(raiz)
    
    if nombre_carpeta in [".", "csv", ""]:
        continue
    
    # .rsplit('_', 1)[0] quita únicamente el "_Senamhi" del final
    # Respeta nombres compuestos como "La_Libertad", "Madre_de_Dios" o "San_Martin"
    region = nombre_carpeta.rsplit('_', 1)[0]
    
    for archivo in archivos:
        if archivo.endswith(".csv"):
            coincidencia = patron_fecha.search(archivo)
            
            if coincidencia:
                anio = coincidencia.group(1)
                mes = coincidencia.group(2)
                
                nuevo_nombre = f"{region}_{anio}_{mes}.csv"
                
                ruta_vieja = os.path.join(raiz, archivo)
                ruta_nueva = os.path.join(raiz, nuevo_nombre)
                
                if MODO_PRUEBA:
                    print(f"📁 Subcarpeta [{nombre_carpeta}]: {archivo}  ===>  {nuevo_nombre}")
                else:
                    os.rename(ruta_vieja, ruta_nueva)
                    print(f"✅ [RENOMBRADO en {nombre_carpeta}]: {archivo}  ===>  {nuevo_nombre}")

if MODO_PRUEBA:
    print("\n--- SIMULACIÓN FINALIZADA ---")
    print("Revisa la lista. Ahora 'La_Libertad_Senamhi' generará 'La_Libertad_2023_01.csv'.")