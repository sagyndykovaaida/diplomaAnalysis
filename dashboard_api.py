# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import yfinance as yf
# import pandas as pd
# import json
# from plotly.utils import PlotlyJSONEncoder
# import plotly.express as px  # Лучше импортировать в начале файла
#
# app = Flask(__name__)
# # Настройка CORS для всех маршрутов
# CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST"]}})
#
# def load_data(ticker, start_date, end_date):
#     data = yf.download(ticker, start=start_date, end=end_date)
#     data.reset_index(inplace=True)
#     return data
#
# # @app.route('/api/get_stock_data', methods=['GET'])
# # def get_stock_data():
# #     ticker = request.args.get('ticker', default='AAPL')
# #     start_date = request.args.get('start', default='2022-01-01')
# #     end_date = request.args.get('end', default=pd.to_datetime('today').strftime('%Y-%m-%d'))
# #
# #     data = load_data(ticker, start_date, end_date)
# #     return jsonify(data.to_dict(orient='records'))
#
#
# @app.route('/api/get_stock_data', methods=['GET'])
# def get_stock_data():
#     ticker = request.args.get('ticker', default='AAPL')
#     start_date = request.args.get('start', default='2022-01-01')
#     end_date = request.args.get('end', default=pd.to_datetime('today').strftime('%Y-%m-%d'))
#     data = load_data(ticker, start_date, end_date)
#     return jsonify(data.to_dict(orient='records'))
#
#
#
# @app.route('/api/get_stock_chart', methods=['GET'])
# def get_stock_chart():
#     ticker = request.args.get('ticker', default='AAPL')
#     start_date = request.args.get('start', default='2022-01-01')
#     end_date = request.args.get('end', default=pd.to_datetime('today').strftime('%Y-%m-%d'))
#
#     data = load_data(ticker, start_date, end_date)
#     fig = px.line(data, x='Date', y='Close', title=f'Closing Price of {ticker}')
#     graph_json = json.dumps(fig, cls=PlotlyJSONEncoder)
#     return graph_json
#
# @app.route('/api/get_stock_statistics', methods=['GET'])
# def get_stock_statistics():
#     ticker = request.args.get('ticker', default='AAPL')
#     start_date = request.args.get('start', default='2022-01-01')
#     end_date = request.args.get('end', default=pd.to_datetime('today').strftime('%Y-%m-%d'))
#
#     data = load_data(ticker, start_date, end_date)
#     stats = data.describe().to_dict()
#     return jsonify(stats)
#
# if __name__ == '__main__':
#     app.run(debug=True)



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yfinance as yf
import pandas as pd
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
API_KEY = os.getenv('Z5PRD4266B2CCZJL', 'default_api_key_if_any')  # Use environment variable for API Key

# url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={API_KEY}"
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Specifies the allowed origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Your existing routes and logic here

def get_stock_data(ticker, period):
    data = yf.download(ticker, period=period)
    data.reset_index(inplace=True)
    if data.empty:
        return None
    return data
class TickerRequest(BaseModel):
    ticker: str
class StockRequest(BaseModel):
    ticker: str
    start_date: str
    end_date: str



@app.post("/load_data/")
def load_data(request: StockRequest):
    data = yf.download(request.ticker, start=request.start_date, end=request.end_date)
    data.reset_index(inplace=True)
    return data.to_dict(orient="records")

@app.post("/statistics/")
def get_statistics(request: StockRequest):
    data = yf.download(request.ticker, start=request.start_date, end=request.end_date)
    return data.describe().to_dict()


@app.post("/data/day/")
def get_data_for_day(request: TickerRequest):
    data = get_stock_data(request.ticker, "1d")
    if data is None:
        raise HTTPException(status_code=404, detail="No data found for the given ticker.")
    return data.to_dict(orient="records")

@app.post("/data/week/")
def get_data_for_week(request: TickerRequest):
    data = get_stock_data(request.ticker, "1wk")
    if data is None:
        raise HTTPException(status_code=404, detail="No data found for the given ticker.")
    return data.to_dict(orient="records")

@app.post("/data/month/")
def get_data_for_month(request: TickerRequest):
    data = get_stock_data(request.ticker, "1mo")
    if data is None:
        raise HTTPException(status_code=404, detail="No data found for the given ticker.")
    return data.to_dict(orient="records")

@app.post("/data/year/")
def get_data_for_year(request: TickerRequest):
    data = get_stock_data(request.ticker, "1y")
    if data is None:
        raise HTTPException(status_code=404, detail="No data found for the given ticker.")
    return data.to_dict(orient="records")

