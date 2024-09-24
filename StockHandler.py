import os 
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

load_dotenv()

API_BASE_URL = os.getenv("APCA_API_BASE_URL")
API_KEY_ID = os.getenv("APCA_API_KEY_ID")
API_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")

trading_client = TradingClient('PKITDZWXUD3QS5TXLGJ8', API_SECRET_KEY, paper=True)

def Trade(_symbol, _qty):
    market_order_data = MarketOrderRequest(
                        symbol=_symbol,
                        qty=_qty,
                        side=OrderSide.BUY,
                        time_in_force=TimeInForce.DAY
                        )

    market_order = trading_client.submit_order(
                    order_data=market_order_data
                )