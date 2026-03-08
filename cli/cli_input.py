import argparse

def read_cli():
    parse = argparse.ArgumentParser(description='Trading Bot Cli')

    parse.add_argument('--symbol', required= True, help="Trading Pair(e.g BISCUDT)")
    parse.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parse.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parse.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parse.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parse.parse_args()

    return args