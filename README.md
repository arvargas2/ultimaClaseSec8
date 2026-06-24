He generado el archivo de documentación Markdown (`README.md`) ideal para la estructura de tu proyecto de Gestión de Usuarios basado en la arquitectura en capas (Lógica de Negocio y Presentación).

Tu archivo Markdown está listo para descargar:
[file-tag: code-generated-file-0-1782306938423229097]

A continuación, tienes una copia exacta del contenido en texto plano para que puedas copiarlo y pegarlo directamente en tu repositorio de GitHub si lo prefieres:

```markdown
# Sistema de Gestión de Usuarios

Este proyecto es una aplicación de consola en Python diseñada bajo principios de **Ingeniería de Software**, implementando una arquitectura en capas para separar la lógica de negocio de la interfaz de presentación. El sistema permite registrar, buscar, validar y eliminar usuarios manteniendo los datos en una base de datos en memoria.

## 🚀 Arquitectura del Proyecto

El programa está organizado de forma limpia en dos capas o niveles distintos, distribuidos en los siguientes archivos:

1. **Capa de Negocio (Lógica de Negocio) — `modulo_usuario.py`**:
   - Contiene la estructura de datos global (`usuarios_list`).
   - Implementa todas las funciones que definen las reglas del negocio: validaciones, inserción, búsqueda y eliminación.
   - **Independencia de Interfaz**: Esta capa no depende de la interfaz de usuario (consola), lo que permite que sea reutilizada en otros contextos como una API Web o una aplicación de escritorio (GUI).

2. **Capa de Aplicación (Presentación) — `app_usuario.py`**:
   - Encargada de la interacción directa con el usuario (entrada y salida por consola).
   - Administra el menú interactivo, captura las opciones del usuario y delega la ejecución de las acciones a las funciones correspondientes del módulo lógico.

### 🧠 Beneficios de esta Separación
* **Separación de Responsabilidades**: La lógica del negocio está totalmente aislada de la interfaz de usuario.
* **Mantenibilidad**: Los cambios aplicados a la lógica interna no afectan la presentación y viceversa.
* **Reutilización**: Las funciones analíticas del módulo pueden importarse y usarse en futuros proyectos.
* **Pruebas Unitarias**: Facilita la creación de tests independientes para comprobar las reglas de negocio sin requerir emulación de clics o entradas de teclado.
* **Escalabilidad**: Permite migrar o añadir nuevas interfaces (Web, Móvil, GUI) sin alterar el núcleo de la aplicación.

---

## 📊 Estructura de Datos

El sistema implementa una **base de datos en memoria**, lo que significa que no utiliza archivos externos y toda la información se almacena temporalmente durante el tiempo de ejecución del programa.

Cada usuario se modela mediante un diccionario (formato JSON) con la siguiente estructura básica:

```json
{
  "nombre_usuario": "J.Rojas",
  "sexo": "M",
  "password": "1234qwer"
}
