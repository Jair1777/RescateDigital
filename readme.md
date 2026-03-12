# Rescate Digital de la Historia Musical Lojana

**SRS – Especificación de Requerimientos de Software**

---

## 1. Introducción

### 1.1 Propósito
El propósito de este documento es describir los requerimientos del sistema web **“Rescate Digital de la Historia Musical Lojana”**, una plataforma informativa desarrollada con Python y el framework Django, que permitirá recopilar, organizar y difundir información sobre los principales artistas y compositores de la música lojana.

### 1.2 Alcance del sistema
El sistema será una página web educativa e interactiva que permitirá a los usuarios conocer la historia musical de la ciudad de Loja, sus compositores, intérpretes y obras más representativas.

La plataforma incluirá:
- Información histórica y biográfica de artistas.
- Contenido multimedia.
- Sistema multiidioma (español, inglés y francés).
- Elementos gamificados para incentivar el aprendizaje.
- Acceso desde navegadores web.

El sistema será desarrollado utilizando **Python** con el framework **Django**, lo que permitirá una gestión eficiente de datos y contenido dinámico.

### 1.3 Definiciones
- **Django**: Framework de desarrollo web basado en Python.
- **Gamificación**: Uso de elementos de juego para incentivar la participación del usuario.
- **Multiidioma**: Capacidad del sistema de mostrar contenido en varios idiomas.

---

## 2. Descripción general del sistema

### 2.1 Perspectiva del producto
El sistema será una plataforma web informativa y educativa orientada a preservar la memoria cultural musical de Loja. 
Permitirá a los usuarios:
- Consultar información sobre artistas lojanos.
- Explorar cronologías musicales.
- Participar en actividades interactivas.

### 2.2 Funciones del sistema
El sistema deberá permitir:
1. Visualizar información sobre artistas lojanos.
2. Consultar la historia musical de Loja.
3. Cambiar el idioma del sitio web.
4. Participar en actividades gamificadas.
5. Administrar el contenido desde un panel administrativo.

### 2.3 Tipos de usuarios
**Usuario visitante**
- Navega por la información.
- Cambia idioma.
- Participa en actividades.

**Administrador**
- Gestiona artistas.
- Publica contenido.
- Administra juegos o actividades.

---

## 3. Objetivos del sistema

**Objetivo general**
Rescatar la historia musical lojana mediante la recopilación de información sobre sus principales artistas y su aporte al desarrollo cultural de Loja, utilizando una plataforma web interactiva.

**Objetivos específicos**
- Investigar la carrera musical de los artistas más representativos de Loja.
- Promover el conocimiento y valoración de la música lojana entre las nuevas generaciones mediante herramientas digitales.

---

## 4. Requerimientos funcionales

- **RF1 – Sistema informativo**: El sistema deberá mostrar información sobre: compositores, intérpretes e historia musical de Loja.
- **RF2 – Sistema multiidioma**: La plataforma deberá permitir cambiar el idioma entre Español, Inglés y Francés. Esto se implementará usando Django Internationalization (i18n).
- **RF3 – Sistema de artistas**: El sistema deberá permitir mostrar: biografía de artistas, fotografías, obras o canciones destacadas y línea del tiempo de su carrera.
- **RF4 – Sistema de gamificación**: El sistema deberá incluir elementos de aprendizaje interactivo como: quiz sobre música lojana, retos culturales y sistema de puntos o logros.
- **RF5 – Panel administrativo**: El sistema deberá permitir a los administradores: agregar artistas, editar información, eliminar contenido y subir imágenes. Esto se realizará mediante el panel admin de Django.

---

## 5. Requerimientos no funcionales

- **RNF1 – Usabilidad**: La página deberá ser fácil de navegar para usuarios jóvenes y estudiantes.
- **RNF2 – Rendimiento**: El sistema deberá cargar las páginas en menos de 3 segundos.
- **RNF3 – Compatibilidad**: El sistema deberá funcionar en Chrome, Edge, Firefox y dispositivos móviles.
- **RNF4 – Seguridad**: El panel de administración deberá requerir autenticación.
- **RNF5 – Escalabilidad**: El sistema deberá permitir agregar más artistas o contenido sin afectar su funcionamiento.

---

## 6. Tecnologías utilizadas

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- JavaScript

### Base de datos
- SQLite (fase inicial)
- PostgreSQL (opcional)

### Herramientas adicionales
- Django i18n (multiidioma)
- Bootstrap (diseño web)
- Git (control de versiones)

---

## 7. Modelo de datos básico

La base de datos incluirá tablas como:

**Artistas**
- `id`
- `nombre`
- `fecha de nacimiento`
- `biografía`
- `imagen`
- `obras destacadas`

**Juegos / Quiz**
- `id`
- `pregunta`
- `respuesta correcta`
- `opciones`

**Usuarios**
- `id`
- `nombre`
- `correo`
- `contraseña`

---

## 8. Características de gamificación
El sistema incluirá:
- Quiz musical
- Sistema de puntos
- Logros por aprendizaje
- Ranking de usuarios

*Esto permitirá que los jóvenes aprendan sobre la música lojana de manera entretenida.*

---

## 9. Futuras mejoras
En futuras versiones se podría agregar:
- Biblioteca musical con audio
- Línea del tiempo interactiva
- Mapa musical de Loja
- Aplicación móvil
