from typing import Protocol

from commons import CustomerData, PaymentData, PaymentResponse

from service_protocol import PaymentServiceProtocol


class PaymentServiceDecoratorProtocol(Protocol):
    wrapped: PaymentServiceProtocol
    
    def process_transaction(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: ...
    
    def process_refund(self, transaction_id: str) -> PaymentResponse: ...
    
    def setup_recurring(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: ...
