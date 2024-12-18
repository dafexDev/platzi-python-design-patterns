from commons import CustomerData, ContactInfo, PaymentData

from notifiers import NotifierProtocol, EmailNotifier, SMSNotifier

from service import PaymentService

from logging_service import PaymentServiceLogging

from loggers import TransactionLogger

from validators import CustomerValidator, PaymentDataValidator

from builder import PaymentServiceBuilder


def get_email_notifier() -> EmailNotifier:
    return EmailNotifier()


def get_sms_notifier() -> SMSNotifier:
    return SMSNotifier(gateway="SMSGatewayExample")


def get_notifier_implementation(customer_data: CustomerData) -> NotifierProtocol:
    if customer_data.contact_info.phone:
        return get_sms_notifier()
    elif customer_data.contact_info.email:
        return get_email_notifier()
    else:
        ValueError("Cannot choice the correct implementation")


def get_customer_data() -> CustomerData:
    contact_info = ContactInfo(email="johndoe@email.com")
    customer_data = CustomerData(name="John Doe", contact_info=contact_info)
    return customer_data


"""stripe_payment_processor = StripePaymentProcessor(
    os.getenv("STRIPE_API_KEY"), os.getenv("STRIPE_PRICE_ID")
)"""

customer_data = get_customer_data()

notifier = get_notifier_implementation(customer_data)
email_notifier = get_email_notifier()
sms_notifier = get_sms_notifier()

customer_validator = CustomerValidator()

payment_validator = PaymentDataValidator()

logger = TransactionLogger()


payment_data = PaymentData(amount=100, source="tok_visa", currency="USD")

builder = PaymentServiceBuilder()

service = (
    builder.set_logger()
    .set_customer_validatior()
    .set_payment_validator()
    .set_payment_processor(payment_data)
    .set_notifier(customer_data)
    .set_listeners()
    .build()
)

logging_service = PaymentServiceLogging(service)

logging_service.process_transaction(customer_data, payment_data)

"""Change notification strategy to email
service.set_notifier(email_notifier)

Change notification strategy to sms
service.set_notifier(sms_notifier) """
