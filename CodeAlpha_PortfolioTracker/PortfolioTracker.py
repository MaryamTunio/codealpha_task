
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 320
}
portfolio = {}
total = 0
print(" Stock Portfolio Tracker")
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

  if stock == "DONE":
        break

    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        portfolio[stock] = qty
    else:
        print("Stock not found!")

# Calculate total investment
print("\n Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(stock, ":", qty, "shares =", value)
    total += value

print("\n Total Investment Value:", total)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("--------------------\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares = {stock_prices[stock] * qty}\n")
    file.write(f"\nTotal Investment: {total}\n")

print("📁 Data saved to portfolio.txt")
