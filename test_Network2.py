import time

from playwright.sync_api import Page

# --------------------- Note (Test Edge Case Scenarios) ---------------
# Sending Fake URL Request from browser to server
# And validating
# -------------------------------------------

#-> api call from browser -> api call contact server and return back response to browser -> browser use response to generate html data
#-> Continue to the server with the request call with the new url -> intercept_request



def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=68c8f1a8f669d6cb0ad03a62")


def test_Network_2(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="  ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(4)
    message = page.locator(".blink_me").text_content()
    print(message)

