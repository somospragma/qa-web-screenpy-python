import os
import pytest
from typing import Generator
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

from screenpy import Actor
from screenpy.pacing import the_narrator

from screenpy_selenium.abilities import BrowseTheWeb
from screenpy_selenium.actions import SaveScreenshot

from screenpy_adapter_allure import AllureAdapter

from chromedriver.driver_manager import CustomDriver

# Cargar variables de entorno
load_dotenv()

@pytest.fixture(scope="function", name="Pragma")
def fixture_actions() -> Generator:
    """Inicializar al actor y entregarle la habilidad de navegar por la web con Chrome"""
    actor = Actor.named("Pragma").who_can(BrowseTheWeb.using(CustomDriver.chrome()))
    yield actor
    actor.exit()

# Le agregamos el plugin de allure al narrador
the_narrator.adapters.append(AllureAdapter())

# Definimos URL del proyecto desde variables de entorno
URL = os.getenv('TARGET_URL', 'https://www.pragma.co/es/')
