from payment.factory import *


def main():
    # Customer chooses to pay bill with credit card
    CreditCardFactory().process_payment(100)

    # Customer chooses to pay bill with PayPal
    PayPalFactory().process_payment(100)

    # Customer chooses to pay bill with bank transfer
    BankTransferFactory().process_payment(100)

    # Customer chooses to pay bill with crypto payment
    CryptoPaymentFactory().process_payment(100)

    # Customer chooses to pay bill with google pay
    GooglePayFactory().process_payment(100)


if __name__ == '__main__':
    main()