import matplotlib.pyplot as plt

def plot_intraday_data(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['close'], label='Close Price', color='blue')
    # plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_weekly_data(df):
    plt.figure(figsize=(14, 7))
    # Измените 'adjusted close' на правильное имя вашего столбца
    plt.plot(df.index, df['high'], label='high Price', color='green')
    # plt.title(title)
    plt.xlabel('Week')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_daily_data(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['close'], label='Close Price', color='red')
    # plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
