cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if cost_price > selling_price:
    print("Loss:", cost_price - selling_price)
elif selling_price > cost_price:
    print("Profit:", selling_price - cost_price)
else:
    print("No profit, no loss")