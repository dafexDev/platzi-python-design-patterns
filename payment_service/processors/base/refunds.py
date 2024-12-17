__all__ = ["RefundProcessorProtocol"]


from typing import Protocol

from commons import PaymentResponse


class RefundProcessorProtocol(Protocol):
    """Protocol for processing refunds."""

    def refund_payment(self, transaction_id: str) -> PaymentResponse: ...
