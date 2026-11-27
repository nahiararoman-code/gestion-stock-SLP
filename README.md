# Gestor de Stock Almacén SLP

Sistema de consola en Python para administrar el inventario de un almacén de barrio.

## Integrantes
- Román Nahiara 
- Saucedo Fabián 

## Ejecución
python main.py


## 📖 Manual de Usuario — Gestor de Stock Almacén SLP

Este programa permite administrar los productos, precios y cantidades disponibles de un almacén de forma sencilla desde la consola, sin necesidad de conocimientos de programación.

### 🚀 Cómo iniciar el sistema
1. Abrí la terminal o consola en la carpeta donde se encuentra el archivo main.py.
2. Escribí el siguiente comando y presioná *Enter*:
   ```bash
   python main.py

   Aparecerá en pantalla el menú principal con las opciones disponibles (1 a 6, y 0 para salir).
📋 Opciones del Menú Principal
 Opción 1 — Agregar producto:
Permite cargar un artículo nuevo al inventario. El sistema te pedirá:
 Nombre del producto: no puede quedar vacío.
 Stock inicial: debe ser un número entero mayor a 0 (ej. 15).
 Precio: debe ser un número positivo mayor a 0 (ej. 1250.50).
 Opción 2 — Listar productos:
Muestra en pantalla todos los artículos cargados junto con su cantidad disponible y su precio. Si todavía no cargaste nada, te avisará que la lista está vacía.
 Opción 3 — Buscar producto:
Permite escribir el nombre de un artículo para consultar rápidamente cuánto stock queda y cuánto cuesta.
Opción 4 — Modificar producto:
Buscá un producto por su nombre para actualizar su cantidad en stock y su precio de venta.
 Opción 5 — Eliminar producto:
Buscá un producto por su nombre para quitarlo definitivamente del inventario.
 Opción 6 — Ver stock bajo (Alerta de reposición):
Revisa todo el inventario y muestra únicamente los productos que tienen menos de 5 unidades disponibles, para que sepas qué mercadería necesitás reponer con urgencia.
 Opción 0 — Salir:
Cierra el programa de forma segura.

💡 Consejos importantes de uso
 Números sin letras: Cuando el sistema pida stock o precio, ingresá solo números. Si escribís letras por error, el programa te avisará y volverá a pedirte el dato sin cerrarse.
 Punto decimal: Para precios con centavos, usá punto (.) en lugar de coma (por ejemplo: 850.50).
 Datos en memoria: Los productos cargados se mantienen mientras el programa esté abierto; al elegir la opción 0 (Salir), se reinicia la sesión.
   
   
