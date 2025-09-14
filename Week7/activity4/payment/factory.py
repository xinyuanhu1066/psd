from abc import ABC, abstractmethod
from payment.method import *


class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self):
        pass

    def process_payment(self, amount):
        payment = self.create_payment()
        payment.pay_money(amount)


class CreditCardFactory(PaymentFactory):
    def create_payment(self):
        return CreditCard()


class PayPalFactory(PaymentFactory):
    def create_payment(self):
        return PayPal()


class BankTransferFactory(PaymentFactory):
    def create_payment(self):
        return BankTransfer()


class CryptoPaymentFactory(PaymentFactory):
    def create_payment(self):
        return CryptoPayment()


class GooglePayFactory(PaymentFactory):
    def create_payment(self):
        return GooglePay()