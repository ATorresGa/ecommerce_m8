# Changelog

Todos los cambios importantes de **PortafolioCommerce** serán documentados en este archivo.

El formato está basado en Keep a Changelog y este proyecto utiliza Versionado Semántico (SemVer).

---

## [Unreleased]

### Added

* Pendiente de desarrollo.

---

## [0.4.0] - 2026-07-08

### Added

* Implementación completa del CRUD de productos mediante vistas genéricas de Django.
* Formularios reutilizables para crear y editar productos.
* Confirmación de eliminación de productos.
* Protección del CRUD mediante autenticación y permisos de administrador.
* Integración del catálogo con la gestión de productos.
* Mejoras visuales utilizando Bootstrap y Bootstrap Icons.

### Fixed

* Corrección de la configuración del formulario de autenticación (`LoginForm`).
* Mejora en la asignación de clases CSS para los campos del formulario, diferenciando correctamente los `checkbox` del resto de los controles.

---

## [0.3.0] - 2026-07-07

### Added

* Configuración del sistema de autenticación de Django.
* Personalización de la plantilla de inicio de sesión.
* Implementación de un formulario de autenticación con estilos Bootstrap.
* Configuración de redirecciones para inicio y cierre de sesión.
* Implementación de una barra de navegación dinámica según el estado del usuario.
* Visualización del nombre del usuario autenticado en la barra de navegación.
* Preparación de la navegación para clientes y administradores.
* Implementación del cierre de sesión mediante petición POST siguiendo las buenas prácticas de Django.

---

## [0.2.0] - 2026-07-07

### Added

* Configuración de archivos estáticos (`static/`).
* Configuración de archivos multimedia (`media/`).
* Configuración de plantillas globales.
* Creación de la plantilla base (`base.html`).
* Integración de Bootstrap 5.
* Integración de Bootstrap Icons.
* Implementación de una barra de navegación reutilizable.
* Implementación de un footer reutilizable.
* Configuración del sistema de mensajes de Django.
* Creación de la página de inicio.
* Implementación del catálogo de productos.
* Implementación de la vista de detalle de producto.
* Organización de plantillas mediante componentes reutilizables (`partials`).

---

## [0.1.0] - 2026-07-0

### Added

* Inicialización del proyecto Django.
* Configuración de PostgreSQL como base de datos principal.
* Configuración de credenciales mediante `config/secrets.py`.
* Creación del archivo `config/secrets.example.py`.
* Configuración inicial del archivo `.gitignore`.
* Implementación de los modelos `Producto`, `Pedido` e `ItemPedido`.
* Registro de modelos en el panel de administración de Django.
* Configuración inicial del repositorio Git.
* Primer commit del proyecto.
