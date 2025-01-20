class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, item_name, price, *args, **kwargs):
        # Check if item already exists
        if item_name in self.cart:
            print(f"'{item_name}' already exists in cart!")
            return False

        # Calculate discounts if any
        final_price = price
        if args:
            for discount in args:
                discount_amount = float(discount) / 100
                final_price -= final_price * discount_amount

        # Store item details
        self.cart[item_name] = {
            'price': final_price,
            'details': kwargs
        }

        # Display confirmation
        print(f"Item added: {item_name} - Final Price: ${final_price}")
        return True

    def display_summary(self):
        print("\n--- Cart Summary ---")
        total_cost = 0
        
        for item_name, item_data in self.cart.items():
            price = item_data['price']
            details = item_data['details']
            
            # Format item details if any exist
            details_str = ""
            if details:
                details_str = f" ({', '.join(f'{k}={v}' for k, v in details.items())})"
            
            print(f"{item_name} - ${price}{details_str}")
            total_cost += price
            
        print(f"Total Cost: ${total_cost}")


def main():
    cart = ShoppingCart()
    
    while True:
        item_name = input("\nEnter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
            
        try:
            price = float(input("Enter item price: "))
            
            # Get discounts
            discounts = input("Enter discounts (if any, separated by spaces): ").strip()
            discounts = [float(d) for d in discounts.split()] if discounts else []
            
            # Get item details
            details_input = input("Enter item details (e.g., color=red size=large): ").strip()
            details = {}
            if details_input:
                # Split and convert input into dictionary
                pairs = details_input.split()
                for pair in pairs:
                    key, value = pair.split('=')
                    details[key] = value
            
            # Add item to cart
            cart.add_to_cart(item_name, price, *discounts, **details)
            
        except ValueError as e:
            print("Invalid input! Please enter valid numbers for price and discounts.")
            continue

    cart.display_summary()

if __name__ == "__main__":
    main()
