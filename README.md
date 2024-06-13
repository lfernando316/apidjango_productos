## Endpoints:

### Obtener todos los productos
- **Método:** `GET`
- **URL:** `http://localhost:8000/productos/`
- **Descripción:** Devuelve una lista de todos los productos.

### Obtener un producto específico
- **Método:** `GET`
- **URL:** `http://localhost:8000/productos/{id}/`
- **Descripción:** Devuelve los detalles de un producto específico.
- **Parámetros:**
  - `id` (int): ID del producto.

### Crear un producto nuevo
- **Método:** `POST`
- **URL:** `http://localhost:8000/productos/crear_producto/`
- **Descripción:** Crea un nuevo producto.
- **Datos de la solicitud:**
  ```json
  {
    "nombre": "producto 1",
    "precio": 100.00,
    "descripcion": "descripción del producto"
  }

### Editar un producto 
- **Método:** `PUT`
- **URL:** `http://localhost:8000/productos/editar_producto/{id}/`
- **Descripción:** Edita el producto.
- **Datos de la solicitud:**  pasar el id del producto a editar
  ```json
  {
    "nombre": "producto editado"
  }
### Eliminar un producto 
- **Método:** `DELETE`
- **URL:** `http://localhost:8000/productos/eliminar_producto/{id}/`
- **Descripción:** Elimina el producto.
- **Datos de la solicitud: pasar el id del producto a eliminar
