# 🏥 Sistema de gestión de pacientes de una clínica


## 📝 Descripción
Este proyecto corresponde a un sistema desarrollado en Python que permite gestionar el registro de pacientes en una clínica privada, visualizarlos, buscarlos por nombre o ID, calcular el valor de una consulta según su previsión y también se puede eliminar los pacientes registrados.

El programa funciona mediante un menú interactivo y se encuentra modularizado para facilitar su mantenimiento y legibilidad.

---

## Funcionalidades
- Registro de nuevos pacientes en el sistema
- Visualización de todos los pacientes registrados
- Búsqueda de pacientes por nombre
- Búsqueda de pacientes por ID
- Cálculo de la atención médica total dependiendo de su previsión médica y el tipo de consulta seleccionada.
- Eliminación de pacientes mediante su ID para evitar confusiones de nombre similares
- Conteo recursivo del total de pacientes registrados en el sistema.

---

## 📁 Estructura de datos utilizadas
- **Lista**: Almacena los pacientes registrados
- **Diccionarios**: Representa cada paciente, tabla de valores y descuentos
- **Set**: Evita el registro de nombres duplicados
- **Tupla**: Contiene los tipos de consulta médica
- **Recursividad**: Utilizada para el conteo de pacientes registrados

---

## Estructura del proyecto
```text
sistema_clinico/
|---gestion_pacientes.py 
|---menu.py
|
main.py
README.md
```
---

## Cómo ejecutar el proyecto
1. Clonar o descargar el repositorio
2. Abrir el proyecto en VS Code
3. Ejecutar el archivo 'main.py'
4. Interactuar con el menú desde la consola

---

## 💻 Tecnologías utilizadas
- Python 3

---

## 👩🏻‍💻 Autor
Proyecto "Fundamentos de programación en Python" 
Desarrollado por Susan Inostroza A.
