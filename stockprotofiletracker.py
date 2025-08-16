import csv

def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 320,
        "GOOGL": 140,
        "AMZN": 135
    }

    portfolio = {}  # To store user input
    total_investment = 0

    print("\n📊 Stock Portfolio Tracker")
    print("Available stocks and prices (USD):")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    print("\nEnter 'done' when finished.\n")

    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("⚠️ Invalid stock symbol. Please choose from available list.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    # Calculate total investment
    print("\n📈 Portfolio Summary:")
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"{stock} - {quantity} shares → ${value}")

    print(f"\n💰 Total Investment Value: ${total_investment}")

    # Save to CSV
    save = input("Do you want to save portfolio to a CSV file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, quantity in portfolio.items():
                writer.writerow([stock, quantity, stock_prices[stock], stock_prices[stock] * quantity])
            writer.writerow(["Total", "", "", total_investment])
        print("✅ Portfolio saved to 'portfolio.csv'")

    # Save to TXT
    save_txt = input("Do you want to save portfolio to a TXT file? (yes/no): ").lower()
    if save_txt == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            for stock, quantity in portfolio.items():
                file.write(f"{stock} - {quantity} shares → ${stock_prices[stock] * quantity}\n")
            file.write(f"\nTotal Investment: ${total_investment}")
        print("✅ Portfolio saved to 'portfolio.txt'")


# Run the program
if __name__ == "__main__":
    stock_portfolio_tracker()
