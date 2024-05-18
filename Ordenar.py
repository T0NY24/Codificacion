# Primero hize una lista de trabajadores con Nombres al azar
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
def ordenar(personas, clave):
    for i in range(len(personas) - 1):
        min_idx = i
        for j in range(i + 1, len(personas)):
            if personas[j][clave] < personas[min_idx][clave]:
                min_idx = j
        personas[i], personas[min_idx] = personas[min_idx], personas[i]

print("Hola, ¿qué quieres hacer?")
opcion = input("1. Ordenar por nombre\n2. Ordenar por sueldo\nElige 1 o 2: ")

if opcion == '1':
    ordenar(personas, "nombre")
    print("Ordenado por nombre:")
elif opcion == '2':
    ordenar(personas, "sueldo")
    print("Ordenado por sueldo:")
else:
    print("Opción no válida")

for persona in personas:
    print(persona)
