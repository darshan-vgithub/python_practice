import yfinance as yf
import pandas as pd
import os

#I want set a default path to store the data how to do that 



equity_details=pd.read_csv("D:\FlameBack\Repos\python_practice\statementData\EQUITY_L.csv")
print(equity_details.SYMBOL)

for name in equity_details.SYMBOL:
    try:
        data=yf.download(f"{name}.NS")
        data.to_csv(f"D:\FlameBack\Repos\python_practice\statementData\Data\{name}.csv")
    except Exception as e:
        print(f"Error in {name} ====> {e}")
