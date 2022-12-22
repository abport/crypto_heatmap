# crypto_heatmap
A Python Script that creates a heatmap of cryptocurrency prices

To create a heatmap of cryptocurrency prices, you can use the `matplotlib` library in Python. Here's an example of how you could go about it:

    import matplotlib.pyplot as plt
    import pandas as pd

    # Load the data into a Pandas DataFrame
    df = pd.read_csv('crypto_prices.csv')

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

This script assumes that you have a CSV file called `crypto_prices.csv` with the following format:

    Date,Cryptocurrency,Price
    2021-01-01,Bitcoin,10000
    2021-01-01,Ethereum,1000
    2021-01-02,Bitcoin,10050
    2021-01-02,Ethereum,1050
    2021-01-03,Bitcoin,10100
    2021-01-03,Ethereum,1100
    2021-01-04,Bitcoin,9950
    2021-01-04,Ethereum,1050
    2021-01-05,Bitcoin,10200
    2021-01-05,Ethereum,1100

This data represents the price of Bitcoin and Ethereum on five consecutive days in January 2021. You can use this data to create a heatmap that shows the changes in price over time.

To use this data, you can save it to a file called `crypto_prices.csv` and then run the script I provided above. This should generate a heatmap showing the price trends for Bitcoin and Ethereum.

This will create a heatmap with the cryptocurrency names on the x-axis and the dates on the y-axis, and the cell colors will indicate the price of the cryptocurrency on that date. You can customize the appearance of the heatmap by setting various options in the `pcolor` and `colorbar` functions.

I hope this helps! Let me know if you have any questions or need further assistance.
