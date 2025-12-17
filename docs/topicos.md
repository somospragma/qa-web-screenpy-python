# Tópicos

## 🐍 Python
- **Versión**: Python 3.12+
- **Paradigma**: Programación orientada a objetos
- **Uso**: Lenguaje principal del framework
- **Características**:
  - Sintaxis clara y legible
  - Amplio ecosistema de librerías
  - Soporte nativo para testing
  - Integración con herramientas DevOps

## 🧪 Pytest
- **Descripción**: Framework de testing para Python
- **Características**:
  - Fixtures para setup/teardown
  - Parametrización de tests
  - Plugins extensibles
  - Reportes detallados
- **Uso en el proyecto**:
  - Ejecución de tests automatizados
  - Gestión de fixtures (Actor Pragma)
  - Integración con Allure para reportes

## 🌐 Selenium
- **Descripción**: Herramienta de automatización web
- **Componentes**:
  - WebDriver API
  - Localizadores de elementos
  - Gestión de navegadores
  - Sincronización y esperas
- **Uso en el proyecto**:
  - Interacción con elementos web
  - Navegación automatizada
  - Captura de screenshots
  - Gestión de sesiones de navegador

## 🎭 ScreenPy
- **Descripción**: Framework que implementa el patrón Screenplay
- **Conceptos principales**:
  - **Actors**: Usuarios que interactúan con la aplicación
  - **Abilities**: Habilidades que poseen los actores
  - **Actions**: Acciones que pueden realizar
  - **Questions**: Preguntas sobre el estado de la aplicación
- **Beneficios**:
  - Tests más legibles y expresivos
  - Separación clara de responsabilidades
  - Reutilización de componentes
  - Mantenimiento simplificado

## 🎭 ScreenPy-Selenium
- **Descripción**: Integración de ScreenPy con Selenium
- **Componentes**:
  - `BrowseTheWeb`: Habilidad para navegar
  - `Target`: Definición de localizadores
  - `Actions`: Open, Click, Wait, etc.
  - `Questions`: Element, Text, etc.
- **Ventajas**:
  - Abstracción de Selenium WebDriver
  - API más expresiva
  - Integración nativa con reportes

## 📊 Allure
- **Descripción**: Framework de reportes de testing
- **Características**:
  - Reportes HTML interactivos
  - Capturas de pantalla automáticas
  - Categorización de tests
  - Métricas y tendencias
- **Integración**:
  - `allure-pytest`: Plugin para pytest
  - `screenpy-adapter-allure`: Adaptador ScreenPy
  - Reportes automáticos en CI/CD

## 🔒 Herramientas de Seguridad

### Bandit (SAST)
- **Propósito**: Análisis estático de seguridad
- **Funcionalidad**: Detecta vulnerabilidades en código Python
- **Integración**: Pre-commit hooks y CI/CD pipeline

### Safety (SCA)
- **Propósito**: Análisis de composición de software
- **Funcionalidad**: Verifica vulnerabilidades en dependencias
- **Base de datos**: CVE y advisories de seguridad

### Pre-commit
- **Propósito**: Hooks de Git para calidad de código
- **Herramientas integradas**:
  - Black (formateo)
  - Flake8 (linting)
  - Bandit (seguridad)
  - Safety (dependencias)

## 🚀 DevOps y CI/CD

### Azure DevOps
- **Pipeline**: Automatización de testing
- **Características**:
  - Ejecución en Ubuntu
  - Instalación automática de Chrome
  - Reportes de Allure
  - Análisis de seguridad integrado

### Docker (Preparado)
- **Uso**: Containerización para CI/CD
- **Beneficios**:
  - Entornos consistentes
  - Escalabilidad
  - Aislamiento de dependencias

## 🛠️ Gestión de Dependencias

### Pipenv
- **Propósito**: Gestión de entornos virtuales
- **Archivos**: Pipfile y Pipfile.lock
- **Ventajas**:
  - Resolución determinística
  - Separación dev/prod
  - Integración con pip

### Requirements.txt
- **Propósito**: Lista de dependencias
- **Uso**: Instalación en CI/CD
- **Formato**: Versiones específicas para reproducibilidad

## 🌍 Variables de Entorno

### Python-dotenv
- **Propósito**: Carga de variables de entorno
- **Archivos**: .env, .env.example
- **Beneficios**:
  - Configuración flexible
  - Separación de secretos
  - Diferentes entornos (dev/test/prod)

## 📋 Patrones de Diseño

### Screenplay Pattern
- **Origen**: Serenity BDD
- **Principios**:
  - Separación de qué vs cómo
  - Composición sobre herencia
  - Expresividad en el código

### Page Object Model (Opcional)
- **Uso**: Localizadores organizados
- **Estructura**: Archivos por página/componente
- **Beneficios**: Mantenimiento centralizado

### Factory Pattern
- **Uso**: CustomDriver para WebDriver
- **Beneficios**: Configuración centralizada de navegadores