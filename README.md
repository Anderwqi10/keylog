# Keyboard Event Logger

Aplicación desarrollada en Python para registrar eventos del teclado, almacenar información en archivos de texto y automatizar el envío de reportes mediante correo electrónico.

---

##  Descripción

Keyboard Event Logger es un proyecto desarrollado en Python que permite capturar y registrar las pulsaciones realizadas en el teclado. La información recopilada se almacena en un archivo de texto y puede ser enviada automáticamente por correo electrónico mediante una configuración previa.

El propósito de este proyecto fue poner en práctica conceptos relacionados con el manejo de eventos, la automatización de tareas, el trabajo con archivos y la integración de servicios externos en Python. Durante su desarrollo se utilizaron librerías especializadas para detectar eventos del teclado y gestionar el envío de información a través de correo electrónico.

Este proyecto permitió fortalecer conocimientos sobre programación en Python, manejo de librerías externas y automatización de procesos, aplicando conceptos vistos durante la formación académica.

---

##  Características

- Captura de eventos del teclado en tiempo real.
- Registro automático de pulsaciones en archivos de texto.
- Almacenamiento local de información.
- Automatización del envío de reportes mediante correo electrónico.
- Integración con servicios SMTP.
- Uso de librerías externas para el monitoreo de eventos.
- Procesamiento continuo de información durante la ejecución.
- Implementación de conceptos de automatización y programación orientada a eventos.

---

##  Tecnologías Utilizadas

- Python
- Keyboard
- Yagmail
- SMTP
- Archivos TXT

---

##  Arquitectura General

La aplicación se basa en la captura de eventos generados por el teclado, el procesamiento de la información obtenida y el almacenamiento de los registros para su posterior envío mediante correo electrónico.

```text
Usuario
   │
   ▼
Eventos del Teclado
   │
   ▼
Procesamiento de Datos
   │
   ├── Archivo TXT
   │
   └── Correo Electrónico
```

---

## Estructura del Proyecto

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

Permite detectar las teclas presionadas por el usuario durante la ejecución del programa y registrar la información generada.

### Registro de Información

Los eventos capturados son almacenados en archivos de texto para mantener un historial de la actividad registrada.

### Automatización de Procesos

El sistema automatiza tareas relacionadas con el almacenamiento y envío de la información recopilada.

### Envío de Reportes

Integra servicios de correo electrónico para compartir los registros generados de forma automática.

### Procesamiento Continuo

La aplicación permanece activa mientras monitorea y registra eventos producidos por el teclado.

---

## Flujo de Funcionamiento

1. Inicio de la aplicación.
2. Activación del monitoreo de eventos del teclado.
3. Captura de pulsaciones.
4. Registro de información en archivos de texto.
5. Procesamiento de los datos recopilados.
6. Envío automático de reportes por correo electrónico.
7. Finalización de la ejecución.

---

##  Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de contar con:

Python 3.8 o superior.
Conexión a Internet para el envío de correos.
Cuenta de correo configurada para el envío de reportes.
Permisos necesarios para la captura de eventos del teclado según el sistema operativo.

##  Dependencias

El proyecto utiliza las siguientes librerías:

keyboard
yagmail

Instalación rápida:

pip install keyboard yagmail


##  Variables de Entorno

Para una mayor seguridad, se recomienda almacenar las credenciales en un archivo .env.

| Variable | Descripción |
|-----------|-------------|
| `EMAIL_USER` | Correo electrónico utilizado para enviar los reportes generados por la aplicación. |
| `EMAIL_PASSWORD` | Contraseña o contraseña de aplicación asociada al correo electrónico configurado. |
| `EMAIL_DESTINATION` | Correo destinatario que recibirá los registros y reportes enviados por el sistema. |


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

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

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

##  Objetivo del Proyecto

Desarrollar una aplicación que permita comprender el funcionamiento de los eventos del teclado en Python, así como el almacenamiento de información y la automatización de tareas mediante el uso de archivos y servicios de correo electrónico.

---

## Conceptos Aplicados

Durante el desarrollo de este proyecto se trabajó con conceptos como:

- Programación orientada a eventos.
- Automatización de tareas.
- Manejo de archivos.
- Uso de librerías externas.
- Comunicación mediante correo electrónico.
- Integración de servicios SMTP.
- Procesamiento de información en tiempo real.
- Desarrollo de aplicaciones en Python.

---


##  Licencia

Proyecto académico y educativo.

> ⚠️ Este proyecto fue desarrollado con fines de aprendizaje y demostración de conceptos relacionados con la captura de eventos, automatización y manejo de información en Python.
