from decimal import Decimal, ROUND_HALF_UP
from constants import Constants

class DiscountEngine:
    def __init__(self):
        self.monthly_discount = {}
        self.large_lp_counter = {}

    def apply_discounts(self, transaction):
        if not transaction.valid:
            return

        date, size, provider = transaction.date, transaction.size, transaction.provider
        month = date[:7]
        price = Constants.PRICES[provider][size]
        discount = Decimal('0.00')

        # Rule 1: Smallest "S" package price
        if size == 'S':
            lowest_s_price = min(Constants.PRICES['LP']['S'], Constants.PRICES['MR']['S'])
            if price > lowest_s_price:
                discount = price - lowest_s_price
                price = lowest_s_price

        # Rule 2: Every 3rd "L" size from LP is free
        if size == 'L' and provider == 'LP':
            self.large_lp_counter[month] = self.large_lp_counter.get(month, 0) + 1
            if self.large_lp_counter[month] == 3:
                discount = price
                price = Decimal('0.00')

        # Rule 3: Monthly discount cap
        self.monthly_discount.setdefault(month, Decimal('0.00'))
        remaining_discount = Constants.MAX_DISCOUNT - self.monthly_discount[month]
        if discount > remaining_discount:
            discount = remaining_discount
            price = (Constants.PRICES[provider][size] - discount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        self.monthly_discount[month] += discount
        transaction.set_price(price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        transaction.apply_discount(discount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
