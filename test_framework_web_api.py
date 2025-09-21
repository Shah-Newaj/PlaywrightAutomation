import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.dashboard import DashBoardPage
from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

# -------------------------Note------------------------
# Scenario
# E2E scenario covered using hybrid way with API and UI validation...
# Make order using API and validate that order in orders page in UI
# ------------------------------------------------------------------

# Json file -> util -> access into test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credential_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credential_list)
def test_e2e_web_api(playwright: Playwright, browserInstance, user_credentials):
    userEmail = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]


    # Create order -> Order id
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    print("Order Id is: ", orderId)

    # Login Page
    # instead of using page, browserInstance is used as parameter as page is coming through browserInstance
    # browserInstance giving back page object through fixture
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userEmail, userPassword)

    # Dashboard Page
    orderHistoryPage = dashboardPage.selectOrderNavLink()

    # Order history page -> order is present
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.verifyOrderMessage()


