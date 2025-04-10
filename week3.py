def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.
        
    Returns:
        float: The final price after applying the discount if it is 20% or higher,
               otherwise the original price.
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount)
    
    if discount >= 20:
        print(f"The final price after a {discount}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")

