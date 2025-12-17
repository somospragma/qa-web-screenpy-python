# Tecnologías

## 🐍 Python

### Información General
- **Versión**: 3.12+
- **Tipo**: Lenguaje de programación interpretado
- **Paradigma**: Orientado a objetos, funcional, imperativo
- **Licencia**: Python Software Foundation License

### Características Principales
- **Sintaxis clara**: Fácil de leer y escribir
- **Multiplataforma**: Windows, Linux, macOS
- **Ecosistema rico**: Amplia biblioteca de paquetes
- **Comunidad activa**: Gran soporte y documentación

### Uso en el Proyecto
```python
# Gestión de dependencias
import os
from typing import Generator

# Programación orientada a objetos
class CustomDriver:
    @staticmethod
    def chrome() -> webdriver.Chrome:
        return webdriver.Chrome()
```

### Enlaces
- **Sitio oficial**: [python.org](https://www.python.org/)
- **Documentación**: [docs.python.org](https://docs.python.org/3/)
- **PEP 8**: [pep8.org](https://pep8.org/)

---

## 🌐 Selenium

### Información General
- **Versión**: 4.21.0
- **Tipo**: Framework de automatización web
- **Licencia**: Apache License 2.0
- **Mantenedor**: Selenium Project

### Componentes Principales
- **WebDriver**: API para controlar navegadores
- **Grid**: Ejecución distribuida de tests
- **IDE**: Grabación y reproducción de tests

### Arquitectura WebDriver
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Inicialización del driver
driver = webdriver.Chrome()

# Localización de elementos
element = driver.find_element(By.ID, "element-id")

# Esperas explícitas
wait = WebDriverWait(driver, 10)
```

### Navegadores Soportados
- **Chrome/Chromium**: ChromeDriver
- **Firefox**: GeckoDriver  
- **Safari**: SafariDriver
- **Edge**: EdgeDriver

### Enlaces
- **Sitio oficial**: [selenium.dev](https://selenium.dev/)
- **Documentación Python**: [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/)
- **GitHub**: [github.com/SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium)

---

## 🎭 ScreenPy

### Información General
- **Versión**: 4.2.4
- **Tipo**: Framework de testing basado en Screenplay Pattern
- **Licencia**: MIT License
- **Creador**: Perryn Fowler, mantenido por ScreenPyHQ

### Patrón Screenplay
```python
from screenpy import Actor, given, when, then

# Actor con habilidades
actor = Actor.named("Usuario").who_can(BrowseTheWeb.using(driver))

# Estructura Given-When-Then
given(actor).was_able_to(Open.their_browser_on(URL))
when(actor).attempts_to(Click.on(button))
then(actor).should(See.the(Element(result), IsVisible()))
```

### Componentes Core
- **Actors**: Usuarios que interactúan con el sistema
- **Abilities**: Habilidades que poseen los actores
- **Actions**: Acciones que pueden realizar
- **Questions**: Preguntas sobre el estado del sistema
- **Resolutions**: Resoluciones de las preguntas

### Beneficios
- **Legibilidad**: Tests expresivos y fáciles de entender
- **Mantenibilidad**: Separación clara de responsabilidades
- **Reutilización**: Componentes reutilizables
- **Escalabilidad**: Fácil agregar nuevas funcionalidades

### Enlaces
- **Documentación**: [screenpy.readthedocs.io](https://screenpy.readthedocs.io/)
- **GitHub**: [github.com/ScreenPyHQ/screenpy](https://github.com/ScreenPyHQ/screenpy)
- **Ejemplos**: [github.com/ScreenPyHQ/screenpy_examples](https://github.com/ScreenPyHQ/screenpy_examples)

---

## 🎭 ScreenPy-Selenium

### Información General
- **Versión**: 4.0.4
- **Tipo**: Integración de ScreenPy con Selenium
- **Dependencias**: ScreenPy + Selenium
- **Licencia**: MIT License

### Componentes Principales

#### Abilities
```python
from screenpy_selenium.abilities import BrowseTheWeb

# Habilidad de navegación web
actor.who_can(BrowseTheWeb.using(driver))
```

#### Actions
```python
from screenpy_selenium.actions import Open, Click, Wait, Enter

Open.their_browser_on(URL)
Click.on(locator)
Wait.for_the(locator).to_be_visible()
Enter.the_text("texto").into_the(field)
```

#### Questions
```python
from screenpy_selenium.questions import Element, Text, Attribute

Element(locator)  # Estado del elemento
Text.of_the(locator)  # Texto del elemento
Attribute("class").of_the(locator)  # Atributo específico
```

#### Targets (Locators)
```python
from screenpy_selenium import Target
from selenium.webdriver.common.by import By

button = Target.the("Botón").located_by((By.ID, "button-id"))
```

### Enlaces
- **GitHub**: [github.com/ScreenPyHQ/screenpy_selenium](https://github.com/ScreenPyHQ/screenpy_selenium)
- **PyPI**: [pypi.org/project/screenpy-selenium](https://pypi.org/project/screenpy-selenium/)

---

## 🧪 Pytest

### Información General
- **Versión**: 8.2.1
- **Tipo**: Framework de testing para Python
- **Licencia**: MIT License
- **Características**: Simple, escalable, extensible

### Características Principales
- **Sintaxis simple**: Tests con funciones simples
- **Fixtures**: Setup y teardown reutilizable
- **Parametrización**: Tests con múltiples datos
- **Plugins**: Ecosistema extenso de plugins
- **Reportes**: Múltiples formatos de salida

### Uso en el Proyecto
```python
import pytest
from typing import Generator

@pytest.fixture(scope="function")
def actor_fixture() -> Generator:
    actor = Actor.named("Test")
    yield actor
    actor.exit()

def test_ejemplo(actor_fixture):
    # Lógica del test
    pass
```

### Plugins Utilizados
- **allure-pytest**: Integración con Allure
- **pytest-html**: Reportes HTML
- **pytest-cov**: Cobertura de código

### Enlaces
- **Sitio oficial**: [pytest.org](https://pytest.org/)
- **Documentación**: [docs.pytest.org](https://docs.pytest.org/)
- **Plugins**: [plugincompat.herokuapp.com](https://plugincompat.herokuapp.com/)

---

## 📊 Allure

### Información General
- **Versión**: 2.13.5 (allure-pytest)
- **Tipo**: Framework de reportes de testing
- **Licencia**: Apache License 2.0
- **Desarrollador**: Qameta Software

### Características
- **Reportes interactivos**: HTML con JavaScript
- **Categorización**: Organización por features y stories
- **Attachments**: Screenshots, logs, videos
- **Tendencias**: Histórico de ejecuciones
- **Integración**: Múltiples frameworks de testing

### Integración ScreenPy
```python
from screenpy_adapter_allure import AllureAdapter
from screenpy.pacing import the_narrator

# Configuración del adaptador
the_narrator.adapters.append(AllureAdapter())

# Annotations en tests
@allure.feature("Login")
@allure.story("Login exitoso")
def test_login(actor):
    pass
```

### Componentes
- **allure-pytest**: Plugin para pytest
- **allure-commandline**: Generador de reportes
- **screenpy-adapter-allure**: Adaptador para ScreenPy

### Enlaces
- **Sitio oficial**: [qameta.io/allure](https://qameta.io/allure/)
- **Documentación**: [docs.qameta.io/allure](https://docs.qameta.io/allure/)
- **GitHub**: [github.com/allure-framework](https://github.com/allure-framework)

---

## 🔒 Herramientas de Seguridad

### Bandit (SAST)
- **Versión**: 1.7.5
- **Propósito**: Análisis estático de seguridad
- **Tipo**: SAST (Static Application Security Testing)
- **Lenguaje**: Python

```bash
# Ejecución básica
bandit -r .

# Con configuración personalizada
bandit -r . -c .bandit
```

### Safety (SCA)
- **Versión**: 3.0.1
- **Propósito**: Análisis de composición de software
- **Tipo**: SCA (Software Composition Analysis)
- **Base de datos**: CVE, GitHub Security Advisories

```bash
# Verificar dependencias
safety check

# Con archivo específico
safety check -r requirements.txt
```

### Pre-commit
- **Versión**: 3.6.0
- **Propósito**: Git hooks para calidad de código
- **Integración**: Múltiples herramientas de linting

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pycqa/bandit
    hooks:
      - id: bandit
```

---

## 🛠️ Herramientas de Desarrollo

### WebDriver Manager
- **Versión**: 4.0.1
- **Propósito**: Gestión automática de drivers
- **Beneficio**: No requiere descarga manual de ChromeDriver

```python
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
```

### Python-dotenv
- **Versión**: 1.0.1
- **Propósito**: Carga de variables de entorno
- **Uso**: Configuración flexible sin hardcoding

```python
from dotenv import load_dotenv
import os

load_dotenv()
URL = os.getenv('TARGET_URL')
```

### Black (Formatter)
- **Versión**: 23.12.1
- **Propósito**: Formateo automático de código Python
- **Estilo**: PEP 8 compliant

### Flake8 (Linter)
- **Versión**: 7.0.0
- **Propósito**: Análisis de calidad de código
- **Verificaciones**: Estilo, complejidad, errores

---

## 🚀 DevOps y CI/CD

### Azure DevOps
- **Plataforma**: Microsoft Azure
- **Componentes**: Pipelines, Repos, Artifacts
- **Configuración**: YAML pipelines

```yaml
# pipeline.yml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.12'
```

### Docker (Preparado)
- **Uso**: Containerización para CI/CD
- **Base**: python:3.12-slim
- **Beneficios**: Entornos consistentes

---

## 📦 Gestión de Dependencias

### Pip
- **Propósito**: Instalador de paquetes Python
- **Archivo**: requirements.txt
- **Uso**: Instalación de dependencias

### Pipenv
- **Propósito**: Gestión de entornos virtuales
- **Archivos**: Pipfile, Pipfile.lock
- **Beneficios**: Resolución determinística

---

## 🌐 Navegadores y Drivers

### Google Chrome
- **Versión**: Última estable
- **Driver**: ChromeDriver (gestionado automáticamente)
- **Configuración**: Headless, no-sandbox, disable-dev-shm-usage

### Configuraciones de Seguridad
```python
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
```

---

## 📋 Resumen del Stack

### Core Testing
- **Python 3.12+**: Lenguaje principal
- **ScreenPy 4.2.4**: Framework Screenplay
- **Selenium 4.21.0**: Automatización web
- **Pytest 8.2.1**: Framework de testing

### Reporting
- **Allure 2.13.5**: Reportes interactivos
- **ScreenPy-Adapter-Allure**: Integración

### Security & Quality
- **Bandit 1.7.5**: SAST analysis
- **Safety 3.0.1**: SCA analysis
- **Flake8 7.0.0**: Code quality
- **Pre-commit 3.6.0**: Git hooks

### DevOps
- **Azure DevOps**: CI/CD pipeline
- **Docker**: Containerización (preparado)
- **WebDriver Manager**: Gestión de drivers

### Configuration
- **Python-dotenv**: Variables de entorno
- **Pipenv**: Gestión de dependencias