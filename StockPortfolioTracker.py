stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}
total_investment = 0
n = int(input("How many stocks do you want to add? "))
for i in range(n):
    stock_name = input("Enter stock name (AAPL, TSLA, GOOG, MSFT): ").upper()
    quantity = int(input("Enter quantity: "))
    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"{stock_name}: {quantity} shares × {stock_prices[stock_name]} = {investment}")
    else:
        print("Stock not found!")
print("\nTotal Investment Value =", total_investment)
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = {total_investment}")
print("Result saved to portfolio.txt")