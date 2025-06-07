# 🚀 Selenium Web Testing Suite

Proyecto de automatización web para testing de páginas DemoQA usando Selenium WebDriver.

## 📋 Descripción

Suite de pruebas automatizadas que valida diferentes funcionalidades web:
- Registro y login de usuarios
- Elementos dinámicos (botones, cambios de color)
- Validación de enlaces e imágenes rotas

## 🛠️ Requisitos

- Python 3.7+
- Google Chrome
- ChromeDriver

## 📦 Instalación

```bash
# Instalar dependencias
pip install selenium requests

# Descargar ChromeDriver desde:
# https://chromedriver.chromium.org/
```

## 🏃‍♂️ Uso

### 1. Registro y Login Automático
```bash
python main.py
```
- Registra un usuario nuevo
- Realiza login automático
- Valida sesión exitosa

### 2. Pruebas de Elementos Dinámicos
```bash
python dinamica.py
```
- Detecta cambios de color en tiempo real
- Verifica botones que aparecen dinámicamente
- Valida elementos habilitados después de tiempo

### 3. Verificación de Enlaces Rotos
```bash
python roto.py
```
- Encuentra imágenes rotas
- Detecta enlaces inválidos
- Reporta errores HTTP

## 📁 Estructura del Proyecto

```
proyecto/
├── main.py           # Registro y login de usuarios
├── dinamica.py       # Testing de elementos dinámicos
├── roto.py          # Verificación de enlaces rotos
└── README.md        # Este archivo
```

## 🎯 Características

- **Automatización completa** - Sin intervención manual
- **Capturas automáticas** - Screenshots de resultados
- **Manejo de errores** - Control robusto de excepciones
- **Timeouts inteligentes** - Esperas optimizadas

## 📊 Resultados

Los scripts generan:
- Reportes en consola con estado OK/ERROR
- Screenshots automáticos (.png)
- Validaciones HTTP de enlaces e imágenes

## 🔧 Configuración

### Cambiar datos de usuario (main.py):
```python
datos = {
    "firstname": "TuNombre",
    "lastname": "TuApellido", 
    "userName": "TuUsuario",
    "password": "TuPassword"
}
```

### Ajustar timeouts:
```python
timeout=5  # Cambiar según necesidad
```

## 🚨 Notas Importantes

- El CAPTCHA requiere intervención manual (10 segundos)
- Chrome debe estar instalado y actualizado
- Verificar que ChromeDriver coincida con la versión de Chrome

**Desarrollado con ❤️ por Daniel Pacheco**
