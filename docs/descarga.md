# Descarga y Recursos

## 📥 Enlaces de Descarga

### Repositorio Principal
- **GitHub**: [qa-web-screenpy-python](https://github.com/somospragma/qa-web-screenpy-python)
- **Clonar**: `git clone https://github.com/somospragma/qa-web-screenpy-python.git`
- **Descargar ZIP**: [Download ZIP](https://github.com/somospragma/qa-web-screenpy-python/archive/refs/heads/main.zip)

### Releases
- **Última versión**: [v1.0.0](https://github.com/somospragma/qa-web-screenpy-python/releases/latest)
- **Todas las versiones**: [Releases](https://github.com/somospragma/qa-web-screenpy-python/releases)

## 🛠️ Herramientas Requeridas

### Python
- **Versión recomendada**: Python 3.12+
- **Descargar**: [python.org](https://www.python.org/downloads/)
- **Instalador Windows**: [Python 3.12.x](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)

### Git
- **Descargar**: [git-scm.com](https://git-scm.com/downloads)
- **Windows**: [Git for Windows](https://gitforwindows.org/)
- **Mac**: `brew install git`
- **Linux**: `sudo apt-get install git`

### Google Chrome
- **Descargar**: [google.com/chrome](https://www.google.com/chrome/)
- **Versión recomendada**: Última versión estable
- **ChromeDriver**: Se instala automáticamente via webdriver-manager

## 📦 Dependencias Principales

### Core Framework
```bash
# ScreenPy Framework
pip install screenpy==4.2.4
pip install screenpy-selenium==4.0.4
pip install screenpy-adapter-allure==4.0.4

# Testing Framework  
pip install pytest==8.2.1
pip install allure-pytest==2.13.5

# WebDriver
pip install selenium==4.21.0
pip install webdriver-manager==4.0.1
```

### Herramientas de Desarrollo
```bash
# Seguridad
pip install bandit==1.7.5
pip install safety==3.0.1

# Calidad de Código
pip install flake8==7.0.0
pip install black==23.12.1
pip install pre-commit==3.6.0

# Variables de Entorno
pip install python-dotenv==1.0.1
```

## 🔗 Recursos Externos

### Documentación Oficial
- **ScreenPy**: [screenpy-docs.readthedocs.io](https://screenpy-docs.readthedocs.io/)
- **Selenium**: [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/)
- **Pytest**: [docs.pytest.org](https://docs.pytest.org/)
- **Allure**: [docs.qameta.io/allure](https://docs.qameta.io/allure/)

### Ejemplos y Tutoriales
- **ScreenPy Examples**: [github.com/ScreenPyHQ/screenpy_examples](https://github.com/ScreenPyHQ/screenpy_examples)
- **Selenium Examples**: [selenium.dev/documentation](https://selenium.dev/documentation/)
- **Pytest Examples**: [pytest.org/en/latest/example](https://docs.pytest.org/en/latest/example/)

### Herramientas de Desarrollo
- **Visual Studio Code**: [code.visualstudio.com](https://code.visualstudio.com/)
- **PyCharm**: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- **Allure Commandline**: [github.com/allure-framework/allure2](https://github.com/allure-framework/allure2/releases)

## 📋 Archivos de Configuración

### requirements.txt
```bash
# Descargar archivo de dependencias
wget https://raw.githubusercontent.com/somospragma/qa-web-screenpy-python/main/requirements.txt

# O copiar contenido desde GitHub
curl -O https://raw.githubusercontent.com/somospragma/qa-web-screenpy-python/main/requirements.txt
```

### .env.example
```bash
# Descargar plantilla de variables de entorno
wget https://raw.githubusercontent.com/somospragma/qa-web-screenpy-python/main/.env.example

# Copiar como .env
cp .env.example .env
```

### .gitignore
```bash
# Descargar configuración de Git
wget https://raw.githubusercontent.com/somospragma/qa-web-screenpy-python/main/.gitignore
```

## 🐳 Imágenes Docker

### Imagen Base
```bash
# Python oficial
docker pull python:3.12-slim

# Con Chrome preinstalado
docker pull selenium/standalone-chrome:latest
```

### Dockerfile del Proyecto
```bash
# Descargar Dockerfile
wget https://raw.githubusercontent.com/somospragma/qa-web-screenpy-python/main/Dockerfile
```

## 📊 Reportes y Plantillas

### Plantillas de Allure
- **Allure Report**: Se genera automáticamente
- **Configuración**: Incluida en el proyecto

### Plantillas de CI/CD
```bash
# Azure DevOps Pipeline
wget https://raw.githubusercontent.com/somospragma/qa-web-screenpy-python/main/pipeline.yml

# GitHub Actions (si disponible)
wget https://raw.githubusercontent.com/somospragma/qa-web-screenpy-python/main/.github/workflows/ci.yml
```

## 🔧 Scripts de Utilidad

### setup.py
```bash
# Script de configuración automática
wget https://raw.githubusercontent.com/somospragma/qa-web-screenpy-python/main/setup.py
python setup.py
```

### Scripts de Testing
```bash
# Script para ejecutar todos los tests
pytest features/ --alluredir=allure-results

# Script para análisis de seguridad
safety check && bandit -r . && flake8 .
```

## 📱 Extensiones Recomendadas

### Visual Studio Code
```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.flake8",
    "ms-python.black-formatter",
    "ms-vscode.test-adapter-converter",
    "littlefoxteam.vscode-python-test-adapter"
  ]
}
```

### Chrome Extensions (Para Testing Manual)
- **Selenium IDE**: [chrome.google.com/webstore](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd)
- **ChroPath**: Para generar XPath
- **SelectorsHub**: Para validar selectores CSS

## 🌐 Recursos de la Comunidad

### Foros y Comunidades
- **ScreenPy Discussions**: [github.com/ScreenPyHQ/screenpy/discussions](https://github.com/ScreenPyHQ/screenpy/discussions)
- **Selenium Community**: [selenium.dev/support](https://selenium.dev/support/)
- **Python Testing**: [reddit.com/r/Python](https://www.reddit.com/r/Python/)

### Blogs y Artículos
- **Pragma Blog**: [pragma.co/blog](https://www.pragma.co/blog/)
- **ScreenPy Blog**: [screenpy.readthedocs.io](https://screenpy.readthedocs.io/)
- **Test Automation**: [testautomationu.applitools.com](https://testautomationu.applitools.com/)

## 📞 Soporte y Contacto

### Soporte Técnico
- **GitHub Issues**: [Reportar problema](https://github.com/somospragma/qa-web-screenpy-python/issues/new)
- **Documentación**: Esta carpeta `docs/`
- **Wiki**: [GitHub Wiki](https://github.com/somospragma/qa-web-screenpy-python/wiki)

### Equipo de Desarrollo
- **Pragma QA Team**: qa-team@pragma.co
- **Contribuciones**: Ver [CONTRIBUTING.md](../CONTRIBUTING.md)
- **Código de Conducta**: Ver [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md)

## 🔄 Actualizaciones

### Mantenerse Actualizado
```bash
# Verificar actualizaciones
git fetch origin
git status

# Actualizar a la última versión
git pull origin main
pip install -r requirements.txt --upgrade
```

### Notificaciones
- **GitHub Watch**: Activar notificaciones en el repositorio
- **Releases**: Suscribirse a nuevas versiones
- **Newsletter Pragma**: [pragma.co/newsletter](https://www.pragma.co/newsletter)