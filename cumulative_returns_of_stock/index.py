import os
import pandas as pd
import matplotlib.pyplot as plt

# Set base path to current script's directory
base_path = os.path.dirname(os.path.abspath(__file__))

# CSV filename (assumes it's in the same folder as index.py)
csv_file = os.path.join(base_path, './20MICRONS.csv')  # Replace with actual file name

# Load CSV
df = pd.read_csv(csv_file, parse_dates=['Date'])
df.sort_values('Date', inplace=True)

# Calculate cumulative returns
df['Cumulative Return'] = (df['Close'] / df['Close'].iloc[0]) - 1

# Plot the cumulative returns
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Cumulative Return'], color='blue', linewidth=2)
plt.title('Cumulative Return Over Time', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid(True)
plt.tight_layout()
plt.show()
