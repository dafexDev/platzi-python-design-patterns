__all__ = ["PaymentDataHandler"]


from .chain import ChainHandler

from commons.request import Request

from ..payment import PaymentDataValidator


class PaymentDataHandler(ChainHandler):
    def handle(self, request: Request):
        validator = PaymentDataValidator()
        try:
            validator.validate(request.payment_data)
            if self._next_handler:
                self._next_handler.handle(request)
        except Exception as e:
            print("error")
            raise e
