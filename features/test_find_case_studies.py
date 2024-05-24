from screenpy import Actor, given, when, then
from screenpy.actions import See
from allure_commons.types import AttachmentType

from screenpy_selenium import SaveScreenshot
from screenpy_selenium.actions import Open, Click, Wait
from screenpy_selenium.questions import Element
from screenpy_selenium.resolutions import IsVisible

from features.conftest import URL

from locators.PragmaHomePage import menu_locator,about_pragma_menu_locator, case_studies_locator
from locators.PragmaCaseStudies import nequi_case_study_locator


def test_enter_case_studios_view(Pragma: Actor) -> None:
    given(Pragma).was_able_to(
        Open.their_browser_on(URL)
    )
    when(Pragma).attempts_to(
        Wait.for_the(about_pragma_menu_locator).to_be_clickable(),
        Click.on(about_pragma_menu_locator),
        Wait.for_the(case_studies_locator).to_be_clickable(),
        Click.on(case_studies_locator),
        SaveScreenshot.as_("fin_prueba.png").and_attach_it(
        name="fin prueba", attachment_type = AttachmentType.PNG
    )
    )
    then(Pragma).should(
        See.the(Element(nequi_case_study_locator), IsVisible())
    )