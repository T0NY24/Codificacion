# Primero hize una lista de trabajadores con su sueldo
personas = [
    {"nombre": "Juan", "trabajo": "Ingeniero", "sueldo": 75000},
    {"nombre": "María", "trabajo": "Doctora", "sueldo": 90000},
    {"nombre": "Carlos", "trabajo": "Profesor", "sueldo": 55000},
    {"nombre": "Laura", "trabajo": "Abogada", "sueldo": 80000},
    {"nombre": "Pedro", "trabajo": "Chef", "sueldo": 60000},
    {"nombre": "Ana", "trabajo": "Enfermera", "sueldo": 50000},
    {"nombre": "Luis", "trabajo": "Electricista", "sueldo": 45000},
    {"nombre": "Marta", "trabajo": "Diseñadora", "sueldo": 70000},
    {"nombre": "Raúl", "trabajo": "Mecánico", "sueldo": 48000},
    {"nombre": "Sofía", "trabajo": "Programadora", "sueldo": 85000},
    {"nombre": "David", "trabajo": "Contador", "sueldo": 65000},
    {"nombre": "Julia", "trabajo": "Arquitecta", "sueldo": 78000},
    {"nombre": "Fernando", "trabajo": "Piloto", "sueldo": 95000},
    {"nombre": "Lucía", "trabajo": "Fotógrafa", "sueldo": 52000},
    {"nombre": "Sergio", "trabajo": "Carpintero", "sueldo": 43000}
]

print("Hola, ¿qué quieres hacer?")
opcion = input("1. Ver el sueldo más bajo\n2. Ver el sueldo más alto\nElige una opción (1 o 2): ")

if opcion == "1":
    
    sueldo_mas_bajo = min(persona["sueldo"] for persona in personas)
    personas_sueldo_mas_bajo = [persona for persona in personas if persona["sueldo"] == sueldo_mas_bajo]

    print("\nLa persona con el sueldo más bajo es:")
    for persona in personas_sueldo_mas_bajo:
        print(f"Nombre: {persona['nombre']}, Trabajo: {persona['trabajo']}, Sueldo: {persona['sueldo']}")

elif opcion == "2":
    
    sueldo_mas_alto = max(persona["sueldo"] for persona in personas)
    personas_sueldo_mas_alto = [persona for persona in personas if persona["sueldo"] == sueldo_mas_alto]

    print("\nLa persona con el sueldo más alto es:")
    for persona in personas_sueldo_mas_alto:
        print(f"Nombre: {persona['nombre']}, Trabajo: {persona['trabajo']}, Sueldo: {persona['sueldo']}")

else:
    print("Opción no válida. Por favor, elige 1 o 2.")