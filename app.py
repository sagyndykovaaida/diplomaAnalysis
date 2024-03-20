from src.data_loader import fetch_intraday_data, fetch_weekly_adjusted_data, fetch_daily_data
from src.data_processing import process_intraday_data, process_weekly_data, process_daily_data
from src.visualization import plot_intraday_data, plot_weekly_data, plot_daily_data
from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
from io import BytesIO


app = Flask(__name__)

API_KEY = 'APGNKEV3UU8JV07M'

@app.route('/intraday', methods=['POST'])
def get_intraday_data():
    request_intraday_data = request.get_json()
    symbol = request_intraday_data['symbol']

    data = fetch_intraday_data(symbol, '5min', API_KEY)
    processed_data = process_intraday_data(data)
    img = BytesIO()
    plot_intraday_data(processed_data)
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png', as_attachment=True, attachment_filename=f'{symbol}_intraday.png')

@app.route('/weekly', methods=['POST'])
def get_weekly_data():
    request_weekly_data = request.get_json()
    symbol = request_weekly_data['symbol']

    data = fetch_weekly_adjusted_data(symbol, API_KEY)
    processed_data = process_weekly_data(data)
    img = BytesIO()
    plot_weekly_data(processed_data)
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)

    return send_file(img, mimetype='image/png', as_attachment=True, attachment_filename=f'{symbol}weekly.png')


@app.route('/daily', methods=['POST'])
def get_daily_data():
    request_daily_data = request.get_json()
    symbol = request_daily_data['symbol']

    data = fetch_daily_data(symbol, API_KEY)
    processed_data = process_daily_data(data)
    img = BytesIO()
    plot_daily_data(processed_data)
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)

    return send_file(img, mimetype='image/png', as_attachment=True, attachment_filename=f'{symbol}daily.png')


if __name__ == '__main__':
    app.run(debug=True)
