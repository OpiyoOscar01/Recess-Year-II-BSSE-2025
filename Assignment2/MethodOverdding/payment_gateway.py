class PaymentGateway:
    def pay(self, amount):
        print(f"Processing payment of ${amount} through generic gateway.")

class PayPalGateway(PaymentGateway):
    def pay(self, amount):
        print(f"Processing payment of ${amount} via PayPal.")

# Usage
default_gateway = PaymentGateway()
default_gateway.pay(100)

paypal = PayPalGateway()
paypal.pay(150)
