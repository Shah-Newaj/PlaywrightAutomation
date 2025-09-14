import time

from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

# -------------------------Note------------------------
# Scenario
# E2E scenario covered using hybrid way with API and UI validation...
# Make order using API and validate that order in orders page in UI
# ------------------------------------------------------------------

def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create order -> Order id
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)
    print("Order Id is: ", orderId)

    # Login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    Title = page.title()
    assert Title == "Let's Shop"


    # Order history page -> order is present
    orders = page.get_by_role("button", name="  ORDERS")
    orders.click()
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    text = page.locator(".tagline").text_content()
    print(text)
    # time.sleep(5)