import os
import sys

from tabulate import tabulate
from controllers.coleccion_services import (
    agregar_elemento,
    listar_elementos,
    buscar_elemento,
    editar_elemento,
    eliminar_elemento,
    listar_por_categoria
)
from utils.json_handler import cargar_json, guardar_json

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "coleccion.json")

def mostrar_menu_principal():
    print("""
===========================================
         Administrador de Colección
===========================================
1. Añadir un Nuevo Elemento
2. Ver Todos los Elementos
3. Buscar un Elemento
4. Editar un Elemento
5. Eliminar un Elemento
6. Ver Elementos por Categoría
7. Salir
===========================================
Selecciona una opción (1-7): """)

def menu_añadir():
    while True:
        print("""
===========================================
          Añadir un Nuevo Elemento
===========================================
¿Qué tipo de elemento deseas añadir?
1. Ingredientes
2. Hamburguesas
3. Chefs
4. Categorias
5. Regresar al menu principal
===========================================
Selecciona una opción (1-5): """, end='')
        op = input().strip()
        if op == '5':
            break
        tipos = {'1': 'ingredientes', '2': 'hamburguesas', '3': 'chefs', '4': 'categorias'}
        if op in tipos:
            agregar_elemento(tipos[op])
        else:
            print("Opción inválida, intenta de nuevo.")

def menu_listar():
    while True:
        print("""
===========================================
           Ver Todos los Elementos
===========================================
¿Qué categoría deseas ver?
1. Ver Todos los ingredientes
2. Ver Todas las hamburguesas
3. Ver Todos los chefs
4. Ver Todas las categorias
5. Regresar al menu principal
===========================================
Selecciona una opción (1-5): """, end='')
        op = input().strip()
        categorias = {'1': 'ingredientes', '2': 'hamburguesas', '3': 'chefs', '4': 'categorias'}
        if op == '5':
            break
        elif op in categorias:
            listar_elementos(categorias[op])
        else:
            print("Opción inválida, intenta de nuevo.")

def menu_buscar():
    while True:
        print("""
===========================================
             Buscar un Elemento
===========================================
¿Cómo deseas buscar?
1. Buscar por ingredientes
2. Buscar por tipo de hamburguesa
3. Buscar por chef
4. buscar por categoria        
5. Regresar al Menú Principal
===========================================
Selecciona una opción (1-5): """, end='')
        op = input().strip()
        if op == '5':
            break
        criterios = {'1': 'ingredientes', '2': 'hamburguesas', '3': 'chefs', '4': 'categorias'}
        if op in criterios:
            buscar_elemento(criterios[op])
        else:
            print("Opción inválida, intenta de nuevo.")

def menu_editar():
    while True:
        print("""
===========================================
            Editar un Elemento
===========================================
¿Qué tipo de cambio deseas realizar?
1. Editar ingredientes
2. Editar hamburguesas
3. Editar categorias
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4): """, end='')
        op = input().strip()
        if op == '5':
            break
        campos = {'1': 'ingredientes', '2': 'hamburguesas', '3': 'categorias'}
        if op in campos:
            editar_elemento(campos[op])
        else:
            print("Opción inválida, intenta de nuevo.")

def menu_eliminar():
    while True:
        print("""
===========================================
          Eliminar un Elemento
===========================================
¿Cómo deseas eliminar?
1. Eliminar ingredientes
2. Eliminar hamburguesas
3. Eliminar categoria
4. Regresar al Menú Principal
===========================================
Selecciona una opción (1-4): """, end='')
        op = input().strip()
        if op == '4':
            break
        campos = {'1': 'ingredientes', '2': 'hamburguesas', '3': 'categorias'}
        if op in ['1', '2', '3']:
            eliminar_elemento(op)
        else:
            print("Opción inválida, intenta de nuevo.")

def menu_por_categoria():
    while True:
        print("""
===========================================
       Ver Elementos por Categoría
===========================================
¿Qué categoría deseas ver?
1. Ver categoria
===========================================
Selecciona una opción (1-1): """, end='')
        op = input().strip()
        categorias = {'1': 'categoria',}
        if op == '1':
            break
        elif op in categorias:
            listar_por_categoria(categorias[op])
        else:
            print("Opción inválida, intenta de nuevo.")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input().strip()
        if opcion == '1':
            menu_añadir()
            agregar_elemento()
        elif opcion == '2':
            menu_listar()
            listar_elementos()
        elif opcion == '3':
            menu_buscar()
            buscar_elemento()
        elif opcion == '5':
            menu_editar()
            editar_elemento()
        elif opcion == '6':
            menu_eliminar()
            eliminar_elemento()
        elif opcion == '7':
            menu_por_categoria()
            listar_por_categoria()
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()