import time

from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

# chromium headless mode, 1 single context
def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningfdgfds")
    page.get_by_role("combobox").select_option("teach")
    # every element in a webpage can be located with CSS selector: #id, .classname, tagname
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)
