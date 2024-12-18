from typing import Protocol
from typing import Optional

from commons import CustomerData, PaymentData, PaymentResponse

from loggers import TransactionLogger

from notifiers import NotifierProtocol

from processors import (
    PaymentProcessorProtocol,
    RefundProcessorProtocol,
    RecurringPaymentProcessorProtocol,
)

from validators.handlers import ChainHandler

from listeners import ListenersManager


class PaymentServiceProtocol(Protocol):
    payment_processor: PaymentProcessorProtocol
    notifier: NotifierProtocol
    validators: ChainHandler
    logger: TransactionLogger
    listeners: ListenersManager
    refund_processor: Optional[RefundProcessorProtocol] = None
    recurring_processor: Optional[RecurringPaymentProcessorProtocol] = None

    def process_transaction(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: ...

    def process_refund(self, transaction_id: str) -> PaymentResponse: ...

    def setup_recurring(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: ...
