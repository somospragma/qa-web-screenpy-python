from screenpy_selenium import Target
from selenium.webdriver.common.by import By

about_pragma_menu_locator = Target.the("Opcion 'Sobre pragma' en menú superior").located_by(
    (By.LINK_TEXT, 'Sobre Pragma')
)

case_studies_locator = Target.the("Opción 'Casos de exito' en submenu").located_by(
    (By.LINK_TEXT, 'Casos de éxito')
)

menu_locator = Target.the("Localizador menu").located_by(
    (By.XPATH, "//*[@id='hs_cos_wrapper_header_mobile_nav']/div/div/div/a")
)