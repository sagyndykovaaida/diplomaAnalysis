# Stock Data Analysis API 

This is a FastAPI-based application for retrieving and analyzing stock data using the `yfinance` library. It provides several endpoints for fetching stock data over different periods and generating statistics for a given stock ticker.

## Features

- Fetch stock data for a specific day, week, month, or year.
- Retrieve statistics for a given stock over a specified period.
- Support for Cross-Origin Resource Sharing (CORS) to enable interaction with a frontend application.

## Requirements

- Python 3.7+
- FastAPI
- Pydantic
- yfinance
- Uvicorn

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/stock-data-analysis-api.git
   cd stock-data-analysis-api
##  Create a virtual environment and activate it:
  ```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
