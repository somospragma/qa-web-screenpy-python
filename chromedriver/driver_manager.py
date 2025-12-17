import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CustomDriver:
    @staticmethod
    def chrome() -> webdriver.Chrome:
        """Configurar y retornar una instancia de Chrome WebDriver"""
        chrome_options = Options()
        
        # Configurar modo headless desde variables de entorno
        headless_mode = os.getenv('HEADLESS_MODE', 'true').lower() == 'true'
        if headless_mode:
            chrome_options.add_argument("--headless")
        
        # Configuraciones de seguridad y rendimiento
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        
        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=chrome_options
        )   