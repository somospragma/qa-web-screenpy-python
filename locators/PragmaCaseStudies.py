from screenpy_selenium import Target
from selenium.webdriver.common.by import By


nequi_case_study_locator = Target.the("caso de exito nequi").located_by(
    (By.PARTIAL_LINK_TEXT, "Nequi")
)

