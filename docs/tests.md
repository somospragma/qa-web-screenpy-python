# Guía de Tests

## 🧪 Estructura de Tests

### Organización de Archivos
```
features/
├── __init__.py
├── conftest.py              # Configuración y fixtures
├── test_find_case_studies.py # Test de casos de estudio
└── test_*.py               # Otros tests

locators/
├── __init__.py
├── PragmaHomePage.py       # Localizadores página principal
├── PragmaCaseStudies.py    # Localizadores casos de estudio
└── *.py                    # Otros localizadores
```

### Convenciones de Nomenclatura
- **Tests**: `test_*.py` (requerido por pytest)
- **Funciones**: `test_descripcion_funcionalidad()`
- **Localizadores**: `elemento_locator`
- **Páginas**: `NombrePaginaPage.py`

## 📝 Escribir Tests

### Estructura Básica de un Test
```python
from screenpy import Actor, given, when, then
from screenpy.actions import See
from screenpy_selenium.actions import Open, Click, Wait
from screenpy_selenium.questions import Element
from screenpy_selenium.resolutions import IsVisible

from features.conftest import URL
from locators.PragmaHomePage import menu_locator

def test_ejemplo_basico(Pragma: Actor) -> None:
    """Test básico siguiendo el patrón Given-When-Then"""
    
    given(Pragma).was_able_to(
        Open.their_browser_on(URL)
    )
    
    when(Pragma).attempts_to(
        Click.on(menu_locator)
    )
    
    then(Pragma).should(
        See.the(Element(menu_locator), IsVisible())
    )
```

### Patrón Given-When-Then

#### Given (Dado que)
Establece el estado inicial del test:
```python
given(Pragma).was_able_to(
    Open.their_browser_on(URL),
    Wait.for_the(page_locator).to_be_visible()
)
```

#### When (Cuando)
Ejecuta la acción que se está probando:
```python
when(Pragma).attempts_to(
    Click.on(menu_locator),
    Wait.for_the(submenu_locator).to_be_clickable(),
    Click.on(option_locator)
)
```

#### Then (Entonces)
Verifica el resultado esperado:
```python
then(Pragma).should(
    See.the(Element(result_locator), IsVisible()),
    See.the(Text.of_the(title_locator), ContainsTheText("Esperado"))
)
```

## 🎯 Localizadores

### Definir Localizadores
```python
# locators/MiPagina.py
from screenpy_selenium import Target
from selenium.webdriver.common.by import By

# Por ID
boton_enviar_locator = Target.the("Botón Enviar").located_by(
    (By.ID, "submit-button")
)

# Por clase CSS
menu_principal_locator = Target.the("Menú Principal").located_by(
    (By.CLASS_NAME, "main-menu")
)

# Por texto de enlace
enlace_contacto_locator = Target.the("Enlace Contacto").located_by(
    (By.LINK_TEXT, "Contacto")
)

# Por XPath
elemento_complejo_locator = Target.the("Elemento Complejo").located_by(
    (By.XPATH, "//div[@class='container']//button[contains(text(), 'Enviar')]")
)

# Por selector CSS
card_producto_locator = Target.the("Card de Producto").located_by(
    (By.CSS_SELECTOR, ".product-card:first-child")
)
```

### Mejores Prácticas para Localizadores
1. **Usar nombres descriptivos**: `boton_login_locator` vs `button1_locator`
2. **Preferir ID y clases**: Más estables que XPath
3. **Evitar selectores frágiles**: No usar índices cuando sea posible
4. **Documentar localizadores complejos**: Agregar comentarios explicativos

## 🎬 Acciones Disponibles

### Navegación
```python
from screenpy_selenium.actions import Open, Refresh, GoBack, GoForward

# Abrir URL
Open.their_browser_on("https://ejemplo.com")

# Refrescar página
Refresh.the_page()

# Navegar hacia atrás
GoBack()

# Navegar hacia adelante  
GoForward()
```

### Interacción con Elementos
```python
from screenpy_selenium.actions import Click, DoubleClick, RightClick

# Click simple
Click.on(boton_locator)

# Click con JavaScript (para elementos ocultos)
Click.on_the(boton_locator).using_javascript()

# Doble click
DoubleClick.on_the(elemento_locator)

# Click derecho
RightClick.on_the(elemento_locator)
```

### Entrada de Texto
```python
from screenpy_selenium.actions import Enter, Clear, SendKeys

# Escribir texto
Enter.the_text("mi texto").into_the(campo_locator)

# Limpiar campo
Clear.the_text_from_the(campo_locator)

# Enviar teclas especiales
SendKeys.the_keys(Keys.ENTER).to_the(campo_locator)
```

### Esperas y Sincronización
```python
from screenpy_selenium.actions import Wait

# Esperar que elemento sea visible
Wait.for_the(elemento_locator).to_be_visible()

# Esperar que elemento sea clickeable
Wait.for_the(boton_locator).to_be_clickable()

# Esperar que elemento desaparezca
Wait.for_the(loading_locator).to_disappear()

# Esperar con timeout personalizado
Wait(timeout=30).for_the(elemento_locator).to_be_visible()
```

## ❓ Preguntas y Verificaciones

