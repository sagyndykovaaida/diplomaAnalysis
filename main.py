import time
from src.data_loader import fetch_intraday_data, fetch_weekly_adjusted_data, fetch_daily_data
from src.data_processing import process_intraday_data, process_weekly_data, process_daily_data
from src.visualization import plot_intraday_data, plot_weekly_data, plot_daily_data

API_KEY = 'APGNKEV3UU8JV07M'

def main():
    while True:
        print("Запуск задачи по обновлению данных...")
        intraday_data = fetch_intraday_data('IBM', '5min', API_KEY)
        processed_data = process_intraday_data(intraday_data)
        plot_intraday_data(processed_data, 'IBM Intraday Data')
        time.sleep(900)

        yearly_df = fetch_weekly_adjusted_data('IBM', API_KEY)
        yearly_data = process_weekly_data(yearly_df)
        plot_weekly_data(yearly_data, 'IBM Yearly Price Movements')
        time.sleep(900)

# here for perioud
        weekly_df = fetch_daily_data('IBM', API_KEY)
        weekly_data = process_daily_data(weekly_df)
        plot_daily_data(weekly_data, 'IBM Weekly Price Movements')
        time.sleep(900)

if __name__ == '__main__':
    main()
