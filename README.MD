# Módulo 8 – Entrega final de portafolio

## enlace al repositorio público

- <https://github.com/ATorresGa/ecommerce_m8>

## requisitos e instalación (entorno virtual, dependencias)

- Requisitos de paquetes de instalacion todo esta agregado al archivo requirements.txt generado con pip freeze

## cómo ejecutar en local (migraciones, runserver)

- Crea una base de datos con el nombre de ecommerce-m8
- Usa el archivo en config llamado secrets-example para tener una guia de estructura del archivo secrets
- Ejecuta python manage.py makemigrations y python manage.py migrate para generar las tablas en bd
- Ejecuta python runserver y ejecuta el proyecto en la ip que te entrega la consola

## Rutas Principales

---

- Rutas Publicas

---

- <http://127.0.0.1:8000/>
- <http://127.0.0.1:8000/productos/>
- <http://127.0.0.1:8000/producto/1/> (Detalle producto)

---

- Rutas Privadas

---

- <http://127.0.0.1:8000/carrito/>

---

- Rutas Admin

---

- <http://127.0.0.1:8000/admin/>

---

## Credenciales de prueba

- admin - 1234
- user1 - asdasd1234
