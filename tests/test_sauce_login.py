import pytest
import re
from playwright.sync_api import Page, expect
from pages.sauce_login_page import SauceLoginPage

@pytest.mark.parametrize(
    "username, password, expected_url, expected_error",
    [
        ("standard_user", "secret_sauce", ".*inventory.html", None),
        ("locked_out_user", "secret_sauce", ".*saucedemo.com/", "Sorry, this user has been locked out."),
    ]
)
def test_saucedemo_login_flows(page: Page, username, password, expected_url, expected_error):
    login_page = SauceLoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    expect(page).to_have_url(re.compile(expected_url))

    if expected_error:
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(expected_error)
