from factory import *


def client_code(factory: PaymentFactory, amount):
    # client code does not know the specific payment factory,
    # just uses the base factory and common interface.
    processor = factory.create_processor()
    print(processor.process_payment(amount))


if __name__ == '__main__':
    paypal_factory = PayPalFactory()
    client_code(paypal_factory, 100)

    stripe_factory = StripeFactory()
    client_code(stripe_factory, 100)

    credit_card_factory = CreditCardFactory()
    client_code(credit_card_factory, 100)