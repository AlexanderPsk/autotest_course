from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_basket_button_check(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "add_to_basket_form")), "Page wasn't loaded correctly"
    )
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), "'Add to cart' button not found"