__all__ = ["RecurringPaymentProcessorProtocol"]


from typing import Protocol, runtime_checkable

from commons import CustomerData, PaymentData, PaymentResponse


@runtime_checkable
class RecurringPaymentProcessorProtocol(Protocol):
    """Protocol for setting up recurring payments."""

    def setup_recurring_payment(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: ...
