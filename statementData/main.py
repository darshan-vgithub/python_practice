import yfinance as yf
import pandas as pd
import os

# Set default base path
base_path = r"D:\FlameBack\Repos\python_practice\statementData"
data_path = os.path.join(base_path, "Data")
financials_path = os.path.join(base_path, "Financials")

# Ensure directories exist
os.makedirs(data_path, exist_ok=True)
os.makedirs(financials_path, exist_ok=True)

# Load equity details
equity_details = pd.read_csv(os.path.join(base_path, "EQUITY_L.csv"))
print(equity_details.SYMBOL)

for name in equity_details.SYMBOL[:1]:
    try:
        ticker = yf.Ticker(f"{name}.NS")

        # Download full price history
        price_data = ticker.history(period="max")
        price_data.to_csv(os.path.join(data_path, f"{name}.csv"))

        # Fetch financial statements
        income_statement = ticker.financials.T
        balance_sheet = ticker.balance_sheet.T
        cash_flow = ticker.cashflow.T

        # Save to one Excel file with multiple sheets
        with pd.ExcelWriter(os.path.join(financials_path, f"{name}_financials.xlsx")) as writer:
            income_statement.to_excel(writer, sheet_name="Income Statement")
            balance_sheet.to_excel(writer, sheet_name="Balance Sheet")
            cash_flow.to_excel(writer, sheet_name="Cash Flow")

        print(f"Saved data for {name}")

    except Exception as e:
        print(f"Error in {name} ====> {e}")
