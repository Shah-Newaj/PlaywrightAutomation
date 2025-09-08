import time

from playwright.sync_api import Page, expect


def test_uiValiationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    # every element in a webpage can be located with CSS selector: #id, .classname, tagname
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # page.locator("id=signInBtn").click()

    iPhoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iPhoneProduct.get_by_role("button").click()
    nokiaEdgeProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaEdgeProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    # time.sleep(5)

def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.locator("//a[contains(text(),'Free Access to InterviewQues/ResumeAssistance/Mate')]").click() #new page
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)
        text = "  mentor@rahulshettyacademy.com  "
        email = text.strip()
        print(email)
        assert email == "mentor@rahulshettyacademy.com"



