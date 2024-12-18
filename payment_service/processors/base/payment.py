__all__ = ["PaymentProcessorProtocol"]


from typing import Protocol, runtime_checkable

from commons import CustomerData, PaymentData, PaymentResponse


@runtime_checkable
class PaymentProcessorProtocol(Protocol):
    """
    Protocol for processing payments.

    This protocol defines the interface for payment processors. Implementations
    should provide methods for processing payments.
    """

    def process_transaction(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: ...
