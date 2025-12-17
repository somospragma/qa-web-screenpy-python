# Política de Seguridad

## Configuración de Seguridad

### Variables de Entorno
Este proyecto utiliza variables de entorno para configuraciones sensibles:

- `TARGET_URL`: URL objetivo para las pruebas
- `HEADLESS_MODE`: Modo headless del navegador (true/false)
- `BROWSER_TIMEOUT`: Timeout del navegador en segundos

### Archivos Sensibles Excluidos
Los siguientes archivos están excluidos del control de versiones:
- `.env` - Variables de entorno locales
- `*.key`, `*.pem` - Archivos de certificados
- `config.ini` - Archivos de configuración local
- `allure-report/` - Reportes generados

## Herramientas de Seguridad Integradas

### SAST (Análisis Estático)
- **Bandit**: Análisis de vulnerabilidades en código Python
- **Flake8**: Análisis de calidad y estilo de código

### SCA (Análisis de Composición)
- **Safety**: Verificación de vulnerabilidades en dependencias
- **Pre-commit hooks**: Análisis automático antes de commits

## Excepciones de Seguridad Documentadas

### URL Hardcodeada
- **Ubicación**: `features/conftest.py`
- **Justificación**: URL de fallback para testing, no contiene credenciales
- **Control**: Uso de variables de entorno como método principal

### Modo Headless
- **Ubicación**: `chromedriver/driver_manager.py`
- **Justificación**: Configuración por defecto para CI/CD
- **Control**: Configurable via variable de entorno

## Procedimientos de Seguridad

### Antes de Commit
```bash
# Instalar pre-commit hooks
pre-commit install

# Ejecutar análisis manual
safety check
bandit -r .
flake8 .
```

### En CI/CD
El pipeline ejecuta automáticamente:
1. Análisis de dependencias con Safety
2. Análisis estático con Bandit
3. Verificación de calidad con Flake8

## Reportar Vulnerabilidades

Si encuentras una vulnerabilidad de seguridad, por favor:
1. No la publiques en issues públicos
2. Contacta al equipo de seguridad de Pragma
3. Proporciona detalles técnicos y pasos para reproducir

## Actualizaciones de Seguridad

- Revisar dependencias mensualmente
- Actualizar herramientas de seguridad trimestralmente
- Revisar configuraciones de seguridad semestralmente