import pandas as pd

def process_intraday_data(data):
    time_series_key = next(key for key in data if 'Time Series' in key)
    time_series = data[time_series_key]
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = [col.split(' ')[1] for col in df.columns]
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    return df

def process_weekly_data(data):
    time_series_key = next(key for key in data if 'Weekly Adjusted Time Series' in key)
    time_series = data[time_series_key]
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = [col.split(' ')[1] for col in df.columns]
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    return df

def process_daily_data(data):
    time_series_key = next(key for key in data if 'Time Series' in key)
    time_series = data[time_series_key]
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = [col.split(' ')[1] for col in df.columns]
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    return df
