import os

def cargar_clientes(nombre_archivo):
    clientes = []
    with open(nombre_archivo, "r") as archivo:
        next(archivo)  # saltar encabezado
        for linea in archivo:
            cedula, nombre, saldo = linea.strip().split(",")
            clientes.append([cedula.strip(), nombre.strip(), float(saldo)])
    return clientes

def buscar_saldo_por_nombre(clientes, nombre_buscar):
    for cliente in clientes:
        if cliente[1].lower() == nombre_buscar.lower():
            return cliente[2]
    return None

def contar_saldos_mayores(clientes, limite=50):
    return sum(1 for cliente in clientes if cliente[2] > limite)

def listar_clientes_por_saldo(clientes):
    clientes_ordenados = sorted(clientes, key=lambda x: x[2])
    for cliente in clientes_ordenados:
        print(f"{cliente[1]} - Saldo: {cliente[2]}")

# Asegurar ruta correcta
base_dir = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(base_dir, "clientes.txt")

clientes = cargar_clientes(archivo)

print("=BANCO=")
print("1. Buscar saldo por nombre")
print("2. Contar clientes con saldo > 50")
print("3. Listar clientes por saldo ascendente")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    nombre = input("Ingrese el nombre del cliente: ")
    saldo = buscar_saldo_por_nombre(clientes, nombre)
    if saldo is not None:
        print(f"El saldo de {nombre} es: {saldo}")
    else:
        print("Cliente no encontrado.")

elif opcion == "2":
    cantidad = contar_saldos_mayores(clientes, 50)
    print(f"Hay {cantidad} cliente(s) con saldo mayor a 50.")

elif opcion == "3":
    print("\nClientes ordenados por saldo:")
    listar_clientes_por_saldo(clientes)

else:
    print("Opción no válida.")
