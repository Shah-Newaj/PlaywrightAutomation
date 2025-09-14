from playwright.sync_api import Playwright

ordersPayload = {"orders":[{"country":"India","productOrderedId":"68a961719320a140fe1ca57c"}]}

# ----------------Important Notes to Test API----------------------------------------------
# base_url="https://rahulshettyacademy.com"
# response url="/api/ecom/order/create-order"
# data={"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"}
# Payload = {"orders":[{"country":"India","productOrderedId":"68a961719320a140fe1ca57c"}]}
# payload means order information order id etc
# --------------------------------------------------------------------------------------------------

class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                            data={"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"})

        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                 data=ordersPayload,
                                 headers={"Authorization": token,
                                          "Content-Type":"application/json"
                                          })

        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId