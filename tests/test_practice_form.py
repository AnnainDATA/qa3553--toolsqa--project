import time
from pages.home_page import HomePage


class TestFormPage:
    def test_open_practice_form(self,driver,student):
        practice_form_page=HomePage(driver).open().open_forms().open_practice_form()
        time.sleep(5)
        practice_form_page.fill_and_click_submit(student)



