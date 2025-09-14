from abc import ABC, abstractmethod
from payment.gateway import PaymentGateway


class PaymentMethod(ABC):
    @abstractmethod
    def pay_money(self, amount):
        gateway = PaymentGateway()
        gateway.complete_payment(amount)


class PayPal(PaymentMethod):
    def pay_money(self, amount):
        print(f'Pay ${amount} with PayPal')
        super().pay_money(amount)


class CreditCard(PaymentMethod):
    def pay_money(self, amount):
        print(f'Pay ${amount} with Credit Card')
        super().pay_money(amount)


class PayPal(PaymentMethod):
    def pay_money(self, amount):
        print(f'Pay ${amount} with PayPal')
        super().pay_money(amount)


class BankTransfer(PaymentMethod):
    def pay_money(self, amount):
        print(f'Pay ${amount} with Bank Transfer')
        super().pay_money(amount)


class CryptoPayment(PaymentMethod):
    def pay_money(self, amount):
        print(f'Pay ${amount} with Crypto Payment')
        super().pay_money(amount)


class GooglePay(PaymentMethod):
    def pay_money(self, amount):
        print(f'Pay ${amount} with Google Pay')
        super().pay_money(amount)