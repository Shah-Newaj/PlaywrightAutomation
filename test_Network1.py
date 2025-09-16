import time

from playwright.sync_api import Page

# --------------------- Note (Test Edge Case Scenarios) ---------------
# Sending Fake Payload Response from server to browser
# And validating
# -------------------------------------------

#-> api call from browser -> api call contact server and return back response to browser -> browser use response to generate html data
#-> mock after we get real response from server

fakePyloadCartResponse = {"message":"No Product in Cart"}
fakePyloadOrderResponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePyloadOrderResponse
    )


def test_Network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="  ORDERS").click()
    time.sleep(4)
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
    # page.get_by_role("button", name="  Cart ").click()
    # time.sleep(4)
    # cart_text = page.locator("//h1[normalize-space()='No Products in Your Cart !']").text_content()
    # print(cart_text)
