# Administrador de Colección

Este proyecto es una aplicación de consola para administrar una colección de elementos relacionados con ingredientes, hamburguesas, chefs y categorías. Permite añadir, listar, buscar, editar y eliminar elementos, así como filtrar por categorías.

---

## Características

- Añadir nuevos elementos (ingredientes, hamburguesas, chefs, categorías).
- Listar todos los elementos por tipo.
- Buscar elementos específicos según diferentes criterios.
- Editar elementos existentes.
- Eliminar elementos.
- Visualizar elementos filtrados por categoría.
- Interfaz de usuario basada en menú de texto en consola.

---

## Estructura del Proyecto

- 'main.py'(o archivo principal): contiene la lógica del menú y la interacción con el usuario.
- 'controllers/coleccion_services.py': funciones para manejar la lógica de negocio (agregar, listar, buscar, editar, eliminar).
- 'utils/json_handler.py': funciones para cargar y guardar datos en formato JSON.
- 'data/coleccion.json': archivo JSON donde se almacenan los datos de la colección.

---
