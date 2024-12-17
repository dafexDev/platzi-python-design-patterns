import os

from commons import CustomerData, ContactInfo

from notifiers import EmailNotifier

from service import PaymentService

from processors import StripePaymentProcessor

from loggers import TransactionLogger

from validators import CustomerValidator, PaymentDataValidator


def get_customer_data() -> CustomerData:
    contact_info = ContactInfo(email="johndoe@email.com")
    customer_data = CustomerData(
        name="John Doe", contact_info=contact_info
    )
    return customer_data


stripe_payment_processor = StripePaymentProcessor(
    os.getenv("STRIPE_API_KEY"), os.getenv("STRIPE_PRICE_ID")
)

customer_data = get_customer_data()

notifier = EmailNotifier()

customer_validator = CustomerValidator()

payment_validator = PaymentDataValidator()

logger = TransactionLogger()

service = PaymentService(
    payment_processor=stripe_payment_processor,
    notifier=notifier,
    customer_validator=customer_validator,
    payment_validator=payment_validator,
    logger=logger,
)
