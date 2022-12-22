import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Load the data into a Pandas DataFrame
df = pd.read_csv(
    'blog and github posts\crypto heatmap\crypto_prices.csv')

# Set the index to the date and pivot the DataFrame to have cryptocurrencies as columns
df.index = df['Date']
df = df.pivot(columns='Cryptocurrency', values='Price')

# Create the heatmap
plt.pcolor(df)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, rotation=90)
plt.colorbar()

# Show the plot
plt.show()
