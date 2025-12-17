# Instalación y Configuración

## 📋 Prerrequisitos

### Software Requerido
- **Python 3.12+** - [Descargar](https://www.python.org/downloads/)
- **Git** - [Descargar](https://git-scm.com/downloads)
- **Google Chrome** - [Descargar](https://www.google.com/chrome/)

### Verificar Instalación
```bash
# Verificar Python
python --version
# Salida esperada: Python 3.12.x

# Verificar Git
git --version
# Salida esperada: git version x.x.x

# Verificar Chrome (Windows)
"C:\Program Files\Google\Chrome\Application\chrome.exe" --version
```

## 🚀 Instalación Rápida

### Opción 1: Configuración Automática (Recomendada)

```bash
# 1. Clonar repositorio
git clone https://github.com/somospragma/qa-web-screenpy-python.git
cd qa-web-screenpy-python

# 2. Ejecutar configuración automática
python setup.py
```

El script `setup.py` realiza automáticamente:
- ✅ Actualización de pip
- ✅ Instalación de dependencias
- ✅ Configuración de variables de entorno
- ✅ Instalación de pre-commit hooks
- ✅ Análisis inicial de seguridad

### Opción 2: Configuración Manual

```bash
# 1. Clonar repositorio
git clone https://github.com/somospragma/qa-web-screenpy-python.git
cd qa-web-screenpy-python

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Actualizar pip
python -m pip install --upgrade pip

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Configurar variables de entorno
cp .env.example .env

# 6. Instalar pre-commit hooks
pre-commit install
```

## ⚙️ Configuración de Variables de Entorno

### Archivo .env
Edita el archivo `.env` con tus configuraciones:

```bash
# URL objetivo para las pruebas
TARGET_URL=https://www.pragma.co/es/

# Configuración del navegador
HEADLESS_MODE=true
BROWSER_TIMEOUT=30

# Configuración de reportes
ALLURE_RESULTS_DIR=allure-results
SCREENSHOT_DIR=screenshots

# Configuración de testing
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20
```

### Variables Disponibles

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `TARGET_URL` | URL base para las pruebas | `https://www.pragma.co/es/` |
| `HEADLESS_MODE` | Ejecutar navegador sin interfaz | `true` |
| `BROWSER_TIMEOUT` | Timeout general del navegador (seg) | `30` |
| `ALLURE_RESULTS_DIR` | Directorio de resultados Allure | `allure-results` |
| `SCREENSHOT_DIR` | Directorio de capturas | `screenshots` |
| `IMPLICIT_WAIT` | Espera implícita (seg) | `10` |
| `EXPLICIT_WAIT` | Espera explícita (seg) | `20` |

## 🔧 Configuración Avanzada

### Pipenv (Alternativa)
```bash
# Instalar pipenv
pip install pipenv

# Instalar dependencias con pipenv
pipenv install

# Activar entorno
pipenv shell

# Instalar dependencias de desarrollo
pipenv install --dev
```

### Configuración de IDE

#### Visual Studio Code
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["features/"],
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.banditEnabled": true
}
```

#### PyCharm
1. Abrir proyecto en PyCharm
2. File → Settings → Project → Python Interpreter
3. Seleccionar intérprete del entorno virtual
4. Configurar pytest como test runner

## 🧪 Verificación de Instalación

### Tests de Verificación
```bash
# Ejecutar test básico
pytest features/test_find_case_studies.py -v

# Verificar con reporte Allure
pytest features/ --alluredir=allure-results
allure serve allure-results
```

### Análisis de Seguridad
```bash
# Verificar dependencias
safety check

# Análisis estático
bandit -r .

# Calidad de código
flake8 .
```

### Verificar Pre-commit
```bash
# Ejecutar hooks manualmente
pre-commit run --all-files
```

## 🐳 Instalación con Docker (Opcional)

### Dockerfile
```dockerfile
FROM python:3.12-slim

# Instalar Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["pytest", "features/", "--alluredir=allure-results"]
```

### Docker Compose
```yaml
version: '3.8'
services:
  qa-tests:
    build: .
    volumes:
      - ./allure-results:/app/allure-results
    environment:
      - TARGET_URL=https://www.pragma.co/es/
      - HEADLESS_MODE=true
```

## 🚨 Solución de Problemas

### Error: Python no encontrado
```bash
# Windows: Agregar Python al PATH
# Verificar instalación
where python
```

### Error: ChromeDriver incompatible
```bash
# Limpiar cache de webdriver-manager
pip uninstall webdriver-manager
pip install webdriver-manager
```

### Error: Permisos en Linux/Mac
```bash
# Dar permisos de ejecución
chmod +x setup.py
sudo python setup.py
```

### Error: Dependencias conflictivas
```bash
# Limpiar e instalar desde cero
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Error: Variables de entorno no cargadas
```bash
# Verificar archivo .env existe
ls -la .env

# Verificar contenido
cat .env

# Reinstalar python-dotenv
pip install python-dotenv --upgrade
```

## 📚 Próximos Pasos

Después de la instalación exitosa:

1. **Leer documentación**: [tests.md](tests.md)
2. **Revisar ejemplos**: Carpeta `features/`
3. **Configurar IDE**: Según tu editor preferido
4. **Ejecutar primer test**: `pytest features/ -v`
5. **Ver reportes**: `allure serve allure-results`

## 🆘 Soporte

Si encuentras problemas durante la instalación:
- **Documentación**: [docs/](index.md)
- **Issues**: [GitHub Issues](https://github.com/somospragma/qa-web-screenpy-python/issues)
- **Equipo**: Contactar al equipo de QA de Pragma