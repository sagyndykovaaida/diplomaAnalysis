# from datetime import datetime, timedelta
#
# from app import redis_client
# from src.data_loader import fetch_intraday_data, fetch_weekly_adjusted_data, fetch_daily_data
# from src.data_processing import process_intraday_data, process_weekly_data, process_daily_data
# from src.visualization import plot_intraday_data, plot_weekly_data, plot_daily_data
# from flask import Flask, request, jsonify, send_file
# import matplotlib.pyplot as plt
# from io import BytesIO
# from flask import Flask
#
# app = Flask(__name__)
#
# from redis import Redis
# # ... (остальные импорты)
# API_KEY = 'APGNKEV3UU8JV07M'
# # Функция для кэширования изображения графика
# def cache_chart(symbol, chart_type, image_bytes):
#     # Срок действия кэша, например, 15 минут
#     expires_in = timedelta(minutes=15)
#
#     # Генерация уникального ключа для кэша
#     cache_key = f"{symbol}_{chart_type}_{datetime.now().strftime('%Y%m%d%H%M')}"
#
#     # Сохранение изображения в кэше
#     redis_client.setex(cache_key, expires_in, image_bytes)
#
#     return cache_key
#
#
# # Функция для попытки получения графика из кэша
# def get_cached_chart(symbol, chart_type):
#     keys_pattern = f"{symbol}_{chart_type}_*"
#     keys = redis_client.keys(keys_pattern)
#
#     # Если ключи найдены, берем самый свежий ключ
#     if keys:
#         latest_key = sorted(keys)[-1]
#         image_bytes = redis_client.get(latest_key)
#         if image_bytes:
#             return image_bytes
#
#     return None
#
#
# # Использование кэширования в маршруте для интрадневных данных
# @app.route('/intraday', methods=['POST'])
# def get_intraday_data():
#     request_intraday_data = request.get_json()
#     symbol = request_intraday_data['symbol']
#
#     # Попытка получить график из кэша
#     cached_image = get_cached_chart(symbol, 'intraday')
#     if cached_image:
#         return send_file(BytesIO(cached_image), mimetype='image/png', as_attachment=True,
#                          attachment_filename=f'{symbol}_intraday.png')
#
#     # Если нет в кэше, загружаем данные и генерируем график
#     data = fetch_intraday_data(symbol, '5min', API_KEY)
#     processed_data = process_intraday_data(data)
#     img = BytesIO()
#     plot_intraday_data(processed_data)
#     plt.savefig(img, format='png', bbox_inches='tight')
#     plt.close()
#     img.seek(0)
#
#     # Кэширование графика перед отправкой
#     image_bytes = img.getvalue()
#     cache_chart(symbol, 'intraday', image_bytes)
#
#     return send_file(BytesIO(image_bytes), mimetype='image/png', as_attachment=True,
#                      attachment_filename=f'{symbol}_intraday.png')
