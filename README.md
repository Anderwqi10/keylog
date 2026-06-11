#  Keyboard Event Logger

Aplicación desarrollada en Python para la captura y procesamiento de eventos de teclado, permitiendo registrar información en archivos locales y automatizar el envío de reportes mediante correo electrónico.

---

##  Descripción

Keyboard Event Logger es una aplicación desarrollada en Python orientada al estudio y comprensión de la captura de eventos generados por el teclado, el procesamiento de información en tiempo real y la automatización de tareas. El proyecto implementa mecanismos para detectar pulsaciones de teclas, registrar la información obtenida y almacenarla en archivos locales para su posterior análisis.

Además, integra servicios de correo electrónico para automatizar el envío de reportes, permitiendo explorar conceptos relacionados con la comunicación entre aplicaciones, protocolos de correo, manejo de archivos y programación orientada a eventos. Su desarrollo contribuye al fortalecimiento de habilidades en automatización, monitoreo de eventos, manejo de librerías externas y administración de información mediante Python.

Este proyecto fue concebido como una práctica académica para comprender el funcionamiento de aplicaciones que reaccionan a eventos del sistema, así como los principios básicos de registro de actividad y transmisión automatizada de datos en entornos controlados.

---

##  Características

- Captura eventos de teclado en tiempo real.
- Registro automático de pulsaciones.
- Almacenamiento de información en archivos locales.
- Procesamiento continuo de eventos.
- Automatización de reportes mediante correo electrónico.
- Uso de librerías externas para monitoreo y comunicación.
- Gestión básica de registros y seguimiento de actividad.
- Implementación de programación orientada a eventos.

---

##  Tecnologías Utilizadas

- Python
- Keyboard
- Yagmail
- SMTP
- Archivos TXT

---

##  Arquitectura General

La aplicación sigue una arquitectura simple basada en eventos, donde las acciones realizadas por el usuario son capturadas, procesadas y almacenadas para posteriormente generar reportes automatizados.

```text
Usuario
   │
   ▼
Eventos de Teclado
   │
   ▼
Procesamiento de Eventos
   │
   ├── Registro Local
   │      │
   │      └── Archivo TXT
   │
   └── Envío de Reportes
           │
           └── Correo Electrónico
```

---

##  Estructura del Proyecto

```text
keylog-main/
│
├── tp.py
│
└── README.md
```

---

##  Funcionalidades Principales

### Captura de Eventos

Permite detectar las pulsaciones realizadas en el teclado mediante eventos generados por el sistema operativo, registrando la información en tiempo real.

### Procesamiento de Información

Los eventos capturados son procesados para identificar y organizar los datos obtenidos durante la ejecución de la aplicación.

### Registro de Actividad

La información recopilada se almacena en archivos de texto locales, permitiendo conservar un historial de los eventos registrados.

### Automatización de Reportes

El sistema integra servicios de correo electrónico para enviar automáticamente la información recopilada, facilitando la automatización de tareas y el manejo de reportes.

### Ejecución Continua

La aplicación permanece en funcionamiento mientras monitorea los eventos del teclado, procesando cada interacción detectada durante la ejecución.

---

##  Flujo de Funcionamiento

1. Inicio de la aplicación.
2. Activación del monitoreo de teclado.
3. Captura de eventos generados por el usuario.
4. Procesamiento de la información obtenida.
5. Registro de datos en archivos locales.
6. Generación y envío de reportes automáticos.
7. Finalización de la ejecución.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/keylog-main.git
```

### 2. Acceder al directorio del proyecto

```bash
cd keylog-main
```

### 3. Crear un entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 5. Instalar dependencias

```bash
pip install keyboard yagmail
```

### 6. Ejecutar la aplicación

```bash
python tp.py
```

---

## Objetivo del Proyecto

Desarrollar una aplicación que permita comprender el funcionamiento de la captura de eventos del sistema, el almacenamiento de información y la automatización de procesos mediante servicios de comunicación en Python.

---

##  Conceptos Aplicados

Durante el desarrollo de este proyecto se aplicaron conceptos relacionados con:

- Programación orientada a eventos.
- Manejo de librerías externas.
- Automatización de tareas.
- Gestión de archivos.
- Comunicación mediante protocolos SMTP.
- Procesamiento de información en tiempo real.
- Manejo de estructuras de control y ciclos de ejecución.
- Integración de servicios externos en aplicaciones Python.

---

##  Equipo de Desarrollo

Proyecto desarrollado con fines académicos para fortalecer competencias en programación, automatización de procesos y manejo de eventos utilizando Python.

---
