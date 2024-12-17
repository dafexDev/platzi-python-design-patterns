from constants import STRIPE_API_KEY, STRIPE_PRICE_ID

from commons import PaymentData, PaymentType

from processors import (
    PaymentProcessorProtocol,
    LocalPaymentProcessor,
    OfflinePaymentProcessor,
    StripePaymentProcessor,
)


class PaymentProcessorFactory:
    @staticmethod
    def create_payment_processor(payment_data: PaymentData) -> PaymentProcessorProtocol:
        match payment_data.type:
            case PaymentType.ONLINE:
                match payment_data.currency:
                    case "USD":
                        return StripePaymentProcessor(STRIPE_API_KEY, STRIPE_PRICE_ID)
                    case _:
                        return LocalPaymentProcessor()
            case PaymentType.OFFLINE:
                return OfflinePaymentProcessor()
            case _:
                raise ValueError("Unsupported payment type")
