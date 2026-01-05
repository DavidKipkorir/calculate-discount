def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    A discount is applied only if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Prompt the user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price}")
else:
    print(f"No discount applied. Original price: {final_price}")
