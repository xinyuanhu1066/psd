from abc import ABC, abstractmethod
from payment import *

class PaymentFactory(ABC):
    @abstractmethod
    def create_processor(self):
        '''Common interface for factory'''
        pass


class PayPalFactory(PaymentFactory):
    def create_processor(self):
        return PayPalPayment()


class StripeFactory(PaymentFactory):
    def create_processor(self):
        return StripePayment()


class CreditCardFactory(PaymentFactory):
    def create_processor(self):
        return CreditCardPayment()