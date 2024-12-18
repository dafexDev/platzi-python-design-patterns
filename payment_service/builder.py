from typing import Optional, Self

from dataclasses import dataclass

from commons import CustomerData, PaymentData

from service import PaymentService

from loggers import TransactionLogger

from notifiers import NotifierProtocol, EmailNotifier, SMSNotifier

from factory import PaymentProcessorFactory

from processors import (
    PaymentProcessorProtocol,
    RefundProcessorProtocol,
    RecurringPaymentProcessorProtocol,
)

from validators import CustomerValidator, PaymentDataValidator

from listeners import ListenersManager, AccountabilityListener


@dataclass
class PaymentServiceBuilder:
    payment_processor: Optional[PaymentProcessorProtocol] = None
    notifier: Optional[NotifierProtocol] = None
    customer_validator: Optional[CustomerValidator] = None
    payment_validator: Optional[PaymentDataValidator] = None
    logger: Optional[TransactionLogger] = None
    listener: Optional[ListenersManager] = None
    refund_processor: Optional[RefundProcessorProtocol] = None
    recurring_processor: Optional[RecurringPaymentProcessorProtocol] = None

    def set_logger(self) -> Self:
        self.logger = TransactionLogger()
        return self

    def set_customer_validatior(self) -> Self:
        self.customer_validator = CustomerValidator()
        return self

    def set_payment_validator(self) -> Self:
        self.payment_validator = PaymentDataValidator()
        return self

    def set_payment_processor(self, payment_data: PaymentData) -> Self:
        self.payment_processor = PaymentProcessorFactory.create_payment_processor(
            payment_data
        )
        if isinstance(self.payment_processor, RefundProcessorProtocol):
            self.refund_processor = self.payment_processor
        if isinstance(self.payment_processor, RecurringPaymentProcessorProtocol):
            self.recurring_processor = self.recurring_processor
        return self

    def set_notifier(self, customer_data: CustomerData) -> Self:
        if customer_data.contact_info.email:
            self.notifier = EmailNotifier()
            return self
        if customer_data.contact_info.phone:
            self.notifier = SMSNotifier(gateway="MyCustomGateway")
            return self

        raise ValueError("Cannot select notifier class")
    
    def set_listeners(self) -> Self:
        listener = ListenersManager()
        accontability_listener = AccountabilityListener()
        listener.subscribe(accontability_listener)
        self.listener = listener
        return self

    def build(self) -> PaymentService:
        if not all(
            [
                self.payment_processor,
                self.notifier,
                self.customer_validator,
                self.payment_validator,
                self.logger,
                self.listener
            ]
        ):
            missing = [
                name
                for name, value in [
                    ("payment_processor", self.payment_processor),
                    ("notifier", self.notifier),
                    ("customer_validator", self.customer_validator),
                    ("payment_validator", self.payment_validator),
                    ("logger", self.logger),
                    ("listener", self.listener)
                ]
                if value is None
            ]
            raise ValueError(f"Missing dependencies: {missing}")

        return PaymentService(
            payment_processor=self.payment_processor,
            customer_validator=self.customer_validator,
            payment_validator=self.payment_validator,
            notifier=self.notifier,
            logger=self.logger,
            listeners=self.listener,
            refund_processor=self.refund_processor,
            recurring_processor=self.recurring_processor,
        )
