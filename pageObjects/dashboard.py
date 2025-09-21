from pageObjects.ordersHistory import OrdersHistoryPage


class DashBoardPage:

    def __init__(self, page):
        self.page = page

    def selectOrderNavLink(self):
        self.page.get_by_role("button", name="  ORDERS").click()
        orderHistoryPage = OrdersHistoryPage(self.page)
        return orderHistoryPage

