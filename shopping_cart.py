customer_name = input("Customer Name: ")
product1 = input("\nProduct 1: ")
price1 = float(input("Price: "))
product2 = input("\nProduct 2: ")
price2 = float(input("Price: "))
product3 = input("\nProduct 3: ")
price3 = float(input("Price: "))
subtotal = price1 + price2 + price3
if subtotal >= 5000:
    discount = subtotal * 0.20
elif subtotal >= 3000:
    discount = subtotal * 0.10
elif subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0
final_total = subtotal - discount
print(f"\nSubtotal: {subtotal:g}")
print(f"Discount: {discount:g}")
print(f"Final Total: {final_total:g}")