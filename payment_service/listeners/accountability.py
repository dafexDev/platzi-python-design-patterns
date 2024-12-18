__all__ = ["AccountabilityListener"]


from .listener import Listener


class AccountabilityListener[T](Listener):
    def notify(self, event: T):
        print(f"Notifying event {event}")
