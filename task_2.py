#Stock Portfolio Tracker


stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 120,
    "MSFT": 310
}

def stock_portfolio_tracker():
    portfolio = {}
    total_value = 0

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' when finished.\n")

    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Please enter a valid number.")

    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")
        total_value += value

    print(f"\nTotal Investment Value: ${total_value}")

    # Save to file
    save = input("Do you want to save the result to 'portfolio.txt'? (yes/no): ").lower()
    if save == 'yes':
        with open("portfolio.txt", "w") as file:
            file.write("--- Portfolio Summary ---\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
            file.write(f"\nTotal Investment Value: ${total_value}\n")
        print("Portfolio saved to 'portfolio.txt'.")


stock_portfolio_tracker()