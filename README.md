# Binance Futures Testnet Trading Bot

## Overview

This project is a simple Python-based CLI trading bot that interacts with the Binance Futures Testnet (USDT-M).
The application allows users to place **MARKET** and **LIMIT** orders using command line arguments.

The project demonstrates:

* CLI input handling
* Interaction with Binance Futures API
* Structured project architecture
* Environment-based configuration

This project is designed as a simplified backend trading tool for learning and evaluation purposes.

---

## Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Supports **BUY** and **SELL**
* Command Line Interface (CLI)
* Environment variable configuration
* Clean modular structure

---

## Project Structure

```
BOT/
│
├── cli/
│   └── cli_input.py        # Reads command line arguments
│
├── client/
│   └── binance_client.py   # Binance API connection
│
├── service/
│   └── services.py         # Order placement logic
│
├── .env                    # API credentials
│
└── app.py                  # Application entry point
```

---

## Requirements

* Python 3.8+
* Binance Testnet account
* Binance API credentials

Install dependencies:

```
pip install python-binance python-dotenv
```

---

## Environment Configuration

Create a `.env` file in the root directory.

Example:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

Generate testnet API keys from:

https://testnet.binancefuture.com

---

## Running the Application

### Place a MARKET Order

```
python app.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example:

```
python app.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

### Place a LIMIT Order

```
python app.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

Example:

```
python app.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## Example Output

```
Order Request Summary
---------------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Response
--------------
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001
```

---

## Assumptions

* The user provides valid Binance Futures trading symbols.
* The user has sufficient testnet balance.
* Price is required only for **LIMIT** orders.

---

## Notes

* All trades are executed on **Binance Futures Testnet**, not the real market.
* This project is intended for demonstration and evaluation purposes.

---

## Author

Python Trading Bot – Assignment Implementation
