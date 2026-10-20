import re
from playwright.sync_api import Page, expect

def test_saucedemo_login(page: Page):
    # 1. Open the browser and go to the target website
    page.goto("https://www.saucedemo.com/")

    # 2. Find the username field and type the text
    page.locator("[data-test='username']").fill("standard_user")

    # 3. Find the password field and type the text
    page.locator("[data-test='password']").fill("secret_sauce")

    # 4. Click the Login button
    page.locator("[data-test='login-button']").click()

    # 5. Freeze the browser right after clicking login
    

    # 6. Assertion: Verify the login actually worked
    expect(page).to_have_url(re.compile(".*inventory.html"))
