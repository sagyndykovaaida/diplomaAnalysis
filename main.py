from src.data_loader import fetch_intraday_data, fetch_weekly_adjusted_data, fetch_daily_data, fetch_intraday_for_period
from src.data_processing import process_intraday_data, process_weekly_data, process_daily_data
from src.visualization import plot_intraday_data, plot_weekly_data, plot_daily_data

API_KEY = 'APGNKEV3UU8JV07M'


def main():
    # Пример вызова для интрадневных данных
    intraday_data = fetch_intraday_data('IBM', '5min', API_KEY)
    processed_intraday = process_intraday_data(intraday_data)
    plot_intraday_data(processed_intraday, 'IBM Intraday Data')

    # Аналогично для остальных функций...


if __name__ == '__main__':
    main()
