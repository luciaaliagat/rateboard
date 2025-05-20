# RateBoard

**RateBoard** es una aplicación web desarrollada con **Django 5.2.1** que permite visualizar y comparar el tipo de cambio del dólar en Perú. Extrae información de casas de cambio online, de la SUNAT y de la API del **Banco Central de Reserva del Perú (BCRP)**, presentando los datos de manera clara y visual mediante una interfaz responsiva.

## 🧩 Características generales del proyecto

- Aplicación web basada en el patrón **MTV de Django**
- Extracción de datos mediante **scraping dinámico con Playwright**
- Consumo de la **API REST del BCRP** para mostrar variaciones históricas
- Lectura y procesamiento de archivos `.txt` publicados por SUNAT
- Persistencia de datos en una base de datos **SQLite**
- Interfaz responsiva con **estilos animados en CSS**
- Visualización de gráficos interactivos con **Chart.js**
- Actualización automática de tasas y almacenamiento centralizado de datos

## 🚀 Funcionalidades

- Consulta de tipos de cambio **compra/venta** de distintas casas de cambio 
- Visualización del tipo de cambio oficial promedio SUNAT/SBS
- Gráfico histórico de la variación del dólar (últimos 30 días)
- Interfaz clara, moderna y optimizada para escritorio y móvil
- Base de datos con registros persistentes

## 📦 Instalación

### Requisitos previos

- Python 3.13.3 (u otra versión compatible)
- Node.js (requerido por Playwright)

### Pasos

1. Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/rateboard.git
cd rateboard
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate
```
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Instala Playwright y sus navegadores:
```bash
playwright install
```

5. Aplica las migraciones:
```bash
python manage.py migrate
```

6. Ejecuta el servidor:
```bash
python manage.py runserver
```
Accede a http://127.0.0.1:8000 desde tu navegador.

## 📊 Visualización
El gráfico muestra la variación del tipo de cambio en los últimos 30 días, tanto para la compra como la venta, con datos oficiales del BCRP. Se genera dinámicamente utilizando Chart.js embebido en los templates de Django

![Screenshot](static/img/img1.png)

## 👩‍💻 Desarrollado por
**Lucía Aliaga**  
[LinkedIn](https://www.linkedin.com/in/luciaaliagat/) - [GitHub](https://www.github.com/luciaaliagat) 

#### Sobre la información mostrada:
Este proyecto ha sido desarrollado con fines personales y académicos. Está disponible para su uso con propósitos educativos, de estudio o experimentación. **La información debe ser utilizada únicamente con fines referenciales o educativos, y no como base para decisiones financieras reales.**
