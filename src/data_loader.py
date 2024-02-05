import requests

url = "https://www.alphavantage.co/query"
def fetch_data(url, params):
    response = requests.get(url, params=params)
    data = response.json()
    return data

def fetch_intraday_data(symbol, interval, apikey):
    # url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": apikey
    }
    return fetch_data(url, params)

def fetch_weekly_adjusted_data(symbol, apikey):
    # url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_WEEKLY_ADJUSTED",
        "symbol": symbol,
        "apikey": apikey
    }
    return fetch_data(url, params)

def fetch_daily_data(symbol, apikey):
    # url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": apikey
    }
    return fetch_data(url, params)

# Обратите внимание: последний API имеет параметр `month`, который не поддерживается Alpha Vantage напрямую.
# Этот пример предполагает загрузку интрадневных данных за период, но вы должны реализовать логику фильтрации данных за этот месяц вручную после загрузки.
def fetch_intraday_for_period(symbol, interval, month, apikey):
    # Используется та же функция что и для интрадневных данных, но потребуется дополнительная обработка данных
    return fetch_intraday_data(symbol, interval, apikey)
