# import pandas as pd
#     def process_intraday_data(data):
#         # Получаем данные временного ряда
#         time_series = data["Time Series (5min)"]
#
#         # Преобразовываем в DataFrame
#         df = pd.DataFrame.from_dict(time_series, orient='index')
#         df.index = pd.to_datetime(df.index)
#
#         # Преобразуем все колонки в числовой формат
#         for column in df.columns:
#             df[column] = pd.to_numeric(df[column], errors='coerce')
#
#         df.rename(columns=lambda x: x[3:], inplace=True)  # Убираем лишнюю часть названия колонок
#         return df
#

import pandas as pd

def process_intraday_data(data):

    # Получение ключа временного ряда
    time_series_key = next(key for key in data if 'Time Series' in key)
    time_series = data[time_series_key]

    # Преобразование данных в DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = [col.split(' ')[1] for col in df.columns]  # Убрать номера и сохранить только названия метрик
    df.index = pd.to_datetime(df.index)  # Преобразование индекса в datetime
    df = df.astype(float)  # Преобразование всех данных в float

    return df

def process_weekly_data(data):

    # Получение ключа временного ряда
    time_series_key = next(key for key in data if 'Weekly Adjusted Time Series' in key)
    time_series = data[time_series_key]

    # Преобразование данных в DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = [col.split(' ')[1] for col in df.columns]  # Убрать номера и сохранить только названия метрик
    df.index = pd.to_datetime(df.index)  # Преобразование индекса в datetime
    df = df.astype(float)  # Преобразование всех данных в float

    return df

def process_daily_data(data):

    # Получение ключа временного ряда
    time_series_key = next(key for key in data if 'Time Series' in key)
    time_series = data[time_series_key]

    # Преобразование данных в DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = [col.split(' ')[1] for col in df.columns]  # Убрать номера и сохранить только названия метрик
    df.index = pd.to_datetime(df.index)  # Преобразование индекса в datetime
    df = df.astype(float)  # Преобразование всех данных в float

    return df
