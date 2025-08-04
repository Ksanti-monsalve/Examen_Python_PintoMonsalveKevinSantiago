import os
import sys

from tabulate import tabulate



DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "coleccion.json")

coleccion = []

def agregar_elemento(tipo):
    print(f"Ingresando un nuevo {tipo}:")
    ingredientes = input("ingredientes: ").strip()
    comida = input("hamburguesas: ").strip()
    chef = input("chefs: ").strip()
    categoria = input("categoria: ").strip()
    nuevo = Item(tipo, ingredientes, comida, chef, categoria)
    coleccion.append(nuevo)
    print(f"{tipo} agregado correctamente.\n")

def listar_elementos(tipo=None):
    if tipo:
        items = [i for i in coleccion if i.tipo == tipo]
    else:
        items = coleccion

    if not items:
        print("No hay elementos para mostrar.")
        return

    tabla = []
    for i in items:
        tabla.append([i.id, i.tipo, i.ingredientes, i.comida, i.chefs, i.categoria or ""])
    headers = ["ID", "Tipo", "ingredientes", "comida", "chefs", "categoria"]
    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))

def listar_por_categoria(categoria):
    listar_elementos(categoria)

def buscar_elemento(criterio):
    valor = input(f"Ingrese el {criterio} para buscar: ").strip().lower()
    encontrados = []
    for item in coleccion:
        attr = getattr(item, criterio)
        if attr and valor in attr.lower():
            encontrados.append(item)
    if encontrados:
        tabla = [[i.id, i.tipo, i.ingredientes, i.comida, i.chefs, i.categoria or ""] for i in encontrados]
        headers = ["ID", "Tipo", "inf¡gredientes", "comida", "chefs", "categoria"]
        print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No se encontraron elementos con ese criterio.")

def editar_elemento(campo):
    id_buscar = input("Ingrese el ID del elemento a editar: ").strip()
    item = next((i for i in coleccion if i.id == id_buscar), None)
    if not item:
        print("Elemento no encontrado.")
        return

    nuevo_valor = input(f"Ingrese nuevo valor para {campo}: ").strip()
    if campo == "valoracion" and nuevo_valor == "":
        nuevo_valor = None

    setattr(item, campo, nuevo_valor)
    print("Elemento actualizado correctamente.")

def eliminar_elemento(opcion):
    if opcion == '1':
        titulo = input("Ingrese el título del elemento a eliminar: ").strip().lower()
        antes = len(coleccion)
        coleccion[:] = [i for i in coleccion if i.titulo.lower() != titulo]
        eliminados = antes - len(coleccion)
        print(f"{eliminados} elementos eliminados.")
    elif opcion == '2':
        id_eliminar = input("Ingrese el ID del elemento a eliminar: ").strip()
        antes = len(coleccion)
        coleccion[:] = [i for i in coleccion if i.id != id_eliminar]
        if len(coleccion) < antes:
            print("Elemento eliminado correctamente.")
        else:
            print("No se encontró elemento con ese ID.")

def guardar_coleccion():
    datos = [i.to_dict() for i in coleccion]
    guardar_json(DATA_FILE, datos)
    print("Colección guardada correctamente.")

def cargar_coleccion():
    global coleccion
    datos = cargar_json(DATA_FILE)
    coleccion = [Item.from_dict(d) for d in datos]
    print("Colección cargada correctamente.")