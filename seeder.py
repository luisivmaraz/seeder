import requests
import random

API_URL = "https://space-api-7odx.onrender.com/"

espacios_defecto = [
    "Sala de Urgencias",
    "Quirófano 1",
    "Consultorio 2",
    "Radiología",
    "Laboratorio",
    "Sala de Espera",
    "Área de Rehabilitación",
    "Farmacia",
    "Consultorio 3",
    "Área de Cuidados Intensivos"
]

areas_defecto = [
    "Área de atención crítica",
    "Área quirúrgica",
    "Área de diagnóstico",
    "Área de consulta externa",
    "Área administrativa",
    "Área de emergencias"
]

estados = ["Cerrado", "En mantenimiento", "Operativo", "Disponible"]

def crear_datos(cantidad):
    for _ in range(cantidad):
        datos = {
            "espacio": random.choice(espacios_defecto),
            "area": random.choice(areas_defecto),
            "estado": random.choice(estados)
        }
        respuesta = requests.post(API_URL, json=datos)
        if respuesta.status_code == 200:
            print(f"Datos enviados correctamente: {datos}")
        else:
            print(f"Error al enviar datos: {respuesta.status_code} - {respuesta.text}")

if __name__ == "__main__":
    try:
        cantidad = int(input("¿Cuántos registros deseas crear?: "))
        crear_datos(cantidad)
    except ValueError:
        print("Por favor, ingresa un número válido.")
