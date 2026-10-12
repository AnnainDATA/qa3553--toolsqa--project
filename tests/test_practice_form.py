import time
import pytest
import allure
import pytest_check as check
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

FIRST_NAME = (By.XPATH, "//tbody/tr[1]/td[2]")
TEXT_FORM = "Thanks for submitting the form"

@allure.epic("DemoQA project")
@allure.feature("Students form")
class TestFormPage:
    @allure.story("Filling students form")
    @allure.title("Main positive test")
    @allure.description(TEXT_FORM)
    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.skip(reason="passed, not relevant")
    def test_open_practice_form(self, driver, student):
        allure.attach(
            str(student),
            name = "Students DATA",
            attachment_type=allure.attachment_type.TEXT
        )

        practice_forms_page = HomePage(driver).open().open_forms().open_practice_form()
        time.sleep(5)
        practice_forms_page.fill_and_click_submit(student)

        #assert practice_forms_page.check_message() == "Thanks fo submitting the form"
        print("Test working")

        with allure.step("Check text form"):
            assert practice_forms_page.check_message() == TEXT_FORM


    @allure.story("Filling students form")
    @allure.title("Second positive test")
    @allure.description(TEXT_FORM)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_submit_check_data_in_table(self, driver, student):
        practice_forms_page = HomePage(driver).open().open_forms().open_practice_form()
        time.sleep(5)
        practice_forms_page.fill_and_click_submit(student)

        check.equal(practice_forms_page.check_message(), TEXT_FORM)
        check.is_in(student.first_name, driver.find_element(*FIRST_NAME).text)
        check.equal(practice_forms_page.check_message(), "TEXT_FORM")
        print("Test working")
        check.is_in(student.last_name, driver.find_element(*FIRST_NAME).text)