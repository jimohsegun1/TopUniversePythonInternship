# Dynamic Shopping Cart Program

A Python program that simulates an interactive shopping cart with discount calculation and item detail management capabilities.

## Features

- Add items to cart with prices
- Apply multiple percentage discounts
- Add custom item details (color, size, etc.)
- Prevent duplicate items
- Calculate final prices after discounts
- Display detailed cart summary

## Usage

1. Run the program:
   ```bash
   python shopping_cart.py
   ```

2. Follow the prompts to:
   - Enter item name
   - Enter item price
   - Add optional discounts (space-separated percentages)
   - Add optional item details (format: key=value)
   - Type 'done' when finished

## Example

```
Enter item name (or 'done' to finish): Laptop
Enter item price: 1000
Enter discounts (if any, separated by spaces): 10 5
Enter item details (e.g., color=red size=large): color=black weight=2kg
Item added: Laptop - Final Price: $855.0

Enter item name (or 'done' to finish): Mouse
Enter item price: 50
Enter discounts (if any, separated by spaces):
Enter item details (e.g., color=red size=large): color=white
Item added: Mouse - Final Price: $50.0

Enter item name (or 'done' to finish): done

--- Cart Summary ---
Laptop - $855.0 (color=black, weight=2kg)
Mouse - $50.0 (color=white)
Total Cost: $905.0
```

## Requirements

- Python 3.x

## Implementation Details

The program uses:
- Classes for object-oriented design
- Variable-length arguments (*args) for multiple discounts
- Keyword arguments (**kwargs) for item details
- Dictionary data structure for cart storage
- Error handling for invalid inputs