from flask import Flask, request, send_file
from io import BytesIO
import matplotlib.pyplot as plt

from src.data_loader import fetch_intraday_data, fetch_weekly_adjusted_data, fetch_daily_data
from src.data_processing import process_intraday_data, process_weekly_data, process_daily_data
from src.visualization import plot_intraday_data, plot_weekly_data, plot_daily_data

app = Flask(__name__)
API_KEY = 'APGNKEV3UU8JV07M'

@app.route('/intraday', methods=['GET'])
def get_intraday_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return "Symbol query parameter is required.", 400

    data = fetch_intraday_data(symbol, '5min', API_KEY)
    processed_data = process_intraday_data(data)
    img = BytesIO()
    plot_intraday_data(processed_data)
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)

    return send_file(img, mimetype='image/png')

@app.route('/weekly', methods=['GET'])
def get_weekly_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return "Symbol query parameter is required.", 400

    data = fetch_weekly_adjusted_data(symbol, API_KEY)
    processed_data = process_weekly_data(data)
    img = BytesIO()
    plot_weekly_data(processed_data)
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)

    return send_file(img, mimetype='image/png')

@app.route('/daily', methods=['GET'])
def get_daily_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return "Symbol query parameter is required.", 400

    data = fetch_daily_data(symbol, API_KEY)
    processed_data = process_daily_data(data)
    img = BytesIO()
    plot_daily_data(processed_data)
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0)

    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
