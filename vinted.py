class ShipmentProcessor:
    def __init__(self):
        # Store prices in a dictionary for easy access
        self.prices = {
            'LP': {'S': 1.50, 'M': 4.90, 'L': 6.90},
            'MR': {'S': 2.00, 'M': 3.00, 'L': 4.00}
        }
        self.rules = [self.lowest_s_price, self.third_l_free, self.monthly_discount_limit]
        self.monthly_discount = {}
        self.lp_l_count = {}
        self.max_discount = 10.0

    def process_shipment(self, date, size, provider):
        if not self.validate_input(date, size, provider):
            return f"{date} {size} {provider} Ignored"

        discount = 0.0
        price = self.get_price(size, provider)

        for rule in self.rules:
            price, discount = rule(date, size, provider, price, discount)

        return f"{date} {size} {provider} {price:.2f} {discount:.2f}" if discount else f"{date} {size} {provider} {price:.2f} -"

    def validate_input(self, date, size, provider):
        # Validate that the input format and values are correct
        valid_sizes = ['S', 'M', 'L']
        valid_providers = ['LP', 'MR']
        return size in valid_sizes and provider in valid_providers

    def get_price(self, size, provider):
        # Retrieve the price based on package size and provider
        return self.prices.get(provider, {}).get(size, 0.0)

    def lowest_s_price(self, date, size, provider, price, discount):
        if size == 'S':
            lowest_price = min(self.get_price('S', 'LP'), self.get_price('S', 'MR'))
            discount = price - lowest_price
            price = lowest_price
        return price, discount

    def third_l_free(self, date, size, provider, price, discount):
        if size == 'L' and provider == 'LP':
            month = date[:7]  # Extract year-month
            if month not in self.lp_l_count:
                self.lp_l_count[month] = 0
            self.lp_l_count[month] += 1

            if self.lp_l_count[month] == 3:
                discount = price
                price = 0.0
        return price, discount

    def monthly_discount_limit(self, date, size, provider, price, discount):
        month = date[:7]
        if month not in self.monthly_discount:
            self.monthly_discount[month] = 0.0

        available_discount = self.max_discount - self.monthly_discount[month]
        if discount > available_discount:
            discount = available_discount
            price += discount - available_discount

        self.monthly_discount[month] += discount
        return price, discount


def main():
    processor = ShipmentProcessor()
    with open('input.txt', 'r') as file:
        with open('output.txt', 'w') as output_file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    date, size, provider = parts
                    result = processor.process_shipment(date, size, provider)
                    output_file.write(result + "\n")
                    print(result)
                else:
                    output_file.write(f"{line.strip()} Ignored\n")
                    print(f"{line.strip()} Ignored")


if __name__ == "__main__":
    main()
