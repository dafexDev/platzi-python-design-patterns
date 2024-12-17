import os

from dotenv import load_dotenv

_ = load_dotenv()


STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

STRIPE_PRICE_ID = os.getenv("STRIPE_PRICE_ID")