### Verificar Elementos
```python
from screenpy_selenium.questions import Element, Text, Attribute
from screenpy_selenium.resolutions import IsVisible, IsClickable, ContainsTheText

# Verificar visibilidad
See.the(Element(elemento_locator), IsVisible())

# Verificar texto
See.the(Text.of_the(titulo_locator), ContainsTheText("Bienvenido"))

# Verificar atributo
See.the(Attribute("class").of_the(elemento_locator), ContainsTheText("active"))
```

### Verificaciones Personalizadas
```python
from screenpy.resolutions import IsEqualTo, IsNot

# Verificar igualdad exacta
See.the(Text.of_the(contador_locator), IsEqualTo("5"))

# Verificar negación
See.the(Element(error_locator), IsNot(IsVisible()))
```

## 📸 Capturas de Pantalla

### Captura Automática
```python
from screenpy_selenium.actions import SaveScreenshot
from allure_commons.types import AttachmentType

# Captura simple
SaveScreenshot.as_("captura.png")

# Captura con adjunto a Allure
SaveScreenshot.as_("captura.png").and_attach_it(
    name="Captura de pantalla",
    attachment_type=AttachmentType.PNG
)
```

### Capturas en Fallos
```python
# En conftest.py
@pytest.fixture(autouse=True)
def screenshot_on_failure(request, Pragma):
    yield
    if request.node.rep_call.failed:
        SaveScreenshot.as_(f"failure_{request.node.name}.png")
```

## 🏃‍♂️ Ejecutar Tests

### Comandos Básicos
```bash
# Ejecutar todos los tests
pytest features/

# Ejecutar test específico
pytest features/test_find_case_studies.py

# Ejecutar con verbose
pytest features/ -v

# Ejecutar con reportes Allure
pytest features/ --alluredir=allure-results
```

### Filtros y Marcadores
```python
# Marcar tests
@pytest.mark.smoke
def test_login_basico(Pragma: Actor):
    pass

@pytest.mark.regression  
def test_flujo_completo(Pragma: Actor):
    pass
```

```bash
# Ejecutar por marcadores
pytest -m smoke
pytest -m "smoke or regression"
pytest -m "not slow"
```

### Parametrización
```python
@pytest.mark.parametrize("usuario,password", [
    ("admin", "admin123"),
    ("user", "user123"),
    ("guest", "guest123")
])
def test_login_multiples_usuarios(Pragma: Actor, usuario, password):
    # Test con diferentes combinaciones
    pass
```

## 📊 Reportes

### Allure Reports
```bash
# Generar resultados
pytest features/ --alluredir=allure-results

# Servir reporte
allure serve allure-results

# Generar reporte estático
allure generate allure-results --output allure-report
```

### Configuración de Allure
```python
# En el test
import allure

@allure.feature("Navegación")
@allure.story("Menú principal")
@allure.severity(allure.severity_level.CRITICAL)
def test_navegacion_menu(Pragma: Actor):
    with allure.step("Abrir página principal"):
        given(Pragma).was_able_to(Open.their_browser_on(URL))
    
    with allure.step("Hacer click en menú"):
        when(Pragma).attempts_to(Click.on(menu_locator))
```

## 🔧 Configuración Avanzada

### Fixtures Personalizados
```python
# En conftest.py
@pytest.fixture
def usuario_logueado(Pragma):
    """Fixture que deja al usuario logueado"""
    Pragma.attempts_to(
        Open.their_browser_on(LOGIN_URL),
        Enter.the_text(USERNAME).into_the(username_field),
        Enter.the_text(PASSWORD).into_the(password_field),
        Click.on(login_button)
    )
    return Pragma
```

### Configuración de pytest
```ini
# pytest.ini
[tool:pytest]
testpaths = features
python_files = test_*.py
python_functions = test_*
markers =
    smoke: Tests de humo
    regression: Tests de regresión
    slow: Tests lentos
addopts = 
    -v
    --strict-markers
    --tb=short
```

## 🚨 Debugging y Troubleshooting

### Debugging Tests
```python
# Usar breakpoint
def test_debug_ejemplo(Pragma: Actor):
    given(Pragma).was_able_to(Open.their_browser_on(URL))
    breakpoint()  # Pausa aquí
    when(Pragma).attempts_to(Click.on(menu_locator))
```

```bash
# Ejecutar con debugger
pytest features/test_ejemplo.py --pdb
```

### Logs Detallados
```bash
# Ejecutar con logs
pytest features/ -v -s --log-cli-level=DEBUG
```

### Modo No-Headless
```bash
# Ver navegador durante ejecución
HEADLESS_MODE=false pytest features/ -v
```

## 📋 Mejores Prácticas

### Estructura de Tests
1. **Un test, una funcionalidad**: Cada test debe probar una sola cosa
2. **Tests independientes**: No deben depender del orden de ejecución
3. **Datos de prueba**: Usar fixtures o archivos de datos
4. **Limpieza**: Asegurar cleanup después de cada test

### Mantenibilidad
1. **DRY (Don't Repeat Yourself)**: Reutilizar código común
2. **Nombres descriptivos**: Tests y funciones con nombres claros
3. **Comentarios**: Documentar lógica compleja
4. **Refactoring**: Mantener código limpio y actualizado

### Performance
1. **Esperas inteligentes**: Usar esperas explícitas, no sleep()
2. **Reutilizar sesiones**: Cuando sea posible
3. **Paralelización**: Usar pytest-xdist para tests paralelos
4. **Cleanup eficiente**: Cerrar recursos correctamente