closing_prices = [
    150.5, 152.3, 153.1, 151.8, 150.9, 149.7, 150.2, 151.5, 152.9, 154.1,
    155.0, 154.2, 153.5, 152.3, 151.1, 150.8, 149.9, 148.7, 149.5, 150.3,
    151.4, 152.2, 153.7, 154.6, 155.3, 156.1, 155.0, 154.2, 153.1, 152.5
]

def calculate_sma(closing_prices, window):
    sma = []
    for i in range(len(closing_prices)):
        if i + 1 >= window:
            avg = sum(closing_prices[i - window + 1:i + 1]) / window
            sma.append(round(avg, 2))
        else:
            sma.append(None)  # Not enough data for SMA
        print(sma[-1])  # Print only the latest SMA value at each step

calculate_sma(closing_prices, 20)
