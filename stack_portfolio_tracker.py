# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock} - Quantity: {quantity}, Price: {price}, Value: {value}")

print("\nTotal Investment Value:", total_investment)

# Optional: Save to file
save = input("Do you want to save to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock} - Quantity: {quantity}, Value: {value}\n")
        file.write(f"\nTotal Investment: {total_investment}")

    print("Portfolio saved to portfolio.txt")