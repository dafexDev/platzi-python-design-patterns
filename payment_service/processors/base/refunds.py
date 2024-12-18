__all__ = ["RefundProcessorProtocol"]


from typing import Protocol, runtime_checkable

from commons import PaymentResponse


@runtime_checkable
class RefundProcessorProtocol(Protocol):
    """Protocol for processing refunds."""

    def refund_payment(self, transaction_id: str) -> PaymentResponse: ...
