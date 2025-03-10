from transaction import Transaction
from discount_engine import DiscountEngine
from constants import Constants

class ShipmentProcessor:
    def __init__(self):
        self.discount_engine = DiscountEngine()

    def process_line(self, line):
        parts = line.strip().split()
        if len(parts) != 3:
            return f"{line.strip()} Ignored"
        
        date, size, provider = parts
        transaction = Transaction(date, size, provider)

        if not self.validate_input(transaction):
            transaction.valid = False
            return transaction.format_output()

        transaction.set_price(Constants.PRICES[provider][size])
        self.discount_engine.apply_discounts(transaction)
        return transaction.format_output()

    def validate_input(self, transaction):
        return (transaction.size in Constants.VALID_SIZES) and (transaction.provider in Constants.VALID_PROVIDERS)
