# Documentación - QA Web ScreenPy Python

Bienvenido a la documentación completa del framework de testing automatizado basado en ScreenPy y Selenium.

## 📚 Estructura de Documentación

### 🏗️ [Arquitectura](./architecture/)
- [Visión General](./architecture/overview.md) - Arquitectura del framework
- [Componentes](./architecture/components.md) - Descripción de componentes principales
- [Patrones de Diseño](./architecture/patterns.md) - Patrones implementados

### 📖 [Guías](./guides/)
- [Guía de Inicio Rápido](./guides/quick-start.md) - Configuración inicial
- [Configuración](./guides/configuration.md) - Variables de entorno y configuraciones
- [Escribir Tests](./guides/writing-tests.md) - Cómo crear nuevos tests
- [Mejores Prácticas](./guides/best-practices.md) - Recomendaciones y estándares
- [Seguridad](./guides/security.md) - Políticas y procedimientos de seguridad

### 🔧 [API Reference](./api/)
- [Locators](./api/locators.md) - Documentación de localizadores
- [Actions](./api/actions.md) - Acciones disponibles
- [Fixtures](./api/fixtures.md) - Fixtures de pytest

### 💡 [Ejemplos](./examples/)
- [Tests Básicos](./examples/basic-tests.md) - Ejemplos de tests simples
- [Tests Avanzados](./examples/advanced-tests.md) - Casos de uso complejos
- [Integración CI/CD](./examples/cicd-integration.md) - Configuración de pipelines

## 🚀 Inicio Rápido

1. **Instalación**
   ```bash
   git clone https://github.com/somospragma/qa-web-screenpy-python.git
   cd qa-web-screenpy-python
   python setup.py
   ```

2. **Configuración**
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

3. **Ejecutar Tests**
   ```bash
   pytest features/ --alluredir=allure-results
   ```

## 📋 Requisitos

- Python 3.12+
- Chrome/Chromium Browser
- Git

## 🔗 Enlaces Útiles

- [Repositorio Principal](https://github.com/somospragma/qa-web-screenpy-python)
- [ScreenPy Documentation](https://screenpy-docs.readthedocs.io/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)

## 🤝 Contribuir

Para contribuir al proyecto, consulta nuestra [Guía de Contribución](./guides/contributing.md).

## 📞 Soporte

- **Issues**: [GitHub Issues](https://github.com/somospragma/qa-web-screenpy-python/issues)
- **Documentación**: Esta carpeta docs/
- **Equipo**: Pragma QA Team