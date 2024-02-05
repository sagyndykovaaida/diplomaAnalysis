import matplotlib.pyplot as plt

def plot_intraday_data(df, title='Intraday Price Movements'):
    """
    Визуализация интрадневных цен акций.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['close'], label='Close Price', color='blue')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_weekly_data(df, title='Weekly Price Movements'):
    """
    Визуализация еженедельных цен акций.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['adjusted close'], label='Adjusted Close Price', color='green')
    plt.title(title)
    plt.xlabel('Week')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_daily_data(df, title='Daily Price Movements'):
    """
    Визуализация ежедневных цен акций.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['close'], label='Close Price', color='red')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
