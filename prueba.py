import os
import shutil

RUTA_LOGS = "logs"

# Contenido de los archivos
archivos = {
    "error1.log_app_1": """[2026-01-11 10:15:23] ERROR: No se pudo conectar a la base de datos.
[2026-01-11 10:16:01] INFO: Reintentando conexión.
[2026-01-11 10:16:05] ERROR: Tiempo de espera agotado.
""",
    "error2.log_app_1": """[2026-01-11 11:02:10] ERROR: Usuario no autorizado.
[2026-01-11 11:02:11] WARNING: Intento de acceso sospechoso.
[2026-01-11 11:02:15] INFO: Sesión bloqueada.
""",
    "sistema1.log_app_2": """[2026-01-11 09:30:00] INFO: Servicio iniciado correctamente.
[2026-01-11 09:45:12] INFO: Uso de CPU: 35%.
[2026-01-11 09:50:45] INFO: Uso de memoria: 512MB.
""",
    "sistema2.log_app_2": """[2026-01-11 12:20:33] INFO: Actualización del sistema completada.
[2026-01-11 12:21:00] INFO: Reinicio programado.
[2026-01-11 12:25:10] INFO: Sistema operativo estable.
""",
    "seguridad.log_app_3": """[2026-01-11 08:05:40] SECURITY: Antivirus actualizado.
[2026-01-11 08:10:22] SECURITY: Escaneo completo iniciado.
[2026-01-11 08:45:00] SECURITY: No se encontraron amenazas.
"""
}

# Extensiones y carpetas
EXTENSIONES = {
    ".log_app_1": "log_app_1",
    ".log_app_2": "log_app_2",
    ".log_app_3": "log_app_3"
}

# Crear carpeta principal
if not os.path.exists(RUTA_LOGS):
    os.makedirs(RUTA_LOGS)

# Crear carpetas destino
for carpeta in EXTENSIONES.values():
    ruta = os.path.join(RUTA_LOGS, carpeta)
    if not os.path.exists(ruta):
        os.makedirs(ruta)

# Crear archivos
for nombre, contenido in archivos.items():
    with open(os.path.join(RUTA_LOGS, nombre), "w", encoding="utf-8") as f:
        f.write(contenido)

print("Archivos de log creados.")

# Clasificar archivos
for archivo in os.listdir(RUTA_LOGS):
    ruta_archivo = os.path.join(RUTA_LOGS, archivo)
    if os.path.isfile(ruta_archivo):
        for ext, carpeta in EXTENSIONES.items():
            if archivo.endswith(ext):
                destino = os.path.join(RUTA_LOGS, carpeta, archivo)
                shutil.move(ruta_archivo, destino)
                print(f"Movido: {archivo} -> {carpeta}")
                break

print("Clasificación de logs finalizada.")
