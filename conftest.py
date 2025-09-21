import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="session")
def credentials(request):
    return request.param

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "firefox":
        browser = playwright.firefox.launch(headless= False)
        print("Launching Firefox browser ..............")
    else:
        browser = playwright.chromium.launch(headless= False, args=["--start-maximized"])
        print("Launching Chrome browser ..............")

    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page #returning page object through browserInstance
    context.close()
    browser.close()