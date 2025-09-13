from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        '''Common interface for payment'''
        pass


class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f'Processing ${amount} via PayPal'
    

class StripePayment(Payment):
    def process_payment(self, amount):
        return f'Processing ${amount} via Stripe'


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f'Processing ${amount} via Credit Card'