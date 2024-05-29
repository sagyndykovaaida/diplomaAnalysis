from pydantic import BaseModel
import yfinance as yf
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI, HTTPException, APIRouter
from typing import List
app = FastAPI()
API_KEY = os.getenv('Z5PRD4266B2CCZJL', 'default_api_key_if_any')

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


timeframe_mapping = {
    '1D': '1d',
    '1W': '1wk',
    '1M': '1mo',
    '1Y': '1y'
}
api_router = APIRouter()

@api_router.post("/data/{timeframe}/", response_model=List[dict])
def get_data_for_timeframe(request: TickerRequest, timeframe: str):
    if timeframe not in timeframe_mapping:
        raise HTTPException(status_code=400, detail="Invalid timeframe specified.")
    data = get_stock_data(request.ticker, timeframe_mapping[timeframe])
    if data is None:
        raise HTTPException(status_code=404, detail="No data found for the given ticker.")
    return data.to_dict(orient="records")

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
