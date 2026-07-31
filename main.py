# Hardcoded stock prices

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 330,
    "AMZN": 170
}

print("=" * 45)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 45)

total = 0

while True:

    stock = input("\nEnter Stock Name (AAPL/TSLA/GOOGL/MSFT/AMZN): ").upper()

    if stock not in stock_prices:
        print("Invalid Stock Name!")
        continue

    quantity = int(input("Enter Quantity: "))

    price = stock_prices[stock]

    investment = price * quantity

    total += investment

    print("------------------------------")
    print("Stock :", stock)
    print("Price :", price)
    print("Quantity :", quantity)
    print("Investment :", investment)
    print("------------------------------")

    choice = input("Add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\nYour Total Investment =", total)

# Save Result in Text File
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=========================\n")
    file.write(f"Total Investment = {total}")

print("\nReport saved successfully in portfolio.txt")